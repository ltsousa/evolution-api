# Integração EvolutionAPI (conceito)

## Enviar mensagem
- Usar endpoint de envio com `template_id` + variáveis

## Marcar conversa como não lida (handoff humano)
- Endpoint de conversa com flag `unread`

## Receber mídia (webhook)
- Webhook recebe metadados
- Backend baixa conteúdo bruto e processa arquivos
- Registro criado em `uploads`

## Notas operacionais
- Setup de tokens/instância feito por humano; código apenas consome rotas
- Tratar retries e idempotência
