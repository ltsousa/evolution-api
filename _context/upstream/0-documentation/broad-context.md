# Broad Context: Raffles and Experiences Management

This document provides a comprehensive overview of the processes, challenges, and opportunities related to managing raffles and consumer experiences. The information is based on the analysis of current workflows, which are predominantly manual, complex, and prone to errors.

## 1. Process Overview

The application allows consumers to use accumulated points to redeem for benefits, which fall into two main categories:

- **Raffles**: Infrequent events that require a large volume of communication over a short period.
- **Experiences**: Daily events, such as game or event tickets, involving a continuous flow of communication and delivery tasks.

---

## 2. Current Challenges

The primary challenges stem from the manual and fragmented nature of the notification, validation, and delivery processes.

### 2.1. Raffles (Sorteios)

The raffle process is highly manual and labor-intensive.

- **Winner Generation**:
  - The winning number is provided by a federal entity (Caixa Econômica Federal).
  - The team manually cross-references the winning number with a raw database of participants.

- **Validation and Disqualification**:
  - A manual list of backup winners must be maintained.
  - Disqualification occurs if a winner fails to meet prerequisites (e.g., valid passport/visa).
  - The next person on the list becomes the new winner.

- **Notification and Contact**:
  - The team manually triggers a generic push notification ("Congratulations, you were drawn").
  - Primary contact is made via a corporate WhatsApp account to request additional data (e.g., companion's name).
  - **Problems**:
    - Consumers are often suspicious of the contact and may perceive it as fraud.
    - Users may block the corporate WhatsApp number.
    - There is a 72-hour waiting period for a response before moving to the next potential winner.
    - The initial push notification is uninformative.
    - For large-scale coupon raffles (e.g., 500 winners), manual contact via WhatsApp is unmanageable.

### 2.2. Experiences (Ingressos para Eventos)

The process for experiences is even more complex due to its daily frequency and varied delivery methods.

- **Opportunity Mapping**:
  - Events are sourced from central administration and regional offices.
  - Information is consolidated in a manually created spreadsheet.

- **System Registration**:
  - An intern manually registers events in the system based on the spreadsheet.
  - There are no automated alerts for event closures or sell-outs.

- **Redemption Tracking**:
  - The intern manually tracks redemptions via the spreadsheet and by extracting data from Metabase.
  - The ticket is **not** delivered at the time of redemption. The team waits until the redemption period ends to contact the user.

- **Delivery and Confirmation (Highly Manual)**:
  - **Varied Formats**: Delivery methods include:
    - **PDF**: Manually sent via WhatsApp.
    - **Ticket Platforms (Ticket Master, Ingresse)**: Requires collecting the user's email, forwarding it to another team, and manually following up to confirm the transfer before notifying the user via WhatsApp.
    - **Links**: Specific links (e.g., for Flamengo games) are sent manually.
    - **Facial Recognition Registration (Total Acesso)**: Requires manual contact to confirm user registration.
  - **External Dependencies**: The team depends on other departments (e.g., regional offices) to provide the tickets in a timely manner.
  - **Lack of Consumer Notification**: Without manual communication, the consumer is often unaware they have received the ticket, as they do not proactively check third-party apps.

---

## 3. Suggested Solutions and Opportunities

The core need is the automation and simplification of communication and delivery workflows.

### 3.1. Automate Benefit Delivery

- **Automatic Delivery at Redemption**:
  - Allow the team to upload a PDF or link when creating the event in the system.
  - The system should automatically deliver the benefit to the consumer upon redemption.

- **Post-Redemption Batch Delivery**:
  - For cases where the benefit is not immediately available, enable the team to import a file (e.g., spreadsheet with links/codes) to trigger a mass delivery via email.

- **Combined Notifications**:
  - Use a push notification to alert the user that their ticket/benefit has been sent to their email.

### 3.2. Improve Winner/Redeemer Communication

- **In-App Forms (Content Cards)**:
  - Use in-app forms to collect necessary information from raffle winners (e.g., passport info, companion's name), reducing reliance on WhatsApp.
  - This could be a simple form or a guided flow (chatbot-like experience).

- **Partial Automation**:
  - Require users to fill out a form with preliminary information before enabling a direct WhatsApp chat.

- **Automated Coupon Delivery**:
  - For large-scale coupon raffles, implement a system to link an email to a coupon code and deliver it automatically within the app, allowing users to easily copy the code.

### 3.3. Technical Integration and Support

- **System Dependency**: The proposed solutions require modifications to the internal system.
- **Internal Knowledge**: Leveraging team members with prior knowledge of the system is a key advantage for development and integration. 