# Modelo de Dados (PostgreSQL)

## Tabelas
| Tabela | Chave | Campos |
|-------|------|--------|
| `giveaways` | `id` UUID | `name`, `number_format`, `rules_md`, `rules_hash`, `rules_version`, `created_at` |
| `sessions` | `whatsapp_id` PK | `giveaway_id`, `drawn_number`, `email`, `human_intervention` BOOL, `step` INT, `docs_ok` JSONB, `deadline` TIMESTAMP |
| `uploads` | `id` UUID | `whatsapp_id`, `type`, `url`, `uploaded_at`, `valid` BOOL |

> Estado mínimo por usuário: `human_intervention`, `step` (0–4), `docs_ok` (array), `deadline`.

## Tipos de Documento (enum lógico)
```
CPF, RG, CNH, COMPROVANTE_RESIDENCIA,
PASSAPORTE_GANHADOR, PASSAPORTE_ACOMP,
VISTO_GANHADOR, VISTO_ACOMP,
VACINA_GANHADOR, VACINA_ACOMP
```

## Migrações — Checklist
- [ ] Criar `giveaways` com índices: (`name`), (`rules_hash`)
- [ ] Criar `sessions` com FK para `giveaways(id)`
- [ ] Criar `uploads` com índice por `whatsapp_id` e `uploaded_at`
- [ ] Constraints: tamanho máximo `docs_ok`, `step` entre 0 e 4

## Esboço SQL (referência)
```sql
CREATE TABLE giveaways (
  id uuid PRIMARY KEY,
  name text NOT NULL,
  number_format text,
  rules_md text NOT NULL,
  rules_hash text NOT NULL,
  rules_version text NOT NULL,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE sessions (
  whatsapp_id text PRIMARY KEY,
  giveaway_id uuid REFERENCES giveaways(id),
  drawn_number text,
  email text,
  human_intervention boolean DEFAULT false,
  step int DEFAULT 0,
  docs_ok jsonb DEFAULT '[]',
  deadline timestamptz
);

CREATE TABLE uploads (
  id uuid PRIMARY KEY,
  whatsapp_id text NOT NULL,
  type text NOT NULL,
  url text NOT NULL,
  valid boolean DEFAULT true,
  uploaded_at timestamptz DEFAULT now()
);
```
