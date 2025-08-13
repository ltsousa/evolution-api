### V0 Manual — WhatsApp Proativo (CTA)

**Objetivo**: Documentar a primeira versão (V0) do processo em que o cliente inicia proativamente o contato via WhatsApp a partir de um call to action (CTA) pré-configurado, com a mensagem: "Fui contemplado no sorteio {Nome do sorteio} com o número sorteado {Número}." A partir desse primeiro contato, o time responde de forma natural e livre, sem templates ou organizações estruturadas.

#### Escopo da V0
- **Incluído**:
  - **WhatsApp** como canal único de entrada (mensagem iniciada pelo cliente).
  - **Mensagem CTA fixa** no material de comunicação (e-mail/SMS/push/etc.).
  - **Atendimento 100% humano** livre e natural após a primeira mensagem do cliente.
- **Fora de escopo**:
  - Qualquer automação de bot, validações sistêmicas ou integrações (Braze, S3, banco de dados, etc.).
  - Coleta de documentos/arquivos por fluxo automatizado.
  - Regras de prazo e alertas automáticos.
  - Registro em planilhas ou ferramentas externas.
  - Templates de resposta ou organização estruturada das conversas.

#### Fluxo resumido
1) Cliente recebe a comunicação de premiação e clica no CTA.
2) Abre o WhatsApp com texto pré-preenchido: "Fui contemplado no sorteio {Nome do sorteio} com o número sorteado {Número}."
3) Cliente envia a mensagem.
4) Equipe de atendimento responde de forma natural, valida dados básicos e conduz os próximos passos.

#### Entregáveis desta V0
- `01-escopo-v0.md`: limites, requisitos e responsabilidades.
- `02-mensagens-cta.md`: mensagem padrão do CTA e diretrizes de atendimento.
- `03-operacao-suporte.md`: procedimento operacional com checklist básico.
- `04-criterios-aceitacao-checklist.md`: checklist de go-live e testes.
- `05-faq.md`: dúvidas recorrentes e tratativas.

#### SLAs e Qualidade (V0)
- **Tempo de primeira resposta**: até 2 horas úteis.
- **Atendimento natural**: sem templates obrigatórios, focando em parabenizar, confirmar dados e explicar próximos passos.


