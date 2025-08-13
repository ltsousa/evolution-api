# Interview Analysis: Sorteios

## Overview
- **Interviewee Name:** Not specified (Process expert/stakeholder)
- **Date of Interview:** Not specified
- **Interviewer Name:** Not specified

## Key Insights

### People Involved:
- **Equipe Interna/Responsável pelo Processo**: Realiza todas etapas manuais de identificação, contato e follow-up com ganhadores
- **Time de CRM**: Tentou disparo automático de WhatsApp (problemas com bloqueios)
- **Time de Desenvolvimento/Suporte do Sistema**: Responsável pelo sistema de sorteios
- **Pedrinho (ex-PM)**: Pessoa chave com conhecimento sobre o sistema para soluções de automação
- **Caixa Econômica Federal**: Entidade externa que sorteia o número oficial
- **Times de Parceiros**: Responsáveis por envio de prêmios específicos (ex: time da Brahma)
- **Consumidores/Ganhadores**: Usuários que participam dos sorteios

### Areas Discussed:
- **Processo de Sorteio**: Desde geração de números até entrega de prêmios
- **Identificação de Ganhadores**: Processo manual de matching entre números sorteados e participantes
- **Notificação e Comunicação**: Push notifications e contato via WhatsApp
- **Validação e Desclassificação**: Verificação de pré-requisitos e gestão de lista de espera
- **Entrega de Prêmios**: Diferentes formatos e coordenação com parceiros

### Processes (As-Is Journey):
1. **Base de Ganhadores**: Download manual de "base crua" do sistema com números e dados
2. **Identificação do Ganhador**: Matching manual entre número sorteado e dados do participante
3. **Registro no Sistema**: Inserção manual do ganhador na área de "ganhadores"
4. **Notificação Inicial**: Push notification automática ("Parabéns, você foi sorteado!")
5. **Contato para Coleta**: WhatsApp manual para coletar dados adicionais
6. **Gestão de Desclassificação**: Lista manual de próximos ganhadores com espera de 72h
7. **Esclarecimento de Dúvidas**: Contato manual para confirmar veracidade

## Identified Pain Points

### **Pain Point 1: Excesso de Processos Manuais**
- Identificação manual do ganhador na planilha
- Registro manual no sistema
- Todo processo de contato descrito como "muito manual e trabalhoso"

### **Pain Point 2: Perda de Tempo Operacional**
- Tempo "perdido" em enviar mensagens individuais
- Espera de 72 horas por resposta antes de contatar próximo ganhador
- Follow-ups manuais constantes

### **Pain Point 3: Desconfiança dos Ganhadores**
- Comum ganhadores desconfiarem da veracidade do contato
- Resulta em bloqueios do WhatsApp corporativo
- Força equipe a reforçar que informação está no sistema
- Exemplo: "mandou a gente se f**** e bloqueou o número"

### **Pain Point 4: Escalabilidade Inviável**
- Para sorteios com muitos ganhadores (ex: 500 cupons Shopee)
- Contato manual via WhatsApp se torna incontrolável
- "Se eu tiver 500 pessoas me mandando mensagem, vou perder o controle"

### **Pain Point 5: Complexidade da Coleta de Informações**
- Necessidade de informações diferentes para cada sorteio
- Nome de acompanhante, foto de passaporte/visto
- Torna difícil padronizar contato e coleta

### **Pain Point 6: Notificação Inicial Insuficiente**
- Push notification muito genérica: "Parabéns, você foi sorteado!"
- Não informa como proceder para resgatar
- Gera necessidade de contato manual adicional

### **Pain Point 7: Gestão Manual de Desclassificação**
- Lista manual de próximos ganhadores
- Espera de 72h por resposta antes de avançar
- Processo alonga significativamente o tempo total

### **Pain Point 8: Problemas com Time de CRM**
- Tentativa de automação via CRM falhou
- Problemas com pessoas que bloquearam recebimento de mensagens
- Volta para processo manual

## Needs and Opportunities

### **Need 1: Automatização da Comunicação**
- Automatizar comunicação desde notificação detalhada
- Incluir coleta de informações e envio do prêmio
- Reduzir dependência de WhatsApp manual

### **Need 2: Coleta Padronizada de Dados**
- Desenvolver formulários estruturados dentro do aplicativo
- Content card para diferentes tipos de informação
- Eliminar necessidade de conversas manuais

### **Need 3: Notificação Clara e Confiável**
- Garantir que ganhador saiba inequivocamente que ganhou
- Informar claramente como proceder para resgatar
- Reduzir desconfiança e bloqueios

### **Need 4: Escalabilidade para Grandes Volumes**
- Implementar soluções para sorteios com centenas de ganhadores
- Automação de entrega especialmente para cupons
- Controle eficiente de múltiplos ganhadores

### **Opportunity 1: Formulários Digitais Integrados**
- Content cards no aplicativo para coleta de dados específicos
- Exemplos: dados de acompanhante, passaporte
- Eliminar pedido manual via WhatsApp

### **Opportunity 2: Automação de Entrega de Prêmios**
- Para cupons (Shopee), envio automático via app ou e-mail
- Permitir cópia de código ou inserção em carteira digital
- Crítico para sorteios com centenas de ganhadores

### **Opportunity 3: Integração com Plataformas Parceiras**
- Integrar com Ticket Master, Ingresse, Total Acesso
- Envio automático de ingressos após confirmação
- Eliminar coordenação manual com times de eventos

### **Opportunity 4: Notificação e Local de Resgate Automatizados**
- Foco principal: avisar pessoa para resgatar prêmio
- Fornecer local de resgate automaticamente
- Eliminar mensagens individuais

### **Opportunity 5: Fluxo Híbrido de Contato**
- Combinação de automação com opção de contato manual
- Após formulário no app, botão para WhatsApp pré-preenchido
- Manter flexibilidade para casos especiais

### **Opportunity 6: Aproveitar Conhecimento Interno**
- Colaboração com Pedrinho (ex-PM com experiência no sistema)
- Resolver dependências de integração
- Implementar melhorias técnicas aproveitando recursos existentes

### **Opportunity 7: Sistema Flexível por Tipo de Prêmio**
- Configurar formato do ingresso: PDF, Link, Carteira digital
- Automatizar upload e envio conforme formato
- Análise caso a caso para diferentes abordagens 