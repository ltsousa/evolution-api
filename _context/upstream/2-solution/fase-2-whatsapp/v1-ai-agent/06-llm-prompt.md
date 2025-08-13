# Design de Prompt (LLM)

## Payload (todas as chamadas)
```json
[
  {"role":"system","content":"⚠️ NUNCA altere prazos/datas ou a lista de documentos obrigatórios. Siga estritamente o regulamento."},
  {"role":"system","name":"rules","content":"<rules_md (markdown do sorteio, trecho relevante/resumo)>"},
  {"role":"assistant","name":"context","content":"{\"step\":2,\"docs_ok\":[\"CPF\",\"RG\"],\"deadline\":\"2025-06-18T14:05:00Z\",\"human_intervention\":false}"},
  {"role":"user","content":"<mensagem do usuário>"}
]
```

## Guardrails (system)
- Nunca inventar informações fora do regulamento
- Não responder sobre outros sorteios
- Não alterar prazos/datas/documentos
- Se `human_intervention=true`, não responder
- Respeitar mensagens padronizadas

## Parâmetros
- Modelo: gpt-4o
- `temperature = 0`, `top_p = 0`

## Auditoria
- Logar: `system`, `rules`, `snapshot`, `user`, `assistant` (trilha completa)
