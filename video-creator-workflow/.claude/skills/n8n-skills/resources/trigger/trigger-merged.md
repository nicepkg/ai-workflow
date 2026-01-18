# Trigger Nodes - Node Collection

This file contains complete information for 99 nodes.

## Table of Contents

- [Bitbucket Trigger](#bitbucket-trigger)
- [Box Trigger](#box-trigger)
- [Brevo Trigger](#brevo-trigger)
- [Cal.com Trigger](#calcom-trigger)
- [Calendly Trigger](#calendly-trigger)
- [Chargebee Trigger](#chargebee-trigger)
- [Chat Trigger](#chat-trigger)
- [ClickUp Trigger](#clickup-trigger)
- [Clockify Trigger](#clockify-trigger)
- [ConvertKit Trigger](#convertkit-trigger)
- [Copper Trigger](#copper-trigger)
- [Cron](#cron)
- [crowd.dev Trigger](#crowddev-trigger)
- [Customer.io Trigger](#customerio-trigger)
- [Email Trigger (IMAP)](#email-trigger-imap)
- [Emelia Trigger](#emelia-trigger)
- [Error Trigger](#error-trigger)
- [Eventbrite Trigger](#eventbrite-trigger)
- [Execute Workflow Trigger](#execute-workflow-trigger)
- [Facebook Lead Ads Trigger](#facebook-lead-ads-trigger)
- [Facebook Trigger](#facebook-trigger)
- [Figma Trigger (Beta)](#figma-trigger-beta)
- [Flow Trigger](#flow-trigger)
- [Form.io Trigger](#formio-trigger)
- [Formstack Trigger](#formstack-trigger)
- [GetResponse Trigger](#getresponse-trigger)
- [Github Trigger](#github-trigger)
- [GitLab Trigger](#gitlab-trigger)
- [Gmail Trigger](#gmail-trigger)
- [Google Business Profile Trigger](#google-business-profile-trigger)
- [Google Calendar Trigger](#google-calendar-trigger)
- [Google Drive Trigger](#google-drive-trigger)
- [Google Sheets Trigger](#google-sheets-trigger)
- [Gumroad Trigger](#gumroad-trigger)
- [Help Scout Trigger](#help-scout-trigger)
- [HubSpot Trigger](#hubspot-trigger)
- [Interval](#interval)
- [Invoice Ninja Trigger](#invoice-ninja-trigger)
- [Jira Trigger](#jira-trigger)
- [Jotform Trigger](#jotform-trigger)
- [Kafka Trigger](#kafka-trigger)
- [Keap Trigger](#keap-trigger)
- [KoBoToolbox Trigger](#kobotoolbox-trigger)
- [Lemlist Trigger](#lemlist-trigger)
- [Linear Trigger](#linear-trigger)
- [Local File Trigger](#local-file-trigger)
- [LoneScale Trigger](#lonescale-trigger)
- [Mailchimp Trigger](#mailchimp-trigger)
- [MailerLite Trigger](#mailerlite-trigger)
- [Mailjet Trigger](#mailjet-trigger)
- [Manual Chat Trigger](#manual-chat-trigger)
- [Manual Trigger](#manual-trigger)
- [Mautic Trigger](#mautic-trigger)
- [MCP Server Trigger](#mcp-server-trigger)
- [Microsoft OneDrive Trigger](#microsoft-onedrive-trigger)
- [Microsoft Outlook Trigger](#microsoft-outlook-trigger)
- [Microsoft Teams Trigger](#microsoft-teams-trigger)
- [MQTT Trigger](#mqtt-trigger)
- [n8n Form Trigger](#n8n-form-trigger)
- [n8n Trigger](#n8n-trigger)
- [Netlify Trigger](#netlify-trigger)
- [Notion Trigger](#notion-trigger)
- [Onfleet Trigger](#onfleet-trigger)
- [PayPal Trigger](#paypal-trigger)
- [Pipedrive Trigger](#pipedrive-trigger)
- [Postgres Trigger](#postgres-trigger)
- [Postmark Trigger](#postmark-trigger)
- [Pushcut Trigger](#pushcut-trigger)
- [RabbitMQ Trigger](#rabbitmq-trigger)
- [Redis Trigger](#redis-trigger)
- [RSS Feed Trigger](#rss-feed-trigger)
- [Salesforce Trigger](#salesforce-trigger)
- [Schedule Trigger](#schedule-trigger)
- [SeaTable Trigger](#seatable-trigger)
- [Shopify Trigger](#shopify-trigger)
- [Simulate Trigger](#simulate-trigger)
- [Slack Trigger](#slack-trigger)
- [SSE Trigger](#sse-trigger)
- [Strava Trigger](#strava-trigger)
- [Stripe Trigger](#stripe-trigger)
- [SurveyMonkey Trigger](#surveymonkey-trigger)
- [Taiga Trigger](#taiga-trigger)
- [Telegram Trigger](#telegram-trigger)
- [TheHive 5 Trigger](#thehive-5-trigger)
- [TheHive Trigger](#thehive-trigger)
- [Toggl Trigger](#toggl-trigger)
- [Trello Trigger](#trello-trigger)
- [Twilio Trigger](#twilio-trigger)
- [Typeform Trigger](#typeform-trigger)
- [Venafi TLS Protect Cloud Trigger](#venafi-tls-protect-cloud-trigger)
- [Webex by Cisco Trigger](#webex-by-cisco-trigger)
- [Webflow Trigger](#webflow-trigger)
- [WhatsApp Trigger](#whatsapp-trigger)
- [Wise Trigger](#wise-trigger)
- [WooCommerce Trigger](#woocommerce-trigger)
- [Workable Trigger](#workable-trigger)
- [Workflow Trigger](#workflow-trigger)
- [Wufoo Trigger](#wufoo-trigger)
- [Zendesk Trigger](#zendesk-trigger)

---

## Bitbucket Trigger

## Basic Information

- Node Type: `nodes-base.bitbucketTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Bitbucket events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"workspace"` | - |
| `workspace` | options | Yes | `""` | The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `events` | multiOptions | Yes | `[]` | The events to listen to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `repository` | options | Yes | `""` | The repository of which to listen to the events. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `events` | multiOptions | Yes | `[]` | The events to listen to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `authentication` | options | No | `"password"` | - |
| `authentication` | options | No | `"accessToken"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `repository`: Repository
- `workspace`: Workspace

##### Authentication (`authentication`)

Optional values:
- `password`: Password (Deprecated)
- `accessToken`: Access Token

##### Authentication (`authentication`)

Optional values:
- `password`: Password (Deprecated)
- `accessToken`: Access Token

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Bitbucket Trigger",
  "type": "nodes-base.bitbucketTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "workspace",
    "workspace": "",
    "events": [],
    "repository": ""
  }
}
```

---

## Box Trigger

## Basic Information

- Node Type: `nodes-base.boxTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Box events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events to listen to |
| `targetType` | options | No | `""` | The type of item to trigger a webhook |
| `targetId` | string | No | `""` | The ID of the item to trigger a webhook |

#### Property Details

##### Events (`events`)

The events to listen to

Optional values:
- `COLLABORATION.ACCEPTED`: Collaboration Accepted - A collaboration has been accepted
- `COLLABORATION.CREATED`: Collaboration Created - A collaboration is created
- `COLLABORATION.REJECTED`: Collaboration Rejected - A collaboration has been rejected
- `COLLABORATION.REMOVED`: Collaboration Removed - A collaboration has been removed
- `COLLABORATION.UPDATED`: Collaboration Updated - A collaboration has been updated
- `COMMENT.CREATED`: Comment Created - A comment object is created
- `COMMENT.DELETED`: Comment Deleted - A comment object is removed
- `COMMENT.UPDATED`: Comment Updated - A comment object is edited
- `FILE.COPIED`: File Copied - A file is copied
- `FILE.DELETED`: File Deleted - A file is moved to the trash
- `FILE.DOWNLOADED`: File Downloaded - A file is downloaded
- `FILE.LOCKED`: File Locked - A file is locked
- `FILE.MOVED`: File Moved - A file is moved from one folder to another
- `FILE.PREVIEWED`: File Previewed - A file is previewed
- `FILE.RENAMED`: File Renamed - A file was renamed
- `FILE.RESTORED`: File Restored - A file is restored from the trash
- `FILE.TRASHED`: File Trashed - A file is moved to the trash
- `FILE.UNLOCKED`: File Unlocked - A file is unlocked
- `FILE.UPLOADED`: File Uploaded - A file is uploaded to or moved to this folder
- `FOLDER.COPIED`: Folder Copied - A copy of a folder is made
- `FOLDER.CREATED`: Folder Created - A folder is created
- `FOLDER.DELETED`: Folder Deleted - A folder is permanently removed
- `FOLDER.DOWNLOADED`: Folder Downloaded - A folder is downloaded
- `FOLDER.MOVED`: Folder Moved - A folder is moved to a different folder
- `FOLDER.RENAMED`: Folder Renamed - A folder was renamed
- `FOLDER.RESTORED`: Folder Restored - A folder is restored from the trash
- `FOLDER.TRASHED`: Folder Trashed - A folder is moved to the trash
- `METADATA_INSTANCE.CREATED`: Metadata Instance Created - A new metadata template instance is associated with a file or folder
- `METADATA_INSTANCE.DELETED`: Metadata Instance Deleted - An existing metadata template instance associated with a file or folder is deleted
- `METADATA_INSTANCE.UPDATED`: Metadata Instance Updated - An attribute (value) is updated/deleted for an existing metadata template instance associated with a file or folder
- `SHARED_LINK.CREATED`: Sharedlink Created - A shared link was created
- `SHARED_LINK.DELETED`: Sharedlink Deleted - A shared link was deleted
- `SHARED_LINK.UPDATED`: Sharedlink Updated - A shared link was updated
- `TASK_ASSIGNMENT.CREATED`: Task Assignment Created - A task is created
- `TASK_ASSIGNMENT.UPDATED`: Task Assignment Updated - A task is updated
- `WEBHOOK.DELETED`: Webhook Deleted - When a webhook is deleted

##### Target Type (`targetType`)

The type of item to trigger a webhook

Optional values:
- `file`: File
- `folder`: Folder

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Box Trigger",
  "type": "nodes-base.boxTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Brevo Trigger

## Basic Information

- Node Type: `nodes-base.sendInBlueTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Brevo events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `type` | options | Yes | `"transactional"` | - |
| `events` | multiOptions | Yes | `[]` | - |
| `events` | multiOptions | Yes | `[]` | - |
| `events` | multiOptions | Yes | `[]` | - |

#### Property Details

##### Resource (`type`)

Optional values:
- `inbound`: Inbound
- `marketing`: Marketing
- `transactional`: Transactional

##### Trigger On (`events`)

Optional values:
- `blocked`: Email Blocked - Triggers when transactional email is blocked
- `click`: Email Clicked - Triggers when transactional email is clicked
- `deferred`: Email Deferred - Triggers when transactional email is deferred
- `delivered`: Email Delivered - Triggers when transactional email is delivered
- `hardBounce`: Email Hard Bounce - Triggers when transactional email is hard bounced
- `invalid`: Email Invalid - Triggers when transactional email is invalid
- `spam`: Email Marked Spam - Triggers when transactional email is set to spam
- `opened`: Email Opened - Triggers when transactional email is opened
- `request`: Email Sent - Triggers when transactional email is sent
- `softBounce`: Email Soft-Bounce - Triggers when transactional email is soft bounced
- `uniqueOpened`: Email Unique Open - Triggers when transactional email is unique opened
- `unsubscribed`: Email Unsubscribed - Triggers when transactional email is unsubscribed

##### Trigger On (`events`)

Optional values:
- `click`: Marketing Email Clicked - Triggers when marketing email is clicked
- `delivered`: Marketing Email Delivered - Triggers when marketing email is delivered
- `hardBounce`: Marketing Email Hard Bounce - Triggers when marketing email is hard bounced
- `listAddition`: Marketing Email List Addition - Triggers when marketing email is clicked
- `opened`: Marketing Email Opened - Triggers when marketing email is opened
- `softBounce`: Marketing Email Soft Bounce - Triggers when marketing email is soft bounced
- `spam`: Marketing Email Spam - Triggers when marketing email is spam
- `unsubscribed`: Marketing Email Unsubscribed - Triggers when marketing email is unsubscribed

##### Trigger On (`events`)

Optional values:
- `inboundEmailProcessed`: Inbound Email Processed - Triggers when inbound email is processed

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Brevo Trigger",
  "type": "nodes-base.sendInBlueTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "type": "transactional",
    "events": []
  }
}
```

---

## Cal.com Trigger

## Basic Information

- Node Type: `nodes-base.calTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Cal.com events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | - |
| `version` | options | No | `1` | - |
| `version` | options | No | `2` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Events (`events`)

Optional values:
- `BOOKING_CANCELLED`: Booking Cancelled - Receive notifications when a Cal event is canceled
- `BOOKING_CREATED`: Booking Created - Receive notifications when a new Cal event is created
- `BOOKING_RESCHEDULED`: Booking Rescheduled - Receive notifications when a Cal event is rescheduled
- `MEETING_ENDED`: Meeting Ended - Receive notifications when a Cal event or meeting has ended

##### API Version (`version`)

Optional values:
- `1`: Before v2.0
- `2`: v2.0 Onwards

##### API Version (`version`)

Optional values:
- `1`: Before v2.0
- `2`: v2.0 Onwards

##### Options (`options`)

Optional values:
- `undefined`: appId - The ID of the App to monitor
- `undefined`: eventTypeId - The EventType to monitor. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: payloadTemplate - Template to customize the webhook payload

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Cal.com Trigger",
  "type": "nodes-base.calTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Calendly Trigger

## Basic Information

- Node Type: `nodes-base.calendlyTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Calendly events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `scope` | options | Yes | `"user"` | - |
| `events` | multiOptions | Yes | `[]` | - |
| `authentication` | options | No | `"apiKey"` | - |
| `deprecationNotice` | notice | No | `""` | - |

#### Property Details

##### Scope (`scope`)

Optional values:
- `organization`: Organization - Triggers the webhook for all subscribed events within the organization
- `user`: User - Triggers the webhook for subscribed events that belong to the current user

##### Events (`events`)

Optional values:
- `invitee.created`: Event Created - Receive notifications when a new Calendly event is created
- `invitee.canceled`: Event Canceled - Receive notifications when a Calendly event is canceled

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `apiKey`: API Key or Personal Access Token

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Calendly Trigger",
  "type": "nodes-base.calendlyTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "scope": "user",
    "events": []
  }
}
```

---

## Chargebee Trigger

## Basic Information

- Node Type: `nodes-base.chargebeeTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Starts the workflow when Chargebee events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | - |

#### Property Details

##### Events (`events`)

Optional values:
- `*`: * - Any time any event is triggered (Wildcard Event)
- `card_added`: Card Added - Triggered when a card is added for a customer
- `card_deleted`: Card Deleted - Triggered when a card is deleted for a customer
- `card_expired`: Card Expired - Triggered when the card for a customer has expired
- `card_expiring`: Card Expiring - Triggered when the customer's credit card is expiring soon.Triggered 30 days before the expiry date
- `card_updated`: Card Updated - Triggered when the card is updated for a customer
- `customer_changed`: Customer Changed - Triggered when a customer is changed
- `customer_created`: Customer Created - Triggered when a customer is created
- `customer_deleted`: Customer Deleted - Triggered when a customer is deleted
- `invoice_created`: Invoice Created - Event triggered (in the case of metered billing) when a 'Pending' invoice is created that has usage related charges or line items to be added, before being closed. This is triggered only when the “Notify for Pending Invoices” option is enabled.
- `invoice_deleted`: Invoice Deleted - Event triggered when an invoice is deleted
- `invoice_generated`: Invoice Generated - Event triggered when a new invoice is generated. In case of metered billing, this event is triggered when a 'Pending' invoice is closed.
- `invoice_updated`: Invoice Updated - Triggered when the invoice’s shipping/billing address is updated, if the invoice is voided, or when the amount due is modified due to payments applied/removed
- `payment_failed`: Payment Failed - Triggered when attempt to charge customer's credit card fails
- `payment_initiated`: Payment Initiated - Triggered when a payment is initiated via direct debit
- `payment_refunded`: Payment Refunded - Triggered when a payment refund is made
- `payment_succeeded`: Payment Succeeded - Triggered when the payment is successfully collected
- `refund_initiated`: Refund Initiated - Triggered when a refund is initiated via direct debit
- `subscription_activated`: Subscription Activated - Triggered after the subscription has been moved from 'Trial' to 'Active' state
- `subscription_cancellation_scheduled`: Subscription Cancellation Scheduled - Triggered when subscription is scheduled to cancel at end of current term
- `subscription_cancelled`: Subscription Cancelled - Triggered when the subscription is cancelled. If it is cancelled due to non payment or because the card details are not present, the subscription will have the possible reason as 'cancel\_reason'.
- `subscription_cancelling`: Subscription Cancelling - Triggered 6 days prior to the scheduled cancellation date
- `subscription_changed`: Subscription Changed - Triggered when the subscription's recurring items are changed
- `subscription_created`: Subscription Created - Triggered when a new subscription is created
- `subscription_deleted`: Subscription Deleted - Triggered when a subscription is deleted
- `subscription_reactivated`: Subscription Reactivated - Triggered when the subscription is moved from cancelled state to 'Active' or 'Trial' state
- `subscription_renewal_reminder`: Subscription Renewal Reminder - Triggered 3 days before each subscription's renewal
- `subscription_renewed`: Subscription Renewed - Triggered when the subscription is renewed from the current term
- `subscription_scheduled_cancellation_removed`: Subscription Scheduled Cancellation Removed - Triggered when scheduled cancellation is removed for the subscription
- `subscription_shipping_address_updated`: Subscription Shipping Address Updated - Triggered when shipping address is added or updated for a subscription
- `subscription_started`: Subscription Started - Triggered when a 'future' subscription gets started
- `subscription_trial_ending`: Subscription Trial Ending - Triggered 6 days prior to the trial period's end date
- `transaction_created`: Transaction Created - Triggered when a transaction is recorded
- `transaction_deleted`: Transaction Deleted - Triggered when a transaction is deleted
- `transaction_updated`: Transaction Updated - Triggered when a transaction is updated. E.g. (1) When a transaction is removed, (2) or when an excess payment is applied on an invoice, (3) or when amount\_capturable gets updated.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Chargebee Trigger",
  "type": "nodes-base.chargebeeTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Chat Trigger

## Basic Information

- Node Type: `nodes-langchain.chatTrigger`
- Category: trigger
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Runs the workflow when an n8n generated webchat is submitted

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `authentication` | options | No | `"none"` | The way to authenticate |
| `mode` | options | No | `"hostedChat"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `public` | boolean | No | `false` | Whether the chat should be publicly available or only accessible through the manual chat interface |
| `initialMessages` | string | No | `"Hi there! 👋\nMy name is Nathan. How can I assist you today?"` | Default messages shown at the start of the chat, one per line |
| `availableInChat` | boolean | No | `false` | Whether to make the agent available in n8n Chat |

#### Property Details

##### Authentication (`authentication`)

The way to authenticate

Optional values:
- `basicAuth`: Basic Auth - Simple username and password (the same one for all users)
- `n8nUserAuth`: n8n User Auth - Require user to be logged in with their n8n account
- `none`: None

##### Mode (`mode`)

Optional values:
- `hostedChat`: Hosted Chat - Chat on a page served by n8n
- `webhook`: Embedded Chat - Chat through a widget embedded in another page, or by calling a webhook

##### Options (`options`)

Optional values:
- `undefined`: allowFileUploads - Whether to allow file uploads in the chat
- `undefined`: allowedFilesMimeTypes - Allowed file types for upload. Comma-separated list of \<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics\_of\_HTTP/MIME\_types/Common\_types" target="\_blank"\>MIME types\</a\>.

##### Options (`options`)

Optional values:
- `undefined`: allowedOrigins - Comma-separated list of URLs allowed for cross-origin non-preflight requests. Use \* (default) to allow all origins.
- `undefined`: allowFileUploads - Whether to allow file uploads in the chat
- `undefined`: allowedFilesMimeTypes - Allowed file types for upload. Comma-separated list of \<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics\_of\_HTTP/MIME\_types/Common\_types" target="\_blank"\>MIME types\</a\>.
- `undefined`: inputPlaceholder - Shown as placeholder text in the chat input field
- `undefined`: loadPreviousSession - If loading messages of a previous session should be enabled
- `undefined`: showWelcomeScreen - Whether to show the welcome screen at the start of the chat
- `undefined`: getStarted - Shown as part of the welcome screen, in the middle of the chat window
- `undefined`: subtitle - Shown at the top of the chat, under the title
- `undefined`: title - Shown at the top of the chat
- `undefined`: customCss - Override default styling of the public chat interface with CSS
- `undefined`: responseMode - When and how to respond to the webhook

##### Options (`options`)

Optional values:
- `undefined`: allowedOrigins - Comma-separated list of URLs allowed for cross-origin non-preflight requests. Use \* (default) to allow all origins.
- `undefined`: allowFileUploads - Whether to allow file uploads in the chat
- `undefined`: allowedFilesMimeTypes - Allowed file types for upload. Comma-separated list of \<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics\_of\_HTTP/MIME\_types/Common\_types" target="\_blank"\>MIME types\</a\>.
- `undefined`: inputPlaceholder - Shown as placeholder text in the chat input field
- `undefined`: loadPreviousSession - If loading messages of a previous session should be enabled
- `undefined`: showWelcomeScreen - Whether to show the welcome screen at the start of the chat
- `undefined`: getStarted - Shown as part of the welcome screen, in the middle of the chat window
- `undefined`: subtitle - Shown at the top of the chat, under the title
- `undefined`: title - Shown at the top of the chat
- `undefined`: customCss - Override default styling of the public chat interface with CSS
- `undefined`: responseMode - When and how to respond to the webhook

##### Options (`options`)

Optional values:
- `undefined`: allowFileUploads - Whether to allow file uploads in the chat
- `undefined`: allowedFilesMimeTypes - Allowed file types for upload. Comma-separated list of \<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics\_of\_HTTP/MIME\_types/Common\_types" target="\_blank"\>MIME types\</a\>.
- `undefined`: responseMode - When and how to respond to the chat

##### Options (`options`)

Optional values:
- `undefined`: allowedOrigins - Comma-separated list of URLs allowed for cross-origin non-preflight requests. Use \* (default) to allow all origins.
- `undefined`: allowFileUploads - Whether to allow file uploads in the chat
- `undefined`: allowedFilesMimeTypes - Allowed file types for upload. Comma-separated list of \<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics\_of\_HTTP/MIME\_types/Common\_types" target="\_blank"\>MIME types\</a\>.
- `undefined`: inputPlaceholder - Shown as placeholder text in the chat input field
- `undefined`: loadPreviousSession - If loading messages of a previous session should be enabled
- `undefined`: showWelcomeScreen - Whether to show the welcome screen at the start of the chat
- `undefined`: getStarted - Shown as part of the welcome screen, in the middle of the chat window
- `undefined`: subtitle - Shown at the top of the chat, under the title
- `undefined`: title - Shown at the top of the chat
- `undefined`: customCss - Override default styling of the public chat interface with CSS
- `undefined`: responseMode - When and how to respond to the chat
- `undefined`: responseMode - When and how to respond to the webhook

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Webhook - via `main` connection
7. Merge - via `main` connection
8. Airtable - via `main` connection
9. Discord - via `main` connection
10. Dropbox - via `main` connection

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Chat Trigger",
  "type": "nodes-langchain.chatTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## ClickUp Trigger

## Basic Information

- Node Type: `nodes-base.clickUpTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle ClickUp events via webhooks (Beta)

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | - |
| `team` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `authentication` | options | No | `"accessToken"` | - |
| `filters` | collection | No | `{}` | - |

#### Property Details

##### Events (`events`)

Optional values:
- `*`: *
- `folderCreated`: folder.created
- `folderDeleted`: folder.deleted
- `folderUpdated`: folder.updated
- `goalCreated`: goal.created
- `goalDeleted`: goal.deleted
- `goalUpdated`: goal.updated
- `keyResultCreated`: keyResult.created
- `keyResultDelete`: keyResult.deleted
- `keyResultUpdated`: keyResult.updated
- `listCreated`: list.created
- `listDeleted`: list.deleted
- `listUpdated`: list.updated
- `spaceCreated`: space.created
- `spaceDeleted`: space.deleted
- `spaceUpdated`: space.updated
- `taskAssigneeUpdated`: task.assignee.updated
- `taskCommentPosted`: task.comment.posted
- `taskCommentUpdated`: task.comment.updated
- `taskCreated`: task.created
- `taskDeleted`: task.deleted
- `taskDueDateUpdated`: task.dueDate.updated
- `taskMoved`: task.moved
- `taskStatusUpdated`: task.status.updated
- `taskTagUpdated`: task.tag.updated
- `taskTimeEstimateUpdated`: task.timeEstimate.updated
- `taskTimeTrackedUpdated`: task.timeTracked.updated
- `taskUpdated`: task.updated

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

##### Filters (`filters`)

Optional values:
- `undefined`: folderId
- `undefined`: listId
- `undefined`: spaceId
- `undefined`: taskId

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "ClickUp Trigger",
  "type": "nodes-base.clickUpTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": [],
    "team": ""
  }
}
```

---

## Clockify Trigger

## Basic Information

- Node Type: `nodes-base.clockifyTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Listens to Clockify events

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `watchField` | options | Yes | `0` | - |
| `workspaceId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Trigger (`watchField`)

Optional values:
- `0`: New Time Entry

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Clockify Trigger",
  "type": "nodes-base.clockifyTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "watchField": 0,
    "workspaceId": ""
  }
}
```

---

## ConvertKit Trigger

## Basic Information

- Node Type: `nodes-base.convertKitTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle ConvertKit events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | The events that can trigger the webhook and whether they are enabled |
| `formId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `courseId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `link` | string | Yes | `""` | The URL of the initiating link |
| `tagId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `productId` | string | Yes | `""` | - |

#### Property Details

##### Event (`event`)

The events that can trigger the webhook and whether they are enabled

Optional values:
- `formSubscribe`: Form Subscribe
- `linkClick`: Link Click
- `productPurchase`: Product Purchase
- `purchaseCreate`: Purchase Created
- `courseComplete`: Sequence Complete
- `courseSubscribe`: Sequence Subscribe
- `subscriberActivate`: Subscriber Activated
- `subscriberUnsubscribe`: Subscriber Unsubscribe
- `tagAdd`: Tag Add
- `tagRemove`: Tag Remove

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "ConvertKit Trigger",
  "type": "nodes-base.convertKitTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "",
    "formId": "",
    "courseId": "",
    "link": "",
    "tagId": "",
    "productId": ""
  }
}
```

---

## Copper Trigger

## Basic Information

- Node Type: `nodes-base.copperTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Copper events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `""` | The resource which will fire the event |
| `event` | options | Yes | `""` | The event to listen to |

#### Property Details

##### Resource (`resource`)

The resource which will fire the event

Optional values:
- `company`: Company
- `lead`: Lead
- `opportunity`: Opportunity
- `person`: Person
- `project`: Project
- `task`: Task

##### Event (`event`)

The event to listen to

Optional values:
- `delete`: Delete - An existing record is removed
- `new`: New - A new record is created
- `update`: Update - Any field in the existing entity record is changed

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Copper Trigger",
  "type": "nodes-base.copperTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "",
    "event": ""
  }
}
```

---

## Cron

## Basic Information

- Node Type: `nodes-base.cron`
- Category: trigger
- Package: n8n-nodes-base

### Description

Triggers the workflow at a specific time

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `triggerTimes` | fixedCollection | No | `{}` | Triggers for the workflow |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Trigger Times (`triggerTimes`)

Triggers for the workflow

Optional values:
- `undefined`: item

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Cron",
  "type": "nodes-base.cron",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## crowd.dev Trigger

## Basic Information

- Node Type: `nodes-base.crowdDevTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when crowd.dev events occur.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `trigger` | options | Yes | `"new_activity"` | What will trigger an automation |

#### Property Details

##### Trigger (`trigger`)

What will trigger an automation

Optional values:
- `new_activity`: New Activity
- `new_member`: New Member

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "crowd.dev Trigger",
  "type": "nodes-base.crowdDevTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "trigger": "new_activity"
  }
}
```

---

## Customer.io Trigger

## Basic Information

- Node Type: `nodes-base.customerIoTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow on a Customer.io update (Beta)

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events that can trigger the webhook and whether they are enabled |

#### Property Details

##### Events (`events`)

The events that can trigger the webhook and whether they are enabled

Optional values:
- `customer.subscribed`: Customer Subscribed - Whether the webhook is triggered when a list subscriber is added
- `customer.unsubscribed`: Customer Unsubscribe - Whether the webhook is triggered when a list member unsubscribes
- `email.attempted`: Email Attempted - Whether the webhook is triggered when a list member unsubscribes
- `email.bounced`: Email Bounced - Whether the webhook is triggered when a list member unsubscribes
- `email.clicked`: Email Clicked - Whether the webhook is triggered when a list member unsubscribes
- `email.converted`: Email Converted - Whether the webhook is triggered when a list member unsubscribes
- `email.delivered`: Email Delivered - Whether the webhook is triggered when a list member unsubscribes
- `email.drafted`: Email Drafted - Whether the webhook is triggered when a list member unsubscribes
- `email.failed`: Email Failed - Whether the webhook is triggered when a list member unsubscribes
- `email.opened`: Email Opened - Whether the webhook is triggered when a list member unsubscribes
- `email.sent`: Email Sent - Whether the webhook is triggered when a list member unsubscribes
- `email.spammed`: Email Spammed - Whether the webhook is triggered when a list member unsubscribes
- `push.attempted`: Push Attempted - Whether the webhook is triggered when a list member unsubscribes
- `push.bounced`: Push Bounced - Whether the webhook is triggered when a list member unsubscribes
- `push.clicked`: Push Clicked - Whether the webhook is triggered when a list member unsubscribes
- `push.delivered`: Push Delivered - Whether the webhook is triggered when a list member unsubscribes
- `push.drafted`: Push Drafted - Whether the webhook is triggered when a list member unsubscribes
- `push.failed`: Push Failed - Whether the webhook is triggered when a list member unsubscribes
- `push.opened`: Push Opened - Whether the webhook is triggered when a list member unsubscribes
- `push.sent`: Push Sent - Whether the webhook is triggered when a list member unsubscribes
- `slack.attempted`: Slack Attempted - Whether the webhook is triggered when a list member unsubscribes
- `slack.clicked`: Slack Clicked - Whether the webhook is triggered when a list member unsubscribes
- `slack.drafted`: Slack Drafted - Whether the webhook is triggered when a list member unsubscribes
- `slack.failed`: Slack Failed - Whether the webhook is triggered when a list member unsubscribes
- `slack.sent`: Slack Sent - Whether the webhook is triggered when a list member unsubscribes
- `sms.attempted`: SMS Attempted - Whether the webhook is triggered when a list member unsubscribes
- `sms.bounced`: SMS Bounced - Whether the webhook is triggered when a list member unsubscribes
- `sms.clicked`: SMS Clicked - Whether the webhook is triggered when a list member unsubscribes
- `sms.delivered`: SMS Delivered - Whether the webhook is triggered when a list member unsubscribes
- `sms.drafted`: SMS Drafted - Whether the webhook is triggered when a list member unsubscribes
- `sms.failed`: SMS Failed - Whether the webhook is triggered when a list member unsubscribes
- `sms.sent`: SMS Sent - Whether the webhook is triggered when a list member unsubscribes

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Customer.io Trigger",
  "type": "nodes-base.customerIoTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Email Trigger (IMAP)

## Basic Information

- Node Type: `nodes-base.emailReadImap`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Triggers the workflow when a new email is received

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `postProcessAction` | options | No | `"read"` | What to do after the email has been received. If "nothing" gets selected it will be processed multiple times. |
| `format` | options | No | `"simple"` | The format to return the message in |
| `options` | collection | No | `{}` | - |
| `downloadAttachments` | boolean | No | `false` | Whether attachments of emails should be downloaded. Only set if needed as it increases processing. |
| `dataPropertyAttachmentsPrefixName` | string | No | `"attachment_"` | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment\_" the first attachment is saved to "attachment\_0" |
| `dataPropertyAttachmentsPrefixName` | string | No | `"attachment_"` | Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment\_" the first attachment is saved to "attachment\_0" |
| `mailbox` | string | No | `"INBOX"` | - |

#### Property Details

##### Action (`postProcessAction`)

What to do after the email has been received. If "nothing" gets selected it will be processed multiple times.

Optional values:
- `read`: Mark as Read
- `nothing`: Nothing

##### Format (`format`)

The format to return the message in

Optional values:
- `raw`: RAW - Returns the full email message data with body content in the raw field as a base64url encoded string; the payload field is not used
- `resolved`: Resolved - Returns the full email with all data resolved and attachments saved as binary data
- `simple`: Simple - Returns the full email; do not use if you wish to gather inline attachments

##### Options (`options`)

Optional values:
- `undefined`: customEmailConfig - Custom email fetching rules. See \<a href="https://github.com/mscdex/node-imap"\>node-imap\</a\>'s search function for more details.
- `undefined`: forceReconnect - Sets an interval (in minutes) to force a reconnection
- `undefined`: trackLastMessageId - Whether to fetch only new emails since the last run, or all emails that match the "Custom Email Rules" (\["UNSEEN"\] by default)

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Email Trigger (IMAP)",
  "type": "nodes-base.emailReadImap",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Emelia Trigger

## Basic Information

- Node Type: `nodes-base.emeliaTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Emelia campaign activity events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | - |
| `campaignId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Events (`events`)

Optional values:
- `bounced`: Email Bounced
- `opened`: Email Opened
- `replied`: Email Replied
- `sent`: Email Sent
- `clicked`: Link Clicked
- `unsubscribed`: Unsubscribed Contact

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Emelia Trigger",
  "type": "nodes-base.emeliaTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": [],
    "campaignId": ""
  }
}
```

---

## Error Trigger

## Basic Information

- Node Type: `nodes-base.errorTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Triggers the workflow when another workflow has an error

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Error Trigger",
  "type": "nodes-base.errorTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Eventbrite Trigger

## Basic Information

- Node Type: `nodes-base.eventbriteTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Eventbrite events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `actions` | multiOptions | Yes | `[]` | One or more action to subscribe to |
| `organization` | options | Yes | `""` | The Eventbrite Organization to work on. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `event` | options | Yes | `""` | Limit the triggers to this event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `authentication` | options | No | `"privateKey"` | - |
| `resolveData` | boolean | No | `true` | By default does the webhook-data only contain the URL to receive the object data manually. If this option gets activated, it will resolve the data automatically. |

#### Property Details

##### Actions (`actions`)

One or more action to subscribe to

Optional values:
- `attendee.checked_in`: attendee.checked_in
- `attendee.checked_out`: attendee.checked_out
- `attendee.updated`: attendee.updated
- `event.created`: event.created
- `event.published`: event.published
- `event.unpublished`: event.unpublished
- `event.updated`: event.updated
- `order.placed`: order.placed
- `order.refunded`: order.refunded
- `order.updated`: order.updated
- `organizer.updated`: organizer.updated
- `ticket_class.created`: ticket_class.created
- `ticket_class.deleted`: ticket_class.deleted
- `ticket_class.updated`: ticket_class.updated
- `venue.updated`: venue.updated

##### Authentication (`authentication`)

Optional values:
- `privateKey`: Private Key
- `oAuth2`: OAuth2

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Eventbrite Trigger",
  "type": "nodes-base.eventbriteTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "actions": [],
    "organization": "",
    "event": ""
  }
}
```

---

## Execute Workflow Trigger

## Basic Information

- Node Type: `nodes-base.executeWorkflowTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Helpers for calling other n8n workflows. Used for designing modular, microservice-like workflows.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workflowInputs` | fixedCollection | No | `{}` | Define expected input fields. If no inputs are provided, all data from the calling workflow will be passed through. |
| `events` | hidden | No | `"worklfow_call"` | - |
| `inputSource` | options | No | `"workflowInputs"` | - |
| `notice` | notice | No | `""` | - |
| `outdatedVersionWarning` | notice | No | `""` | - |
| `jsonExample_notice` | notice | No | `""` | - |
| `jsonExample` | json | No | `"{\n  \"aField\": \"a string\",\n  \"aNumber\": 123,\n  \"thisFieldAcceptsAnyType\": null,\n  \"anArray\": []\n}"` | - |

#### Property Details

##### Workflow Input Schema (`workflowInputs`)

Define expected input fields. If no inputs are provided, all data from the calling workflow will be passed through.

Optional values:
- `undefined`: values

##### Events (`events`)

Optional values:
- `worklfow_call`: Workflow Call - When executed by another workflow using Execute Workflow Trigger

##### Input data mode (`inputSource`)

Optional values:
- `workflowInputs`: Define using fields below - Provide input fields via UI
- `jsonExample`: Define using JSON example - Generate a schema from an example JSON object
- `passthrough`: Accept all data - Use all incoming data from the parent workflow

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Execute Workflow Trigger",
  "type": "nodes-base.executeWorkflowTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Facebook Lead Ads Trigger

## Basic Information

- Node Type: `nodes-base.facebookLeadAdsTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Facebook Lead Ads events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"newLead"` | - |
| `page` | resourceLocator | Yes | `{"mode":"list","value":""}` | The page linked to the form for retrieving new leads |
| `form` | resourceLocator | Yes | `{"mode":"list","value":""}` | The form to monitor for fetching lead details upon submission |
| `options` | collection | No | `{}` | - |
| `facebookLeadAdsNotice` | notice | No | `""` | - |

#### Property Details

##### Event (`event`)

Optional values:
- `newLead`: New Lead

##### Options (`options`)

Optional values:
- `undefined`: simplifyOutput - Whether to return a simplified version of the webhook event instead of all fields

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Facebook Lead Ads Trigger",
  "type": "nodes-base.facebookLeadAdsTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "newLead",
    "page": {
      "mode": "list",
      "value": ""
    },
    "form": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Facebook Trigger

## Basic Information

- Node Type: `nodes-base.facebookTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Facebook events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `object` | options | Yes | `"user"` | The object to subscribe to |
| `appId` | string | Yes | `""` | Facebook APP ID |
| `options` | collection | No | `{}` | - |
| `fields` | multiOptions | No | `[]` | The set of fields in this object that are subscribed to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `whatsappBusinessAccountNotice` | notice | No | `""` | - |

#### Property Details

##### Object (`object`)

The object to subscribe to

Optional values:
- `adAccount`: Ad Account - Get updates about Ad Account
- `application`: Application - Get updates about the app
- `certificateTransparency`: Certificate Transparency - Get updates about Certificate Transparency
- `group`: Group - Get updates about activity in groups and events in groups for Workplace
- `instagram`: Instagram - Get updates about comments on your media
- `link`: Link - Get updates about links for rich previews by an external provider
- `page`: Page - Page updates
- `permissions`: Permissions - Updates regarding granting or revoking permissions
- `user`: User - User profile updates
- `whatsappBusinessAccount`: Whatsapp Business Account - Get updates about Whatsapp business account
- `workplaceSecurity`: Workplace Security - Get updates about Workplace Security

##### Options (`options`)

Optional values:
- `undefined`: includeValues - Whether change notifications should include the new values

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Facebook Trigger",
  "type": "nodes-base.facebookTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "object": "user",
    "appId": ""
  }
}
```

---

## Figma Trigger (Beta)

## Basic Information

- Node Type: `nodes-base.figmaTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Figma events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `triggerOn` | options | Yes | `""` | - |
| `teamId` | string | Yes | `""` | Trigger will monitor this Figma Team for changes. Team ID can be found in the URL of a Figma Team page when viewed in a web browser: figma.com/files/team/{TEAM-ID}/. |

#### Property Details

##### Trigger On (`triggerOn`)

Optional values:
- `fileComment`: File Commented - Triggers when someone comments on a file
- `fileDelete`: File Deleted - Triggers whenever a file has been deleted. Does not trigger on all files within a folder, if the folder is deleted.
- `fileUpdate`: File Updated - Triggers whenever a file saves or is deleted. This occurs whenever a file is closed or within 30 seconds after changes have been made.
- `fileVersionUpdate`: File Version Updated - Triggers whenever a named version is created in the version history of a file
- `libraryPublish`: Library Publish - Triggers whenever a library file is published

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Figma Trigger (Beta)",
  "type": "nodes-base.figmaTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "triggerOn": "",
    "teamId": ""
  }
}
```

---

## Flow Trigger

## Basic Information

- Node Type: `nodes-base.flowTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Flow events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `listIds` | string | Yes | `""` | Lists IDs, perhaps known better as "Projects" separated by a comma (,) |
| `taskIds` | string | Yes | `""` | Task IDs separated by a comma (,) |
| `resource` | options | No | `""` | Resource that triggers the webhook |

#### Property Details

##### Resource (`resource`)

Resource that triggers the webhook

Optional values:
- `list`: Project
- `task`: Task

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Flow Trigger",
  "type": "nodes-base.flowTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "listIds": "",
    "taskIds": ""
  }
}
```

---

## Form.io Trigger

## Basic Information

- Node Type: `nodes-base.formIoTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle form.io events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | - |
| `projectId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `formId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Trigger Events (`events`)

Optional values:
- `create`: Submission Created
- `update`: Submission Updated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Form.io Trigger",
  "type": "nodes-base.formIoTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": [],
    "projectId": "",
    "formId": ""
  }
}
```

---

## Formstack Trigger

## Basic Information

- Node Type: `nodes-base.formstackTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow on a Formstack form submission.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `formId` | options | Yes | `""` | The Formstack form to monitor for new submissions. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `authentication` | options | No | `"accessToken"` | - |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Formstack Trigger",
  "type": "nodes-base.formstackTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "formId": ""
  }
}
```

---

## GetResponse Trigger

## Basic Information

- Node Type: `nodes-base.getResponseTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when GetResponse events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | - |
| `authentication` | options | No | `"apiKey"` | - |
| `options` | collection | No | `{}` | - |
| `listIds` | multiOptions | No | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Events (`events`)

Optional values:
- `subscribe`: Customer Subscribed - Receive notifications when a customer is subscribed to a list
- `unsubscribe`: Customer Unsubscribed - Receive notifications when a customer is unsubscribed from a list
- `click`: Email Clicked - Receive notifications when a email is clicked
- `open`: Email Opened - Receive notifications when a email is opened
- `survey`: Survey Submitted - Receive notifications when a survey is submitted

##### Authentication (`authentication`)

Optional values:
- `apiKey`: API Key
- `oAuth2`: OAuth2

##### Options (`options`)

Optional values:
- `undefined`: delete - Whether to delete the current subscription

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "GetResponse Trigger",
  "type": "nodes-base.getResponseTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Github Trigger

## Basic Information

- Node Type: `nodes-base.githubTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Github events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events to listen to |
| `owner` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `repository` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `authentication` | options | No | `"accessToken"` | - |
| `options` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Events (`events`)

The events to listen to

Optional values:
- `*`: * - Any time any event is triggered (Wildcard Event)
- `check_run`: Check Run - Triggered when a check run is created, rerequested, completed, or has a requested\_action
- `check_suite`: Check Suite - Triggered when a check suite is completed, requested, or rerequested
- `commit_comment`: Commit Comment - Triggered when a commit comment is created
- `create`: Create - Represents a created repository, branch, or tag
- `delete`: Delete - Represents a deleted branch or tag
- `deploy_key`: Deploy Key - Triggered when a deploy key is added or removed from a repository
- `deployment`: Deployment - Represents a deployment
- `deployment_status`: Deployment Status - Represents a deployment status
- `fork`: Fork - Triggered when a user forks a repository
- `github_app_authorization`: Github App Authorization - Triggered when someone revokes their authorization of a GitHub App
- `gollum`: Gollum - Triggered when a Wiki page is created or updated
- `installation`: Installation - Triggered when someone installs (created), uninstalls (deleted), or accepts new permissions (new\_permissions\_accepted) for a GitHub App. When a GitHub App owner requests new permissions, the person who installed the GitHub App must accept the new permissions request.
- `installation_repositories`: Installation Repositories - Triggered when a repository is added or removed from an installation
- `issue_comment`: Issue Comment - Triggered when an issue comment is created, edited, or deleted
- `issues`: Issues - Triggered when an issue is opened, edited, deleted, transferred, pinned, unpinned, closed, reopened, assigned, unassigned, labeled, unlabeled, locked, unlocked, milestoned, or demilestoned
- `label`: Label - Triggered when a repository's label is created, edited, or deleted
- `marketplace_purchase`: Marketplace Purchase - Triggered when someone purchases a GitHub Marketplace plan, cancels their plan, upgrades their plan (effective immediately), downgrades a plan that remains pending until the end of the billing cycle, or cancels a pending plan change
- `member`: Member - Triggered when a user accepts an invitation or is removed as a collaborator to a repository, or has their permissions changed
- `membership`: Membership - Triggered when a user is added or removed from a team. Organization hooks only.
- `meta`: Meta - Triggered when the webhook that this event is configured on is deleted
- `milestone`: Milestone - Triggered when a milestone is created, closed, opened, edited, or deleted
- `org_block`: Org Block - Triggered when an organization blocks or unblocks a user. Organization hooks only.
- `organization`: Organization - Triggered when an organization is deleted and renamed, and when a user is added, removed, or invited to an organization. Organization hooks only.
- `page_build`: Page Build - Triggered on push to a GitHub Pages enabled branch (gh-pages for project pages, master for user and organization pages)
- `project`: Project - Triggered when a project is created, updated, closed, reopened, or deleted
- `project_card`: Project Card - Triggered when a project card is created, edited, moved, converted to an issue, or deleted
- `project_column`: Project Column - Triggered when a project column is created, updated, moved, or deleted
- `public`: Public - Triggered when a private repository is open sourced
- `pull_request`: Pull Request - Triggered when a pull request is assigned, unassigned, labeled, unlabeled, opened, edited, closed, reopened, synchronize, ready\_for\_review, locked, unlocked, a pull request review is requested, or a review request is removed
- `pull_request_review`: Pull Request Review - Triggered when a pull request review is submitted into a non-pending state, the body is edited, or the review is dismissed
- `pull_request_review_comment`: Pull Request Review Comment - Triggered when a comment on a pull request's unified diff is created, edited, or deleted (in the Files Changed tab)
- `push`: Push - Triggered on a push to a repository branch. Branch pushes and repository tag pushes also trigger webhook push events. This is the default event.
- `release`: Release - Triggered when a release is published, unpublished, created, edited, deleted, or prereleased
- `repository`: Repository - Triggered when a repository is created, archived, unarchived, renamed, edited, transferred, made public, or made private. Organization hooks are also triggered when a repository is deleted.
- `repository_import`: Repository Import - Triggered when a successful, cancelled, or failed repository import finishes for a GitHub organization or a personal repository
- `repository_vulnerability_alert`: Repository Vulnerability Alert - Triggered when a security alert is created, dismissed, or resolved
- `security_advisory`: Security Advisory - Triggered when a new security advisory is published, updated, or withdrawn
- `star`: Star - Triggered when a star is added or removed from a repository
- `status`: Status - Triggered when the status of a Git commit changes
- `team`: Team - Triggered when an organization's team is created, deleted, edited, added\_to\_repository, or removed\_from\_repository. Organization hooks only.
- `team_add`: Team Add - Triggered when a repository is added to a team
- `watch`: Watch - Triggered when someone stars a repository

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

##### Options (`options`)

Optional values:
- `undefined`: insecureSSL - Whether the SSL certificate of the n8n host be verified by GitHub when delivering payloads

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Github Trigger",
  "type": "nodes-base.githubTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": [],
    "owner": {
      "mode": "list",
      "value": ""
    },
    "repository": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## GitLab Trigger

## Basic Information

- Node Type: `nodes-base.gitlabTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when GitLab events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events to listen to |
| `owner` | string | Yes | `""` | Owner of the repository |
| `repository` | string | Yes | `""` | The name of the repository |
| `authentication` | options | No | `"accessToken"` | - |

#### Property Details

##### Events (`events`)

The events to listen to

Optional values:
- `note`: Comment - Triggered when a new comment is made on commits, merge requests, issues, and code snippets
- `confidential_issues`: Confidential Issues - Triggered on confidential issues' events
- `confidential_note`: Confidential Comments - Triggered when a confidential comment is made
- `deployment`: Deployments - Triggered when a deployment starts/succeeds/fails/is cancelled
- `issues`: Issue - Triggered when a new issue is created or an existing issue was updated/closed/reopened
- `job`: Job - Triggered on status change of a job
- `merge_requests`: Merge Request - Triggered when a new merge request is created, an existing merge request was updated/merged/closed or a commit is added in the source branch
- `pipeline`: Pipeline - Triggered on status change of Pipeline
- `push`: Push - Triggered when you push to the repository except when pushing tags
- `releases`: Release - Release events are triggered when a release is created or updated
- `tag_push`: Tag - Triggered when you create (or delete) tags to the repository
- `wiki_page`: Wiki Page - Triggered when a wiki page is created, updated or deleted
- `*`: * - Any time any event is triggered (Wildcard Event)

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "GitLab Trigger",
  "type": "nodes-base.gitlabTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": [],
    "owner": "",
    "repository": ""
  }
}
```

---

## Gmail Trigger

## Basic Information

- Node Type: `nodes-base.gmailTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Fetches emails from Gmail and starts the workflow on specified polling intervals.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `authentication` | options | No | `"oAuth2"` | - |
| `event` | options | No | `"messageReceived"` | - |
| `filters` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `serviceAccount`: Service Account

##### Event (`event`)

Optional values:
- `messageReceived`: Message Received

##### Filters (`filters`)

Optional values:
- `undefined`: includeSpamTrash - Whether to include messages from SPAM and TRASH in the results
- `undefined`: includeDrafts - Whether to include email drafts in the results
- `undefined`: labelIds - Only return messages with labels that match all of the specified label IDs. Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: q - Only return messages matching the specified query
- `undefined`: readStatus
- `undefined`: sender - Sender name or email to filter by

##### Options (`options`)

Optional values:
- `undefined`: dataPropertyAttachmentsPrefixName - Prefix for name of the binary property to which to write the attachment. An index starting with 0 will be added. So if name is 'attachment\_' the first attachment is saved to 'attachment\_0'.
- `undefined`: downloadAttachments - Whether the email's attachments will be downloaded

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Gmail Trigger",
  "type": "nodes-base.gmailTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Google Business Profile Trigger

## Basic Information

- Node Type: `nodes-base.googleBusinessProfileTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Fetches reviews from Google Business Profile and starts the workflow on specified polling intervals.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"reviewAdded"` | - |
| `account` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Google Business Profile account |
| `location` | resourceLocator | Yes | `{"mode":"list","value":""}` | The specific location or business associated with the account |

#### Property Details

##### Event (`event`)

Optional values:
- `reviewAdded`: Review Added

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Google Business Profile Trigger",
  "type": "nodes-base.googleBusinessProfileTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "reviewAdded",
    "account": {
      "mode": "list",
      "value": ""
    },
    "location": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Google Calendar Trigger

## Basic Information

- Node Type: `nodes-base.googleCalendarTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Google Calendar events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `triggerOn` | options | Yes | `""` | - |
| `calendarId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Google Calendar to operate on |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Trigger On (`triggerOn`)

Optional values:
- `eventCancelled`: Event Cancelled
- `eventCreated`: Event Created
- `eventEnded`: Event Ended
- `eventStarted`: Event Started
- `eventUpdated`: Event Updated

##### Options (`options`)

Optional values:
- `undefined`: matchTerm - Free text search terms to filter events that match these terms in any field, except for extended properties

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Google Calendar Trigger",
  "type": "nodes-base.googleCalendarTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "triggerOn": "",
    "calendarId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Google Drive Trigger

## Basic Information

- Node Type: `nodes-base.googleDriveTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Google Drive events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"fileUpdated"` | When to trigger this node |
| `event` | options | Yes | `"fileCreated"` | When to trigger this node |
| `triggerOn` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `driveToWatch` | options | Yes | `"root"` | The drive to monitor. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `fileToWatch` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `folderToWatch` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `authentication` | options | No | `"oAuth2"` | - |
| `options` | collection | No | `{}` | - |
| `asas` | notice | No | `""` | - |

#### Property Details

##### Watch For (`event`)

When to trigger this node

Optional values:
- `fileUpdated`: File Updated

##### Watch For (`event`)

When to trigger this node

Optional values:
- `fileCreated`: File Created - When a file is created in the watched drive
- `fileUpdated`: File Updated - When a file is updated in the watched drive
- `folderCreated`: Folder Created - When a folder is created in the watched drive
- `folderUpdated`: Folder Updated - When a folder is updated in the watched drive

##### Trigger On (`triggerOn`)

Optional values:
- `specificFile`: Changes to a Specific File
- `specificFolder`: Changes Involving a Specific Folder

##### Watch For (`event`)

Optional values:
- `fileCreated`: File Created - When a file is created in the watched folder
- `fileUpdated`: File Updated - When a file is updated in the watched folder
- `folderCreated`: Folder Created - When a folder is created in the watched folder
- `folderUpdated`: Folder Updated - When a folder is updated in the watched folder
- `watchFolderUpdated`: Watch Folder Updated - When the watched folder itself is modified

##### Credential Type (`authentication`)

Optional values:
- `oAuth2`: OAuth2 (recommended)
- `serviceAccount`: Service Account

##### Options (`options`)

Optional values:
- `undefined`: fileType - Triggers only when the file is this type

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Google Drive Trigger",
  "type": "nodes-base.googleDriveTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "",
    "triggerOn": "",
    "driveToWatch": "root",
    "fileToWatch": {
      "mode": "list",
      "value": ""
    },
    "folderToWatch": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Google Sheets Trigger

## Basic Information

- Node Type: `nodes-base.googleSheetsTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Google Sheets events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"anyUpdate"` | It will be triggered also by newly created columns (if the 'Columns to Watch' option is not set) |
| `documentId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `sheetName` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `authentication` | hidden | No | `"triggerOAuth2"` | - |
| `includeInOutput` | options | No | `"new"` | This option will be effective only when automatically executing the workflow |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Trigger On (`event`)

It will be triggered also by newly created columns (if the 'Columns to Watch' option is not set)

Optional values:
- `rowAdded`: Row Added
- `rowUpdate`: Row Updated
- `anyUpdate`: Row Added or Updated

##### Authentication (`authentication`)

Optional values:
- `triggerOAuth2`: OAuth2 (recommended)

##### Include in Output (`includeInOutput`)

This option will be effective only when automatically executing the workflow

Optional values:
- `new`: New Version
- `old`: Old Version
- `both`: Both Versions

##### Options (`options`)

Optional values:
- `undefined`: columnsToWatch - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: dataLocationOnSheet
- `undefined`: valueRender - Determines how values will be rendered in the output. \<a href="https://developers.google.com/sheets/api/reference/rest/v4/ValueRenderOption" target="\_blank"\>More info\</a\>.
- `undefined`: dateTimeRenderOption - Determines how dates should be rendered in the output.  \<a href="https://developers.google.com/sheets/api/reference/rest/v4/DateTimeRenderOption" target="\_blank"\>More info\</a\>.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Google Sheets Trigger",
  "type": "nodes-base.googleSheetsTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "anyUpdate",
    "documentId": {
      "mode": "list",
      "value": ""
    },
    "sheetName": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Gumroad Trigger

## Basic Information

- Node Type: `nodes-base.gumroadTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Gumroad events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `""` | The resource is gonna fire the event |

#### Property Details

##### Resource (`resource`)

The resource is gonna fire the event

Optional values:
- `cancellation`: Cancellation - When subscribed to this resource, you will be notified of cancellations of the user's subscribers
- `dispute`: Dispute - When subscribed to this resource, you will be notified of the disputes raised against user's sales
- `dispute_won`: Dispute Won - When subscribed to this resource, you will be notified of the sale disputes won
- `refund`: Refund - When subscribed to this resource, you will be notified of refunds to the user's sales
- `sale`: Sale - When subscribed to this resource, you will be notified of the user's sales

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Gumroad Trigger",
  "type": "nodes-base.gumroadTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": ""
  }
}
```

---

## Help Scout Trigger

## Basic Information

- Node Type: `nodes-base.helpScoutTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Help Scout events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | - |

#### Property Details

##### Events (`events`)

Optional values:
- `convo.assigned`: Conversation - Assigned
- `convo.created`: Conversation - Created
- `convo.deleted`: Conversation - Deleted
- `convo.merged`: Conversation - Merged
- `convo.moved`: Conversation - Moved
- `convo.status`: Conversation - Status
- `convo.tags`: Conversation - Tags
- `convo.agent.reply.created`: Conversation Agent Reply - Created
- `convo.customer.reply.created`: Conversation Customer Reply - Created
- `convo.note.created`: Conversation Note - Created
- `customer.created`: Customer - Created
- `satisfaction.ratings`: Rating - Received

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Help Scout Trigger",
  "type": "nodes-base.helpScoutTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## HubSpot Trigger

## Basic Information

- Node Type: `nodes-base.hubspotTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when HubSpot events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `eventsUi` | fixedCollection | No | `{}` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Events (`eventsUi`)

Optional values:
- `undefined`: eventValues

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: maxConcurrentRequests

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "HubSpot Trigger",
  "type": "nodes-base.hubspotTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Interval

## Basic Information

- Node Type: `nodes-base.interval`
- Category: trigger
- Package: n8n-nodes-base

### Description

Triggers the workflow in a given interval

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `unit` | options | No | `"seconds"` | Unit of the interval value |
| `interval` | number | No | `1` | Interval value |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Unit (`unit`)

Unit of the interval value

Optional values:
- `seconds`: Seconds
- `minutes`: Minutes
- `hours`: Hours

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Interval",
  "type": "nodes-base.interval",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Invoice Ninja Trigger

## Basic Information

- Node Type: `nodes-base.invoiceNinjaTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Invoice Ninja events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | - |
| `apiVersion` | options | No | `"v4"` | - |
| `apiVersion` | options | No | `"v5"` | - |

#### Property Details

##### Event (`event`)

Optional values:
- `create_client`: Client Created
- `create_invoice`: Invoice Created
- `create_payment`: Payment Created
- `create_quote`: Quote Created
- `create_vendor`: Vendor Created

##### API Version (`apiVersion`)

Optional values:
- `v4`: Version 4
- `v5`: Version 5

##### API Version (`apiVersion`)

Optional values:
- `v4`: Version 4
- `v5`: Version 5

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Invoice Ninja Trigger",
  "type": "nodes-base.invoiceNinjaTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": ""
  }
}
```

---

## Jira Trigger

## Basic Information

- Node Type: `nodes-base.jiraTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Jira events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events to listen to |
| `incomingAuthentication` | options | No | `"none"` | If authentication should be activated for the webhook (makes it more secure) |
| `jiraVersion` | options | No | `"cloud"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `authenticateWebhook` | boolean | No | `false` | Whether authentication should be activated for the incoming webhooks (makes it more secure) |

#### Property Details

##### Events (`events`)

The events to listen to

Optional values:
- `*`: *
- `board_configuration_changed`: Board Configuration Changed
- `board_created`: Board Created
- `board_deleted`: Board Deleted
- `board_updated`: Board Updated
- `comment_created`: Comment Created
- `comment_deleted`: Comment Deleted
- `comment_updated`: Comment Updated
- `jira:issue_created`: Issue Created
- `jira:issue_deleted`: Issue Deleted
- `issuelink_created`: Issue Link Created
- `issuelink_deleted`: Issue Link Deleted
- `jira:issue_updated`: Issue Updated
- `option_attachments_changed`: Option Attachments Changed
- `option_issuelinks_changed`: Option Issue Links Changed
- `option_subtasks_changed`: Option Subtasks Changed
- `option_timetracking_changed`: Option Timetracking Changed
- `option_unassigned_issues_changed`: Option Unassigned Issues Changed
- `option_voting_changed`: Option Voting Changed
- `option_watching_changed`: Option Watching Changed
- `project_created`: Project Created
- `project_deleted`: Project Deleted
- `project_updated`: Project Updated
- `sprint_closed`: Sprint Closed
- `sprint_created`: Sprint Created
- `sprint_deleted`: Sprint Deleted
- `sprint_started`: Sprint Started
- `sprint_updated`: Sprint Updated
- `user_created`: User Created
- `user_deleted`: User Deleted
- `user_updated`: User Updated
- `jira:version_created`: Version Created
- `jira:version_deleted`: Version Deleted
- `jira:version_moved`: Version Moved
- `jira:version_released`: Version Released
- `jira:version_unreleased`: Version Unreleased
- `jira:version_updated`: Version Updated
- `worklog_created`: Worklog Created
- `worklog_deleted`: Worklog Deleted
- `worklog_updated`: Worklog Updated

##### Authenticate Webhook With (`incomingAuthentication`)

If authentication should be activated for the webhook (makes it more secure)

Optional values:
- `queryAuth`: Query Auth
- `none`: None

##### Jira Version (`jiraVersion`)

Optional values:
- `cloud`: Cloud
- `server`: Server (Self Hosted)
- `serverPat`: Server (Pat) (Self Hosted)

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: excludeBody - Whether a request with empty body will be sent to the URL. Leave unchecked if you want to receive JSON.
- `undefined`: filter - You can specify a JQL query to send only events triggered by matching issues. The JQL filter only applies to events under the Issue and Comment columns.
- `undefined`: includeFields

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Jira Trigger",
  "type": "nodes-base.jiraTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Jotform Trigger

## Basic Information

- Node Type: `nodes-base.jotFormTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Jotform events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `form` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `resolveData` | boolean | No | `true` | By default does the webhook-data use internal keys instead of the names. If this option gets activated, it will resolve the keys automatically to the actual names. |
| `onlyAnswers` | boolean | No | `true` | Whether to return only the answers of the form and not any of the other data |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Jotform Trigger",
  "type": "nodes-base.jotFormTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "form": ""
  }
}
```

---

## Kafka Trigger

## Basic Information

- Node Type: `nodes-base.kafkaTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume messages from a Kafka topic

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `topic` | string | Yes | `""` | Name of the queue of topic to consume from |
| `groupId` | string | Yes | `""` | ID of the consumer group |
| `schemaRegistryUrl` | string | Yes | `""` | URL of the schema registry |
| `options` | collection | No | `{}` | - |
| `useSchemaRegistry` | boolean | No | `false` | Whether to use Confluent Schema Registry |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: allowAutoTopicCreation - Whether to allow sending message to a previously non exisiting topic
- `undefined`: autoCommitThreshold - The consumer will commit offsets after resolving a given number of messages
- `undefined`: autoCommitInterval - The consumer will commit offsets after a given period, for example, five seconds
- `undefined`: heartbeatInterval - Heartbeats are used to ensure that the consumer's session stays active
- `undefined`: maxInFlightRequests - The maximum number of unacknowledged requests the client will send on a single connection
- `undefined`: fromBeginning - Whether to read message from beginning
- `undefined`: jsonParseMessage - Whether to try to parse the message to an object
- `undefined`: parallelProcessing - Whether to process messages in parallel or by keeping the message in order
- `undefined`: onlyMessage - Whether to return only the message property
- `undefined`: returnHeaders - Whether to return the headers received from Kafka
- `undefined`: sessionTimeout - The time to await a response in ms

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Kafka Trigger",
  "type": "nodes-base.kafkaTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "topic": "",
    "groupId": "",
    "schemaRegistryUrl": ""
  }
}
```

---

## Keap Trigger

## Basic Information

- Node Type: `nodes-base.keapTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Infusionsoft events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `eventId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `rawData` | boolean | No | `false` | Whether to return the data exactly in the way it got received from the API |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Keap Trigger",
  "type": "nodes-base.keapTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "eventId": ""
  }
}
```

---

## KoBoToolbox Trigger

## Basic Information

- Node Type: `nodes-base.koBoToolboxTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Process KoBoToolbox submissions

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `triggerOn` | options | Yes | `"formSubmission"` | - |
| `formId` | options | Yes | `""` | Form ID (e.g. aSAvYreNzVEkrWg5Gdcvg). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `formatOptions` | collection | No | `{}` | - |

#### Property Details

##### Trigger On (`triggerOn`)

Optional values:
- `formSubmission`: On Form Submission

##### Options (`formatOptions`)

Optional values:
- `undefined`: download - Whether to download submitted attachments
- `undefined`: binaryNamingScheme
- `undefined`: dataPropertyAttachmentsPrefixName - Prefix for name of the binary property to which to write the attachments. An index starting with 0 will be added. So if name is "attachment\_" the first attachment is saved to "attachment\_0"
- `undefined`: version - Attachment size to retrieve, if multiple versions are available
- `undefined`: selectMask - Comma-separated list of wildcard-style selectors for fields that should be treated as multiselect fields, i.e. parsed as arrays.
- `undefined`: numberMask - Comma-separated list of wildcard-style selectors for fields that should be treated as numbers
- `undefined`: reformat - Whether to apply some reformatting to the submission data, such as parsing GeoJSON coordinates

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "KoBoToolbox Trigger",
  "type": "nodes-base.koBoToolboxTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "triggerOn": "formSubmission",
    "formId": ""
  }
}
```

---

## Lemlist Trigger

## Basic Information

- Node Type: `nodes-base.lemlistTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Lemlist events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Event (`event`)

Optional values:
- `*`: *
- `contacted`: Contacted
- `hooked`: Hooked
- `attracted`: Attracted
- `warmed`: Warmed
- `interested`: Interested
- `skipped`: Skipped
- `notInterested`: Not Interested
- `emailsSent`: Emails Sent
- `emailsOpened`: Emails Opened
- `emailsClicked`: Emails Clicked
- `emailsReplied`: Emails Replied
- `emailsBounced`: Emails Bounced
- `emailsSendFailed`: Emails Send Failed
- `emailsFailed`: Emails Failed
- `emailsUnsubscribed`: Emails Unsubscribed
- `emailsInterested`: Emails Interested
- `emailsNotInterested`: Emails Not Interested
- `opportunitiesDone`: Opportunities Done
- `aircallCreated`: Aircall Created
- `aircallEnded`: Aircall Ended
- `aircallDone`: Aircall Done
- `aircallInterested`: Aircall Interested
- `aircallNotInterested`: Aircall Not Interested
- `apiDone`: Api Done
- `apiInterested`: Api Interested
- `apiNotInterested`: Api Not Interested
- `apiFailed`: Api Failed
- `linkedinVisitDone`: LinkedIn Visit Done
- `linkedinVisitFailed`: LinkedIn Visit Failed
- `linkedinInviteDone`: LinkedIn Invite Done
- `linkedinInviteFailed`: LinkedIn Invite Failed
- `linkedinInviteAccepted`: LinkedIn Invite Accepted
- `linkedinReplied`: LinkedIn Replied
- `linkedinSent`: LinkedIn Sent
- `linkedinVoiceNoteDone`: LinkedIn Voice Note Done
- `linkedinVoiceNoteFailed`: LinkedIn Voice Note Failed
- `linkedinInterested`: LinkedIn Interested
- `linkedinNotInterested`: LinkedIn Not Interested
- `linkedinSendFailed`: LinkedIn Send Failed
- `manualInterested`: Manual Interested
- `manualNotInterested`: Manual Not Interested
- `paused`: Paused
- `resumed`: Resumed
- `customDomainErrors`: Custom Domain Errors
- `connectionIssue`: Connection Issue
- `sendLimitReached`: Send Limit Reached
- `lemwarmPaused`: Lemwarm Paused

##### Options (`options`)

Optional values:
- `undefined`: campaignId - We'll call this hook only for this campaignId. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: isFirst - Whether to call this hook only the first time this activity happened

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Lemlist Trigger",
  "type": "nodes-base.lemlistTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": ""
  }
}
```

---

## Linear Trigger

## Basic Information

- Node Type: `nodes-base.linearTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Linear events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resources` | multiOptions | Yes | `[]` | - |
| `authentication` | options | No | `"apiToken"` | - |
| `teamId` | options | No | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Listen to Resources (`resources`)

Optional values:
- `reaction`: Comment Reaction
- `cycle`: Cycle
- `issue`: Issue
- `comment`: Issue Comment
- `issueLabel`: Issue Label
- `project`: Project

##### Authentication (`authentication`)

Optional values:
- `apiToken`: API Token
- `oAuth2`: OAuth2

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Linear Trigger",
  "type": "nodes-base.linearTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resources": []
  }
}
```

---

## Local File Trigger

## Basic Information

- Node Type: `nodes-base.localFileTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Triggers a workflow on file system changes

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events to listen to |
| `triggerOn` | options | Yes | `""` | - |
| `path` | string | No | `""` | - |
| `path` | string | No | `""` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Watch for (`events`)

The events to listen to

Optional values:
- `add`: File Added - Triggers whenever a new file was added
- `change`: File Changed - Triggers whenever a file was changed
- `unlink`: File Deleted - Triggers whenever a file was deleted
- `addDir`: Folder Added - Triggers whenever a new folder was added
- `unlinkDir`: Folder Deleted - Triggers whenever a folder was deleted

##### Trigger On (`triggerOn`)

Optional values:
- `file`: Changes to a Specific File
- `folder`: Changes Involving a Specific Folder

##### Options (`options`)

Optional values:
- `undefined`: awaitWriteFinish - Whether to wait until files finished writing to avoid partially read
- `undefined`: followSymlinks - Whether linked files/folders will also be watched (this includes symlinks, aliases on MacOS and shortcuts on Windows). Otherwise only the links themselves will be monitored).
- `undefined`: ignored - Files or paths to ignore. The whole path is tested, not just the filename. Supports \<a href="https://github.com/micromatch/anymatch"\>Anymatch\</a\>- syntax. Regex patterns may not work on macOS. To ignore files based on substring matching, use the 'Ignore Mode' option with 'Contain'.
- `undefined`: ignoreInitial - Whether to ignore existing files/folders to not trigger an event
- `undefined`: depth - How deep into the folder structure to watch for changes
- `undefined`: usePolling - Whether to use polling for watching. Typically necessary to successfully watch files over a network.
- `undefined`: ignoreMode - Whether to ignore files using regex matching (Anymatch patterns) or by checking if the path contains a specified value

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Local File Trigger",
  "type": "nodes-base.localFileTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": [],
    "triggerOn": ""
  }
}
```

---

## LoneScale Trigger

## Basic Information

- Node Type: `nodes-base.loneScaleTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Trigger LoneScale Workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workflow` | options | Yes | `""` | Select one workflow. Choose from the list |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "LoneScale Trigger",
  "type": "nodes-base.loneScaleTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workflow": ""
  }
}
```

---

## Mailchimp Trigger

## Basic Information

- Node Type: `nodes-base.mailchimpTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Mailchimp events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events that can trigger the webhook and whether they are enabled |
| `sources` | multiOptions | Yes | `[]` | The possible sources of any events that can trigger the webhook and whether they are enabled |
| `list` | options | Yes | `""` | The list that is gonna fire the event. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `authentication` | options | No | `"apiKey"` | - |

#### Property Details

##### Events (`events`)

The events that can trigger the webhook and whether they are enabled

Optional values:
- `campaign`: Campaign Sent - Whether the webhook is triggered when a campaign is sent or cancelled
- `cleaned`: Cleaned - Whether the webhook is triggered when a subscriber's email address is cleaned from the list
- `upemail`: Email Address Updated - Whether the webhook is triggered when a subscriber's email address is changed
- `profile`: Profile Updated - Whether the webhook is triggered when a subscriber's profile is updated
- `subscribe`: Subscribe - Whether the webhook is triggered when a list subscriber is added
- `unsubscribe`: Unsubscribe - Whether the webhook is triggered when a list member unsubscribes

##### Sources (`sources`)

The possible sources of any events that can trigger the webhook and whether they are enabled

Optional values:
- `user`: User - Whether the webhook is triggered by subscriber-initiated actions
- `admin`: Admin - Whether the webhook is triggered by admin-initiated actions in the web interface
- `api`: API - Whether the webhook is triggered by actions initiated via the API

##### Authentication (`authentication`)

Optional values:
- `apiKey`: API Key
- `oAuth2`: OAuth2

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Mailchimp Trigger",
  "type": "nodes-base.mailchimpTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": [],
    "sources": [],
    "list": ""
  }
}
```

---

## MailerLite Trigger

## Basic Information

- Node Type: `nodes-base.mailerLiteTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when MailerLite events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The events to listen to |

#### Property Details

##### Events (`events`)

The events to listen to

Optional values:
- `campaign.sent`: Campaign Sent - Fired when campaign is sent
- `subscriber.added_to_group`: Subscriber Added to Group - Fired when a subscriber is added to a group
- `subscriber.automation_completed`: Subscriber Automation Completed - Fired when subscriber finishes automation
- `subscriber.automation_triggered`: Subscriber Automation Triggered - Fired when subscriber starts automation
- `subscriber.bounced`: Subscriber Bounced - Fired when an email address bounces
- `subscriber.created`: Subscriber Created - Fired when a new subscriber is added to an account
- `subscriber.removed_from_group`: Subscriber Removed From Group - Fired when a subscriber is removed from a group
- `subscriber.spam_reported`: Subscriber Spam Reported - Fired when subscriber marks a campaign as a spam
- `subscriber.unsubscribed`: Subscriber Unsubscribe - Fired when a subscriber becomes unsubscribed
- `subscriber.updated`: Subscriber Updated - Fired when any of the subscriber's custom fields are updated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "MailerLite Trigger",
  "type": "nodes-base.mailerLiteTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Mailjet Trigger

## Basic Information

- Node Type: `nodes-base.mailjetTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Mailjet events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"open"` | Determines which resource events the webhook is triggered for |

#### Property Details

##### Event (`event`)

Determines which resource events the webhook is triggered for

Optional values:
- `blocked`: email.blocked
- `bounce`: email.bounce
- `open`: email.open
- `sent`: email.sent
- `spam`: email.spam
- `unsub`: email.unsub

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Mailjet Trigger",
  "type": "nodes-base.mailjetTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "open"
  }
}
```

---

## Manual Chat Trigger

## Basic Information

- Node Type: `nodes-langchain.manualChatTrigger`
- Category: trigger
- Package: @n8n/n8n-nodes-langchain

### Description

Runs the flow on new manual chat message

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `notice` | notice | No | `""` | - |
| `openChat` | button | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Manual Chat Trigger",
  "type": "nodes-langchain.manualChatTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Manual Trigger

## Basic Information

- Node Type: `nodes-base.manualTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Runs the flow on clicking a button in n8n

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Manual Trigger",
  "type": "nodes-base.manualTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Mautic Trigger

## Basic Information

- Node Type: `nodes-base.mauticTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Mautic events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `authentication` | options | No | `"credentials"` | - |
| `eventsOrder` | options | No | `"ASC"` | Order direction for queued events in one webhook. Can be “DESC” or “ASC”. |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `credentials`: Credentials
- `oAuth2`: OAuth2

##### Events Order (`eventsOrder`)

Order direction for queued events in one webhook. Can be “DESC” or “ASC”.

Optional values:
- `ASC`: ASC
- `DESC`: DESC

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Mautic Trigger",
  "type": "nodes-base.mauticTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## MCP Server Trigger

## Basic Information

- Node Type: `nodes-langchain.mcpTrigger`
- Category: trigger
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Expose n8n tools as an MCP Server endpoint

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `path` | string | Yes | `""` | The base path for this MCP server |
| `authentication` | options | No | `"none"` | The way to authenticate |

#### Property Details

##### Authentication (`authentication`)

The way to authenticate

Optional values:
- `none`: None
- `bearerAuth`: Bearer Auth
- `headerAuth`: Header Auth

### Connection Guide

### Connection Type

- Input Types: `ai_tool` (tool)

### Can Receive From

1. AI Agent Tool - via `ai_tool` connection
2. MCP Client Tool - via `ai_tool` connection
3. Calculator - via `ai_tool` connection
4. Code Tool - via `ai_tool` connection
5. HTTP Request Tool - via `ai_tool` connection
6. SearXNG - via `ai_tool` connection
7. SerpApi (Google Search) - via `ai_tool` connection
8. Think Tool - via `ai_tool` connection
9. Vector Store Question Answer Tool - via `ai_tool` connection
10. Wikipedia - via `ai_tool` connection

### Special Requirements

This AI node requires the following special inputs:

- tool (optional, multiple allowed)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "MCP Server Trigger",
  "type": "nodes-langchain.mcpTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": ""
  }
}
```

---

## Microsoft OneDrive Trigger

## Basic Information

- Node Type: `nodes-base.microsoftOneDriveTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Trigger for Microsoft OneDrive API.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fileId` | resourceLocator | Yes | `{"mode":"id","value":""}` | The file to operate on. The 'By URL' option only accepts URLs that start with 'https://onedrive.live.com'. |
| `folderId` | resourceLocator | Yes | `{"mode":"id","value":"","cachedResultName":""}` | The folder to operate on. The 'By URL' option only accepts URLs that start with 'https://onedrive.live.com'. |
| `folderId` | resourceLocator | Yes | `{"mode":"id","value":"","cachedResultName":""}` | The folder to operate on. The 'By URL' option only accepts URLs that start with 'https://onedrive.live.com'. |
| `watch` | options | No | `"anyFile"` | How to select which file to watch |
| `watch` | options | No | `"anyFolder"` | How to select which folder to watch |
| `event` | options | No | `"fileCreated"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |
| `watchFolder` | boolean | No | `false` | Whether to watch for the created file in a given folder, rather than the entire OneDrive |

#### Property Details

##### Watch (`watch`)

How to select which file to watch

Optional values:
- `anyFile`: Any File - Watch for updated files in the entire OneDrive
- `selectedFolder`: Inside a Folder - Watch for updated files inside a selected folder
- `selectedFile`: A Selected File - Watch a specific file for updates

##### Watch (`watch`)

How to select which folder to watch

Optional values:
- `anyFolder`: Any Folder - Watch for updated folders in the entire OneDrive
- `selectedFolder`: Inside a Folder - Watch for updated folders inside a selected folder
- `oneSelectedFolder`: A Selected Folder - Watch a specific folder for updates

##### Trigger On (`event`)

Optional values:
- `fileCreated`: File Created - When a new file is created
- `fileUpdated`: File Updated - When an existing file is modified
- `folderCreated`: Folder Created - When a new folder is created
- `folderUpdated`: Folder Updated - When an existing folder is modified

##### Options (`options`)

Optional values:
- `undefined`: folderChild - Whether to look for modified files/folders in all nested folders, rather than only direct descendants

##### Options (`options`)

Optional values:
- `undefined`: folderChild - Whether to look for modified files/folders in all nested folders, rather than only direct descendants

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Microsoft OneDrive Trigger",
  "type": "nodes-base.microsoftOneDriveTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fileId": {
      "mode": "id",
      "value": ""
    },
    "folderId": {
      "mode": "id",
      "value": "",
      "cachedResultName": ""
    }
  }
}
```

---

## Microsoft Outlook Trigger

## Basic Information

- Node Type: `nodes-base.microsoftOutlookTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Fetches emails from Microsoft Outlook and starts the workflow on specified polling intervals.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fields` | multiOptions | No | `[]` | The fields to add to the output |
| `event` | options | No | `"messageReceived"` | - |
| `output` | options | No | `"simple"` | - |
| `filters` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Fields (`fields`)

The fields to add to the output

Optional values:
- `bccRecipients`: bccRecipients
- `body`: body
- `bodyPreview`: bodyPreview
- `categories`: categories
- `ccRecipients`: ccRecipients
- `changeKey`: changeKey
- `conversationId`: conversationId
- `createdDateTime`: createdDateTime
- `flag`: flag
- `from`: from
- `hasAttachments`: hasAttachments
- `importance`: importance
- `inferenceClassification`: inferenceClassification
- `internetMessageId`: internetMessageId
- `isDeliveryReceiptRequested`: isDeliveryReceiptRequested
- `isDraft`: isDraft
- `isRead`: isRead
- `isReadReceiptRequested`: isReadReceiptRequested
- `lastModifiedDateTime`: lastModifiedDateTime
- `parentFolderId`: parentFolderId
- `receivedDateTime`: receivedDateTime
- `replyTo`: replyTo
- `sender`: sender
- `sentDateTime`: sentDateTime
- `subject`: subject
- `toRecipients`: toRecipients
- `webLink`: webLink

##### Trigger On (`event`)

Optional values:
- `messageReceived`: Message Received

##### Output (`output`)

Optional values:
- `simple`: Simplified
- `raw`: Raw
- `fields`: Select Included Fields

##### Filters (`filters`)

Optional values:
- `undefined`: custom
- `undefined`: hasAttachments
- `undefined`: foldersToExclude - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: foldersToInclude - Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>
- `undefined`: readStatus
- `undefined`: sender - Sender name or email to filter by

##### Options (`options`)

Optional values:
- `undefined`: attachmentsPrefix - Prefix for name of the output fields to put the binary files data in. An index starting from 0 will be added. So if name is "attachment\_" the first attachment is saved to "attachment\_0".
- `undefined`: downloadAttachments - Whether the message's attachments will be downloaded and included in the output

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Microsoft Outlook Trigger",
  "type": "nodes-base.microsoftOutlookTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Microsoft Teams Trigger

## Basic Information

- Node Type: `nodes-base.microsoftTeamsTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Triggers workflows in n8n based on events from Microsoft Teams, such as new messages or team updates, using specified configurations.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `teamId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select a team from the list, enter an ID or a URL |
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select a channel from the list, enter an ID or a URL |
| `chatId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select a chat from the list, enter an ID or a URL |
| `event` | options | No | `"newChannelMessage"` | Select the event to trigger the workflow |
| `watchAllTeams` | boolean | No | `false` | Whether to watch for the event in all the available teams |
| `watchAllChannels` | boolean | No | `false` | Whether to watch for the event in all the available channels |
| `watchAllChats` | boolean | No | `false` | Whether to watch for the event in all the available chats |

#### Property Details

##### Trigger On (`event`)

Select the event to trigger the workflow

Optional values:
- `newChannel`: New Channel - A new channel is created
- `newChannelMessage`: New Channel Message - A message is posted to a channel
- `newChat`: New Chat - A new chat is created
- `newChatMessage`: New Chat Message - A message is posted to a chat
- `newTeamMember`: New Team Member - A new member is added to a team

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Microsoft Teams Trigger",
  "type": "nodes-base.microsoftTeamsTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "teamId": {
      "mode": "list",
      "value": ""
    },
    "channelId": {
      "mode": "list",
      "value": ""
    },
    "chatId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## MQTT Trigger

## Basic Information

- Node Type: `nodes-base.mqttTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Listens to MQTT events

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `topics` | string | No | `""` | Topics to subscribe to, multiple can be defined with comma. Wildcard characters are supported (+ - for single level and # - for multi level). By default all subscription used QoS=0. To set a different QoS, write the QoS desired after the topic preceded by a colom. For Example: topicA:1,topicB:2 |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: jsonParseBody - Whether to try parse the message to an object
- `undefined`: onlyMessage - Whether to return only the message property
- `undefined`: parallelProcessing - Whether to process messages in parallel or by keeping the message in order

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "MQTT Trigger",
  "type": "nodes-base.mqttTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## n8n Form Trigger

## Basic Information

- Node Type: `nodes-base.formTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Generate webforms in n8n and pass their responses to the workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `path` | string | Yes | `""` | The final segment of the form's URL, both for test and production |
| `formTitle` | string | Yes | `""` | Shown at the top of the form |
| `authentication` | options | No | `"none"` | - |
| `responseMode` | options | No | `"onReceived"` | When to respond to the form submission |
| `responseMode` | options | No | `"onReceived"` | When to respond to the form submission |
| `formFields` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `formDescription` | string | No | `""` | Shown underneath the Form Title. Can be used to prompt the user on how to complete the form. Accepts HTML. |
| `formNotice` | notice | No | `""` | - |
| `addFormPage` | notice | No | `""` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `basicAuth`: Basic Auth
- `none`: None

##### Respond When (`responseMode`)

When to respond to the form submission

Optional values:
- `onReceived`: Form Is Submitted - As soon as this node receives the form submission
- `lastNode`: Workflow Finishes - When the last node of the workflow is executed
- `responseNode`: Using 'Respond to Webhook' Node - When the 'Respond to Webhook' node is executed

##### Respond When (`responseMode`)

When to respond to the form submission

Optional values:
- `onReceived`: Form Is Submitted - As soon as this node receives the form submission
- `lastNode`: Workflow Finishes - When the last node of the workflow is executed

##### Form Elements (`formFields`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: appendAttribution - Whether to include the link “Form automated with n8n” at the bottom of the form
- `undefined`: buttonLabel - The label of the submit button in the form
- `undefined`: path - The final segment of the form's URL, both for test and production
- `undefined`: respondWithOptions
- `undefined`: ignoreBots - Whether to ignore requests from bots like link previewers and web crawlers
- `undefined`: useWorkflowTimezone - Whether to use the workflow timezone in 'submittedAt' field or UTC
- `undefined`: useWorkflowTimezone - Whether to use the workflow timezone in 'submittedAt' field or UTC
- `undefined`: customCss - Override default styling of the public form interface with CSS

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "n8n Form Trigger",
  "type": "nodes-base.formTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "path": "",
    "formTitle": ""
  }
}
```

---

## n8n Trigger

## Basic Information

- Node Type: `nodes-base.n8nTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Handle events and perform actions on your n8n instance

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | Specifies under which conditions an execution should happen:
				<ul>
					<li><b>Active Workflow Updated</b>: Triggers when this workflow is updated</li>
					<li><b>Instance Started</b>:  Triggers when this n8n instance is started or re-started</li>
					<li><b>Workflow Activated</b>: Triggers when this workflow is activated</li>
				</ul> |

#### Property Details

##### Events (`events`)

Specifies under which conditions an execution should happen:
				\<ul\>
					\<li\>\<b\>Active Workflow Updated\</b\>: Triggers when this workflow is updated\</li\>
					\<li\>\<b\>Instance Started\</b\>:  Triggers when this n8n instance is started or re-started\</li\>
					\<li\>\<b\>Workflow Activated\</b\>: Triggers when this workflow is activated\</li\>
				\</ul\>

Optional values:
- `update`: Active Workflow Updated - Triggers when this workflow is updated
- `init`: Instance Started - Triggers when this n8n instance is started or re-started
- `activate`: Workflow Activated - Triggers when this workflow is activated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "n8n Trigger",
  "type": "nodes-base.n8nTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Netlify Trigger

## Basic Information

- Node Type: `nodes-base.netlifyTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle netlify events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | - |
| `siteId` | options | Yes | `""` | Select the Site ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `formId` | options | Yes | `""` | Select a form. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |

#### Property Details

##### Event (`event`)

Optional values:
- `deployBuilding`: Deploy Building
- `deployFailed`: Deploy Failed
- `deployCreated`: Deploy Created
- `submissionCreated`: Form Submitted

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Netlify Trigger",
  "type": "nodes-base.netlifyTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "",
    "siteId": "",
    "formId": ""
  }
}
```

---

## Notion Trigger

## Basic Information

- Node Type: `nodes-base.notionTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Notion events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"pageAddedToDatabase"` | - |
| `databaseId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Notion Database to operate on |
| `simple` | boolean | No | `true` | Whether to return a simplified version of the response instead of the raw data |
| `notionNotice` | notice | No | `""` | - |

#### Property Details

##### Event (`event`)

Optional values:
- `pageAddedToDatabase`: Page Added to Database
- `pagedUpdatedInDatabase`: Page Updated in Database

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Notion Trigger",
  "type": "nodes-base.notionTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "pageAddedToDatabase",
    "databaseId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Onfleet Trigger

## Basic Information

- Node Type: `nodes-base.onfleetTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Onfleet events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `triggerOn` | options | Yes | `[]` | - |
| `additionalFields` | collection | No | `{}` | - |

#### Property Details

##### Trigger On (`triggerOn`)

Optional values:
- `SMSRecipientOptOut`: SMS Recipient Opt Out
- `smsRecipientResponseMissed`: SMS Recipient Response Missed
- `taskArrival`: Task Arrival
- `taskAssigned`: Task Assigned
- `taskCloned`: Task Cloned
- `taskCompleted`: Task Completed
- `taskCreated`: Task Created
- `taskDelayed`: Task Delayed
- `taskDeleted`: Task Deleted
- `taskEta`: Task ETA
- `taskFailed`: Task Failed
- `taskStarted`: Task Started
- `taskUnassigned`: Task Unassigned
- `taskUpdated`: Task Updated
- `workerCreated`: Worker Created
- `workerDeleted`: Worker Deleted
- `workerDuty`: Worker Duty

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: name - A name for the webhook for identification

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Onfleet Trigger",
  "type": "nodes-base.onfleetTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "triggerOn": []
  }
}
```

---

## PayPal Trigger

## Basic Information

- Node Type: `nodes-base.payPalTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle PayPal events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The event to listen to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "PayPal Trigger",
  "type": "nodes-base.payPalTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Pipedrive Trigger

## Basic Information

- Node Type: `nodes-base.pipedriveTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Pipedrive events occur

### Available Operations

### Added
Data got added
- Value: `added`

### All
Any change
- Value: `*`

### Deleted
Data got deleted
- Value: `deleted`

### Merged
Data got merged
- Value: `merged`

### Updated
Data got updated
- Value: `updated`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `action` | options | No | `"*"` | Type of action to receive notifications about |
| `action` | options | No | `"*"` | Type of action to receive notifications about |
| `authentication` | options | No | `"apiToken"` | - |
| `incomingAuthentication` | options | No | `"none"` | If authentication should be activated for the webhook (makes it more secure) |
| `entity` | options | No | `"*"` | Type of object to receive notifications about |
| `object` | options | No | `"*"` | Type of object to receive notifications about |

#### Property Details

##### Action (`action`)

Type of action to receive notifications about

Optional values:
- `added`: Added - Data got added
- `*`: All - Any change
- `deleted`: Deleted - Data got deleted
- `merged`: Merged - Data got merged
- `updated`: Updated - Data got updated

##### Action (`action`)

Type of action to receive notifications about

Optional values:
- `*`: All - Any change
- `create`: Create - Data got added
- `delete`: Delete - Data got deleted
- `change`: Change - Data got changed

##### Authentication (`authentication`)

Optional values:
- `apiToken`: API Token
- `oAuth2`: OAuth2

##### Incoming Authentication (`incomingAuthentication`)

If authentication should be activated for the webhook (makes it more secure)

Optional values:
- `basicAuth`: Basic Auth
- `none`: None

##### Entity (`entity`)

Type of object to receive notifications about

Optional values:
- `activity`: Activity
- `activityType`: Activity Type
- `*`: All
- `deal`: Deal
- `note`: Note
- `organization`: Organization
- `person`: Person
- `pipeline`: Pipeline
- `product`: Product
- `stage`: Stage
- `user`: User

##### Object (`object`)

Type of object to receive notifications about

Optional values:
- `activity`: Activity
- `activityType`: Activity Type
- `*`: All
- `deal`: Deal
- `note`: Note
- `organization`: Organization
- `person`: Person
- `pipeline`: Pipeline
- `product`: Product
- `stage`: Stage
- `user`: User

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Pipedrive Trigger",
  "type": "nodes-base.pipedriveTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

#### Added Example
```json
{
  "name": "Pipedrive Trigger",
  "type": "nodes-base.pipedriveTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "added"
  }
}
```

#### All Example
```json
{
  "name": "Pipedrive Trigger",
  "type": "nodes-base.pipedriveTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "operation": "*"
  }
}
```

---

## Postgres Trigger

## Basic Information

- Node Type: `nodes-base.postgresTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Listens to Postgres messages

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `channelName` | string | Yes | `""` | Name of the channel to listen to |
| `schema` | resourceLocator | Yes | `{"mode":"list","value":"public"}` | - |
| `tableName` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `triggerMode` | options | No | `"createTrigger"` | - |
| `firesOn` | options | No | `"INSERT"` | - |
| `additionalFields` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Listen For (`triggerMode`)

Optional values:
- `createTrigger`: Table Row Change Events - Insert, update or delete
- `listenTrigger`: Advanced - Listen to existing Postgres channel

##### Event to listen for (`firesOn`)

Optional values:
- `INSERT`: Insert
- `UPDATE`: Update
- `DELETE`: Delete

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: channelName - Name of the channel to listen to
- `undefined`: functionName - Name of the function to create
- `undefined`: replaceIfExists - Whether to replace an existing function and trigger with the same name
- `undefined`: triggerName - Name of the trigger to create

##### Options (`options`)

Optional values:
- `undefined`: connectionTimeout - Number of seconds reserved for connecting to the database
- `undefined`: delayClosingIdleConnection - Number of seconds to wait before idle connection would be eligible for closing

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Postgres Trigger",
  "type": "nodes-base.postgresTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channelName": "",
    "schema": {
      "mode": "list",
      "value": "public"
    },
    "tableName": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Postmark Trigger

## Basic Information

- Node Type: `nodes-base.postmarkTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Postmark events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | Webhook events that will be enabled for that endpoint |
| `firstOpen` | boolean | No | `false` | Only fires on first open for event "Open" |
| `includeContent` | boolean | No | `false` | Whether to include message content for events "Bounce" and "Spam Complaint" |

#### Property Details

##### Events (`events`)

Webhook events that will be enabled for that endpoint

Optional values:
- `bounce`: Bounce - Trigger on bounce
- `click`: Click - Trigger on click
- `delivery`: Delivery - Trigger on delivery
- `open`: Open - Trigger webhook on open
- `spamComplaint`: Spam Complaint - Trigger on spam complaint
- `subscriptionChange`: Subscription Change - Trigger on subscription change

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Postmark Trigger",
  "type": "nodes-base.postmarkTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Pushcut Trigger

## Basic Information

- Node Type: `nodes-base.pushcutTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Pushcut events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `actionName` | string | No | `""` | Choose any name you would like. It will show up as a server action in the app. |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Pushcut Trigger",
  "type": "nodes-base.pushcutTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## RabbitMQ Trigger

## Basic Information

- Node Type: `nodes-base.rabbitmqTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Listens to RabbitMQ messages

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `queue` | string | No | `""` | The name of the queue to read from |
| `laterMessageNode` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: arguments - Arguments to add
- `undefined`: assertExchange - Whether to assert the exchange exists before sending
- `undefined`: assertQueue - Whether to assert the queue exists before sending
- `undefined`: autoDelete - Whether the queue will be deleted when the number of consumers drops to zero
- `undefined`: binding - Add binding to queu
- `undefined`: contentIsBinary - Whether to save the content as binary
- `undefined`: acknowledge - When to acknowledge the message
- `undefined`: durable - Whether the queue will survive broker restarts
- `undefined`: exclusive - Whether to scope the queue to the connection
- `undefined`: headers - Headers to add
- `undefined`: jsonParseBody - Whether to parse the body to an object
- `undefined`: onlyContent - Whether to return only the content property
- `undefined`: parallelMessages - Max number of executions at a time. Use -1 for no limit.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "RabbitMQ Trigger",
  "type": "nodes-base.rabbitmqTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Redis Trigger

## Basic Information

- Node Type: `nodes-base.redisTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Subscribe to redis channel

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `channels` | string | Yes | `""` | Channels to subscribe to, multiple channels be defined with comma. Wildcard character(\*) is supported. |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: jsonParseBody - Whether to try to parse the message to an object
- `undefined`: onlyMessage - Whether to return only the message property

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Redis Trigger",
  "type": "nodes-base.redisTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channels": ""
  }
}
```

---

## RSS Feed Trigger

## Basic Information

- Node Type: `nodes-base.rssFeedReadTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Starts a workflow when an RSS feed is updated

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `feedUrl` | string | Yes | `"https://blog.n8n.io/rss/"` | URL of the RSS feed to poll |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "RSS Feed Trigger",
  "type": "nodes-base.rssFeedReadTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "feedUrl": "https://blog.n8n.io/rss/"
  }
}
```

---

## Salesforce Trigger

## Basic Information

- Node Type: `nodes-base.salesforceTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Fetches data from Salesforce and starts the workflow on specified polling intervals.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `customObject` | options | Yes | `""` | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `triggerOn` | options | No | `""` | Which Salesforce event should trigger the node |

#### Property Details

##### Trigger On (`triggerOn`)

Which Salesforce event should trigger the node

Optional values:
- `accountCreated`: Account Created - When a new account is created
- `accountUpdated`: Account Updated - When an existing account is modified
- `attachmentCreated`: Attachment Created - When a file is uploaded and attached to an object
- `attachmentUpdated`: Attachment Updated - When an existing file is modified
- `caseCreated`: Case Created - When a new case is created
- `caseUpdated`: Case Updated - When an existing case is modified
- `contactCreated`: Contact Created - When a new contact is created
- `contactUpdated`: Contact Updated - When an existing contact is modified
- `customObjectCreated`: Custom Object Created - When a new object of a given type is created
- `customObjectUpdated`: Custom Object Updated - When an object of a given type is modified
- `leadCreated`: Lead Created - When a new lead is created
- `leadUpdated`: Lead Updated - When an existing lead is modified
- `opportunityCreated`: Opportunity Created - When a new opportunity is created
- `opportunityUpdated`: Opportunity Updated - When an existing opportunity is modified
- `taskCreated`: Task Created - When a new task is created
- `taskUpdated`: Task Updated - When an existing task is modified
- `userCreated`: User Created - When a new user is created
- `userUpdated`: User Updated - When an existing user is modified

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Salesforce Trigger",
  "type": "nodes-base.salesforceTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "customObject": ""
  }
}
```

---

## Schedule Trigger

## Basic Information

- Node Type: `nodes-base.scheduleTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Triggers the workflow on a given schedule

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `rule` | fixedCollection | No | `{"interval":[{"field":"days"}]}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Trigger Rules (`rule`)

Optional values:
- `undefined`: interval

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Schedule Trigger",
  "type": "nodes-base.scheduleTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## SeaTable Trigger

## Basic Information

- Node Type: `nodes-base.seaTableTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when SeaTable events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `tableName` | options | Yes | `""` | The name of SeaTable table to access. Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>. |
| `assetColumn` | options | Yes | `""` | Select the digital-signature column that should be tracked. Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>. |
| `event` | options | No | `"newRow"` | - |
| `options` | collection | No | `{}` | - |
| `viewName` | options | No | `""` | The name of SeaTable view to access. Choose from the list, or specify the name using an <a href="https://docs.n8n.io/code-examples/expressions/">expression</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Event (`event`)

Optional values:
- `newRow`: New Row - Trigger on newly created rows
- `updatedRow`: New or Updated Row - Trigger has recently created or modified rows
- `newAsset`: New Signature - Trigger on new signatures

##### Options (`options`)

Optional values:
- `undefined`: simple - Whether to return a simplified version of the response instead of the raw data
- `undefined`: convert - Whether to return the column keys (false) or the column names (true)

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "SeaTable Trigger",
  "type": "nodes-base.seaTableTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "tableName": "",
    "assetColumn": ""
  }
}
```

---

## Shopify Trigger

## Basic Information

- Node Type: `nodes-base.shopifyTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Shopify events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `authentication` | options | No | `"apiKey"` | - |
| `topic` | options | No | `""` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2
- `apiKey`: API Key

##### Trigger On (`topic`)

Optional values:
- `app/uninstalled`: App Uninstalled
- `carts/create`: Cart Created
- `carts/update`: Cart Updated
- `checkouts/create`: Checkout Created
- `checkouts/delete`: Checkout Delete
- `checkouts/update`: Checkout Update
- `collections/create`: Collection Created
- `collections/delete`: Collection Deleted
- `collection_listings/add`: Collection Listings Added
- `collection_listings/remove`: Collection Listings Removed
- `collection_listings/update`: Collection Listings Updated
- `collections/update`: Collection Updated
- `customers/create`: Customer Created
- `customers/delete`: Customer Deleted
- `customers/disable`: Customer Disabled
- `customers/enable`: Customer Enabled
- `customer_groups/create`: Customer Groups Created
- `customer_groups/delete`: Customer Groups Deleted
- `customer_groups/update`: Customer Groups Updated
- `customers/update`: Customer Updated
- `draft_orders/create`: Draft Orders Created
- `draft_orders/delete`: Draft Orders Deleted
- `draft_orders/update`: Draft Orders Updated
- `fulfillments/create`: Fulfillment Created
- `fulfillment_events/create`: Fulfillment Events Created
- `fulfillment_events/delete`: Fulfillment Events Deleted
- `fulfillments/update`: Fulfillment Updated
- `inventory_items/create`: Inventory Items Created
- `inventory_items/delete`: Inventory Items Deleted
- `inventory_items/update`: Inventory Items Updated
- `inventory_levels/connect`: Inventory Levels Connected
- `inventory_levels/disconnect`: Inventory Levels Disconnected
- `inventory_levels/update`: Inventory Levels Updated
- `locales/create`: Locale Created
- `locales/update`: Locale Updated
- `locations/create`: Location Created
- `locations/delete`: Location Deleted
- `locations/update`: Location Updated
- `orders/cancelled`: Order Cancelled
- `orders/create`: Order Created
- `orders/fulfilled`: Order Fulfilled
- `orders/paid`: Order Paid
- `orders/partially_fulfilled`: Order Partially Fulfilled
- `order_transactions/create`: Order Transactions Created
- `orders/updated`: Order Updated
- `orders/delete`: Orders Deleted
- `products/create`: Product Created
- `products/delete`: Product Deleted
- `product_listings/add`: Product Listings Added
- `product_listings/remove`: Product Listings Removed
- `product_listings/update`: Product Listings Updated
- `products/update`: Product Updated
- `refunds/create`: Refund Created
- `shop/update`: Shop Updated
- `tender_transactions/create`: Tender Transactions Created
- `themes/create`: Theme Created
- `themes/delete`: Theme Deleted
- `themes/publish`: Theme Published
- `themes/update`: Theme Updated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Shopify Trigger",
  "type": "nodes-base.shopifyTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Simulate Trigger

## Basic Information

- Node Type: `nodes-base.simulateTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Simulate a trigger node

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `icon` | options | No | `"n8n-nodes-base.manualTrigger"` | Select a type of node to show corresponding icon |
| `executionDuration` | number | No | `150` | Execution duration in milliseconds |
| `subtitle` | string | No | `""` | - |
| `jsonOutput` | json | No | `"[\n  {\n  \"my_field_1\": \"value\",\n  \"my_field_2\": 1\n  }\n]"` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Simulate Trigger",
  "type": "nodes-base.simulateTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Slack Trigger

## Basic Information

- Node Type: `nodes-base.slackTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Slack events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `channelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | The Slack channel to listen to events from. Applies to events: Bot/App mention, File Shared, New Message Posted on Channel, Reaction Added. |
| `authentication` | hidden | No | `"accessToken"` | - |
| `trigger` | multiOptions | No | `[]` | - |
| `options` | collection | No | `{}` | - |
| `watchWorkspace` | boolean | No | `false` | Whether to watch for the event in the whole workspace, rather than a specific channel |
| `downloadFiles` | boolean | No | `false` | Whether to download the files and add it to the output |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Trigger On (`trigger`)

Optional values:
- `any_event`: Any Event - Triggers on any event
- `app_mention`: Bot / App Mention - When your bot or app is mentioned in a channel the app is added to
- `file_public`: File Made Public - When a file is made public
- `file_share`: File Shared - When a file is shared in a channel the app is added to
- `message`: New Message Posted to Channel - When a message is posted to a channel the app is added to
- `channel_created`: New Public Channel Created - When a new public channel is created
- `team_join`: New User - When a new user is added to Slack
- `reaction_added`: Reaction Added - When a reaction is added to a message the app is added to

##### Options (`options`)

Optional values:
- `undefined`: resolveIds - Whether to resolve the IDs to their respective names and return them
- `undefined`: userIds - A comma-separated string of encoded user IDs. Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Slack Trigger",
  "type": "nodes-base.slackTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "channelId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## SSE Trigger

## Basic Information

- Node Type: `nodes-base.sseTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Triggers the workflow when Server-Sent Events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `url` | string | Yes | `""` | The URL to receive the SSE from |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "SSE Trigger",
  "type": "nodes-base.sseTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "url": ""
  }
}
```

---

## Strava Trigger

## Basic Information

- Node Type: `nodes-base.stravaTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Strava events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `object` | options | No | `"*"` | - |
| `event` | options | No | `"*"` | - |
| `options` | collection | No | `{}` | - |
| `resolveData` | boolean | No | `true` | By default the webhook-data only contain the Object ID. If this option gets activated, it will resolve the data automatically. |

#### Property Details

##### Object (`object`)

Optional values:
- `*`: [All]
- `activity`: Activity
- `athlete`: Athlete

##### Event (`event`)

Optional values:
- `*`: [All]
- `create`: Created
- `delete`: Deleted
- `update`: Updated

##### Options (`options`)

Optional values:
- `undefined`: deleteIfExist - Strava allows just one subscription at all times. If you want to delete the current subscription to make room for a new subscription with the current parameters, set this parameter to true. Keep in mind this is a destructive operation.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Strava Trigger",
  "type": "nodes-base.stravaTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Stripe Trigger

## Basic Information

- Node Type: `nodes-base.stripeTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Stripe events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | The event to listen to |
| `apiVersion` | string | No | `""` | The API version to use for requests. It controls the format and structure of the incoming event payloads that Stripe sends to your webhook. If empty, Stripe will use the default API version set in your account at the time, which may lead to event processing issues if the API version changes in the future. |

#### Property Details

##### Events (`events`)

The event to listen to

Optional values:
- `*`: * - Any time any event is triggered (Wildcard Event)
- `account.updated`: Account Updated - Occurs whenever an account status or property has changed
- `account.application.authorized`: Account Application.authorized - Occurs whenever a user authorizes an application. Sent to the related application only.
- `account.application.deauthorized`: Account Application.deauthorized - Occurs whenever a user deauthorizes an application. Sent to the related application only.
- `account.external_account.created`: Account External_account.created - Occurs whenever an external account is created.
- `account.external_account.deleted`: Account External_account.deleted - Occurs whenever an external account is deleted.
- `account.external_account.updated`: Account External_account.updated - Occurs whenever an external account is updated.
- `application_fee.created`: Application Fee.created - Occurs whenever an application fee is created on a charge.
- `application_fee.refunded`: Application Fee.refunded - Occurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.
- `application_fee.refund.updated`: Application Fee.refund.updated - Occurs whenever an application fee refund is updated.
- `balance.available`: Balance Available - Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis.
- `capability.updated`: Capability Updated - Occurs whenever a capability has new requirements or a new status.
- `charge.captured`: Charge Captured - Occurs whenever a previously uncaptured charge is captured.
- `charge.expired`: Charge Expired - Occurs whenever an uncaptured charge expires.
- `charge.failed`: Charge Failed - Occurs whenever a failed charge attempt occurs.
- `charge.pending`: Charge Pending - Occurs whenever a pending charge is created.
- `charge.refunded`: Charge Refunded - Occurs whenever a charge is refunded, including partial refunds.
- `charge.succeeded`: Charge Succeeded - Occurs whenever a new charge is created and is successful.
- `charge.updated`: Charge Updated - Occurs whenever a charge description or metadata is updated.
- `charge.dispute.closed`: Charge Dispute.closed - Occurs when a dispute is closed and the dispute status changes to lost, warning\_closed, or won.
- `charge.dispute.created`: Charge Dispute.created - Occurs whenever a customer disputes a charge with their bank.
- `charge.dispute.funds_reinstated`: Charge Dispute.funds_reinstated - Occurs when funds are reinstated to your account after a dispute is closed. This includes partially refunded payments.
- `charge.dispute.funds_withdrawn`: Charge Dispute.funds_withdrawn - Occurs when funds are removed from your account due to a dispute.
- `charge.dispute.updated`: Charge Dispute.updated - Occurs when the dispute is updated (usually with evidence).
- `charge.refund.updated`: Charge Refund.updated - Occurs whenever a refund is updated, on selected payment methods.
- `checkout.session.completed`: Checkout Session.completed - Occurs when a Checkout Session has been successfully completed.
- `coupon.created`: Coupon Created - Occurs whenever a coupon is created.
- `coupon.deleted`: Coupon Deleted - Occurs whenever a coupon is deleted.
- `coupon.updated`: Coupon Updated - Occurs whenever a coupon is updated.
- `credit_note.created`: Credit Note.created - Occurs whenever a credit note is created.
- `credit_note.updated`: Credit Note.updated - Occurs whenever a credit note is updated.
- `credit_note.voided`: Credit Note.voided - Occurs whenever a credit note is voided.
- `customer.created`: Customer Created - Occurs whenever a new customer is created.
- `customer.deleted`: Customer Deleted - Occurs whenever a customer is deleted.
- `customer.updated`: Customer Updated - Occurs whenever any property of a customer changes.
- `customer.discount.created`: Customer Discount.created - Occurs whenever a coupon is attached to a customer.
- `customer.discount.deleted`: Customer Discount.deleted - Occurs whenever a coupon is removed from a customer.
- `customer.discount.updated`: Customer Discount.updated - Occurs whenever a customer is switched from one coupon to another.
- `customer.source.created`: Customer Source.created - Occurs whenever a new source is created for a customer.
- `customer.source.deleted`: Customer Source.deleted - Occurs whenever a source is removed from a customer.
- `customer.source.expiring`: Customer Source.expiring - Occurs whenever a card or source will expire at the end of the month.
- `customer.source.updated`: Customer Source.updated - Occurs whenever a source's details are changed.
- `customer.subscription.created`: Customer Subscription.created - Occurs whenever a customer is signed up for a new plan.
- `customer.subscription.deleted`: Customer Subscription.deleted - Occurs whenever a customer's subscription ends.
- `customer.subscription.trial_will_end`: Customer Subscription.trial_will_end - Occurs three days before a subscription's trial period is scheduled to end, or when a trial is ended immediately (using trial\_end=now).
- `customer.subscription.updated`: Customer Subscription.updated - Occurs whenever a subscription changes (e.g., switching from one plan to another, or changing the status from trial to active).
- `customer.tax_id.created`: Customer Tax_id.created - Occurs whenever a tax ID is created for a customer.
- `customer.tax_id.deleted`: Customer Tax_id.deleted - Occurs whenever a tax ID is deleted from a customer.
- `customer.tax_id.updated`: Customer Tax_id.updated - Occurs whenever a customer's tax ID is updated.
- `file.created`: File Created - Occurs whenever a new Stripe-generated file is available for your account.
- `invoice.created`: Invoice Created - Occurs whenever a new invoice is created. To learn how webhooks can be used with this event, and how they can affect it, see Using Webhooks with Subscriptions.
- `invoice.deleted`: Invoice Deleted - Occurs whenever a draft invoice is deleted.
- `invoice.finalized`: Invoice Finalized - Occurs whenever a draft invoice is finalized and updated to be an open invoice.
- `invoice.marked_uncollectible`: Invoice Marked_uncollectible - Occurs whenever an invoice is marked uncollectible.
- `invoice.payment_action_required`: Invoice Payment_action_required - Occurs whenever an invoice payment attempt requires further user action to complete.
- `invoice.payment_failed`: Invoice Payment_failed - Occurs whenever an invoice payment attempt fails, due either to a declined payment or to the lack of a stored payment method.
- `invoice.payment_succeeded`: Invoice Payment_succeeded - Occurs whenever an invoice payment attempt succeeds.
- `invoice.sent`: Invoice Sent - Occurs whenever an invoice email is sent out.
- `invoice.upcoming`: Invoice Upcoming - Occurs X number of days before a subscription is scheduled to create an invoice that is automatically charged—where X is determined by your subscriptions settings. Note: The received Invoice object will not have an invoice ID.
- `invoice.updated`: Invoice Updated - Occurs whenever an invoice changes (e.g., the invoice amount).
- `invoice.voided`: Invoice Voided - Occurs whenever an invoice is voided.
- `invoiceitem.created`: Invoiceitem Created - Occurs whenever an invoice item is created.
- `invoiceitem.deleted`: Invoiceitem Deleted - Occurs whenever an invoice item is deleted.
- `invoiceitem.updated`: Invoiceitem Updated - Occurs whenever an invoice item is updated.
- `issuing_authorization.created`: Issuing Authorization.created - Occurs whenever an authorization is created.
- `issuing_authorization.request`: Issuing Authorization.request - Represents a synchronous request for authorization, see Using your integration to handle authorization requests.
- `issuing_authorization.updated`: Issuing Authorization.updated - Occurs whenever an authorization is updated.
- `issuing_card.created`: Issuing Card.created - Occurs whenever a card is created.
- `issuing_card.updated`: Issuing Card.updated - Occurs whenever a card is updated.
- `issuing_cardholder.created`: Issuing Cardholder.created - Occurs whenever a cardholder is created.
- `issuing_cardholder.updated`: Issuing Cardholder.updated - Occurs whenever a cardholder is updated.
- `issuing_dispute.created`: Issuing Dispute.created - Occurs whenever a dispute is created.
- `issuing_dispute.updated`: Issuing Dispute.updated - Occurs whenever a dispute is updated.
- `issuing_settlement.created`: Issuing Settlement.created - Occurs whenever an issuing settlement is created.
- `issuing_settlement.updated`: Issuing Settlement.updated - Occurs whenever an issuing settlement is updated.
- `issuing_transaction.created`: Issuing Transaction.created - Occurs whenever an issuing transaction is created.
- `issuing_transaction.updated`: Issuing Transaction.updated - Occurs whenever an issuing transaction is updated.
- `order.created`: Order Created - Occurs whenever an order is created.
- `order.payment_failed`: Order Payment_failed - Occurs whenever an order payment attempt fails.
- `order.payment_succeeded`: Order Payment_succeeded - Occurs whenever an order payment attempt succeeds.
- `order.updated`: Order Updated - Occurs whenever an order is updated.
- `order_return.created`: Order Return.created - Occurs whenever an order return is created.
- `payment_intent.amount_capturable_updated`: Payment Intent.amount_capturable_updated - Occurs when a PaymentIntent has funds to be captured. Check the amount\_capturable property on the PaymentIntent to determine the amount that can be captured. You may capture the PaymentIntent with an amount\_to\_capture value up to the specified amount. Learn more about capturing PaymentIntents.
- `payment_intent.canceled`: Payment Intent.canceled - Occurs when a PaymentIntent is canceled.
- `payment_intent.created`: Payment Intent.created - Occurs when a new PaymentIntent is created.
- `payment_intent.payment_failed`: Payment Intent.payment_failed - Occurs when a PaymentIntent has failed the attempt to create a source or a payment.
- `payment_intent.succeeded`: Payment Intent.succeeded - Occurs when a PaymentIntent has been successfully fulfilled.
- `payment_intent.requires_action`: Payment Intent.requires_action - Occurs when a PaymentIntent requires an action.
- `payment_method.attached`: Payment Method.attached - Occurs whenever a new payment method is attached to a customer.
- `payment_method.card_automatically_updated`: Payment Method.card_automatically_updated - Occurs whenever a card payment method's details are automatically updated by the network.
- `payment_method.detached`: Payment Method.detached - Occurs whenever a payment method is detached from a customer.
- `payment_method.updated`: Payment Method.updated - Occurs whenever a payment method is updated via the PaymentMethod update API.
- `payout.canceled`: Payout Canceled - Occurs whenever a payout is canceled.
- `payout.created`: Payout Created - Occurs whenever a payout is created.
- `payout.failed`: Payout Failed - Occurs whenever a payout attempt fails.
- `payout.paid`: Payout Paid - Occurs whenever a payout is expected to be available in the destination account. If the payout fails, a payout.failed notification is also sent, at a later time.
- `payout.updated`: Payout Updated - Occurs whenever a payout is updated.
- `person.created`: Person Created - Occurs whenever a person associated with an account is created.
- `person.deleted`: Person Deleted - Occurs whenever a person associated with an account is deleted.
- `person.updated`: Person Updated - Occurs whenever a person associated with an account is updated.
- `plan.created`: Plan Created - Occurs whenever a plan is created.
- `plan.deleted`: Plan Deleted - Occurs whenever a plan is deleted.
- `plan.updated`: Plan Updated - Occurs whenever a plan is updated.
- `product.created`: Product Created - Occurs whenever a product is created.
- `product.deleted`: Product Deleted - Occurs whenever a product is deleted.
- `product.updated`: Product Updated - Occurs whenever a product is updated.
- `radar.early_fraud_warning.created`: Radar Early_fraud_warning.created - Occurs whenever an early fraud warning is created.
- `radar.early_fraud_warning.updated`: Radar Early_fraud_warning.updated - Occurs whenever an early fraud warning is updated.
- `recipient.created`: Recipient Created - Occurs whenever a recipient is created.
- `recipient.deleted`: Recipient Deleted - Occurs whenever a recipient is deleted.
- `recipient.updated`: Recipient Updated - Occurs whenever a recipient is updated.
- `reporting.report_run.failed`: Reporting Report_run.failed - Occurs whenever a requested \*\*ReportRun\*\* failed to complete.
- `reporting.report_run.succeeded`: Reporting Report_run.succeeded - Occurs whenever a requested \*\*ReportRun\*\* completed succesfully.
- `reporting.report_type.updated`: Reporting Report_type.updated - Occurs whenever a \*\*ReportType\*\* is updated (typically to indicate that a new day's data has come available).
- `review.closed`: Review Closed - Occurs whenever a review is closed. The review's reason field indicates why: approved, disputed, refunded, or refunded\_as\_fraud.
- `review.opened`: Review Opened - Occurs whenever a review is opened.
- `setup_intent.canceled`: Setup Intent.canceled - Occurs when a SetupIntent is canceled.
- `setup_intent.created`: Setup Intent.created - Occurs when a new SetupIntent is created.
- `setup_intent.setup_failed`: Setup Intent.setup_failed - Occurs when a SetupIntent has failed the attempt to setup a payment method.
- `setup_intent.succeeded`: Setup Intent.succeeded - Occurs when an SetupIntent has successfully setup a payment method.
- `sigma.scheduled_query_run.created`: Sigma Scheduled_query_run.created - Occurs whenever a Sigma scheduled query run finishes.
- `sku.created`: Sku Created - Occurs whenever a SKU is created.
- `sku.deleted`: Sku Deleted - Occurs whenever a SKU is deleted.
- `sku.updated`: Sku Updated - Occurs whenever a SKU is updated.
- `source.canceled`: Source Canceled - Occurs whenever a source is canceled.
- `source.chargeable`: Source Chargeable - Occurs whenever a source transitions to chargeable.
- `source.failed`: Source Failed - Occurs whenever a source fails.
- `source.mandate_notification`: Source Mandate_notification - Occurs whenever a source mandate notification method is set to manual.
- `source.refund_attributes_required`: Source Refund_attributes_required - Occurs whenever the refund attributes are required on a receiver source to process a refund or a mispayment.
- `source.transaction.created`: Source Transaction.created - Occurs whenever a source transaction is created.
- `source.transaction.updated`: Source Transaction.updated - Occurs whenever a source transaction is updated.
- `subscription_schedule.aborted`: Subscription Schedule.aborted - Occurs whenever a subscription schedule is canceled due to the underlying subscription being canceled because of delinquency.
- `subscription_schedule.canceled`: Subscription Schedule.canceled - Occurs whenever a subscription schedule is canceled.
- `subscription_schedule.completed`: Subscription Schedule.completed - Occurs whenever a new subscription schedule is completed.
- `subscription_schedule.created`: Subscription Schedule.created - Occurs whenever a new subscription schedule is created.
- `subscription_schedule.expiring`: Subscription Schedule.expiring - Occurs 7 days before a subscription schedule will expire.
- `subscription_schedule.released`: Subscription Schedule.released - Occurs whenever a new subscription schedule is released.
- `subscription_schedule.updated`: Subscription Schedule.updated - Occurs whenever a subscription schedule is updated.
- `tax_rate.created`: Tax Rate.created - Occurs whenever a new tax rate is created.
- `tax_rate.updated`: Tax Rate.updated - Occurs whenever a tax rate is updated.
- `topup.canceled`: Topup Canceled - Occurs whenever a top-up is canceled.
- `topup.created`: Topup Created - Occurs whenever a top-up is created.
- `topup.failed`: Topup Failed - Occurs whenever a top-up fails.
- `topup.reversed`: Topup Reversed - Occurs whenever a top-up is reversed.
- `topup.succeeded`: Topup Succeeded - Occurs whenever a top-up succeeds.
- `transfer.created`: Transfer Created - Occurs whenever a transfer is created.
- `transfer.failed`: Transfer Failed - Occurs whenever a transfer failed.
- `transfer.paid`: Transfer Paid - Occurs after a transfer is paid. For Instant Payouts, the event will be sent on the next business day, although the funds should be received well beforehand.
- `transfer.reversed`: Transfer Reversed - Occurs whenever a transfer is reversed, including partial reversals.
- `transfer.updated`: Transfer Updated - Occurs whenever a transfer's description or metadata is updated.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Stripe Trigger",
  "type": "nodes-base.stripeTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## SurveyMonkey Trigger

## Basic Information

- Node Type: `nodes-base.surveyMonkeyTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Survey Monkey events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `objectType` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `surveyIds` | multiOptions | Yes | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `surveyId` | options | Yes | `[]` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `collectorIds` | multiOptions | Yes | `[]` | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `authentication` | options | No | `"accessToken"` | - |
| `resolveData` | boolean | No | `true` | By default the webhook-data only contain the IDs. If this option gets activated, it will resolve the data automatically. |
| `onlyAnswers` | boolean | No | `true` | Whether to return only the answers of the form and not any of the other data |

#### Property Details

##### Type (`objectType`)

Optional values:
- `collector`: Collector
- `survey`: Survey

##### Event (`event`)

Optional values:
- `collector_created`: Collector Created - A collector is created
- `collector_deleted`: Collector Deleted - A collector is deleted
- `collector_updated`: Collector Updated - A collector is updated
- `response_completed`: Response Completed - A survey response is completed
- `response_created`: Response Created - A respondent begins a survey
- `response_deleted`: Response Deleted - A response is deleted
- `response_disqualified`: Response Disqualified - A survey response is disqualified
- `response_overquota`: Response Overquota - A response is over a survey’s quota
- `response_updated`: Response Updated - A survey response is updated
- `survey_created`: Survey Created - A survey is created
- `survey_deleted`: Survey Deleted - A survey is deleted
- `survey_updated`: Survey Updated - A survey is updated

##### Event (`event`)

Optional values:
- `collector_deleted`: Collector Deleted - A collector is deleted
- `collector_updated`: Collector Updated - A collector is updated
- `response_completed`: Response Completed - A survey response is completed
- `response_created`: Response Created - A respondent begins a survey
- `response_deleted`: Response Deleted - A response is deleted
- `response_disqualified`: Response Disqualified - A survey response is disqualified
- `response_overquota`: Response Overquota - A response is over a survey’s quota
- `response_updated`: Response Updated - A survey response is updated

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "SurveyMonkey Trigger",
  "type": "nodes-base.surveyMonkeyTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "objectType": "",
    "event": "",
    "surveyIds": [],
    "surveyId": [],
    "collectorIds": []
  }
}
```

---

## Taiga Trigger

## Basic Information

- Node Type: `nodes-base.taigaTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Taiga events via webhook

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resources` | multiOptions | Yes | `["all"]` | Resources to listen to |
| `operations` | multiOptions | Yes | `["all"]` | Operations to listen to |
| `projectId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Resources (`resources`)

Resources to listen to

Optional values:
- `all`: All
- `issue`: Issue
- `milestone`: Milestone (Sprint)
- `task`: Task
- `userstory`: User Story
- `wikipage`: Wikipage

##### Operations (`operations`)

Operations to listen to

Optional values:
- `all`: All
- `create`: Create
- `delete`: Delete
- `change`: Update

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Taiga Trigger",
  "type": "nodes-base.taigaTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resources": [
      "all"
    ],
    "operations": [
      "all"
    ],
    "projectId": ""
  }
}
```

---

## Telegram Trigger

## Basic Information

- Node Type: `nodes-base.telegramTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow on a Telegram update

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `updates` | multiOptions | Yes | `[]` | - |
| `additionalFields` | collection | No | `{}` | - |
| `telegramTriggerNotice` | notice | No | `""` | - |
| `attachmentNotice` | notice | No | `""` | - |

#### Property Details

##### Trigger On (`updates`)

Optional values:
- `*`: * - All updates
- `callback_query`: Callback Query - Trigger on new incoming callback query
- `channel_post`: Channel Post - Trigger on new incoming channel post of any kind — text, photo, sticker, etc
- `edited_channel_post`: Edited Channel Post - Trigger on new version of a channel post that is known to the bot and was edited
- `edited_message`: Edited Message - Trigger on new version of a channel post that is known to the bot and was edited
- `inline_query`: Inline Query - Trigger on new incoming inline query
- `message`: Message - Trigger on new incoming message of any kind — text, photo, sticker, etc
- `poll`: Poll - Trigger on new poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot.
- `pre_checkout_query`: Pre-Checkout Query - Trigger on new incoming pre-checkout query. Contains full information about checkout.
- `shipping_query`: Shipping Query - Trigger on new incoming shipping query. Only for invoices with flexible price.

##### Additional Fields (`additionalFields`)

Optional values:
- `undefined`: download - Telegram delivers the image in multiple sizes. By default, just the large image would be downloaded. If you want to change the size, set the field 'Image Size'.
- `undefined`: imageSize - The size of the image to be downloaded
- `undefined`: chatIds - The chat IDs to restrict the trigger to. Multiple can be defined separated by comma.
- `undefined`: userIds - The user IDs to restrict the trigger to. Multiple can be defined separated by comma.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Telegram Trigger",
  "type": "nodes-base.telegramTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updates": []
  }
}
```

---

## TheHive 5 Trigger

## Basic Information

- Node Type: `nodes-base.theHiveProjectTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Starts the workflow when TheHive events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | Events types |
| `filters` | fixedCollection | No | `{}` | Filter any incoming events based on their fields |
| `options` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Events (`events`)

Events types

Optional values:
- `*`: * - Any time any event is triggered (Wildcard Event)
- `alert_create`: Alert Created - Triggered when an alert is created
- `alert_delete`: Alert Deleted - Triggered when an alert is deleted
- `alert_update`: Alert Updated - Triggered when an alert is updated
- `case_create`: Case Created - Triggered when a case is created
- `case_delete`: Case Deleted - Triggered when a case is deleted
- `case_update`: Case Updated - Triggered when a case is updated
- `comment_create`: Comment Created - Triggered when a comment is created
- `comment_delete`: Comment Deleted - Triggered when a comment is deleted
- `comment_update`: Comment Updated - Triggered when a comment is updated
- `observable_create`: Observable Created - Triggered when an observable is created
- `observable_delete`: Observable Deleted - Triggered when an observable is deleted
- `observable_update`: Observable Updated - Triggered when an observable is updated
- `page_create`: Page Created - Triggered when an page is created
- `page_delete`: Page Deleted - Triggered when an page is deleted
- `page_update`: Page Updated - Triggered when an page is updated
- `task_create`: Task Created - Triggered when a task is created
- `task_update`: Task Updated - Triggered when a task is updated
- `log_create`: Task Log Created - Triggered when a task log is created
- `log_delete`: Task Log Deleted - Triggered when a task log is deleted
- `log_update`: Task Log Updated - Triggered when a task log is updated

##### Filters (`filters`)

Filter any incoming events based on their fields

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: outputOnlyData - Whether to output data with additional details and omit headers

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "TheHive 5 Trigger",
  "type": "nodes-base.theHiveProjectTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## TheHive Trigger

## Basic Information

- Node Type: `nodes-base.theHiveTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Starts the workflow when TheHive events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | Events types |
| `events` | multiOptions | Yes | `[]` | Events types |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Events (`events`)

Events types

Optional values:
- `*`: * - Any time any event is triggered (Wildcard Event)
- `alert_create`: Alert Created - Triggered when an alert is created
- `alert_delete`: Alert Deleted - Triggered when an alert is deleted
- `alert_update`: Alert Updated - Triggered when an alert is updated
- `case_create`: Case Created - Triggered when a case is created
- `case_delete`: Case Deleted - Triggered when a case is deleted
- `case_update`: Case Updated - Triggered when a case is updated
- `case_task_log_create`: Log Created - Triggered when a task log is created
- `case_task_log_delete`: Log Deleted - Triggered when a task log is deleted
- `case_task_log_update`: Log Updated - Triggered when a task log is updated
- `case_artifact_create`: Observable Created - Triggered when an observable is created
- `case_artifact_delete`: Observable Deleted - Triggered when an observable is deleted
- `case_artifact_update`: Observable Updated - Triggered when an observable is updated
- `case_task_create`: Task Created - Triggered when a task is created
- `case_task_delete`: Task Deleted - Triggered when a task is deleted
- `case_task_update`: Task Updated - Triggered when a task is updated

##### Events (`events`)

Events types

Optional values:
- `*`: * - Any time any event is triggered (Wildcard Event)
- `alert_create`: Alert Created - Triggered when an alert is created
- `alert_delete`: Alert Deleted - Triggered when an alert is deleted
- `alert_update`: Alert Updated - Triggered when an alert is updated
- `case_create`: Case Created - Triggered when a case is created
- `case_delete`: Case Deleted - Triggered when a case is deleted
- `case_update`: Case Updated - Triggered when a case is updated
- `case_task_log_create`: Log Created - Triggered when a task log is created
- `case_task_log_delete`: Log Deleted - Triggered when a task log is deleted
- `case_task_log_update`: Log Updated - Triggered when a task log is updated
- `case_artifact_create`: Observable Created - Triggered when an observable is created
- `case_artifact_delete`: Observable Deleted - Triggered when an observable is deleted
- `case_artifact_update`: Observable Updated - Triggered when an observable is updated
- `case_task_create`: Task Created - Triggered when a task is created
- `case_task_update`: Task Updated - Triggered when a task is updated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "TheHive Trigger",
  "type": "nodes-base.theHiveTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Toggl Trigger

## Basic Information

- Node Type: `nodes-base.togglTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Toggl events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"newTimeEntry"` | - |

#### Property Details

##### Event (`event`)

Optional values:
- `newTimeEntry`: New Time Entry

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Toggl Trigger",
  "type": "nodes-base.togglTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "newTimeEntry"
  }
}
```

---

## Trello Trigger

## Basic Information

- Node Type: `nodes-base.trelloTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Trello events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `id` | string | Yes | `""` | ID of the model of which to subscribe to events |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Trello Trigger",
  "type": "nodes-base.trelloTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "id": ""
  }
}
```

---

## Twilio Trigger

## Basic Information

- Node Type: `nodes-base.twilioTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow on a Twilio update

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `updates` | multiOptions | Yes | `[]` | - |
| `callTriggerNotice` | notice | No | `""` | - |

#### Property Details

##### Trigger On (`updates`)

Optional values:
- `com.twilio.messaging.inbound-message.received`: New SMS - When an SMS message is received
- `com.twilio.voice.insights.call-summary.complete`: New Call - When a call is received

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Twilio Trigger",
  "type": "nodes-base.twilioTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updates": []
  }
}
```

---

## Typeform Trigger

## Basic Information

- Node Type: `nodes-base.typeformTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow on a Typeform form submission

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `formId` | options | Yes | `""` | Form which should trigger workflow on submission. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `authentication` | options | No | `"accessToken"` | - |
| `simplifyAnswers` | boolean | No | `true` | Whether to convert the answers to a key:value pair ("FIELD\_TITLE":"USER\_ANSER") to be easily processable |
| `onlyAnswers` | boolean | No | `true` | Whether to return only the answers of the form and not any of the other data |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `accessToken`: Access Token
- `oAuth2`: OAuth2

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Typeform Trigger",
  "type": "nodes-base.typeformTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "formId": ""
  }
}
```

---

## Venafi TLS Protect Cloud Trigger

## Basic Information

- Node Type: `nodes-base.venafiTlsProtectCloudTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Venafi events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `[]` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `triggerOn` | multiOptions | Yes | `[]` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Venafi TLS Protect Cloud Trigger",
  "type": "nodes-base.venafiTlsProtectCloudTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": [],
    "triggerOn": []
  }
}
```

---

## Webex by Cisco Trigger

## Basic Information

- Node Type: `nodes-base.ciscoWebexTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Cisco Webex events occur.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `resource` | options | Yes | `"meeting"` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `event` | options | Yes | `""` | - |
| `filters` | collection | No | `{}` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `all`: [All]
- `attachmentAction`: Attachment Action
- `meeting`: Meeting
- `membership`: Membership
- `message`: Message
- `recording`: Recording
- `room`: Room

##### Event (`event`)

Optional values:
- `created`: Created
- `deleted`: Deleted
- `updated`: Updated
- `all`: *

##### Event (`event`)

Optional values:
- `created`: Created
- `deleted`: Deleted
- `updated`: Updated
- `all`: *

##### Event (`event`)

Optional values:
- `created`: Created
- `deleted`: Deleted
- `updated`: Updated
- `all`: *

##### Event (`event`)

Optional values:
- `created`: Created
- `deleted`: Deleted
- `updated`: Updated
- `all`: *

##### Event (`event`)

Optional values:
- `created`: Created
- `deleted`: Deleted
- `updated`: Updated
- `started`: Started
- `ended`: Ended
- `all`: *

##### Event (`event`)

Optional values:
- `created`: Created
- `deleted`: Deleted
- `updated`: Updated
- `all`: *

##### Event (`event`)

Optional values:
- `created`: Created
- `deleted`: Deleted
- `updated`: Updated

##### Event (`event`)

Optional values:
- `created`: Created
- `updated`: Updated
- `deleted`: Deleted
- `all`: *

##### Filters (`filters`)

Optional values:
- `undefined`: hasFiles - Whether to limit to messages which contain file content attachments
- `undefined`: isLocked - Whether to limit to rooms that are locked
- `undefined`: isModerator - Whether to limit to moderators of a room
- `undefined`: mentionedPeople - Limit to messages which contain these mentioned people, by person ID; accepts me as a shorthand for your own person ID; separate multiple values with commas
- `undefined`: messageId - Limit to a particular message, by ID
- `undefined`: ownedBy
- `undefined`: personEmail - Limit to a particular person, by email
- `undefined`: personEmail - Limit to a particular person, by email
- `undefined`: personId - Limit to a particular person, by ID
- `undefined`: personId - Limit to a particular person, by ID
- `undefined`: personId - Limit to a particular person, by ID
- `undefined`: roomId - Limit to a particular room, by ID
- `undefined`: roomId - Limit to a particular room, by ID
- `undefined`: roomId - Limit to a particular room, by ID
- `undefined`: roomType - Limit to a particular room type
- `undefined`: type - Limit to a particular room type

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Webex by Cisco Trigger",
  "type": "nodes-base.ciscoWebexTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "resource": "meeting",
    "event": ""
  }
}
```

---

## Webflow Trigger

## Basic Information

- Node Type: `nodes-base.webflowTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Webflow events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `"form_submission"` | - |
| `site` | options | Yes | `""` | Site that will trigger the events. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

#### Property Details

##### Event (`event`)

Optional values:
- `collection_item_created`: Collection Item Created
- `collection_item_deleted`: Collection Item Deleted
- `collection_item_changed`: Collection Item Updated
- `ecomm_inventory_changed`: Ecomm Inventory Changed
- `ecomm_new_order`: Ecomm New Order
- `ecomm_order_changed`: Ecomm Order Changed
- `form_submission`: Form Submission
- `site_publish`: Site Publish

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Webflow Trigger",
  "type": "nodes-base.webflowTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "form_submission",
    "site": ""
  }
}
```

---

## WhatsApp Trigger

## Basic Information

- Node Type: `nodes-base.whatsAppTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle WhatsApp events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `updates` | multiOptions | Yes | `[]` | - |
| `options` | collection | No | `{}` | - |
| `whatsAppNotice` | notice | No | `""` | - |

#### Property Details

##### Trigger On (`updates`)

Optional values:
- `account_review_update`: Account Review Update
- `account_update`: Account Update
- `business_capability_update`: Business Capability Update
- `message_template_quality_update`: Message Template Quality Update
- `message_template_status_update`: Message Template Status Update
- `messages`: Messages
- `phone_number_name_update`: Phone Number Name Update
- `phone_number_quality_update`: Phone Number Quality Update
- `security`: Security
- `template_category_update`: Template Category Update

##### Options (`options`)

Optional values:
- `undefined`: messageStatusUpdates - WhatsApp sends notifications to the Trigger when the status of a message changes (for example from Sent to Delivered and from Delivered to Read). To avoid multiple executions for one WhatsApp message, you can set the Trigger to execute only on selected message status updates.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "WhatsApp Trigger",
  "type": "nodes-base.whatsAppTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "updates": []
  }
}
```

---

## Wise Trigger

## Basic Information

- Node Type: `nodes-base.wiseTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Wise events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | - |
| `profileId` | options | Yes | `""` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

#### Property Details

##### Event (`event`)

Optional values:
- `balanceCredit`: Balance Credit - Triggered every time a balance account is credited
- `balanceUpdate`: Balance Update - Triggered every time a balance account is credited or debited
- `transferActiveCases`: Transfer Active Case - Triggered every time a transfer's list of active cases is updated
- `tranferStateChange`: Transfer State Changed - Triggered every time a transfer's status is updated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Wise Trigger",
  "type": "nodes-base.wiseTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": "",
    "profileId": ""
  }
}
```

---

## WooCommerce Trigger

## Basic Information

- Node Type: `nodes-base.wooCommerceTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle WooCommerce events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `event` | options | Yes | `""` | Determines which resource events the webhook is triggered for |

#### Property Details

##### Event (`event`)

Determines which resource events the webhook is triggered for

Optional values:
- `coupon.created`: coupon.created
- `coupon.deleted`: coupon.deleted
- `coupon.updated`: coupon.updated
- `customer.created`: customer.created
- `customer.deleted`: customer.deleted
- `customer.updated`: customer.updated
- `order.created`: order.created
- `order.deleted`: order.deleted
- `order.updated`: order.updated
- `product.created`: product.created
- `product.deleted`: product.deleted
- `product.updated`: product.updated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "WooCommerce Trigger",
  "type": "nodes-base.wooCommerceTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "event": ""
  }
}
```

---

## Workable Trigger

## Basic Information

- Node Type: `nodes-base.workableTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Starts the workflow when Workable events occur

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `triggerOn` | options | Yes | `""` | - |
| `filters` | collection | No | `{}` | - |

#### Property Details

##### Trigger On (`triggerOn`)

Optional values:
- `candidateCreated`: Candidate Created
- `candidateMoved`: Candidate Moved

##### Filters (`filters`)

Optional values:
- `undefined`: job - Get notifications only for one job. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.
- `undefined`: stage - Get notifications for specific stages. e.g. 'hired'. Choose from the list, or specify an ID using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Workable Trigger",
  "type": "nodes-base.workableTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "triggerOn": ""
  }
}
```

---

## Workflow Trigger

## Basic Information

- Node Type: `nodes-base.workflowTrigger`
- Category: trigger
- Package: n8n-nodes-base

### Description

Triggers based on various lifecycle events, like when a workflow is activated

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `events` | multiOptions | Yes | `[]` | Specifies under which conditions an execution should happen:
					<ul>
						<li><b>Active Workflow Updated</b>: Triggers when this workflow is updated</li>
						<li><b>Workflow Activated</b>: Triggers when this workflow is activated</li>
					</ul> |
| `oldVersionNotice` | notice | No | `""` | - |

#### Property Details

##### Events (`events`)

Specifies under which conditions an execution should happen:
					\<ul\>
						\<li\>\<b\>Active Workflow Updated\</b\>: Triggers when this workflow is updated\</li\>
						\<li\>\<b\>Workflow Activated\</b\>: Triggers when this workflow is activated\</li\>
					\</ul\>

Optional values:
- `update`: Active Workflow Updated - Triggers when this workflow is updated
- `activate`: Workflow Activated - Triggers when this workflow is activated

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Workflow Trigger",
  "type": "nodes-base.workflowTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "events": []
  }
}
```

---

## Wufoo Trigger

## Basic Information

- Node Type: `nodes-base.wufooTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Wufoo events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `form` | options | Yes | `""` | The form upon which will trigger this node when a new entry is made. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| `onlyAnswers` | boolean | No | `true` | Whether to return only the answers of the form and not any of the other data |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Wufoo Trigger",
  "type": "nodes-base.wufooTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "form": ""
  }
}
```

---

## Zendesk Trigger

## Basic Information

- Node Type: `nodes-base.zendeskTrigger`
- Category: trigger
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Handle Zendesk events via webhooks

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `service` | options | Yes | `"support"` | - |
| `authentication` | options | No | `"apiToken"` | - |
| `conditions` | fixedCollection | No | `{}` | The condition to set |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Service (`service`)

Optional values:
- `support`: Support

##### Authentication (`authentication`)

Optional values:
- `apiToken`: API Token
- `oAuth2`: OAuth2

##### Conditions (`conditions`)

The condition to set

Optional values:
- `undefined`: all
- `undefined`: any

##### Options (`options`)

Optional values:
- `undefined`: fields - The fields to return the values of. Choose from the list, or specify IDs using an \<a href="https://docs.n8n.io/code/expressions/"\>expression\</a\>.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `main` (general data flow)

### Can Connect To

1. Code - via `main` connection
2. Function - via `main` connection
3. HTTP Request - via `main` connection
4. If - via `main` connection
5. Set - via `main` connection
6. Merge - via `main` connection
7. Airtable - via `main` connection
8. Discord - via `main` connection
9. Dropbox - via `main` connection
10. GitHub - via `main` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Zendesk Trigger",
  "type": "nodes-base.zendeskTrigger",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "service": "support"
  }
}
```
