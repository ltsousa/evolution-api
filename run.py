#!/usr/bin/env python3
"""Script para executar a aplicação Evolution API Bot."""

import uvicorn
from app.config import settings

if __name__ == "__main__":
    print("🚀 Iniciando Evolution API Bot...")
    print(f"📡 Servidor rodando em: http://localhost:{settings.port}")
    print(f"🔗 Healthcheck: http://localhost:{settings.port}/healthz")
    print(f"📚 Documentação: http://localhost:{settings.port}/docs")
    print("=" * 50)
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True,
        log_level="info"
    )
