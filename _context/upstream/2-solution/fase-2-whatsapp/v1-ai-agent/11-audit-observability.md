# Auditoria e Observabilidade

## Logs (estruturados)
- Campos por requisição LLM: `system`, `rules_hash`, `rules_version`, `snapshot`, `user`, `assistant`
- Eventos: criação/atualização de sessão, upload, avanço de etapa, agendamento/cancelamento, expiração
- PII mascarada: email, whatsapp_id (hash/salt)

## Métricas
- Contadores por etapa, rejeições de upload, expirações
- Latência por rota e por provedor (LLM, Braze, EvolutionAPI)
- Taxa de handoff e tempo médio até conclusão

## Traços
- Distribuídos por webhook → processamento → chamadas externas
