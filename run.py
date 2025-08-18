#!/usr/bin/env python3
"""Script para executar a aplicação Evolution API Bot."""

import uvicorn
import os
from app.config import settings

if __name__ == "__main__":
    # Force port 5000 for deployment consistency with .replit configuration
    port = 5000
    
    print("🚀 Iniciando Evolution API Bot...")
    print(f"📡 Servidor rodando em: http://0.0.0.0:{port}")
    print(f"🔗 Healthcheck: http://0.0.0.0:{port}/healthz")
    print(f"📚 Documentação: http://0.0.0.0:{port}/docs")
    print("=" * 50)
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,  # Disable reload in production
        log_level="info"
    )
