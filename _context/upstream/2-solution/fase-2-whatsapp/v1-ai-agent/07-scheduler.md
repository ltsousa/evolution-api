# Agendamento de Prazos

## Jobs ao validar email
- T‑12h: alerta de prazo
- T‑3h: alerta
- T‑1h: última chamada
- T‑0: expira → envia “❌ PRAZO VENCIDO” e `human_intervention=true`

## Cancelamentos
- Cancelar todos os jobs se houver handoff humano antes do prazo

## Considerações
- Idempotência dos jobs
- Timezone: UTC no backend; mensagens com horário local se necessário
- Persistir referências de jobs para cancelamento
