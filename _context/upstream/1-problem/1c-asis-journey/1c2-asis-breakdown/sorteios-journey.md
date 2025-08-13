# As-Is Journey: Sorteios

## Stage 1: Base de Ganhadores

### Stage Overview
- **Stage Name:** Extração e Preparação de Dados
- **Description:** Após sorteio da Caixa Econômica Federal, equipe baixa "base crua" do sistema com todos os números e dados dos participantes
- **Objective:** Obter lista completa de participantes para identificar o ganhador oficial

### Tools Involved
- **Sistema de Gestão:** Fonte da base de dados de participantes
- **Planilha/Excel:** Para organizar e manipular dados extraídos
- **Número Oficial CEF:** Resultado do sorteio da Caixa Econômica Federal

### Pain Points
- **Processo Manual:** Download e organização manual de dados
- **Volume de Dados:** Base "crua" contém todos os participantes
- **Complexidade:** Processo descrito como "bem porco" e complexo

### Needs
- **Automação de Extração:** Sistema deveria processar dados automaticamente
- **Filtragem Inteligente:** Mostrar apenas dados relevantes
- **Interface Simplificada:** Reduzir complexidade do processo

### Opportunities
- **Automação Completa:** Sistema processa resultado da CEF automaticamente
- **Dashboard Intuitivo:** Interface visual para navegação dos dados
- **Integração Direta:** Conexão automática com sistema da CEF

---

## Stage 2: Identificação do Ganhador

### Stage Overview
- **Stage Name:** Matching Manual de Ganhador
- **Description:** Busca manual do número sorteado pela CEF na planilha de participantes para identificar o ganhador
- **Objective:** Encontrar exatamente qual pessoa corresponde ao número sorteado

### Tools Involved
- **Planilha de Participantes:** Contém números da sorte e dados pessoais
- **Número Sorteado CEF:** Número oficial do sorteio
- **Ferramentas de Busca:** Ctrl+F ou filtros manuais

### Pain Points
- **Busca Manual:** Processo suscetível a erros humanos
- **Tempo Consumido:** Demora para localizar o ganhador correto
- **Risco de Erro:** Possibilidade de identificar pessoa errada

### Needs
- **Busca Automática:** Sistema deveria encontrar ganhador automaticamente
- **Validação Cruzada:** Confirmar identidade do ganhador
- **Backup Automático:** Lista de próximos ganhadores gerada automaticamente

### Opportunities
- **Matching Automático:** Algoritmo identifica ganhador instantaneamente
- **Validação Multi-nivel:** Confirmações automáticas de identidade
- **Lista Ordenada:** Sequência automática de próximos ganhadores

---

## Stage 3: Registro no Sistema

### Stage Overview
- **Stage Name:** Inserção Manual do Ganhador
- **Description:** Entrada manual na área de "ganhadores" do sistema, digitando número da sorte e selecionando como ganhador
- **Objective:** Oficializar o ganhador no sistema para disparo da notificação

### Tools Involved
- **Sistema de Gestão:** Interface de área de ganhadores
- **Número da Sorte:** Identificador do ganhador
- **Interface Manual:** Formulários para inserção de dados

### Pain Points
- **Entrada Manual:** Re-digitação de informações já existentes no sistema
- **Dependência Humana:** Processo não pode ser automatizado
- **Único Ponto de Falha:** Apenas uma pessoa pode fazer o registro

### Needs
- **Registro Automático:** Sistema deveria registrar ganhador automaticamente
- **Múltiplos Usuários:** Várias pessoas deveriam poder registrar
- **Validação de Dados:** Confirmação automática antes do registro

### Opportunities
- **Fluxo Automático:** Do resultado CEF direto para registro no sistema
- **Aprovação Multi-nivel:** Diferentes níveis de confirmação
- **Auditoria Automática:** Log completo de todas as ações

---

## Stage 4: Notificação Inicial

### Stage Overview
- **Stage Name:** Push Notification Automática
- **Description:** Único processo automático - ganhador recebe push notification genérica no celular
- **Objective:** Informar inicialmente que a pessoa foi sorteada

### Tools Involved
- **Sistema de Push:** Serviço de notificações push
- **Aplicativo Mobile:** App do consumidor
- **Template Genérico:** Mensagem padrão "Parabéns, você foi sorteado!"

### Pain Points
- **Notificação Insuficiente:** Mensagem muito genérica sem detalhes
- **Falta de Instruções:** Não informa próximos passos
- **Aparência de Spam:** Pode parecer mensagem falsa

### Needs
- **Notificação Rica:** Incluir detalhes do prêmio e instruções
- **Credibilidade:** Aparência oficial e confiável
- **Call-to-Action:** Direcionamento claro sobre o que fazer

### Opportunities
- **Notificação Inteligente:** Personalizada por tipo de prêmio
- **Rich Media:** Incluir imagens, links, botões de ação
- **Verificação Fácil:** Link direto para confirmar no app

---

## Stage 5: Contato para Coleta

### Stage Overview
- **Stage Name:** Comunicação Manual via WhatsApp
- **Description:** Equipe entra em contato via WhatsApp corporativo para coletar dados adicionais necessários
- **Objective:** Obter informações específicas do prêmio (acompanhante, passaporte, etc.)

### Tools Involved
- **WhatsApp Corporativo:** Canal principal de comunicação
- **Scripts de Conversa:** Templates para diferentes situações
- **Planilha de Controle:** Para rastrear status das conversas

### Pain Points
- **Desconfiança:** Ganhadores suspeitam que é fraude
- **Bloqueios:** Pessoas bloqueiam o número corporativo
- **Volume Manual:** Inviável para muitos ganhadores simultâneos
- **Coleta Complexa:** Diferentes informações para cada tipo de prêmio

### Needs
- **Canal Oficial:** Comunicação através do próprio app
- **Formulários Estruturados:** Coleta padronizada de informações
- **Escalabilidade:** Processo que funcione para qualquer volume
- **Credibilidade:** Reduzir aparência de fraude

### Opportunities
- **Content Cards:** Formulários no app para coleta de dados
- **Comunicação In-App:** Chat oficial dentro do aplicativo
- **Automação Híbrida:** Formulário + opção de contato humano
- **Validação Automática:** Verificação de documentos quando necessário

---

## Stage 6: Gestão de Desclassificação

### Stage Overview
- **Stage Name:** Controle de Lista de Backup
- **Description:** Manutenção manual de lista de próximos ganhadores com espera de 72h por resposta antes de avançar
- **Objective:** Garantir que prêmio seja entregue mesmo com desclassificações

### Tools Involved
- **Lista Manual:** Sequência de próximos ganhadores
- **Timer de 72h:** Controle manual de tempo de espera
- **Planilha de Status:** Acompanhamento de cada ganhador

### Pain Points
- **Gestão Manual:** Lista e timers controlados manualmente
- **Tempo Excessivo:** 72h de espera alonga muito o processo
- **Perda de Controle:** Múltiplos ganhadores em diferentes estágios
- **Processo Lento:** Pode levar semanas para definir ganhador final

### Needs
- **Automação de Timers:** Sistema controla tempos automaticamente
- **Gestão Inteligente:** Fluxo automático para próximo ganhador
- **Visibilidade Total:** Dashboard de status de todos os ganhadores
- **Tempos Flexíveis:** Configuração de prazos por tipo de prêmio

### Opportunities
- **Workflow Automático:** Sistema gerencia toda a sequência
- **Notificações Escalonadas:** Lembretes antes do timeout
- **Dashboard de Controle:** Visão unificada de todos os processos
- **Regras Configuráveis:** Diferentes fluxos para diferentes prêmios

---

## Stage 7: Esclarecimento de Dúvidas

### Stage Overview
- **Stage Name:** Suporte e Confirmação de Veracidade
- **Description:** Atendimento manual para esclarecer dúvidas dos ganhadores sobre legitimidade do sorteio
- **Objective:** Convencer ganhadores de que o contato é legítimo e confirmar participação

### Tools Involved
- **WhatsApp:** Canal principal para esclarecimentos
- **Aplicativo:** Para mostrar que informação está no sistema
- **Scripts de Atendimento:** Respostas padronizadas para dúvidas comuns

### Pain Points
- **Desconfiança Persistente:** Mesmo com explicações, pessoas desconfiam
- **Tempo Perdido:** Muito esforço para convencer sobre legitimidade
- **Bloqueios:** Pessoas bloqueiam antes de ouvir explicações
- **Retrabalho:** Necessidade de explicar o mesmo processo repetidamente

### Needs
- **Credibilidade Automática:** Canal oficial que não gere desconfiança
- **Auto-explicativo:** Processo que se explique por si só
- **Verificação Fácil:** Forma simples de confirmar legitimidade
- **Comunicação Clara:** Mensagens que não pareçam spam

### Opportunities
- **Comunicação In-App:** Notificações oficiais dentro do aplicativo
- **Portal de Verificação:** Área específica para confirmar sorteios
- **Tutorial Interativo:** Explicação visual do processo
- **FAQ Automático:** Respostas às dúvidas mais comuns

---

## Stage 8: Entrega do Prêmio

### Stage Overview
- **Stage Name:** Envio Final do Benefício
- **Description:** Coordenação final para entrega do prêmio através de parceiros ou canais específicos
- **Objective:** Fazer o prêmio chegar até o ganhador confirmado

### Tools Involved
- **E-mail:** Para coordenação com parceiros
- **Plataformas de Terceiros:** Conforme tipo de prêmio
- **WhatsApp:** Para confirmação final com ganhador
- **Planilhas Compartilhadas:** Para controle com parceiros

### Pain Points
- **Dependência Externa:** Coordenação com múltiplos parceiros
- **Falta de Controle:** Sem visibilidade sobre entrega do parceiro
- **Formatos Variados:** Cada prêmio tem processo específico
- **Follow-ups Manuais:** Necessidade de cobrar parceiros

### Needs
- **Automação de Entrega:** Envio automático quando possível
- **Visibilidade Total:** Status de entrega em tempo real
- **Padronização:** Processo similar independente do prêmio
- **Backup Plans:** Alternativas quando canal principal falha

### Opportunities
- **Integrações Diretas:** APIs com principais parceiros
- **Entrega Digital:** Priorizar cupons e benefícios digitais
- **Central de Controle:** Dashboard único para todas as entregas
- **Automação Máxima:** Reduzir dependência de coordenação manual 