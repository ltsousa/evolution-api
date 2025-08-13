# Análise Detalhada dos Processos de Experiências

## Visão Geral

As **"Experiências"** são um benefício oferecido aos consumidores do aplicativo, onde eles podem acumular pontos e trocá-los por ingressos para jogos, eventos ou outras experiências diferenciadas. Essas experiências são distintas dos "sorteios", e ocorrem com frequência no dia a dia, como jogos e eventos.

---

## 1. Como Funcionam as Experiências (Funcionalidade)

O aplicativo permite que o consumidor utilize pontos para fazer a troca por uma experiência. Uma vez que a troca é realizada, o processo de entrega do ingresso ou acesso à experiência se inicia, sendo atualmente um processo **majoritariamente manual**.

---

## 2. Processos Envolvidos

### 2.1 Mapeamento das Oportunidades (Geração de Eventos)

As oportunidades de eventos e experiências são geradas por **duas fontes principais**:

#### **Administração Central (AC)**
- Responsável por eventos grandes e conhecidos nacionalmente
- Negociações de patrocínio em nível de país 
- Exemplo: Numanice da Ludmilla

#### **Regionais**
- Responsáveis por eventos menores ou locais
- Mesmo que ocorram em vários lugares, cada local pode ter um dono diferente
- Exemplo: festas como Arca de Noé

#### **Processo de Mapeamento**
- Oportunidades são passadas para a equipe em **planilha compartilhada**
- Cada regional preenche informações:
  - Nome do evento
  - Data e horário
  - Local
  - Setor
  - Quantidade de ingressos
  - Formato (digital, PDF)
  - Aplicativo específico para o ingresso (ex: Ingresse)

### 2.2 Cadastro no Sistema

- **Responsável**: Estagiária
- **Processo**: Cadastro dos eventos no sistema baseado na planilha
- **Limitação**: Não há aviso automático no aplicativo quando um evento é fechado ou esgotado
- **Acompanhamento**: Manual pela estagiária através da planilha

### 2.3 Acompanhamento do Resgate

#### **Processo Atual**
1. Estagiária extrai dados do **metabase** (base de dados) para verificar eventos do dia
2. Baixa planilha com informações das pessoas que resgataram ingressos
3. **Importante**: O ingresso não é recebido automaticamente no momento do resgate
4. Contato e envio só ocorrem após o término do período de resgate

**Exemplo**: Se o resgate termina no dia 5, ela entrará em contato apenas no dia 5, mesmo que a pessoa tenha resgatado no dia 2.

### 2.4 Entrega/Disponibilização do Ingresso

> **Ponto de maior complexidade e trabalho manual**

#### **Formatos e Processos por Plataforma**

##### **Ticketmaster**
- Consumidor informa e-mail da Ticketmaster
- E-mail enviado manualmente para o time de eventos da companhia
- **Follow-up manual** necessário para confirmar se o envio foi feito
- **Notificação manual via WhatsApp** para informar que o ingresso foi enviado
- Exemplo: "Oi, tudo bem, enviamos ingressos na sua Ticketmaster, confira por favor"

##### **PDF**
- Estagiária pega WhatsApp da pessoa na planilha
- Envia PDF manualmente pelo WhatsApp
- Se PDF não foi enviado pela regional, precisa cobrar a regional

##### **Ingresse/Sympla (Carteira Digital)**
- E-mails dos usuários enviados para a regional
- Ingresso depositado diretamente na carteira do aplicativo
- Regional confirma o envio
- Aviso manual ao consumidor via WhatsApp (muitos não verificam o app da Ingresse)

##### **Link**
- Para alguns times de futebol (ex: Flamengo)
- Link enviado manualmente ao consumidor

##### **Cadastro Facial / Acompanhante**
- Casos como Total Acesso (exige cadastro facial)
- Direito a acompanhante
- Contato manual para coletar informações adicionais

##### **Parceiros Externos**
- Exemplos: Carnaval com Bramba, camarote de São Paulo com Total Acesso
- Entrega feita por parceiros externos
- Exige planilhas compartilhadas e follow-ups constantes

---

## 3. Times Envolvidos

### 3.1 Externos
- **Administração Central (AC)**: Fonte de grandes oportunidades de eventos
- **Regionais**: 
  - Fontes de oportunidades de eventos locais
  - Cada uma com seu diretor, pessoa de eventos e gerente de marketing
  - Envolvidas no processo de envio/confirmação de ingressos
- **Time de Área de Eventos da Companhia**: Responsáveis por enviar alguns ingressos (ex: Ticketmaster)
- **Parceiros Externos**: Plataformas e empresas que gerenciam os ingressos
- **Consumidores**: Usuários que resgatam as experiências

### 3.2 Internos
- **Estagiária**: 
  - Cadastro de eventos
  - Acompanhamento de resgates
  - Contato inicial para entrega de ingressos
- **Pessoa Responsável pelo Processo**: 
  - Follow-ups com o time de eventos da companhia
  - Follow-ups com parceiros
  - Envio de mensagens via WhatsApp para os consumidores

---

## 4. Dores e Necessidades

### 4.1 Principais Dores Identificadas

#### **Processos Excessivamente Manuais**
- Quase totalidade do fluxo de entrega é manual
- Desde verificação das bases de dados até mensagens de WhatsApp
- Processo descrito como "muito manual e muito caótico"

#### **Falta de Automação na Entrega**
- Não há sistema automático de envio no momento do resgate
- Gera atrasos e dependência de ações humanas

#### **Alto Volume de Comunicação Manual**
- Mensagens individuais via WhatsApp para cada consumidor
- Extremamente demorado
- Pode levar à perda de controle em grandes volumes

#### **Dependência de Terceiros**
- Follow-ups manuais e frequentes necessários
- Pode causar atrasos e esquecimentos

#### **Informações Fragmentadas**
- Uso de planilhas compartilhadas
- Grupos de WhatsApp
- E-mails para gerenciar informações
- Processo ineficiente e propenso a erros

#### **Experiência do Consumidor Ruim**
- Atrasos na entrega
- Falta de comunicação automática
- Necessidade de verificar outros aplicativos
- Gera dúvidas e desconfiança

#### **Diversidade de Formatos de Ingresso**
- Multiplicidade de formatos (PDF, links, carteiras digitais, cadastro facial)
- Dificulta padronização e automação

#### **Sem Notificação de Evento Esgotado/Fechado**
- Falta de aviso automático no aplicativo
- Acompanhamento manual pela estagiária

---

## 5. Objetivos e Oportunidades de Melhoria

### 5.1 Objetivo Principal
Melhorar a eficiência e a experiência do consumidor nas entregas de experiências, tornando o processo menos manual e caótico.

### 5.2 Oportunidades de Automação e Padronização

#### **Automação da Comunicação e Entrega**

##### **In-app Delivery/Notificação**
- Criar seção no aplicativo para acesso direto ao link ou ingresso
- Implementar através de "content card" (formulário no app)
- Usuário preenche ou visualiza informações necessárias

##### **Notificações Push Automáticas**
- Enviar notificações push ou mensagens automáticas no aplicativo
- Informar status da entrega do ingresso
- Evitar necessidade de contato manual via WhatsApp

##### **Integração com Plataformas Parceiras**
- Desenvolver integrações com Ticketmaster, Ingresse e outras
- Envio ou confirmação automática dos ingressos
- Sem necessidade de intervenção manual da equipe

##### **Automatização de Coleta de Dados Adicionais**
- Para casos que exigem informações específicas (acompanhante, foto do passaporte)
- Formulário dinâmico no aplicativo disparado automaticamente
- Reduzir conversa manual

#### **Centralização da Gestão de Eventos**

##### **Interface Unificada**
- Para AC e Regionais cadastrarem oportunidades de eventos
- Integração direta com sistema de gestão de experiências
- Garantir dados mais consistentes e atualizados

##### **Alertas Automáticos**
- Quando ingressos de um evento estiverem esgotando
- Quando evento for fechado no sistema

#### **Redução da Dependência Humana**
- Transformar equipe em gestores do processo automatizado
- Em vez de executores manuais
- Liberar tempo para tarefas mais estratégicas

### 5.3 Priorização

**Foco inicial**: "Como avisar a pessoa para resgatar, dando o local de resgate para ela automaticamente, sem precisar ter que ficar mandando mensagem um por um para a parte de experiência".

---

## 6. Informações Importantes

### 6.1 Sobre Pedrinho (Pedro)

**Contexto**: Pedrinho não faz parte do processo operacional atual de Experiências.

**Perfil**: 
- Ex-PM que trabalhou anteriormente com o sistema utilizado
- Valiosa fonte de consulta para tirar dúvidas sobre:
  - Funcionamento do sistema
  - Capacidades do sistema
- Especialmente útil na fase de implementação de soluções
- Pode fornecer clareza sobre o sistema sem necessidade de falar diretamente com a equipe de desenvolvimento