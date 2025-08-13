# Análise Detalhada dos Processos de Sorteio

> Análise detalhada sobre os processos dos Sorteios, abordando seu funcionamento, os processos e times envolvidos, as dores e necessidades, os objetivos e as oportunidades de melhoria.

## 1. Como Funciona e Seus Processos Atuais

O processo de sorteio inicia-se com o consumidor, que acumula pontos no aplicativo e os troca para concorrer a sorteios de prêmios como ingressos para jogos, eventos ou experiências diferenciadas, como harmonização de cervejas ou conhecer artistas.

Uma vez realizado o sorteio, as etapas são predominantemente manuais:

### 1.1 Processo Atual - Etapas

#### Base de Ganhadores (Manual)
- Após a escolha do número sorteado pela Caixa Econômica Federal, a equipe interna baixa uma "base crua" do sistema
- Contém todos os números da sorte gerados e os dados das pessoas

#### Identificação do Ganhador (Manual)
- É necessário fazer manualmente o encontro do número da sorte sorteado pela Econômica Federal com os dados da pessoa na planilha
- Este processo é descrito como "bem porco" e mais complexo do que o demonstrado

#### Registro no Sistema (Manual)
- A pessoa responsável deve entrar na área de "ganhadores" do sistema
- Digitar o número da sorte do vencedor e selecioná-lo como ganhador

#### Notificação Inicial (Automática - Push Notification)
- Uma vez que o ganhador é registrado no sistema, ele recebe uma push notification no celular
- Mensagem: "Parabéns, você foi sorteado!" ou "Entraremos em contato"
- **Esta é a única etapa automática da notificação**

#### Contato para Coleta de Dados (Manual - WhatsApp)
- Após a push notification, a equipe precisa entrar em contato com o ganhador via WhatsApp
- Informar sobre o prêmio e coletar dados adicionais
- Dados podem incluir:
  - Nome de um acompanhante (já que essa informação não é pedida na participação)
  - Foto de passaporte e visto, dependendo do prêmio

#### Gestão de Desclassificação e Próximos Ganhadores (Manual)
- Caso o ganhador não preencha algum pré-requisito (ex: passaporte/visto válido) ou não responda em 72 horas, ele é desclassificado
- A equipe precisa ter uma lista de próximas pessoas na ordem para contatá-las manualmente
- Esperando novamente 72 horas pela resposta

#### Esclarecimento de Dúvidas (Manual)
- Muitas vezes, as pessoas desconfiam da veracidade do sorteio
- Exige que a equipe tire dúvidas e confirme que a informação está no aplicativo

## 2. Times Envolvidos

### 2.1 Times Internos

#### Equipe Interna/Responsável pelo Processo
- Principal time envolvido
- Realiza todas as etapas manuais de identificação, contato e follow-up com os ganhadores

#### Time de CRM
- Tentou-se usar o time de CRM para um disparo automático de WhatsApp
- **Problema**: houve problemas com pessoas que tinham o recebimento de mensagens bloqueado

#### Time de Desenvolvimento/Suporte do Sistema
- O sistema utilizado para o gerenciamento de sorteios e experiências possui um time de suporte
- **Pedrinho** (ex-PM): pessoa chave que tem conhecimento sobre o sistema e pode auxiliar nas soluções de automação e integração

### 2.2 Times Externos

#### Caixa Econômica Federal
- Entidade externa responsável por sortear o número oficial que define o ganhador

#### Times de Parceiros
- Para certos prêmios, como ingressos de carnaval ou eventos específicos
- Há parceiros que são responsáveis pelo envio efetivo do ingresso (ex: time da Brahma)
- Exige coordenação manual e planilhas compartilhadas

## 3. Dores (Desafios e Problemas)

Os processos de sorteio são marcados por diversas dores, principalmente devido à sua natureza manual:

### 3.1 Problemas Operacionais

#### Excesso de Processos Manuais e Trabalhosos
- Achar quem é a pessoa ganhadora
- Registrar no sistema
- Todo o processo de contato é "muito manual e trabalhoso"

#### Perda de Tempo
- O tempo é "perdido" em enviar mensagens, esperar respostas e esclarecer dúvidas

#### Demora na Resposta
- A espera de 72 horas pela resposta do ganhador antes de contatar o próximo da lista alonga o processo significativamente

### 3.2 Problemas de Comunicação

#### Desconfiança dos Ganhadores
- É comum que os ganhadores desconfiem da veracidade do contato
- Resulta em bloqueios e dificulta a comunicação
- Força a equipe a reforçar que a informação está no sistema

#### Necessidade de Conversa Contínua
- Nem sempre um formulário é suficiente
- A equipe precisa conversar com o ganhador para confirmar dados ou tirar dúvidas
- Especialmente quando há problemas com o recebimento do prêmio

### 3.3 Problemas de Padronização

#### Complexidade da Coleta de Informações
- A necessidade de informações diferentes para cada sorteio (ex: nome do acompanhante, foto de passaporte/visto)
- Torna difícil padronizar o contato e a coleta

#### Escalabilidade Inviável
- Para sorteios com um grande número de ganhadores (ex: 500 cupons da Shopee)
- O contato manual via WhatsApp se torna incontrolável e inviável
- Leva à perda de controle

## 4. Necessidades e Objetivos

### 4.1 Necessidades (surgem diretamente das dores enfrentadas)

#### Automatização da Comunicação
- Há uma necessidade clara de automatizar a comunicação com o ganhador
- Desde a notificação detalhada até a coleta de informações e o envio do prêmio

#### Coleta Padronizada e Eficiente de Dados
- Desenvolver formas para que o usuário forneça as informações necessárias de forma estruturada
- Possivelmente via um formulário dentro do aplicativo (como um "content card")
- Sem a necessidade de conversas manuais

#### Notificação Clara e Confiável
- Garantir que o ganhador saiba de forma inequívoca que ganhou
- Como proceder para resgatar o prêmio, sem gerar desconfiança

#### Redução da Carga Operacional
- Diminuir o esforço manual e o tempo gasto pela equipe nos processos pós-sorteio

#### Escalabilidade
- Implementar soluções que permitam gerenciar sorteios com muitos ganhadores de forma eficiente

### 4.2 Objetivos (alinham-se à proposta de valor do aplicativo e à eficiência operacional)

#### Melhorar a Experiência do Consumidor
- O principal objetivo dos sorteios é oferecer benefícios adicionais e experiências únicas
- Que atraiam e retenham os consumidores no aplicativo

#### Eficiência na Entrega de Prêmios
- Garantir que os ganhadores recebam seus prêmios de forma rápida e descomplicada

#### Aumentar a Credibilidade
- Reduzir a desconfiança dos ganhadores e fortalecer a credibilidade do programa de sorteios

## 5. Oportunidades de Melhoria

Considerando as dores e necessidades, existem diversas oportunidades para otimizar os processos de sorteio:

### 5.1 Automação de Formulários e Coleta de Dados

#### Formulários Digitais Integrados (Content Card)
- Utilizar um "content card" no aplicativo como um formulário para coletar informações específicas de cada sorteio
- Exemplos: dados de acompanhante, passaporte
- **Benefício**: elimina a necessidade de pedir esses dados manualmente via WhatsApp

### 5.2 Automação de Entrega de Prêmios

#### Automação da Entrega de Prêmios (especialmente cupons)
- Para prêmios como cupons da Shopee, automatizar o envio diretamente via aplicativo ou e-mail
- Permitir que o usuário copie o código ou até mesmo o cupom seja "encarteado" (inserido em uma carteira digital no app)
- **Crítico**: para sorteios com centenas de ganhadores

#### Integração Direta com Plataformas de Ingresso/Parceiros
- Explorar a possibilidade de integrar o sistema de sorteios com plataformas como:
  - Ticket Master
  - Ingresse
  - Total Acesso
- **Benefício**: ingressos sejam enviados automaticamente após o resgate ou confirmação
- Sem a necessidade de coordenação manual via e-mail ou WhatsApp com times de eventos ou regionais

### 5.3 Melhorias na Comunicação

#### Notificação e Local de Resgate Automatizados
- **Foco principal**: como avisar a pessoa para resgatar o prêmio
- Fornecendo o local de resgate automaticamente
- Sem a necessidade de mensagens individuais

#### Fluxo Híbrido de Contato
- Combinação de automação com a opção de contato manual quando necessário
- Exemplo: após preencher um formulário no app, se ainda houver dúvidas ou necessidade de interação
- Um botão possa abrir o WhatsApp pré-preenchido com informações básicas

### 5.4 Aproveitamento de Recursos Existentes

#### Aproveitar o Conhecimento do Time de Suporte do Sistema
- A colaboração com o time de desenvolvimento do sistema, especialmente com **Pedrinho** (que tem experiência prévia)
- Oportunidade valiosa para resolver as "dependências de integração" e implementar melhorias técnicas

#### Análise de "Caso a Caso"
- Reconhecer que alguns prêmios ou situações podem exigir diferentes abordagens
- O sistema deveria ter a flexibilidade de configurar o formato do ingresso:
  - PDF
  - Link
  - Direto na carteira
- Idealmente, automatizar o upload e envio desses formatos

## Conclusão

A automação desses processos, começando pela forma de notificar o ganhador e fornecer o local de resgate, é vista como um bom primeiro passo para mitigar o fluxo manual e caótico atualmente existente.