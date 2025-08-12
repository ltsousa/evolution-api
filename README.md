# Evolution API Bot

Bot WhatsApp inteligente usando Evolution API v2 e OpenAI para respostas automáticas.

## 🚀 Características

- **Webhook automático**: Processa mensagens recebidas via Evolution API
- **IA integrada**: Respostas inteligentes usando OpenAI GPT
- **Idempotência**: Evita processamento duplicado de mensagens
- **Fila assíncrona**: Sistema de fila para envio de mensagens
- **Gerenciamento de instâncias**: Criação e controle automático de instâncias WhatsApp
- **Segurança**: Endpoints internos protegidos por Bearer Token
- **Observabilidade**: Logs estruturados com correlação de requisições
- **Docker**: Containerização completa com healthcheck

## 📋 Pré-requisitos

- Python 3.9+
- Evolution API v2 rodando
- Conta OpenAI com API key
- Docker e Docker Compose (opcional)

## 🛠️ Instalação

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd evolution-api-bot
```

### 2. Configure as variáveis de ambiente

Copie o arquivo de exemplo e configure:

```bash
cp env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
EVOLUTION_BASE_URL=https://seu-host-evolution.com
EVOLUTION_API_KEY=seu-token-evolution
EVOLUTION_INSTANCE_NAME=whatsapp-bot
OPENAI_API_KEY=sua-api-key-openai
OPENAI_MODEL=gpt-4o-mini
BOT_SYSTEM_PROMPT="Você é um assistente educado e direto."
WEBHOOK_SECRET=seu-secret-webhook-opcional
INTERNAL_API_TOKEN=seu-token-interno
PORT=8080
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python -m app.main
```

A aplicação estará disponível em `http://localhost:8080`

## 🐳 Usando Docker

### Build e execução

```bash
# Build da imagem
docker build -t evolution-api-bot .

# Execução
docker-compose up -d
```

### Verificar status

```bash
docker-compose ps
docker-compose logs -f app
```

## 🔧 Configuração da Evolution API

### 1. Configure o webhook

Na sua Evolution API, configure o webhook para:

```
URL: http://seu-servidor:8080/webhook/
Eventos: messages.upsert, connection.update
```

### 2. Verifique a instância

```bash
curl -X POST http://localhost:8080/instance/ensure \
  -H "Authorization: Bearer SEU_INTERNAL_API_TOKEN"
```

### 3. Obtenha o QR code

```bash
curl http://localhost:8080/instance/qr \
  -H "Authorization: Bearer SEU_INTERNAL_API_TOKEN"
```

## 📡 Endpoints da API

### Públicos

- `GET /` - Informações da aplicação
- `GET /healthz` - Healthcheck
- `GET /info` - Estatísticas da aplicação
- `POST /webhook/` - Webhook da Evolution API

### Protegidos (Bearer Token)

- `POST /messages/send` - Enviar mensagem programaticamente
- `GET /messages/stats` - Estatísticas de mensagens
- `POST /instance/ensure` - Garantir instância ativa
- `GET /instance/qr` - QR code para conexão
- `GET /instance/status` - Status da instância

## 🧪 Testes

Execute os testes com pytest:

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements.txt[dev]

# Executar todos os testes
pytest

# Executar com verbose
pytest -v

# Executar testes específicos
pytest tests/test_webhook.py
```

## 📊 Monitoramento

### Logs estruturados

A aplicação usa `structlog` para logs em JSON com campos:

- `event`: Tipo do evento
- `message_id`: ID da mensagem
- `wa_from`: Número de origem
- `wa_to`: Número de destino
- `status`: Status da operação
- `latency_ms`: Latência em milissegundos
- `request_id`: ID de correlação

### Healthcheck

Endpoint `/healthz` para monitoramento Docker/Kubernetes.

### Métricas

Endpoint `/info` retorna estatísticas da aplicação.

## 🔒 Segurança

- **Endpoints internos**: Protegidos por Bearer Token
- **Validação de webhook**: Suporte a assinatura (opcional)
- **Usuário não-root**: Container roda como usuário não-privilegiado
- **CORS configurável**: Middleware CORS configurável

## 🚨 Troubleshooting

### Instância não conecta

1. Verifique se a Evolution API está rodando
2. Confirme as credenciais no `.env`
3. Use `/instance/ensure` para criar/iniciar a instância
4. Acesse `/instance/qr` para conectar o WhatsApp

### Webhook não recebe mensagens

1. Verifique a URL do webhook na Evolution API
2. Confirme se o servidor está acessível externamente
3. Verifique os logs da aplicação
4. Teste o endpoint `/webhook/` manualmente

### Erro de OpenAI

1. Confirme a API key no `.env`
2. Verifique o limite de uso da OpenAI
3. Confirme se o modelo especificado está disponível

## 📝 Desenvolvimento

### Estrutura do projeto

```
app/
├── __init__.py
├── config.py          # Configurações
├── models.py          # Modelos Pydantic
├── evolution_client.py # Cliente Evolution API
├── openai_client.py   # Cliente OpenAI
├── idempotency.py     # Sistema de idempotência
├── queue.py           # Fila de mensagens
├── webhook.py         # Roteador de webhook
├── messages.py        # Roteador de mensagens
├── instance.py        # Roteador de instâncias
└── main.py            # Aplicação principal

tests/
├── __init__.py
├── conftest.py        # Configuração pytest
├── test_webhook.py    # Testes de webhook
├── test_sender.py     # Testes de envio
└── test_instance.py   # Testes de instância
```

### Adicionando novos endpoints

1. Crie o roteador em `app/`
2. Adicione as rotas no `main.py`
3. Crie testes correspondentes
4. Documente no README

### Logs personalizados

```python
import structlog

logger = structlog.get_logger()
logger.info("Evento personalizado", campo_extra="valor")
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para detalhes.

## 🆘 Suporte

Para suporte e dúvidas:

- Abra uma issue no GitHub
- Consulte a documentação da [Evolution API](https://doc.evolution-api.com)
- Verifique os logs da aplicação

---

**Nota**: Este bot é para uso educacional e de desenvolvimento. Respeite as políticas de uso do WhatsApp e OpenAI.
