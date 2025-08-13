# Especificação de Endpoints do Backend FastAPI

> **Nota**: Sorteios são criados via Replit Admin Web. Os endpoints abaixo são do Backend FastAPI para operação do bot.

## POST `/webhook/evolution`
- Objetivo: receber mensagens do WhatsApp (texto/mídia)
- Request: payload EvolutionAPI (texto ou mídia + metadados)
- Response: 200 sempre (processamento idempotente/assíncrono)

## GET `/giveaways`
- Objetivo: listar sorteios criados via Replit (diagnóstico/operação)

## GET `/giveaways/{id}`
- Objetivo: obter regras (`rules_md`) e metadados de sorteio criado no Replit

## GET `/sessions/{whatsapp_id}/status`
- Objetivo: snapshot para dashboard CX
- Exemplo:
```json
{
  "step": 2,
  "docs_ok": ["CPF", "RG"],
  "deadline": "2025-06-18T14:05:00Z",
  "human_intervention": false
}
```
