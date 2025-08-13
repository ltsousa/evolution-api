# Admin Web — Ingestão de Regulamentos

## Objetivo
Criar sorteio e extrair regras para Markdown, com versionamento e hash para auditoria.

## Interface
- **Plataforma**: Replit com front-end web
- **Funcionalidade**: Upload de PDF via interface gráfica
- **Usuários**: Time interno para criação de sorteios

## Passos
- Upload de PDF via interface web do Replit
- Processamento automático: LLM extrai Markdown das regras
- Sistema salva `rules_md`, `rules_hash` (SHA‑256) e `rules_version`
- Interface exibe preview das regras extraídas
- Revisão humana obrigatória antes de ativar sorteio

## Critérios de aceite
- [ ] Interface web funcional no Replit
- [ ] Upload de PDF com validação (formato, tamanho)
- [ ] `rules_md` fiel ao regulamento extraído
- [ ] `rules_hash` persistido e imutável
- [ ] `rules_version` incrementado a cada alteração
- [ ] Preview das regras antes da confirmação
- [ ] Log de auditoria de criação/edição de sorteios
