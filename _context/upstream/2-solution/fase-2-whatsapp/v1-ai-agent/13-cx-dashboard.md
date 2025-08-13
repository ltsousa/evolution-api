# Dashboard CX — Contrato do Snapshot

## GET `/sessions/{whatsapp_id}/status`
- Campos:
  - `step` (0–4)
  - `docs_ok` (array de tipos)
  - `deadline` (ISO8601)
  - `human_intervention` (bool)

### Exemplo
```json
{
  "step": 2,
  "docs_ok": ["CPF", "RG"],
  "deadline": "2025-06-18T14:05:00Z",
  "human_intervention": false
}
```
