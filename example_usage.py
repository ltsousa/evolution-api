#!/usr/bin/env python3
"""Exemplo de uso da Evolution API Bot."""

import asyncio
import httpx
from typing import Dict, Any


class EvolutionBotClient:
    """Cliente para interagir com a Evolution API Bot."""
    
    def __init__(self, base_url: str, internal_token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {internal_token}"}
    
    async def health_check(self) -> Dict[str, Any]:
        """Verifica se a aplicação está funcionando."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/healthz")
            return response.json()
    
    async def get_info(self) -> Dict[str, Any]:
        """Obtém informações da aplicação."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/info")
            return response.json()
    
    async def ensure_instance(self) -> Dict[str, Any]:
        """Garante que a instância WhatsApp está ativa."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/instance/ensure",
                headers=self.headers
            )
            return response.json()
    
    async def get_qr_code(self) -> str:
        """Obtém QR code para conexão."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/instance/qr",
                headers=self.headers
            )
            return response.text
    
    async def send_message(self, to: str, text: str, reply_to: str = None) -> Dict[str, Any]:
        """Envia mensagem programaticamente."""
        data = {"to": to, "text": text}
        if reply_to:
            data["reply_to"] = reply_to
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/messages/send",
                json=data,
                headers=self.headers
            )
            return response.json()
    
    async def get_message_stats(self) -> Dict[str, Any]:
        """Obtém estatísticas de mensagens."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/messages/stats",
                headers=self.headers
            )
            return response.json()


async def main():
    """Exemplo de uso principal."""
    # Configuração
    BASE_URL = "http://localhost:8080"
    INTERNAL_TOKEN = "seu-token-interno-aqui"  # Configure no .env
    
    client = EvolutionBotClient(BASE_URL, INTERNAL_TOKEN)
    
    try:
        print("🔍 Verificando saúde da aplicação...")
        health = await client.health_check()
        print(f"✅ Status: {health}")
        
        print("\n📊 Obtendo informações da aplicação...")
        info = await client.get_info()
        print(f"📈 Estatísticas: {info}")
        
        print("\n🔧 Verificando instância WhatsApp...")
        instance = await client.ensure_instance()
        print(f"📱 Instância: {instance}")
        
        if not instance.get("connected"):
            print("\n📱 Instância não conectada. Obtenha o QR code:")
            print("Acesse: http://localhost:8080/instance/qr")
            print("(Use o token de autorização no header)")
        
        print("\n💬 Enviando mensagem de teste...")
        message = await client.send_message(
            to="5511999999999",
            text="Olá! Esta é uma mensagem de teste do bot."
        )
        print(f"📤 Mensagem: {message}")
        
        print("\n📈 Estatísticas de mensagens...")
        stats = await client.get_message_stats()
        print(f"📊 Stats: {stats}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")


if __name__ == "__main__":
    print("🚀 Exemplo de uso da Evolution API Bot")
    print("=" * 50)
    
    # Executar exemplo
    asyncio.run(main())
    
    print("\n" + "=" * 50)
    print("📚 Para mais informações, consulte o README.md")
    print("🔗 Documentação da API: http://localhost:8080/docs")
