"""Aplicação principal FastAPI."""
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import structlog

from .config import settings
from .models import HealthResponse
from .webhook import router as webhook_router
from .messages import router as messages_router
from .instance import router as instance_router
from .queue import message_queue
from .idempotency import idempotency_manager


# Configurar logging estruturado
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.dev.ConsoleRenderer(colors=True)  # Console com cores
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia ciclo de vida da aplicação."""
    # Startup
    logger.info("Iniciando aplicação")
    await message_queue.start()
    logger.info("Aplicação iniciada")
    
    yield
    
    # Shutdown
    logger.info("Parando aplicação")
    await message_queue.stop()
    logger.info("Aplicação parada")


# Criar aplicação FastAPI
app = FastAPI(
    title="Evolution API Bot",
    description="Bot WhatsApp usando Evolution API v2",
    version="1.0.0",
    lifespan=lifespan
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configurar conforme necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Adiciona header de tempo de processamento."""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    """Adiciona ID de correlação para rastreamento."""
    request_id = request.headers.get("X-Request-ID")
    if not request_id:
        request_id = f"req_{int(time.time() * 1000)}"
    
    # Adicionar ao contexto de logging
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(request_id=request_id)
    
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Loga todas as requisições."""
    start_time = time.time()
    
    logger.info(
        "Requisição recebida",
        method=request.method,
        url=str(request.url),
        client_ip=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent")
    )
    
    try:
        response = await call_next(request)
        latency_ms = int((time.time() - start_time) * 1000)
        
        logger.info(
            "Requisição processada",
            method=request.method,
            url=str(request.url),
            status_code=response.status_code,
            latency_ms=latency_ms
        )
        
        return response
        
    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        logger.error(
            "Erro na requisição",
            method=request.method,
            url=str(request.url),
            error=str(e),
            latency_ms=latency_ms
        )
        raise


# Rotas
app.include_router(webhook_router)
app.include_router(messages_router)
app.include_router(instance_router)


@app.get("/", response_model=HealthResponse)
async def root() -> HealthResponse:
    """Endpoint raiz."""
    return HealthResponse()


@app.get("/healthz", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Healthcheck para Docker/Kubernetes."""
    return HealthResponse()


@app.get("/info")
async def get_info() -> dict:
    """Informações da aplicação."""
    return {
        "name": "Evolution API Bot",
        "version": "1.0.0",
        "status": "running",
        "timestamp": time.time(),
        "queue_stats": message_queue.get_stats(),
        "idempotency_stats": idempotency_manager.get_stats()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True
    )
