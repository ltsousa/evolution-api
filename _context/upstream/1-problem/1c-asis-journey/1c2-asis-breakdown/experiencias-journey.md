# As-Is Journey: Experiências

## Stage 1: Mapeamento de Oportunidades

### Stage Overview
- **Stage Name:** Identificação e Cadastro de Eventos
- **Description:** AC e Regionais identificam oportunidades de eventos e preenchem informações em planilha compartilhada
- **Objective:** Coletar informações de eventos disponíveis para oferecer como experiências aos consumidores

### Tools Involved
- **Planilha Compartilhada:** Preenchida por AC e Regionais com dados do evento
- **E-mail/WhatsApp:** Comunicação entre equipes para coordenação
- **Sistema de Gestão:** Recebe dados posteriormente da planilha

### Pain Points
- **Informações Fragmentadas:** Uso de planilhas como único ponto de entrada
- **Falta de Padronização:** Cada regional pode preencher de forma diferente
- **Sem Validação Automática:** Informações não são validadas no momento da entrada

### Needs
- **Interface Unificada:** Para AC e Regionais cadastrarem diretamente no sistema
- **Validação de Dados:** Para garantir consistência das informações
- **Visibilidade de Status:** Para acompanhar quais eventos foram processados

### Opportunities
- **Portal Centralizado:** Substituir planilhas por interface web dedicada
- **Validação Automática:** Campos obrigatórios e formatos padronizados
- **Notificações Automáticas:** Alertas quando eventos são cadastrados

---

## Stage 2: Cadastro no Sistema

### Stage Overview
- **Stage Name:** Registro de Eventos no Sistema
- **Description:** Estagiária realiza cadastro manual dos eventos no sistema baseado na planilha
- **Objective:** Disponibilizar eventos para resgate pelos consumidores no aplicativo

### Tools Involved
- **Sistema de Gestão:** Interface para cadastro de eventos
- **Planilha Compartilhada:** Fonte de dados para o cadastro
- **Metabase:** Para verificação posterior dos dados

### Pain Points
- **Processos Manuais:** Cadastro um por um baseado na planilha
- **Sem Notificação Automática:** Sistema não avisa sobre eventos esgotados/fechados
- **Dependência de Uma Pessoa:** Estagiária como único ponto de entrada

### Needs
- **Integração Direta:** Eliminação da re-digitação de dados
- **Alertas Automáticos:** Notificações sobre status dos eventos
- **Múltiplos Usuários:** Capacidade de múltiplas pessoas cadastrarem

### Opportunities
- **Import Automático:** Integração direta entre fonte de dados e sistema
- **Dashboard de Status:** Visibilidade em tempo real dos eventos
- **Automação de Alertas:** Sistema notifica automaticamente sobre mudanças

---

## Stage 3: Resgate pelo Consumidor

### Stage Overview
- **Stage Name:** Troca de Pontos por Experiência
- **Description:** Consumidor utiliza pontos acumulados para resgatar ingresso/experiência no app
- **Objective:** Permitir que consumidor obtenha benefício usando pontos como moeda

### Tools Involved
- **Aplicativo Mobile:** Interface para o consumidor resgatar
- **Sistema de Pontos:** Controle do saldo e débito
- **Base de Dados:** Registro da transação de resgate

### Pain Points
- **Falta de Automação na Entrega:** Consumidor não recebe ingresso imediatamente
- **Informação Limitada:** Não há detalhes sobre próximos passos
- **Expectativa Frustrada:** Consumidor espera receber o benefício na hora

### Needs
- **Entrega Imediata:** Sistema deveria entregar ingresso automaticamente quando disponível
- **Comunicação Clara:** Informar quando e como receberá o benefício
- **Status Transparente:** Mostrar progresso do processo de entrega

### Opportunities
- **Entrega Instantânea:** Para eventos com PDFs/links pré-carregados
- **Notificação Rica:** Explicar processo e timeline de entrega
- **Centro de Benefícios:** Área no app para acompanhar todos os resgates

---

## Stage 4: Acompanhamento do Resgate

### Stage Overview
- **Stage Name:** Monitoramento de Resgates Realizados
- **Description:** Estagiária extrai dados do metabase para verificar quem resgatou ingressos
- **Objective:** Identificar quais consumidores precisam receber seus ingressos

### Tools Involved
- **Metabase:** Para extração de relatórios de resgates
- **Planilha de Controle:** Para organizar dados dos resgatadores
- **Sistema de Gestão:** Fonte dos dados de resgate

### Pain Points
- **Processo Manual:** Extração e organização manual de dados
- **Timing Inadequado:** Só verifica após fim do período de resgate
- **Falta de Automação:** Sem alertas automáticos de novos resgates

### Needs
- **Monitoramento em Tempo Real:** Saber imediatamente quando alguém resgata
- **Automatização:** Eliminar extração manual de dados
- **Priorização:** Identificar casos urgentes ou especiais

### Opportunities
- **Dashboard em Tempo Real:** Visão instantânea de todos os resgates
- **Automação de Fluxos:** Disparo automático de próximas etapas
- **Segmentação Automática:** Categorizar resgates por tipo de entrega

---

## Stage 5: Entrega do Ingresso

### Stage Overview
- **Stage Name:** Processo de Envio do Benefício
- **Description:** Entrega manual do ingresso via múltiplas plataformas (PDF, Ticketmaster, Ingresse, etc.)
- **Objective:** Fazer o ingresso chegar até o consumidor através do canal apropriado

### Tools Involved
- **WhatsApp:** Para envio de PDFs e comunicação direta
- **E-mail:** Para coordenação com times de parceiros
- **Platforms de Terceiros:** Ticketmaster, Ingresse, Sympla, Total Acesso
- **Planilhas de Follow-up:** Para controle de envios

### Pain Points
- **Diversidade de Formatos:** Cada tipo de ingresso tem processo diferente
- **Dependência de Terceiros:** Precisa coordenar com múltiplos parceiros
- **Alto Volume Manual:** Cada consumidor requer atenção individual
- **Falta de Controle:** Sem visibilidade sobre quando parceiros enviam

### Needs
- **Padronização:** Processo único independente do formato
- **Automação de Entrega:** Envio automático quando possível
- **Visibilidade:** Saber status de envio em tempo real
- **Backup Plans:** Alternativas quando canal principal falha

### Opportunities
- **Integrações Diretas:** APIs com principais parceiros
- **Upload Preventivo:** PDFs/links carregados no cadastro do evento
- **Entrega Híbrida:** Automática quando possível, manual quando necessário
- **Central de Controle:** Dashboard único para todos os canais

---

## Stage 6: Notificação ao Consumidor

### Stage Overview
- **Stage Name:** Comunicação sobre Recebimento do Ingresso
- **Description:** Contato manual via WhatsApp para informar que ingresso foi enviado
- **Objective:** Garantir que consumidor saiba que recebeu o benefício e onde encontrá-lo

### Tools Involved
- **WhatsApp Corporativo:** Para mensagens individuais
- **Templates de Mensagem:** Textos padrão para diferentes situações
- **Planilha de Controle:** Para rastrear quem foi notificado

### Pain Points
- **Comunicação Manual:** Mensagem individual para cada pessoa
- **Múltiplas Plataformas:** Consumidor pode precisar verificar várias apps
- **Desconfiança:** Pode parecer spam ou fraude
- **Falta de Escala:** Inviável para grandes volumes

### Needs
- **Notificação Automática:** Sistema avisar automaticamente sobre entrega
- **Comunicação Clara:** Informação específica sobre onde encontrar o ingresso
- **Canal Oficial:** Reduzir aparência de comunicação não oficial
- **Escalabilidade:** Funcionar para qualquer volume

### Opportunities
- **Push Notifications:** Notificações no próprio app
- **In-App Delivery:** Ingresso disponível diretamente no aplicativo
- **Comunicação Rica:** Links diretos, instruções claras, suporte visual
- **Automação Completa:** Sem necessidade de intervenção manual 