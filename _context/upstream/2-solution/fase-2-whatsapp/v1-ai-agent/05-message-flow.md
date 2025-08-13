# Fluxo de Mensagens

## Regras Gerais
- Se `human_intervention=true`: responder com atendimento humano em andamento
- Stateless no LLM: backend envia regras + snapshot a cada chamada

## Primeiro Contato
1. Extrair `nome_sorteio` + `numero_sorteado`
2. Buscar `rules_md` e persistir `giveaway_id` + `drawn_number`
3. Perguntar: “Qual o seu email cadastrado?”

## Validação de Email (Braze)
- OK: `deadline=now()+72h`, `step=1`, `docs_ok=[]`, agenda alertas, envia ETAPA 1/4
- Falha: template “Email não encontrado”

## Fluxo em Andamento
- Uploads: salvar arquivos, atualizar `docs_ok`, validar extensão/tamanho
- Comando “PRÓXIMO”: verifica completude da etapa
  - Completa → `step += 1` e envia próxima etapa
  - Incompleta → lista pendências
- Finalização: se `step > 4` e todos docs obrigatórios ok
  - Mensagem de análise + `human_intervention=true` + marcar conversa como não lida

## Pseudocódigo (resumo)
```pseudo
on_webhook(msg):
  extract whatsapp_id, text_or_media
  upsert session if missing (human_intervention=False, step=0)
  if session.human_intervention:
    reply("Seu atendimento está com nossa equipe. Aguarde, por favor.")
    return
  if is_first_contact(session):
    handle_first_contact(text)
  else:
    handle_in_flow(text_or_media)
```
