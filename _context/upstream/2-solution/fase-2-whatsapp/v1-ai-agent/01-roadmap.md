# Roadmap e Backlog Priorizado

Fonte: `whatsapp_agent.md` §8 (Ordem de Desenvolvimento) + complementos operacionais.

## Legenda
- [ ] não iniciado  • [~] em progresso  • [x] concluído

## M1 — Fundações
- [ ] Projeto FastAPI (Python 3.12) + Dockerfile
- [ ] Config de ambiente (Postgres, Braze, EvolutionAPI)
- [ ] Estrutura de pastas, linters e logs estruturados
- **Critérios de aceite**
  - [ ] App roda localmente (Docker Compose)
  - [ ] Healthcheck ok e logs JSON

## M2 — Dados e Persistência
- [ ] Migrations: `giveaways`, `sessions`, `uploads`
- [ ] Repositórios e camada de acesso a dados
- **Critérios de aceite**
  - [ ] Migrações idempotentes
  - [ ] Índices e constraints essenciais

## M3 — Webhook EvolutionAPI
- [ ] POST `/webhook/evolution` (texto e mídia)
- [ ] Upsert de `sessions` e gating por `human_intervention`
- [ ] Upload assíncrono de mídia (placeholder)
- **Critérios de aceite**
  - [ ] Mensagens de texto persistem sessão
  - [ ] Mídia gera registro em `uploads` com metadados

## M4 — Primeiro Contato + Braze (mock)
- [ ] Parse de sorteio (nome + número)
- [ ] Busca das `rules_md` e storage de `giveaway_id`
- [ ] Validação de email via mock Braze
- [ ] Definição de `deadline`, `step=1`, `docs_ok=[]`
- **Critérios de aceite**
  - [ ] Fluxo feliz: primeiro contato → email válido → ETAPA 1/4 enviada
  - [ ] Email inválido dispara template de erro

## M5 — Sistema de Uploads + Validação
- [ ] Upload binário (JPG, PNG, PDF; ≤ 10 MB)
- [ ] Atualização de `docs_ok` por tipo
- [ ] Rejeição com motivo (extensão/tamanho)
- **Critérios de aceite**
  - [ ] Arquivos válidos são processados e registrados
  - [ ] Inválidos retornam template padronizado

## M6 — LLM Prompt Engine
- [ ] Builder injeta `rules_md` + snapshot a cada chamada
- [ ] Guardrails de system prompt; temp=0; top_p=0
- [ ] Auditoria completa: `system`, `rules`, `snapshot`, `user`, `assistant`
- **Critérios de aceite**
  - [ ] Respostas consistentes e determinísticas
  - [ ] Logs completos para auditoria

## M7 — Motor de Etapas
- [ ] Comandos “PRÓXIMO/CONTINUAR”
- [ ] Verificação de completude por etapa
- [ ] Proibição de avanço pelo LLM (somente backend)
- **Critérios de aceite**
  - [ ] Etapa só avança com pré‑requisitos atendidos
  - [ ] Pendências listadas corretamente

## M8 — Scheduler de Prazos
- [ ] Agendamentos T-12h, T-3h, T-1h, T-0
- [ ] Expiração seta `human_intervention=true`
- [ ] Cancelamentos em handoff
- **Critérios de aceite**
  - [ ] Jobs criados ao validar email e cancelados no handoff
  - [ ] Mensagens de prazo enviadas nos horários corretos

## M9 — Status + Dashboard CX
- [ ] GET `/sessions/{whatsapp_id}/status`
- [ ] JSON com `step`, `docs_ok`, `deadline`, `human_intervention`
- **Critérios de aceite**
  - [ ] Dashboard consome snapshot sem acoplamento

## M10 — Integrações Reais + Deploy
- [ ] EvolutionAPI (envio/marcação não lida)
- [ ] Braze (validação real)

- [ ] Deploy com observabilidade
- **Critérios de aceite**
  - [ ] p95 ≤ 2s sob carga de 500 sessões
  - [ ] Logs e métricas disponíveis no dashboard

## Riscos e Mitigações
- **Ambiguidade de regulamentos**: revisão humana obrigatória no Admin Web (Replit)
- **Carga concorrente**: filas/worker para uploads e mensagens
- **LGPD/PII**: mascarar logs e restringir acesso a arquivos
