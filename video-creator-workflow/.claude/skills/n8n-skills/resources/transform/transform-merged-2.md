# Data Transformation Nodes - Node Collection (Part 2)

This file contains complete information for 100 nodes.

## Table of Contents

- [Aggregate](#aggregate)
- [AI Agent](#ai-agent)
- [AI Agent Tool](#ai-agent-tool)
- [Anthropic](#anthropic)
- [Anthropic Chat Model](#anthropic-chat-model)
- [Auto-fixing Output Parser](#auto-fixing-output-parser)
- [AWS Bedrock Chat Model](#aws-bedrock-chat-model)
- [Azure AI Search Vector Store](#azure-ai-search-vector-store)
- [Azure OpenAI Chat Model](#azure-openai-chat-model)
- [Basic LLM Chain](#basic-llm-chain)
- [Binary Input Loader](#binary-input-loader)
- [Calculator](#calculator)
- [Call n8n Sub-Workflow Tool](#call-n8n-sub-workflow-tool)
- [Character Text Splitter](#character-text-splitter)
- [Chat Memory Manager](#chat-memory-manager)
- [Chat Messages Retriever](#chat-messages-retriever)
- [Code Tool](#code-tool)
- [Cohere Chat Model](#cohere-chat-model)
- [Cohere Model](#cohere-model)
- [Contextual Compression Retriever](#contextual-compression-retriever)
- [DeepSeek Chat Model](#deepseek-chat-model)
- [Default Data Loader](#default-data-loader)
- [Embeddings AWS Bedrock](#embeddings-aws-bedrock)
- [Embeddings Azure OpenAI](#embeddings-azure-openai)
- [Embeddings Cohere](#embeddings-cohere)
- [Embeddings Google Gemini](#embeddings-google-gemini)
- [Embeddings Google Vertex](#embeddings-google-vertex)
- [Embeddings Hugging Face Inference](#embeddings-hugging-face-inference)
- [Embeddings Lemonade](#embeddings-lemonade)
- [Embeddings Mistral Cloud](#embeddings-mistral-cloud)
- [Embeddings Ollama](#embeddings-ollama)
- [Embeddings OpenAI](#embeddings-openai)
- [GitHub Document Loader](#github-document-loader)
- [Google Gemini](#google-gemini)
- [Google Gemini Chat Model](#google-gemini-chat-model)
- [Google Vertex Chat Model](#google-vertex-chat-model)
- [Groq Chat Model](#groq-chat-model)
- [Hugging Face Inference Model](#hugging-face-inference-model)
- [In Memory Vector Store Insert](#in-memory-vector-store-insert)
- [In Memory Vector Store Load](#in-memory-vector-store-load)
- [Information Extractor](#information-extractor)
- [Item List Output Parser](#item-list-output-parser)
- [JSON Input Loader](#json-input-loader)
- [LangChain Code](#langchain-code)
- [Lemonade Chat Model](#lemonade-chat-model)
- [Lemonade Model](#lemonade-model)
- [Limit](#limit)
- [MCP Client](#mcp-client)
- [Milvus Vector Store](#milvus-vector-store)
- [Mistral Cloud Chat Model](#mistral-cloud-chat-model)
- [MongoDB Atlas Vector Store](#mongodb-atlas-vector-store)
- [MongoDB Chat Memory](#mongodb-chat-memory)
- [Motorhead](#motorhead)
- [MultiQuery Retriever](#multiquery-retriever)
- [Ollama](#ollama)
- [Ollama Chat Model](#ollama-chat-model)
- [Ollama Model](#ollama-model)
- [OpenAI](#openai)
- [OpenAI Assistant](#openai-assistant)
- [OpenAI Chat Model](#openai-chat-model)
- [OpenAI Model](#openai-model)
- [OpenRouter Chat Model](#openrouter-chat-model)
- [Pinecone Vector Store](#pinecone-vector-store)
- [Pinecone: Insert](#pinecone-insert)
- [Pinecone: Load](#pinecone-load)
- [Postgres Chat Memory](#postgres-chat-memory)
- [Postgres PGVector Store](#postgres-pgvector-store)
- [Qdrant Vector Store](#qdrant-vector-store)
- [Question and Answer Chain](#question-and-answer-chain)
- [Recursive Character Text Splitter](#recursive-character-text-splitter)
- [Redis Chat Memory](#redis-chat-memory)
- [Redis Vector Store](#redis-vector-store)
- [Remove Duplicates](#remove-duplicates)
- [Reranker Cohere](#reranker-cohere)
- [SearXNG](#searxng)
- [Sentiment Analysis](#sentiment-analysis)
- [SerpApi (Google Search)](#serpapi-google-search)
- [Simple Memory](#simple-memory)
- [Simple Vector Store](#simple-vector-store)
- [Sort](#sort)
- [Split Out](#split-out)
- [Structured Output Parser](#structured-output-parser)
- [Summarization Chain](#summarization-chain)
- [Summarize](#summarize)
- [Supabase Vector Store](#supabase-vector-store)
- [Supabase: Insert](#supabase-insert)
- [Text Classifier](#text-classifier)
- [Think Tool](#think-tool)
- [Token Splitter](#token-splitter)
- [Vector Store Question Answer Tool](#vector-store-question-answer-tool)
- [Vector Store Retriever](#vector-store-retriever)
- [Vercel AI Gateway Chat Model](#vercel-ai-gateway-chat-model)
- [Wikipedia](#wikipedia)
- [Wolfram|Alpha](#wolframalpha)
- [Workflow Retriever](#workflow-retriever)
- [xAI Grok Chat Model](#xai-grok-chat-model)
- [Xata](#xata)
- [XML](#xml)
- [Zep](#zep)
- [Zoho CRM](#zoho-crm)

---

## Aggregate

## Basic Information

- Node Type: `nodes-base.aggregate`
- Category: transform
- Package: n8n-nodes-base

### Description

Combine a field from many items into a list in a single item

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `aggregate` | options | No | `"aggregateIndividualFields"` | - |
| `fieldsToAggregate` | fixedCollection | No | `{"fieldToAggregate":[{"fieldToAggregate":"","renameField":false}]}` | - |
| `include` | options | No | `"allFields"` | - |
| `options` | collection | No | `{}` | - |
| `destinationFieldName` | string | No | `"data"` | The name of the output field to put the data in |
| `fieldsToExclude` | string | No | `""` | - |
| `fieldsToInclude` | string | No | `""` | - |

#### Property Details

##### Aggregate (`aggregate`)

Optional values:
- `aggregateIndividualFields`: Individual Fields
- `aggregateAllItemData`: All Item Data (Into a Single List)

##### Fields To Aggregate (`fieldsToAggregate`)

Optional values:
- `undefined`: fieldToAggregate

##### Include (`include`)

Optional values:
- `allFields`: All Fields
- `specifiedFields`: Specified Fields
- `allFieldsExcept`: All Fields Except

##### Options (`options`)

Optional values:
- `undefined`: disableDotNotation - Whether to disallow referencing child fields using \`parent.child\` in the field name
- `undefined`: mergeLists - Whether to merge the output into a single flat list (rather than a list of lists), if the field to aggregate is a list
- `undefined`: includeBinaries - Whether to include the binary data in the new item
- `undefined`: keepOnlyUnique - Whether to keep only unique binaries by comparing mime types, file types, file sizes and file extensions
- `undefined`: keepMissing - Whether to add a null entry to the aggregated list when there is a missing or null value

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Aggregate",
  "type": "nodes-base.aggregate",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## AI Agent

## Basic Information

- Node Type: `nodes-langchain.agent`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Generates an action plan and executes it. Can use external tools.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `text` | string | Yes | `"={{ $json.guardrailsInput }}"` | - |
| `text` | string | Yes | `"={{ $json.chatInput }}"` | - |
| `text` | string | Yes | `""` | - |
| `promptType` | options | No | `"auto"` | - |
| `options` | collection | No | `{}` | - |
| `aiAgentStarterCallout` | callout | No | `""` | - |
| `hasOutputParser` | boolean | No | `false` | - |
| `notice` | notice | No | `""` | - |
| `needsFallback` | boolean | No | `false` | - |
| `fallbackNotice` | notice | No | `""` | - |

#### Property Details

##### Source for Prompt (User Message) (`promptType`)

Optional values:
- `auto`: Connected Chat Trigger Node - Looks for an input field called 'chatInput' that is coming from a directly connected Chat Trigger
- `guardrails`: Connected Guardrails Node - Looks for an input field called 'guardrailsInput' that is coming from a directly connected Guardrails Node
- `define`: Define below - Use an expression to reference data in previous nodes or enter static text

##### Options (`options`)

Optional values:
- `undefined`: systemMessage - The message that will be sent to the agent before the conversation starts
- `undefined`: maxIterations - The maximum number of iterations the agent will run before stopping
- `undefined`: returnIntermediateSteps - Whether or not the output should include intermediate steps the agent took
- `undefined`: passthroughBinaryImages - Whether or not binary images should be automatically passed through to the agent as image type messages
- `undefined`: enableStreaming - Whether this agent will stream the response in real-time as it generates text
- `undefined`: batching - Batch processing options for rate limiting
- `undefined`: maxTokensFromMemory - The maximum number of tokens to read from the chat memory history. Set to 0 to read all history.

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_languageModel` (language Model), `ai_memory` (memory), `ai_tool` (tool), `ai_outputParser` (output Parser)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
- memory (optional, multiple allowed)
- tool (optional, multiple allowed)
- output Parser (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "AI Agent",
  "type": "nodes-langchain.agent",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "text": ""
  }
}
```

---

## AI Agent Tool

## Basic Information

- Node Type: `nodes-langchain.agentTool`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Generates an action plan and executes it. Can use external tools.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolDescription` | string | Yes | `"AI Agent that can call other tools"` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `text` | string | Yes | `""` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `hasOutputParser` | boolean | No | `false` | - |
| `notice` | notice | No | `""` | - |
| `needsFallback` | boolean | No | `false` | - |
| `fallbackNotice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: systemMessage - The message that will be sent to the agent before the conversation starts
- `undefined`: maxIterations - The maximum number of iterations the agent will run before stopping
- `undefined`: returnIntermediateSteps - Whether or not the output should include intermediate steps the agent took
- `undefined`: passthroughBinaryImages - Whether or not binary images should be automatically passed through to the agent as image type messages
- `undefined`: batching - Batch processing options for rate limiting

##### Options (`options`)

Optional values:
- `undefined`: systemMessage - The message that will be sent to the agent before the conversation starts
- `undefined`: maxIterations - The maximum number of iterations the agent will run before stopping
- `undefined`: returnIntermediateSteps - Whether or not the output should include intermediate steps the agent took
- `undefined`: passthroughBinaryImages - Whether or not binary images should be automatically passed through to the agent as image type messages
- `undefined`: batching - Batch processing options for rate limiting

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `ai_tool` (tool)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "AI Agent Tool",
  "type": "nodes-langchain.agentTool",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolDescription": "AI Agent that can call other tools",
    "text": ""
  }
}
```

---

## Anthropic

## Basic Information

- Node Type: `nodes-langchain.anthropic`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Interact with Anthropic AI models

### Available Operations

### Analyze Document
Take in documents and answer questions about them
- Value: `analyze`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `resource` | options | No | `"text"` | - |
| `operation` | options | No | `"analyze"` | - |
| `operation` | options | No | `"upload"` | - |
| `operation` | options | No | `"analyze"` | - |
| `operation` | options | No | `"generate"` | - |
| `operation` | options | No | `"message"` | - |
| `messages` | fixedCollection | No | `{"values":[{"content":"","role":"user"}]}` | Messages that constitute the prompt to be improved |

#### Property Details

##### Resource (`resource`)

Optional values:
- `document`: Document
- `file`: File
- `image`: Image
- `prompt`: Prompt
- `text`: Text

##### Operation (`operation`)

Optional values:
- `analyze`: Analyze Document - Take in documents and answer questions about them

##### Operation (`operation`)

Optional values:
- `upload`: Upload File - Upload a file to the Anthropic API for later use
- `get`: Get File Metadata - Get metadata for a file from the Anthropic API
- `list`: List Files - List files from the Anthropic API
- `deleteFile`: Delete File - Delete a file from the Anthropic API

##### Operation (`operation`)

Optional values:
- `analyze`: Analyze Image - Take in images and answer questions about them

##### Operation (`operation`)

Optional values:
- `generate`: Generate Prompt - Generate a prompt for a model
- `improve`: Improve Prompt - Improve a prompt for a model
- `templatize`: Templatize Prompt - Templatize a prompt for a model

##### Operation (`operation`)

Optional values:
- `message`: Message a Model - Create a completion with Anthropic model

##### Messages (`messages`)

Messages that constitute the prompt to be improved

Optional values:
- `undefined`: values

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Anthropic",
  "type": "nodes-langchain.anthropic",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "modelId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Analyze Document Example
```json
{
  "name": "Anthropic",
  "type": "nodes-langchain.anthropic",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "modelId": {
      "mode": "list",
      "value": ""
    },
    "operation": "analyze"
  }
}
```

---

## Anthropic Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatAnthropic`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model Anthropic

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | resourceLocator | Yes | `{"mode":"list","value":"claude-sonnet-4-5-20250929","cachedResultName":"Claude Sonnet 4.5"}` | The model. Choose from the list, or specify an ID. <a href="https://docs.anthropic.com/claude/docs/models-overview">Learn more</a>. |
| `model` | options | No | `"claude-2"` | The model which will generate the completion. <a href="https://docs.anthropic.com/claude/docs/models-overview">Learn more</a>. |
| `model` | options | No | `"claude-3-sonnet-20240229"` | The model which will generate the completion. <a href="https://docs.anthropic.com/claude/docs/models-overview">Learn more</a>. |
| `model` | options | No | `"claude-3-5-sonnet-20240620"` | The model which will generate the completion. <a href="https://docs.anthropic.com/claude/docs/models-overview">Learn more</a>. |
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Model (`model`)

The model which will generate the completion. \<a href="https://docs.anthropic.com/claude/docs/models-overview"\>Learn more\</a\>.

Optional values:
- `claude-3-5-sonnet-20241022`: Claude 3.5 Sonnet(20241022)
- `claude-3-opus-20240229`: Claude 3 Opus(20240229)
- `claude-3-5-sonnet-20240620`: Claude 3.5 Sonnet(20240620)
- `claude-3-sonnet-20240229`: Claude 3 Sonnet(20240229)
- `claude-3-5-haiku-20241022`: Claude 3.5 Haiku(20241022)
- `claude-3-haiku-20240307`: Claude 3 Haiku(20240307)
- `claude-2`: LEGACY: Claude 2
- `claude-2.1`: LEGACY: Claude 2.1
- `claude-instant-1.2`: LEGACY: Claude Instant 1.2
- `claude-instant-1`: LEGACY: Claude Instant 1

##### Model (`model`)

The model which will generate the completion. \<a href="https://docs.anthropic.com/claude/docs/models-overview"\>Learn more\</a\>.

Optional values:
- `claude-3-5-sonnet-20241022`: Claude 3.5 Sonnet(20241022)
- `claude-3-opus-20240229`: Claude 3 Opus(20240229)
- `claude-3-5-sonnet-20240620`: Claude 3.5 Sonnet(20240620)
- `claude-3-sonnet-20240229`: Claude 3 Sonnet(20240229)
- `claude-3-5-haiku-20241022`: Claude 3.5 Haiku(20241022)
- `claude-3-haiku-20240307`: Claude 3 Haiku(20240307)
- `claude-2`: LEGACY: Claude 2
- `claude-2.1`: LEGACY: Claude 2.1
- `claude-instant-1.2`: LEGACY: Claude Instant 1.2
- `claude-instant-1`: LEGACY: Claude Instant 1

##### Model (`model`)

The model which will generate the completion. \<a href="https://docs.anthropic.com/claude/docs/models-overview"\>Learn more\</a\>.

Optional values:
- `claude-3-5-sonnet-20241022`: Claude 3.5 Sonnet(20241022)
- `claude-3-opus-20240229`: Claude 3 Opus(20240229)
- `claude-3-5-sonnet-20240620`: Claude 3.5 Sonnet(20240620)
- `claude-3-sonnet-20240229`: Claude 3 Sonnet(20240229)
- `claude-3-5-haiku-20241022`: Claude 3.5 Haiku(20241022)
- `claude-3-haiku-20240307`: Claude 3 Haiku(20240307)

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: maxTokensToSample - The maximum number of tokens to generate in the completion
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: topK - Used to remove "long tail" low probability responses. Defaults to -1, which disables it.
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.
- `undefined`: thinking - Whether to enable thinking mode for the model
- `undefined`: thinkingBudget - The maximum number of tokens to use for thinking

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Anthropic Chat Model",
  "type": "nodes-langchain.lmChatAnthropic",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": {
      "mode": "list",
      "value": "claude-sonnet-4-5-20250929",
      "cachedResultName": "Claude Sonnet 4.5"
    }
  }
}
```

---

## Auto-fixing Output Parser

## Basic Information

- Node Type: `nodes-langchain.outputParserAutofixing`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Deprecated, use structured output parser

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `info` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: prompt - Prompt template used for fixing the output. Uses placeholders: "{instructions}" for parsing rules, "{completion}" for the failed attempt, and "{error}" for the validation error message.

### Connection Guide

### Connection Type

- Input Types: `ai_languageModel` (language Model), `ai_outputParser` (output Parser)
- Output Types: `ai_outputParser` (output Parser)

### Can Receive From

1. Anthropic Chat Model - via `ai_languageModel` connection
2. Azure OpenAI Chat Model - via `ai_languageModel` connection
3. AWS Bedrock Chat Model - via `ai_languageModel` connection
4. Cohere Chat Model - via `ai_languageModel` connection
5. DeepSeek Chat Model - via `ai_languageModel` connection
6. Google Gemini Chat Model - via `ai_languageModel` connection
7. Google Vertex Chat Model - via `ai_languageModel` connection
8. Groq Chat Model - via `ai_languageModel` connection
9. Mistral Cloud Chat Model - via `ai_languageModel` connection
10. Lemonade Chat Model - via `ai_languageModel` connection

### Can Connect To

1. AI Agent - via `ai_outputParser` connection

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
- output Parser (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Auto-fixing Output Parser",
  "type": "nodes-langchain.outputParserAutofixing",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## AWS Bedrock Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatAwsBedrock`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model AWS Bedrock

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `modelSource` | options | No | `"onDemand"` | Choose between on-demand foundation models or inference profiles |
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `""` | The model which will generate the completion. <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html">Learn more</a>. |
| `model` | options | No | `""` | The inference profile which will generate the completion. <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-use.html">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Model Source (`modelSource`)

Choose between on-demand foundation models or inference profiles

Optional values:
- `onDemand`: On-Demand Models - Standard foundation models with on-demand pricing
- `inferenceProfile`: Inference Profiles - Cross-region inference profiles (required for models like Claude Sonnet 4 and others)

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: maxTokensToSample - The maximum number of tokens to generate in the completion
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "AWS Bedrock Chat Model",
  "type": "nodes-langchain.lmChatAwsBedrock",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Azure AI Search Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStoreAzureAISearch`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in Azure AI Search Vector Store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `indexName` | string | Yes | `"n8n-vectorstore"` | The name of the Azure AI Search index. Will be created automatically if it does not exist. |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `embeddingBatchSize` | number | No | `200` | Number of documents to embed in a single batch |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes
- `update`: Update Documents - Update documents in vector store by ID

##### Options (`options`)

Optional values:
- `undefined`: clearIndex - Whether to delete and recreate the index before inserting new data. Warning: This will reset any custom index configuration (semantic ranking, analyzers, etc.) to defaults.

##### Options (`options`)

Optional values:
- `undefined`: queryType - The type of search query to perform
- `undefined`: filter - Filter results using OData syntax. Use metadata/fieldName for metadata fields. \<a href="https://learn.microsoft.com/en-us/azure/search/search-query-odata-filter" target="\_blank"\>Learn more\</a\>.
- `undefined`: semanticConfiguration - Name of the semantic configuration for semantic ranking (optional)

##### Options (`options`)

Optional values:
- `undefined`: queryType - The type of search query to perform
- `undefined`: filter - Filter results using OData syntax. Use metadata/fieldName for metadata fields. \<a href="https://learn.microsoft.com/en-us/azure/search/search-query-odata-filter" target="\_blank"\>Learn more\</a\>.
- `undefined`: semanticConfiguration - Name of the semantic configuration for semantic ranking (optional)

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Azure AI Search Vector Store",
  "type": "nodes-langchain.vectorStoreAzureAISearch",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "indexName": "n8n-vectorstore",
    "prompt": "",
    "id": ""
  }
}
```

---

## Azure OpenAI Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatAzureOpenAi`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | string | Yes | `""` | The name of the model(deployment) to use (e.g., gpt-4, gpt-35-turbo) |
| `authentication` | options | No | `"azureOpenAiApi"` | - |
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Authentication (`authentication`)

Optional values:
- `azureOpenAiApi`: API Key
- `azureEntraCognitiveServicesOAuth2Api`: Azure Entra ID (OAuth2)

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768). Use -1 for default.
- `undefined`: responseFormat
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds
- `undefined`: maxRetries - Maximum number of retries to attempt on failure
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Azure OpenAI Chat Model",
  "type": "nodes-langchain.lmChatAzureOpenAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": ""
  }
}
```

---

## Basic LLM Chain

## Basic Information

- Node Type: `nodes-langchain.chainLlm`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

A simple chain to prompt a large language model

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `prompt` | string | Yes | `"={{ $json.input }}"` | - |
| `prompt` | string | Yes | `"={{ $json.chat_input }}"` | - |
| `prompt` | string | Yes | `"={{ $json.chatInput }}"` | - |
| `text` | string | Yes | `"={{ $json.guardrailsInput }}"` | - |
| `text` | string | Yes | `"={{ $json.chatInput }}"` | - |
| `text` | string | Yes | `""` | - |
| `batching` | collection | No | `{}` | Batch processing options for rate limiting |
| `promptType` | options | No | `"auto"` | - |
| `messages` | fixedCollection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Batch Processing (`batching`)

Batch processing options for rate limiting

Optional values:
- `undefined`: batchSize - How many items to process in parallel. This is useful for rate limiting, but might impact the log output ordering.
- `undefined`: delayBetweenBatches - Delay in milliseconds between batches. This is useful for rate limiting.

##### Source for Prompt (User Message) (`promptType`)

Optional values:
- `auto`: Connected Chat Trigger Node - Looks for an input field called 'chatInput' that is coming from a directly connected Chat Trigger
- `guardrails`: Connected Guardrails Node - Looks for an input field called 'guardrailsInput' that is coming from a directly connected Guardrails Node
- `define`: Define below - Use an expression to reference data in previous nodes or enter static text

##### Chat Messages (if Using a Chat Model) (`messages`)

Optional values:
- `undefined`: messageValues

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Basic LLM Chain",
  "type": "nodes-langchain.chainLlm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "prompt": "={{ $json.chatInput }}",
    "text": ""
  }
}
```

---

## Binary Input Loader

## Basic Information

- Node Type: `nodes-langchain.documentBinaryInputLoader`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Use binary data from a previous step in the workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `loader` | options | Yes | `"jsonLoader"` | - |
| `binaryDataKey` | string | Yes | `"data"` | Name of the binary property from which to read the file buffer |
| `options` | collection | No | `{}` | - |
| `column` | string | No | `""` | Column to extract from CSV |
| `separator` | string | No | `","` | Separator to use for CSV |
| `pointers` | string | No | `""` | Pointers to extract from JSON, e.g. "/text" or "/text, /meta/title" |
| `notice` | notice | No | `""` | - |
| `splitPages` | boolean | No | `true` | - |

#### Property Details

##### Loader Type (`loader`)

Optional values:
- `csvLoader`: CSV Loader - Load CSV files
- `docxLoader`: Docx Loader - Load Docx documents
- `epubLoader`: EPub Loader - Load EPub files
- `jsonLoader`: JSON Loader - Load JSON files
- `pdfLoader`: PDF Loader - Load PDF documents
- `textLoader`: Text Loader - Load plain text files

##### Options (`options`)

Optional values:
- `undefined`: metadata - Metadata to add to each document. Could be used for filtering during retrieval

### Connection Guide

### Connection Type

- Input Types: `ai_textSplitter` (text Splitter)
- Output Types: `ai_document` (document)

### Can Receive From

1. Character Text Splitter - via `ai_textSplitter` connection
2. Recursive Character Text Splitter - via `ai_textSplitter` connection
3. Token Splitter - via `ai_textSplitter` connection

### Can Connect To

1. In Memory Vector Store Insert - via `ai_document` connection
2. Pinecone: Insert - via `ai_document` connection
3. Supabase: Insert - via `ai_document` connection
4. Zep Vector Store: Insert - via `ai_document` connection

### Special Requirements

This AI node requires the following special inputs:

- text Splitter (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Binary Input Loader",
  "type": "nodes-langchain.documentBinaryInputLoader",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "loader": "jsonLoader",
    "binaryDataKey": "data"
  }
}
```

---

## Calculator

## Basic Information

- Node Type: `nodes-langchain.toolCalculator`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Make it easier for AI agents to perform arithmetic

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Calculator",
  "type": "nodes-langchain.toolCalculator",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Call n8n Sub-Workflow Tool

## Basic Information

- Node Type: `nodes-langchain.toolWorkflow`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Uses another n8n workflow as a tool. Allows packaging any n8n node(s) as a tool.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workflowJson` | json | Yes | `"\n\n\n\n\n\n\n\n\n"` | The workflow JSON code to execute |
| `workflowId` | workflowSelector | Yes | `""` | - |
| `workflowInputs` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `source` | options | No | `"database"` | Where to get the workflow to execute from |
| `name` | string | No | `""` | The name of the function to be called, could contain letters, numbers, and underscores only |
| `notice` | notice | No | `""` | - |
| `noticeTemplateExample` | notice | No | `""` | - |
| `description` | string | No | `""` | - |
| `executeNotice` | notice | No | `""` | - |

#### Property Details

##### Source (`source`)

Where to get the workflow to execute from

Optional values:
- `database`: Database - Load the workflow from the database by ID
- `parameter`: Define Below - Pass the JSON code of a workflow

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Call n8n Sub-Workflow Tool",
  "type": "nodes-langchain.toolWorkflow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workflowJson": "\n\n\n\n\n\n\n\n\n",
    "workflowId": "",
    "workflowInputs": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

---

## Character Text Splitter

## Basic Information

- Node Type: `nodes-langchain.textSplitterCharacterTextSplitter`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Split text into chunks by characters

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `chunkSize` | number | No | `1000` | Maximum number of characters per chunk |
| `chunkOverlap` | number | No | `0` | Number of characters shared between consecutive chunks to preserve context |
| `notice` | notice | No | `""` | - |
| `separator` | string | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_textSplitter` (text Splitter)

### Can Connect To

1. Binary Input Loader - via `ai_textSplitter` connection
2. JSON Input Loader - via `ai_textSplitter` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Character Text Splitter",
  "type": "nodes-langchain.textSplitterCharacterTextSplitter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Chat Memory Manager

## Basic Information

- Node Type: `nodes-langchain.memoryManager`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Manage chat messages memory and use it in the workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `insertMode` | options | No | `"insert"` | Choose how new messages are inserted into the memory |
| `deleteMode` | options | No | `"lastN"` | How messages are deleted from memory |
| `messages` | fixedCollection | No | `{}` | Chat messages to insert into memory |
| `mode` | options | No | `"load"` | - |
| `options` | collection | No | `{}` | - |
| `lastMessagesCount` | number | No | `2` | The amount of last messages to delete |
| `simplifyOutput` | boolean | No | `true` | Whether to simplify the output to only include the sender and the text |

#### Property Details

##### Insert Mode (`insertMode`)

Choose how new messages are inserted into the memory

Optional values:
- `insert`: Insert Messages - Add messages alongside existing ones
- `override`: Override All Messages - Replace the current memory with new messages

##### Delete Mode (`deleteMode`)

How messages are deleted from memory

Optional values:
- `lastN`: Last N - Delete the last N messages
- `all`: All Messages - Clear all messages from memory

##### Chat Messages (`messages`)

Chat messages to insert into memory

Optional values:
- `undefined`: messageValues

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many Messages - Retrieve chat messages from connected memory
- `insert`: Insert Messages - Insert chat messages into connected memory
- `delete`: Delete Messages - Delete chat messages from connected memory

##### Options (`options`)

Optional values:
- `undefined`: groupMessages - Whether to group messages into a single item or return each message as a separate item

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_memory` (memory)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- memory (optional, multiple allowed)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Chat Memory Manager",
  "type": "nodes-langchain.memoryManager",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Chat Messages Retriever

## Basic Information

- Node Type: `nodes-langchain.memoryChatRetriever`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Retrieve chat messages from memory and use them in the workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `simplifyOutput` | boolean | No | `true` | Whether to simplify the output to only include the sender and the text |
| `deprecatedNotice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_memory` (memory)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- memory (optional, multiple allowed)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Chat Messages Retriever",
  "type": "nodes-langchain.memoryChatRetriever",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Code Tool

## Basic Information

- Node Type: `nodes-langchain.toolCode`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Write a tool in JS or Python

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `schemaType` | options | No | `"fromJson"` | How to specify the schema for the function |
| `language` | options | No | `"javaScript"` | - |
| `name` | string | No | `""` | The name of the function to be called, could contain letters, numbers, and underscores only |
| `jsCode` | string | No | `"// Example: convert the incoming query to uppercase and return it\nreturn query.toUpperCase()"` | E.g. Converts any text to uppercase |
| `pythonCode` | string | No | `"# Example: convert the incoming query to uppercase and return it\nreturn query.upper()"` | E.g. Converts any text to uppercase |
| `specifyInputSchema` | boolean | No | `false` | Whether to specify the schema for the function. This would require the LLM to provide the input in the correct format and would validate it against the schema. |
| `jsonSchemaExample` | json | No | `"{\n\t\"some_input\": \"some_value\"\n}"` | Example JSON object to use to generate the schema |
| `inputSchema` | json | No | `"{\n\"type\": \"object\",\n\"properties\": {\n\t\"some_input\": {\n\t\t\"type\": \"string\",\n\t\t\"description\": \"Some input to the function\"\n\t\t}\n\t}\n}"` | Schema to use for the function |
| `notice` | notice | No | `""` | - |
| `noticeTemplateExample` | notice | No | `""` | - |

#### Property Details

##### Schema Type (`schemaType`)

How to specify the schema for the function

Optional values:
- `fromJson`: Generate From JSON Example - Generate a schema from an example JSON object
- `manual`: Define using JSON Schema - Define the JSON schema manually

##### Language (`language`)

Optional values:
- `javaScript`: JavaScript
- `python`: Python (Beta)

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Code Tool",
  "type": "nodes-langchain.toolCode",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Cohere Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatCohere`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"command-a-03-2025"` | The model which will generate the completion. <a href="https://docs.cohere.com/docs/models">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: maxRetries - Maximum number of retries to attempt

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Cohere Chat Model",
  "type": "nodes-langchain.lmChatCohere",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Cohere Model

## Basic Information

- Node Type: `nodes-langchain.lmCohere`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model Cohere

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: model - The name of the model to use
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Cohere Model",
  "type": "nodes-langchain.lmCohere",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Contextual Compression Retriever

## Basic Information

- Node Type: `nodes-langchain.retrieverContextualCompression`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Enhances document similarity search by contextual compression.

### Connection Guide

### Connection Type

- Input Types: `ai_languageModel` (language Model), `ai_retriever` (retriever)
- Output Types: `ai_retriever` (retriever)

### Can Receive From

1. Anthropic Chat Model - via `ai_languageModel` connection
2. Azure OpenAI Chat Model - via `ai_languageModel` connection
3. AWS Bedrock Chat Model - via `ai_languageModel` connection
4. Cohere Chat Model - via `ai_languageModel` connection
5. DeepSeek Chat Model - via `ai_languageModel` connection
6. Google Gemini Chat Model - via `ai_languageModel` connection
7. Google Vertex Chat Model - via `ai_languageModel` connection
8. Groq Chat Model - via `ai_languageModel` connection
9. Mistral Cloud Chat Model - via `ai_languageModel` connection
10. Lemonade Chat Model - via `ai_languageModel` connection

### Can Connect To

1. Question and Answer Chain - via `ai_retriever` connection
2. MultiQuery Retriever - via `ai_retriever` connection

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
- retriever (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Contextual Compression Retriever",
  "type": "nodes-langchain.retrieverContextualCompression",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## DeepSeek Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatDeepSeek`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"deepseek-chat"` | The model which will generate the completion. <a href="https://api-docs.deepseek.com/quick\_start/pricing">Learn more</a>. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: responseFormat
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "DeepSeek Chat Model",
  "type": "nodes-langchain.lmChatDeepSeek",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Default Data Loader

## Basic Information

- Node Type: `nodes-langchain.documentDefaultDataLoader`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Load data from previous step in the workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dataType` | options | Yes | `"json"` | - |
| `jsonMode` | options | Yes | `"allInputData"` | - |
| `binaryMode` | options | Yes | `"allInputData"` | - |
| `loader` | options | Yes | `"auto"` | - |
| `textSplittingMode` | options | Yes | `"simple"` | - |
| `jsonData` | string | Yes | `""` | Drag and drop fields from the input pane, or use an expression |
| `binaryDataKey` | string | Yes | `"data"` | The name of the field in the agent or chain’s input that contains the binary file to be processed |
| `options` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Type of Data (`dataType`)

Optional values:
- `json`: JSON - Process JSON data from previous step in the workflow
- `binary`: Binary - Process binary data from previous step in the workflow

##### Mode (`jsonMode`)

Optional values:
- `allInputData`: Load All Input Data - Use all JSON data that flows into the parent agent or chain
- `expressionData`: Load Specific Data - Load a subset of data, and/or data from any previous step in the workflow

##### Mode (`binaryMode`)

Optional values:
- `allInputData`: Load All Input Data - Use all Binary data that flows into the parent agent or chain
- `specificField`: Load Specific Data - Load data from a specific field in the parent agent or chain

##### Data Format (`loader`)

Optional values:
- `auto`: Automatically Detect by Mime Type - Uses the mime type to detect the format
- `csvLoader`: CSV - Load CSV files
- `docxLoader`: Docx - Load Docx documents
- `epubLoader`: EPub - Load EPub files
- `jsonLoader`: JSON - Load JSON files
- `pdfLoader`: PDF - Load PDF documents
- `textLoader`: Text - Load plain text files

##### Text Splitting (`textSplittingMode`)

Optional values:
- `simple`: Simple - Splits every 1000 characters with a 200 character overlap
- `custom`: Custom - Connect a custom text-splitting sub-node

##### Options (`options`)

Optional values:
- `undefined`: pointers - Pointers to extract from JSON, e.g. "/text" or "/text, /meta/title"
- `undefined`: separator - Separator to use for CSV
- `undefined`: column - Column to extract from CSV
- `undefined`: splitPages - Whether to split PDF pages into separate documents
- `undefined`: metadata - Metadata to add to each document. Could be used for filtering during retrieval

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `ai_document` (document)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

### Can Connect To

1. In Memory Vector Store Insert - via `ai_document` connection
2. Pinecone: Insert - via `ai_document` connection
3. Supabase: Insert - via `ai_document` connection
4. Zep Vector Store: Insert - via `ai_document` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Default Data Loader",
  "type": "nodes-langchain.documentDefaultDataLoader",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataType": "json",
    "jsonMode": "allInputData",
    "binaryMode": "allInputData",
    "loader": "auto",
    "textSplittingMode": "simple",
    "jsonData": "",
    "binaryDataKey": "data"
  }
}
```

---

## Embeddings AWS Bedrock

## Basic Information

- Node Type: `nodes-langchain.embeddingsAwsBedrock`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Embeddings AWS Bedrock

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | No | `""` | The model which will generate the completion. <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html">Learn more</a>. |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings AWS Bedrock",
  "type": "nodes-langchain.embeddingsAwsBedrock",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Embeddings Azure OpenAI

## Basic Information

- Node Type: `nodes-langchain.embeddingsAzureOpenAi`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Embeddings Azure OpenAI

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | string | No | `""` | The name of the model(deployment) to use |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: batchSize - Maximum number of documents to send in each request
- `undefined`: stripNewLines - Whether to strip new lines from the input text
- `undefined`: timeout - Maximum amount of time a request is allowed to take in seconds. Set to -1 for no timeout.
- `undefined`: dimensions - The number of dimensions the resulting output embeddings should have. Only supported in text-embedding-3 and later models.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Azure OpenAI",
  "type": "nodes-langchain.embeddingsAzureOpenAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Embeddings Cohere

## Basic Information

- Node Type: `nodes-langchain.embeddingsCohere`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Cohere Embeddings

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `modelName` | options | No | `"embed-english-v2.0"` | The model which will generate the embeddings. <a href="https://docs.cohere.com/docs/models">Learn more</a>. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Model (`modelName`)

The model which will generate the embeddings. \<a href="https://docs.cohere.com/docs/models"\>Learn more\</a\>.

Optional values:
- `embed-english-light-v2.0`: Embed-English-Light-v2.0 (1024 Dimensions)
- `embed-english-light-v3.0`: Embed-English-Light-v3.0 (384 Dimensions)
- `embed-english-v2.0`: Embed-English-v2.0 (4096 Dimensions)
- `embed-english-v3.0`: Embed-English-v3.0 (1024 Dimensions)
- `embed-multilingual-light-v3.0`: Embed-Multilingual-Light-v3.0 (384 Dimensions)
- `embed-multilingual-v2.0`: Embed-Multilingual-v2.0 (768 Dimensions)
- `embed-multilingual-v3.0`: Embed-Multilingual-v3.0 (1024 Dimensions)

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Cohere",
  "type": "nodes-langchain.embeddingsCohere",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Embeddings Google Gemini

## Basic Information

- Node Type: `nodes-langchain.embeddingsGoogleGemini`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Google Gemini Embeddings

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `modelName` | options | No | `"models/text-embedding-004"` | The model which will generate the embeddings. <a href="https://developers.generativeai.google/api/rest/generativelanguage/models/list">Learn more</a>. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Google Gemini",
  "type": "nodes-langchain.embeddingsGoogleGemini",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Embeddings Google Vertex

## Basic Information

- Node Type: `nodes-langchain.embeddingsGoogleVertex`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Google Vertex Embeddings

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `projectId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select or enter your Google Cloud project ID |
| `modelName` | string | No | `"text-embedding-005"` | The model which will generate the embeddings. <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api">Learn more</a>. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Google Vertex",
  "type": "nodes-langchain.embeddingsGoogleVertex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Embeddings Hugging Face Inference

## Basic Information

- Node Type: `nodes-langchain.embeddingsHuggingFaceInference`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use HuggingFace Inference Embeddings

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `modelName` | string | No | `"sentence-transformers/distilbert-base-nli-mean-tokens"` | The model name to use from HuggingFace library |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: endpointUrl - Custom endpoint URL
- `undefined`: provider

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Hugging Face Inference",
  "type": "nodes-langchain.embeddingsHuggingFaceInference",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Embeddings Lemonade

## Basic Information

- Node Type: `nodes-langchain.embeddingsLemonade`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Lemonade Embeddings

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `""` | The model which will generate the completion. Models are loaded and managed through the Lemonade server. |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Lemonade",
  "type": "nodes-langchain.embeddingsLemonade",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": ""
  }
}
```

---

## Embeddings Mistral Cloud

## Basic Information

- Node Type: `nodes-langchain.embeddingsMistralCloud`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Embeddings Mistral Cloud

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"mistral-embed"` | The model which will compute the embeddings. <a href="https://docs.mistral.ai/platform/endpoints/">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: batchSize - Maximum number of documents to send in each request
- `undefined`: stripNewLines - Whether to strip new lines from the input text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Mistral Cloud",
  "type": "nodes-langchain.embeddingsMistralCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Embeddings Ollama

## Basic Information

- Node Type: `nodes-langchain.embeddingsOllama`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Ollama Embeddings

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `"llama3.2"` | The model which will generate the completion. To download models, visit <a href="https://ollama.ai/library">Ollama Models Library</a>. |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings Ollama",
  "type": "nodes-langchain.embeddingsOllama",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": "llama3.2"
  }
}
```

---

## Embeddings OpenAI

## Basic Information

- Node Type: `nodes-langchain.embeddingsOpenAi`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Embeddings OpenAI

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"text-embedding-ada-002"` | The model which will generate the embeddings. <a href="https://platform.openai.com/docs/models/overview">Learn more</a>. |
| `model` | options | No | `"text-embedding-3-small"` | The model which will generate the embeddings. <a href="https://platform.openai.com/docs/models/overview">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: dimensions - The number of dimensions the resulting output embeddings should have. Only supported in text-embedding-3 and later models.
- `undefined`: baseURL - Override the default base URL for the API
- `undefined`: batchSize - Maximum number of documents to send in each request
- `undefined`: stripNewLines - Whether to strip new lines from the input text
- `undefined`: timeout - Maximum amount of time a request is allowed to take in seconds. Set to -1 for no timeout.
- `undefined`: encodingFormat - The format to return the embeddings in

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_embedding` (embedding)

### Can Connect To

1. In Memory Vector Store Insert - via `ai_embedding` connection
2. In Memory Vector Store Load - via `ai_embedding` connection
3. Pinecone: Insert - via `ai_embedding` connection
4. Pinecone: Load - via `ai_embedding` connection
5. Supabase: Insert - via `ai_embedding` connection
6. Supabase: Load - via `ai_embedding` connection
7. Zep Vector Store: Insert - via `ai_embedding` connection
8. Zep Vector Store: Load - via `ai_embedding` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Embeddings OpenAI",
  "type": "nodes-langchain.embeddingsOpenAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## GitHub Document Loader

## Basic Information

- Node Type: `nodes-langchain.documentGithubLoader`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use GitHub data as input to this chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `textSplittingMode` | options | Yes | `"simple"` | - |
| `additionalOptions` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |
| `repository` | string | No | `""` | - |
| `branch` | string | No | `"main"` | - |

#### Property Details

##### Text Splitting (`textSplittingMode`)

Optional values:
- `simple`: Simple - Splits every 1000 characters with a 200 character overlap
- `custom`: Custom - Connect a custom text-splitting sub-node

##### Options (`additionalOptions`)

Optional values:
- `undefined`: recursive
- `undefined`: ignorePaths - Comma-separated list of paths to ignore, e.g. "docs, src/tests

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `ai_document` (document)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

### Can Connect To

1. In Memory Vector Store Insert - via `ai_document` connection
2. Pinecone: Insert - via `ai_document` connection
3. Supabase: Insert - via `ai_document` connection
4. Zep Vector Store: Insert - via `ai_document` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "GitHub Document Loader",
  "type": "nodes-langchain.documentGithubLoader",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "textSplittingMode": "simple"
  }
}
```

---

## Google Gemini

## Basic Information

- Node Type: `nodes-langchain.googleGemini`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Interact with Google Gemini AI models

### Available Operations

### Analyze Audio
Take in audio and answer questions about it
- Value: `analyze`

### Transcribe a Recording
Transcribes audio into the text
- Value: `transcribe`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `resource` | options | No | `"text"` | - |

#### Property Details

##### Resource (`resource`)

Optional values:
- `audio`: Audio
- `document`: Document
- `file`: File
- `image`: Image
- `text`: Text
- `video`: Video

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Google Gemini",
  "type": "nodes-langchain.googleGemini",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "modelId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Analyze Audio Example
```json
{
  "name": "Google Gemini",
  "type": "nodes-langchain.googleGemini",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "modelId": {
      "mode": "list",
      "value": ""
    },
    "operation": "analyze"
  }
}
```

#### Transcribe a Recording Example
```json
{
  "name": "Google Gemini",
  "type": "nodes-langchain.googleGemini",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "modelId": {
      "mode": "list",
      "value": ""
    },
    "operation": "transcribe"
  }
}
```

---

## Google Gemini Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatGoogleGemini`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Chat Model Google Gemini

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `modelName` | options | No | `"models/gemini-2.5-flash"` | The model which will generate the completion. <a href="https://developers.generativeai.google/api/rest/generativelanguage/models/list">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: maxOutputTokens - The maximum number of tokens to generate in the completion
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: topK - Used to remove "long tail" low probability responses. Defaults to -1, which disables it.
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.
- `undefined`: safetySettings

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Google Gemini Chat Model",
  "type": "nodes-langchain.lmChatGoogleGemini",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Google Vertex Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatGoogleVertex`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Chat Model Google Vertex

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `projectId` | resourceLocator | Yes | `{"mode":"list","value":""}` | Select or enter your Google Cloud project ID |
| `options` | collection | No | `{}` | Additional options to add |
| `modelName` | string | No | `"gemini-2.5-flash"` | The model which will generate the completion. <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: maxOutputTokens - The maximum number of tokens to generate in the completion
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: topK - Used to remove "long tail" low probability responses. Defaults to -1, which disables it.
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.
- `undefined`: safetySettings
- `undefined`: thinkingBudget - Controls reasoning tokens for thinking models. Set to 0 to disable automatic thinking. Set to -1 for dynamic thinking. Leave empty for auto mode.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Google Vertex Chat Model",
  "type": "nodes-langchain.lmChatGoogleVertex",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "projectId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Groq Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatGroq`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model Groq

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"llama3-8b-8192"` | The model which will generate the completion. <a href="https://console.groq.com/docs/models">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: maxTokensToSample - The maximum number of tokens to generate in the completion
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Groq Chat Model",
  "type": "nodes-langchain.lmChatGroq",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Hugging Face Inference Model

## Basic Information

- Node Type: `nodes-langchain.lmOpenHuggingFaceInference`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model HuggingFaceInference

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |
| `model` | string | No | `"mistralai/Mistral-Nemo-Base-2407"` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: endpointUrl - Custom endpoint URL
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: topK - Controls the top tokens to consider within the sample operation to create new text
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Hugging Face Inference Model",
  "type": "nodes-langchain.lmOpenHuggingFaceInference",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## In Memory Vector Store Insert

## Basic Information

- Node Type: `nodes-langchain.vectorStoreInMemoryInsert`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Insert data into an in-memory vector store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `clearStore` | boolean | No | `false` | Whether to clear the store before inserting new data |
| `memoryKey` | string | No | `"vector_store_key"` | The key to use to store the vector memory in the workflow data. The key will be prefixed with the workflow ID to avoid collisions. |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_document` (document), `ai_embedding` (embedding)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- document (optional)
- embedding (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "In Memory Vector Store Insert",
  "type": "nodes-langchain.vectorStoreInMemoryInsert",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## In Memory Vector Store Load

## Basic Information

- Node Type: `nodes-langchain.vectorStoreInMemoryLoad`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Load embedded data from an in-memory vector store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `memoryKey` | string | No | `"vector_store_key"` | The key to use to store the vector memory in the workflow data. The key will be prefixed with the workflow ID to avoid collisions. |

### Connection Guide

### Connection Type

- Input Types: `ai_embedding` (embedding)
- Output Types: `ai_vectorStore` (vector Store)

### Can Receive From

1. Embeddings Cohere - via `ai_embedding` connection
2. Embeddings AWS Bedrock - via `ai_embedding` connection
3. Embeddings Azure OpenAI - via `ai_embedding` connection
4. Embeddings Google Gemini - via `ai_embedding` connection
5. Embeddings Google Vertex - via `ai_embedding` connection
6. Embeddings Hugging Face Inference - via `ai_embedding` connection
7. Embeddings Mistral Cloud - via `ai_embedding` connection
8. Embeddings OpenAI - via `ai_embedding` connection
9. Embeddings Lemonade - via `ai_embedding` connection
10. Embeddings Ollama - via `ai_embedding` connection

### Can Connect To

1. Vector Store Retriever - via `ai_vectorStore` connection
2. Vector Store Question Answer Tool - via `ai_vectorStore` connection

### Special Requirements

This AI node requires the following special inputs:

- embedding (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "In Memory Vector Store Load",
  "type": "nodes-langchain.vectorStoreInMemoryLoad",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Information Extractor

## Basic Information

- Node Type: `nodes-langchain.informationExtractor`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Extract information from text in a structured format

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `schemaType` | options | No | `"fromAttributes"` | How to specify the schema for the desired output |
| `attributes` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `text` | string | No | `""` | The text to extract information from |
| `jsonSchemaExample` | json | No | `"{\n\t\"state\": \"California\",\n\t\"cities\": [\"Los Angeles\", \"San Francisco\", \"San Diego\"]\n}"` | Example JSON object to use to generate the schema |
| `inputSchema` | json | No | `"{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"state\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n\t\t\"cities\": {\n\t\t\t\"type\": \"array\",\n\t\t\t\"items\": {\n\t\t\t\t\"type\": \"string\"\n\t\t\t}\n\t\t}\n\t}\n}"` | Schema to use for the function |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Schema Type (`schemaType`)

How to specify the schema for the desired output

Optional values:
- `fromAttributes`: From Attribute Descriptions - Extract specific attributes from the text based on types and descriptions
- `fromJson`: Generate From JSON Example - Generate a schema from an example JSON object
- `manual`: Define using JSON Schema - Define the JSON schema manually

##### Attributes (`attributes`)

Optional values:
- `undefined`: attributes

##### Options (`options`)

Optional values:
- `undefined`: systemPromptTemplate - String to use directly as the system prompt template
- `undefined`: batching - Batch processing options for rate limiting

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_languageModel` (language Model)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Information Extractor",
  "type": "nodes-langchain.informationExtractor",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Item List Output Parser

## Basic Information

- Node Type: `nodes-langchain.outputParserItemList`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Return the results as separate items

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: numberOfItems - Defines how many items should be returned maximally. If set to -1, there is no limit.
- `undefined`: separator - Defines the separator that should be used to split the results into separate items. Defaults to a new line but can be changed depending on the data that should be returned.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_outputParser` (output Parser)

### Can Connect To

1. AI Agent - via `ai_outputParser` connection
2. Auto-fixing Output Parser - via `ai_outputParser` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Item List Output Parser",
  "type": "nodes-langchain.outputParserItemList",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## JSON Input Loader

## Basic Information

- Node Type: `nodes-langchain.documentJsonInputLoader`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Use JSON data from a previous step in the workflow

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `pointers` | string | No | `""` | Pointers to extract from JSON, e.g. "/text" or "/text, /meta/title" |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: metadata - Metadata to add to each document. Could be used for filtering during retrieval

### Connection Guide

### Connection Type

- Input Types: `ai_textSplitter` (text Splitter)
- Output Types: `ai_document` (document)

### Can Receive From

1. Character Text Splitter - via `ai_textSplitter` connection
2. Recursive Character Text Splitter - via `ai_textSplitter` connection
3. Token Splitter - via `ai_textSplitter` connection

### Can Connect To

1. In Memory Vector Store Insert - via `ai_document` connection
2. Pinecone: Insert - via `ai_document` connection
3. Supabase: Insert - via `ai_document` connection
4. Zep Vector Store: Insert - via `ai_document` connection

### Special Requirements

This AI node requires the following special inputs:

- text Splitter (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "JSON Input Loader",
  "type": "nodes-langchain.documentJsonInputLoader",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## LangChain Code

## Basic Information

- Node Type: `nodes-langchain.code`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

LangChain Code Node

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `inputs` | fixedCollection | No | `{}` | The input to add |
| `outputs` | fixedCollection | No | `{}` | The output to add |
| `code` | fixedCollection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Inputs (`inputs`)

The input to add

Optional values:
- `undefined`: input

##### Outputs (`outputs`)

The output to add

Optional values:
- `undefined`: output

##### Code (`code`)

Optional values:
- `undefined`: execute
- `undefined`: supplyData

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "LangChain Code",
  "type": "nodes-langchain.code",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Lemonade Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatLemonade`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model Lemonade Chat

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `""` | The model which will generate the completion. Models are loaded and managed through the Lemonade server. |
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: temperature - Controls the randomness of the generated text. Lower values make the output more focused and deterministic, while higher values make it more diverse and random.
- `undefined`: topP - Chooses from the smallest possible set of tokens whose cumulative probability exceeds the probability top\_p. Helps generate more human-like text by reducing repetitions.
- `undefined`: frequencyPenalty - Adjusts the penalty for tokens that have already appeared in the generated text. Positive values discourage repetition, negative values encourage it.
- `undefined`: presencePenalty - Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.
- `undefined`: maxTokens - The maximum number of tokens to generate. Set to -1 for no limit. Be cautious when setting this to a large value, as it can lead to very long outputs.
- `undefined`: stop - Comma-separated list of sequences where the model will stop generating text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Lemonade Chat Model",
  "type": "nodes-langchain.lmChatLemonade",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": ""
  }
}
```

---

## Lemonade Model

## Basic Information

- Node Type: `nodes-langchain.lmLemonade`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model Lemonade

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `""` | The model which will generate the completion. Models are loaded and managed through the Lemonade server. |
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: temperature - Controls the randomness of the generated text. Lower values make the output more focused and deterministic, while higher values make it more diverse and random.
- `undefined`: topP - Chooses from the smallest possible set of tokens whose cumulative probability exceeds the probability top\_p. Helps generate more human-like text by reducing repetitions.
- `undefined`: frequencyPenalty - Adjusts the penalty for tokens that have already appeared in the generated text. Positive values discourage repetition, negative values encourage it.
- `undefined`: presencePenalty - Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.
- `undefined`: maxTokens - The maximum number of tokens to generate. Set to -1 for no limit. Be cautious when setting this to a large value, as it can lead to very long outputs.
- `undefined`: stop - Comma-separated list of sequences where the model will stop generating text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Lemonade Model",
  "type": "nodes-langchain.lmLemonade",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": ""
  }
}
```

---

## Limit

## Basic Information

- Node Type: `nodes-base.limit`
- Category: transform
- Package: n8n-nodes-base

### Description

Restrict the number of items

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `keep` | options | No | `"firstItems"` | When removing items, whether to keep the ones at the start or the ending |
| `maxItems` | number | No | `1` | If there are more items than this number, some are removed |

#### Property Details

##### Keep (`keep`)

When removing items, whether to keep the ones at the start or the ending

Optional values:
- `firstItems`: First Items
- `lastItems`: Last Items

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Limit",
  "type": "nodes-base.limit",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## MCP Client

## Basic Information

- Node Type: `nodes-langchain.mcpClient`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Standalone MCP Client

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `endpointUrl` | string | Yes | `""` | The URL of the MCP server to connect to |
| `tool` | resourceLocator | Yes | `{"mode":"list","value":""}` | The tool to use |
| `parameters` | resourceMapper | Yes | `{"mappingMode":"defineBelow","value":null}` | - |
| `authentication` | options | No | `"none"` | The way to authenticate with your endpoint |
| `credentials` | credentials | No | `""` | - |
| `serverTransport` | options | No | `"httpStreamable"` | The transport used by your endpoint |
| `options` | collection | No | `{}` | Additional options to add |
| `inputMode` | options | No | `"manual"` | - |
| `jsonInput` | json | No | `"{\n  \"my_field_1\": \"value\",\n  \"my_field_2\": 1\n}\n"` | - |

#### Property Details

##### Authentication (`authentication`)

The way to authenticate with your endpoint

Optional values:
- `bearerAuth`: Bearer Auth
- `headerAuth`: Header Auth
- `mcpOAuth2Api`: MCP OAuth2
- `multipleHeadersAuth`: Multiple Headers Auth
- `none`: None

##### Server Transport (`serverTransport`)

The transport used by your endpoint

Optional values:
- `httpStreamable`: HTTP Streamable
- `sse`: Server Sent Events (Deprecated)

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: convertToBinary - Whether to convert images and audio to binary data. If false, images and audio will be returned as base64 encoded strings.
- `undefined`: timeout - Time in ms to wait for tool calls to finish

##### Input Mode (`inputMode`)

Optional values:
- `manual`: Manual - Manually specify the input data for each tool parameter
- `json`: JSON - Specify the input data as a JSON object

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "MCP Client",
  "type": "nodes-langchain.mcpClient",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "endpointUrl": "",
    "tool": {
      "mode": "list",
      "value": ""
    },
    "parameters": {
      "mappingMode": "defineBelow",
      "value": null
    }
  }
}
```

---

## Milvus Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStoreMilvus`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in Milvus Vector Store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `milvusCollection` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |
| `embeddingBatchSize` | number | No | `200` | Number of documents to embed in a single batch |
| `topK` | number | No | `4` | Number of top results to fetch from vector store |
| `includeDocumentMetadata` | boolean | No | `true` | Whether or not to include document metadata |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes

##### Options (`options`)

Optional values:
- `undefined`: clearCollection - Whether to clear the collection before inserting new data

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Milvus Vector Store",
  "type": "nodes-langchain.vectorStoreMilvus",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "prompt": "",
    "id": "",
    "milvusCollection": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Mistral Cloud Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatMistralCloud`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"mistral-small"` | The model which will generate the completion. <a href="https://docs.mistral.ai/platform/endpoints/">Learn more</a>. |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.
- `undefined`: safeMode - Whether to inject a safety prompt before all conversations
- `undefined`: randomSeed - The seed to use for random sampling. If set, different calls will generate deterministic results.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Mistral Cloud Chat Model",
  "type": "nodes-langchain.lmChatMistralCloud",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## MongoDB Atlas Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStoreMongoDBAtlas`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in MongoDB Atlas Vector Store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `embedding` | string | Yes | `"embedding"` | The field with the embedding array |
| `metadata_field` | string | Yes | `"text"` | The text field of the raw data |
| `vectorIndexName` | string | Yes | `""` | The name of the vector index |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `mongoCollection` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes
- `update`: Update Documents - Update documents in vector store by ID

##### Options (`options`)

Optional values:
- `undefined`: clearNamespace - Whether to clear documents in the namespace before inserting new data
- `undefined`: namespace - Logical partition for documents. Uses metadata.namespace field for filtering.

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "MongoDB Atlas Vector Store",
  "type": "nodes-langchain.vectorStoreMongoDBAtlas",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "embedding": "embedding",
    "metadata_field": "text",
    "vectorIndexName": "",
    "prompt": "",
    "id": "",
    "mongoCollection": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## MongoDB Chat Memory

## Basic Information

- Node Type: `nodes-langchain.memoryMongoDbChat`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Stores the chat history in MongoDB collection.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sessionIdType` | options | No | `"fromInput"` | - |
| `sessionKey` | string | No | `""` | The key to use to store session ID in the memory |
| `collectionName` | string | No | `"n8n_chat_histories"` | The collection name to store the chat history in. If collection does not exist, it will be created. |
| `databaseName` | string | No | `""` | The database name to store the chat history in. If not provided, the database from credentials will be used. |
| `notice` | notice | No | `""` | - |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | - |
| `contextWindowLength` | number | No | `5` | - |

#### Property Details

##### Session ID (`sessionIdType`)

Optional values:
- `fromInput`: Connected Chat Trigger Node - Looks for an input field called 'sessionId' that is coming from a directly connected Chat Trigger
- `customKey`: Define below - Use an expression to reference data in previous nodes or enter static text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_memory` (memory)

### Can Connect To

1. AI Agent - via `ai_memory` connection
2. Chat Memory Manager - via `ai_memory` connection
3. Chat Messages Retriever - via `ai_memory` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "MongoDB Chat Memory",
  "type": "nodes-langchain.memoryMongoDbChat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Motorhead

## Basic Information

- Node Type: `nodes-langchain.memoryMotorhead`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Motorhead Memory

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sessionId` | string | Yes | `""` | - |
| `sessionIdType` | options | No | `"fromInput"` | - |
| `sessionId` | string | No | `"={{ $json.sessionId }}"` | The key to use to store the memory |
| `sessionKey` | string | No | `""` | The key to use to store session ID in the memory |
| `notice` | notice | No | `""` | - |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | - |

#### Property Details

##### Session ID (`sessionIdType`)

Optional values:
- `fromInput`: Connected Chat Trigger Node - Looks for an input field called 'sessionId' that is coming from a directly connected Chat Trigger
- `customKey`: Define below - Use an expression to reference data in previous nodes or enter static text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_memory` (memory)

### Can Connect To

1. AI Agent - via `ai_memory` connection
2. Chat Memory Manager - via `ai_memory` connection
3. Chat Messages Retriever - via `ai_memory` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Motorhead",
  "type": "nodes-langchain.memoryMotorhead",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sessionId": ""
  }
}
```

---

## MultiQuery Retriever

## Basic Information

- Node Type: `nodes-langchain.retrieverMultiQuery`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Automates prompt tuning, generates diverse queries and expands document pool for enhanced retrieval.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: queryCount - Number of different versions of the given question to generate

### Connection Guide

### Connection Type

- Input Types: `ai_languageModel` (language Model), `ai_retriever` (retriever)
- Output Types: `ai_retriever` (retriever)

### Can Receive From

1. Anthropic Chat Model - via `ai_languageModel` connection
2. Azure OpenAI Chat Model - via `ai_languageModel` connection
3. AWS Bedrock Chat Model - via `ai_languageModel` connection
4. Cohere Chat Model - via `ai_languageModel` connection
5. DeepSeek Chat Model - via `ai_languageModel` connection
6. Google Gemini Chat Model - via `ai_languageModel` connection
7. Google Vertex Chat Model - via `ai_languageModel` connection
8. Groq Chat Model - via `ai_languageModel` connection
9. Mistral Cloud Chat Model - via `ai_languageModel` connection
10. Lemonade Chat Model - via `ai_languageModel` connection

### Can Connect To

1. Question and Answer Chain - via `ai_retriever` connection
2. Contextual Compression Retriever - via `ai_retriever` connection

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
- retriever (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "MultiQuery Retriever",
  "type": "nodes-langchain.retrieverMultiQuery",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Ollama

## Basic Information

- Node Type: `nodes-langchain.ollama`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Interact with Ollama AI models

### Available Operations

### Analyze Image
Take in images and answer questions about them
- Value: `analyze`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `resource` | options | No | `"text"` | - |
| `operation` | options | No | `"analyze"` | - |
| `operation` | options | No | `"message"` | - |
| `inputType` | options | No | `"binary"` | - |
| `options` | collection | No | `{}` | - |
| `messages` | fixedCollection | No | `{"values":[{"content":"","role":"user"}]}` | - |
| `options` | collection | No | `{}` | - |
| `binaryPropertyName` | string | No | `"data"` | Name of the binary field(s) which contains the image(s), separate multiple field names with commas |

#### Property Details

##### Resource (`resource`)

Optional values:
- `image`: Image
- `text`: Text

##### Operation (`operation`)

Optional values:
- `analyze`: Analyze Image - Take in images and answer questions about them

##### Operation (`operation`)

Optional values:
- `message`: Message a Model - Send a message to Ollama model

##### Input Type (`inputType`)

Optional values:
- `binary`: Binary File(s)
- `url`: Image URL(s)

##### Options (`options`)

Optional values:
- `undefined`: system - System message to set the context for the conversation
- `undefined`: temperature - Controls randomness in responses. Lower values make output more focused.
- `undefined`: top_p - The maximum cumulative probability of tokens to consider when sampling
- `undefined`: top_k - Controls diversity by limiting the number of top tokens to consider
- `undefined`: num_predict - Maximum number of tokens to generate in the completion
- `undefined`: frequency_penalty - Adjusts the penalty for tokens that have already appeared in the generated text. Higher values discourage repetition.
- `undefined`: presence_penalty - Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.
- `undefined`: repeat_penalty - Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient.
- `undefined`: num_ctx - Sets the size of the context window used to generate the next token
- `undefined`: repeat_last_n - Sets how far back for the model to look back to prevent repetition. (0 = disabled, -1 = num\_ctx).
- `undefined`: min_p - Alternative to the top\_p, and aims to ensure a balance of quality and variety. The parameter p represents the minimum probability for a token to be considered, relative to the probability of the most likely token.
- `undefined`: seed - Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt.
- `undefined`: stop - Sets the stop sequences to use. When this pattern is encountered the LLM will stop generating text and return. Separate multiple patterns with commas
- `undefined`: keep_alive - Specifies the duration to keep the loaded model in memory after use. Format: 1h30m (1 hour 30 minutes).
- `undefined`: low_vram - Whether to activate low VRAM mode, which reduces memory usage at the cost of slower generation speed. Useful for GPUs with limited memory.
- `undefined`: main_gpu - Specifies the ID of the GPU to use for the main computation. Only change this if you have multiple GPUs.
- `undefined`: num_batch - Sets the batch size for prompt processing. Larger batch sizes may improve generation speed but increase memory usage.
- `undefined`: num_gpu - Specifies the number of GPUs to use for parallel processing. Set to -1 for auto-detection.
- `undefined`: num_thread - Specifies the number of CPU threads to use for processing. Set to 0 for auto-detection.
- `undefined`: penalize_newline - Whether the model will be less likely to generate newline characters, encouraging longer continuous sequences of text
- `undefined`: use_mlock - Whether to lock the model in memory to prevent swapping. This can improve performance but requires sufficient available memory.
- `undefined`: use_mmap - Whether to use memory mapping for loading the model. This can reduce memory usage but may impact performance.
- `undefined`: vocab_only - Whether to only load the model vocabulary without the weights. Useful for quickly testing tokenization.
- `undefined`: format - Specifies the format of the API response

##### Messages (`messages`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: system - System message to set the context for the conversation
- `undefined`: temperature - Controls randomness in responses. Lower values make output more focused.
- `undefined`: top_p - The maximum cumulative probability of tokens to consider when sampling
- `undefined`: top_k - Controls diversity by limiting the number of top tokens to consider
- `undefined`: num_predict - Maximum number of tokens to generate in the completion
- `undefined`: frequency_penalty - Adjusts the penalty for tokens that have already appeared in the generated text. Higher values discourage repetition.
- `undefined`: presence_penalty - Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.
- `undefined`: repeat_penalty - Sets how strongly to penalize repetitions. A higher value (e.g., 1.5) will penalize repetitions more strongly, while a lower value (e.g., 0.9) will be more lenient.
- `undefined`: num_ctx - Sets the size of the context window used to generate the next token
- `undefined`: repeat_last_n - Sets how far back for the model to look back to prevent repetition. (0 = disabled, -1 = num\_ctx).
- `undefined`: min_p - Alternative to the top\_p, and aims to ensure a balance of quality and variety. The parameter p represents the minimum probability for a token to be considered, relative to the probability of the most likely token.
- `undefined`: seed - Sets the random number seed to use for generation. Setting this to a specific number will make the model generate the same text for the same prompt.
- `undefined`: stop - Sets the stop sequences to use. When this pattern is encountered the LLM will stop generating text and return. Separate multiple patterns with commas
- `undefined`: keep_alive - Specifies the duration to keep the loaded model in memory after use. Format: 1h30m (1 hour 30 minutes).
- `undefined`: low_vram - Whether to activate low VRAM mode, which reduces memory usage at the cost of slower generation speed. Useful for GPUs with limited memory.
- `undefined`: main_gpu - Specifies the ID of the GPU to use for the main computation. Only change this if you have multiple GPUs.
- `undefined`: num_batch - Sets the batch size for prompt processing. Larger batch sizes may improve generation speed but increase memory usage.
- `undefined`: num_gpu - Specifies the number of GPUs to use for parallel processing. Set to -1 for auto-detection.
- `undefined`: num_thread - Specifies the number of CPU threads to use for processing. Set to 0 for auto-detection.
- `undefined`: penalize_newline - Whether the model will be less likely to generate newline characters, encouraging longer continuous sequences of text
- `undefined`: use_mlock - Whether to lock the model in memory to prevent swapping. This can improve performance but requires sufficient available memory.
- `undefined`: use_mmap - Whether to use memory mapping for loading the model. This can reduce memory usage but may impact performance.
- `undefined`: vocab_only - Whether to only load the model vocabulary without the weights. Useful for quickly testing tokenization.
- `undefined`: format - Specifies the format of the API response

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Ollama",
  "type": "nodes-langchain.ollama",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "modelId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Analyze Image Example
```json
{
  "name": "Ollama",
  "type": "nodes-langchain.ollama",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "modelId": {
      "mode": "list",
      "value": ""
    },
    "operation": "analyze"
  }
}
```

---

## Ollama Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatOllama`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model Ollama

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `"llama3.2"` | The model which will generate the completion. To download models, visit <a href="https://ollama.ai/library">Ollama Models Library</a>. |
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: temperature - Controls the randomness of the generated text. Lower values make the output more focused and deterministic, while higher values make it more diverse and random.
- `undefined`: topK - Limits the number of highest probability vocabulary tokens to consider at each step. A higher value increases diversity but may reduce coherence. Set to -1 to disable.
- `undefined`: topP - Chooses from the smallest possible set of tokens whose cumulative probability exceeds the probability top\_p. Helps generate more human-like text by reducing repetitions.
- `undefined`: frequencyPenalty - Adjusts the penalty for tokens that have already appeared in the generated text. Higher values discourage repetition.
- `undefined`: keepAlive - Specifies the duration to keep the loaded model in memory after use. Useful for frequently used models. Format: 1h30m (1 hour 30 minutes).
- `undefined`: lowVram - Whether to Activate low VRAM mode, which reduces memory usage at the cost of slower generation speed. Useful for GPUs with limited memory.
- `undefined`: mainGpu - Specifies the ID of the GPU to use for the main computation. Only change this if you have multiple GPUs.
- `undefined`: numBatch - Sets the batch size for prompt processing. Larger batch sizes may improve generation speed but increase memory usage.
- `undefined`: numCtx - The maximum number of tokens to use as context for generating the next token. Smaller values reduce memory usage, while larger values provide more context to the model.
- `undefined`: numGpu - Specifies the number of GPUs to use for parallel processing. Set to -1 for auto-detection.
- `undefined`: numPredict - The maximum number of tokens to generate. Set to -1 for no limit. Be cautious when setting this to a large value, as it can lead to very long outputs.
- `undefined`: numThread - Specifies the number of CPU threads to use for processing. Set to 0 for auto-detection.
- `undefined`: penalizeNewline - Whether the model will be less likely to generate newline characters, encouraging longer continuous sequences of text
- `undefined`: presencePenalty - Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.
- `undefined`: repeatPenalty - Adjusts the penalty factor for repeated tokens. Higher values more strongly discourage repetition. Set to 1.0 to disable repetition penalty.
- `undefined`: useMLock - Whether to lock the model in memory to prevent swapping. This can improve performance but requires sufficient available memory.
- `undefined`: useMMap - Whether to use memory mapping for loading the model. This can reduce memory usage but may impact performance. Recommended to keep enabled.
- `undefined`: vocabOnly - Whether to only load the model vocabulary without the weights. Useful for quickly testing tokenization.
- `undefined`: format - Specifies the format of the API response

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Ollama Chat Model",
  "type": "nodes-langchain.lmChatOllama",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": "llama3.2"
  }
}
```

---

## Ollama Model

## Basic Information

- Node Type: `nodes-langchain.lmOllama`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Language Model Ollama

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `"llama3.2"` | The model which will generate the completion. To download models, visit <a href="https://ollama.ai/library">Ollama Models Library</a>. |
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: temperature - Controls the randomness of the generated text. Lower values make the output more focused and deterministic, while higher values make it more diverse and random.
- `undefined`: topK - Limits the number of highest probability vocabulary tokens to consider at each step. A higher value increases diversity but may reduce coherence. Set to -1 to disable.
- `undefined`: topP - Chooses from the smallest possible set of tokens whose cumulative probability exceeds the probability top\_p. Helps generate more human-like text by reducing repetitions.
- `undefined`: frequencyPenalty - Adjusts the penalty for tokens that have already appeared in the generated text. Higher values discourage repetition.
- `undefined`: keepAlive - Specifies the duration to keep the loaded model in memory after use. Useful for frequently used models. Format: 1h30m (1 hour 30 minutes).
- `undefined`: lowVram - Whether to Activate low VRAM mode, which reduces memory usage at the cost of slower generation speed. Useful for GPUs with limited memory.
- `undefined`: mainGpu - Specifies the ID of the GPU to use for the main computation. Only change this if you have multiple GPUs.
- `undefined`: numBatch - Sets the batch size for prompt processing. Larger batch sizes may improve generation speed but increase memory usage.
- `undefined`: numCtx - The maximum number of tokens to use as context for generating the next token. Smaller values reduce memory usage, while larger values provide more context to the model.
- `undefined`: numGpu - Specifies the number of GPUs to use for parallel processing. Set to -1 for auto-detection.
- `undefined`: numPredict - The maximum number of tokens to generate. Set to -1 for no limit. Be cautious when setting this to a large value, as it can lead to very long outputs.
- `undefined`: numThread - Specifies the number of CPU threads to use for processing. Set to 0 for auto-detection.
- `undefined`: penalizeNewline - Whether the model will be less likely to generate newline characters, encouraging longer continuous sequences of text
- `undefined`: presencePenalty - Adjusts the penalty for tokens based on their presence in the generated text so far. Positive values penalize tokens that have already appeared, encouraging diversity.
- `undefined`: repeatPenalty - Adjusts the penalty factor for repeated tokens. Higher values more strongly discourage repetition. Set to 1.0 to disable repetition penalty.
- `undefined`: useMLock - Whether to lock the model in memory to prevent swapping. This can improve performance but requires sufficient available memory.
- `undefined`: useMMap - Whether to use memory mapping for loading the model. This can reduce memory usage but may impact performance. Recommended to keep enabled.
- `undefined`: vocabOnly - Whether to only load the model vocabulary without the weights. Useful for quickly testing tokenization.
- `undefined`: format - Specifies the format of the API response

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Ollama Model",
  "type": "nodes-langchain.lmOllama",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": "llama3.2"
  }
}
```

---

## OpenAI

## Basic Information

- Node Type: `nodes-langchain.openAi`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Message an assistant or GPT, analyze images, generate audio, etc.

### Available Operations

### Generate Audio
Creates audio from a text prompt
- Value: `generate`

### Transcribe a Recording
Transcribes audio into text
- Value: `transcribe`

### Translate a Recording
Translates audio into text in English
- Value: `translate`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `prompt` | string | Yes | `""` | A text description of the desired image(s). Maximum 1000 characters for dall-e-2, 32000 characters for gpt-image-1. |
| `conversationId` | string | Yes | `""` | The ID of the conversation to delete |
| `conversationId` | string | Yes | `""` | The ID of the conversation to update |
| `metadata` | json | Yes | `"{}"` | Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard. Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters. |
| `conversationId` | string | Yes | `""` | The ID of the conversation to retrieve |
| `prompt` | string | Yes | `"A video of a cat playing with a ball"` | The prompt to generate a video from |
| `seconds` | number | Yes | `4` | Clip duration in seconds |
| `fileId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `modelId` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "OpenAI",
  "type": "nodes-langchain.openAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "prompt": "A video of a cat playing with a ball",
    "conversationId": "",
    "metadata": "{}",
    "seconds": 4,
    "fileId": {
      "mode": "list",
      "value": ""
    },
    "modelId": {
      "mode": "list",
      "value": ""
    }
  }
}
```

#### Generate Audio Example
```json
{
  "name": "OpenAI",
  "type": "nodes-langchain.openAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "prompt": "A video of a cat playing with a ball",
    "conversationId": "",
    "metadata": "{}",
    "seconds": 4,
    "fileId": {
      "mode": "list",
      "value": ""
    },
    "modelId": {
      "mode": "list",
      "value": ""
    },
    "operation": "generate"
  }
}
```

#### Transcribe a Recording Example
```json
{
  "name": "OpenAI",
  "type": "nodes-langchain.openAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "prompt": "A video of a cat playing with a ball",
    "conversationId": "",
    "metadata": "{}",
    "seconds": 4,
    "fileId": {
      "mode": "list",
      "value": ""
    },
    "modelId": {
      "mode": "list",
      "value": ""
    },
    "operation": "transcribe"
  }
}
```

---

## OpenAI Assistant

## Basic Information

- Node Type: `nodes-langchain.openAiAssistant`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Utilizes Assistant API from Open AI.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | options | Yes | `"gpt-3.5-turbo-1106"` | The model which will be used to power the assistant. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. The Retrieval tool requires gpt-3.5-turbo-1106 and gpt-4-1106-preview models. |
| `assistantId` | options | Yes | `""` | The assistant to use. <a href="https://beta.openai.com/docs/assistants/overview">Learn more</a>. |
| `name` | string | Yes | `""` | - |
| `text` | string | Yes | `"={{ $json.chat_input }}"` | - |
| `text` | string | Yes | `"={{ $json.chatInput }}"` | - |
| `options` | collection | No | `{}` | Additional options to add |
| `mode` | options | No | `"existing"` | - |
| `nativeTools` | multiOptions | No | `[]` | - |
| `instructions` | string | No | `""` | How the Assistant and model should behave or respond |
| `noticeTools` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: baseURL - Override the default base URL for the API
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds

##### Operation (`mode`)

Optional values:
- `new`: Use New Assistant
- `existing`: Use Existing Assistant

##### OpenAI Tools (`nativeTools`)

Optional values:
- `code_interpreter`: Code Interpreter
- `retrieval`: Knowledge Retrieval

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_tool` (tool)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- tool (optional, multiple allowed)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "OpenAI Assistant",
  "type": "nodes-langchain.openAiAssistant",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": "gpt-3.5-turbo-1106",
    "assistantId": "",
    "name": "",
    "text": "={{ $json.chatInput }}"
  }
}
```

---

## OpenAI Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatOpenAi`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | resourceLocator | Yes | `{"mode":"list","value":"gpt-4.1-mini"}` | The model. Choose from the list, or specify an ID. |
| `options` | collection | No | `{}` | Additional options to add |
| `builtInTools` | collection | No | `{}` | - |
| `model` | options | No | `"gpt-4o-mini"` | The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |
| `responsesApiEnabled` | boolean | No | `true` | Whether to use the Responses API to generate the response. <a href="https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/#use-responses-api">Learn more</a>. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: baseURL - Override the default base URL for the API
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: responseFormat
- `undefined`: responseFormat
- `undefined`: textFormat
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: reasoningEffort - Controls the amount of reasoning tokens to use. A value of "low" will favor speed and economical token usage, "high" will favor more complete reasoning at the cost of more tokens generated and slower responses.
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.
- `undefined`: conversationId - The conversation that this response belongs to. Input items and output items from this response are automatically added to this conversation after this response completes.
- `undefined`: promptCacheKey - Used by OpenAI to cache responses for similar requests to optimize your cache hit rates
- `undefined`: safetyIdentifier - A stable identifier used to help detect users of your application that may be violating OpenAI's usage policies. The IDs should be a string that uniquely identifies each user.
- `undefined`: serviceTier - The service tier to use for the request
- `undefined`: metadata - Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard. Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.
- `undefined`: topLogprobs - An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability
- `undefined`: promptConfig - Configure the reusable prompt template configured via OpenAI Dashboard. \<a href="https://platform.openai.com/docs/guides/prompt-engineering#reusable-prompts"\>Learn more\</a\>.

##### Built-in Tools (`builtInTools`)

Optional values:
- `undefined`: webSearch
- `undefined`: fileSearch
- `undefined`: codeInterpreter - Whether to allow the model to execute code in a sandboxed environment

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "OpenAI Chat Model",
  "type": "nodes-langchain.lmChatOpenAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": {
      "mode": "list",
      "value": "gpt-4.1-mini"
    }
  }
}
```

---

## OpenAI Model

## Basic Information

- Node Type: `nodes-langchain.lmOpenAi`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `model` | resourceLocator | Yes | `{"mode":"list","value":"gpt-3.5-turbo-instruct"}` | The model which will generate the completion. <a href="https://beta.openai.com/docs/models/overview">Learn more</a>. |
| `options` | collection | No | `{}` | Additional options to add |
| `deprecated` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: baseURL - Override the default base URL for the API
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "OpenAI Model",
  "type": "nodes-langchain.lmOpenAi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "model": {
      "mode": "list",
      "value": "gpt-3.5-turbo-instruct"
    }
  }
}
```

---

## OpenRouter Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatOpenRouter`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"openai/gpt-4.1-mini"` | The model which will generate the completion. <a href="https://openrouter.ai/docs/models">Learn more</a>. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: responseFormat
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "OpenRouter Chat Model",
  "type": "nodes-langchain.lmChatOpenRouter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Pinecone Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStorePinecone`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in Pinecone Vector Store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `pineconeIndex` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `embeddingBatchSize` | number | No | `200` | Number of documents to embed in a single batch |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes
- `update`: Update Documents - Update documents in vector store by ID

##### Options (`options`)

Optional values:
- `undefined`: clearNamespace - Whether to clear the namespace before inserting new data
- `undefined`: pineconeNamespace - Partition the records in an index into namespaces. Queries and other operations are then limited to one namespace, so different requests can search different subsets of your index.

##### Options (`options`)

Optional values:
- `undefined`: pineconeNamespace - Partition the records in an index into namespaces. Queries and other operations are then limited to one namespace, so different requests can search different subsets of your index.
- `undefined`: metadata - Metadata to filter the document by

##### Options (`options`)

Optional values:
- `undefined`: pineconeNamespace - Partition the records in an index into namespaces. Queries and other operations are then limited to one namespace, so different requests can search different subsets of your index.
- `undefined`: metadata - Metadata to filter the document by

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Pinecone Vector Store",
  "type": "nodes-langchain.vectorStorePinecone",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "prompt": "",
    "id": "",
    "pineconeIndex": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Pinecone: Insert

## Basic Information

- Node Type: `nodes-langchain.vectorStorePineconeInsert`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Insert data into Pinecone Vector Store index

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `pineconeIndex` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `clearNamespace` | boolean | No | `false` | Whether to clear the namespace before inserting new data |
| `pineconeNamespace` | string | No | `""` | - |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_document` (document), `ai_embedding` (embedding)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- document (optional)
- embedding (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Pinecone: Insert",
  "type": "nodes-langchain.vectorStorePineconeInsert",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "pineconeIndex": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Pinecone: Load

## Basic Information

- Node Type: `nodes-langchain.vectorStorePineconeLoad`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Load data from Pinecone Vector Store index

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `pineconeIndex` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `options` | collection | No | `{}` | - |
| `pineconeNamespace` | string | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: metadata - Metadata to filter the document by

### Connection Guide

### Connection Type

- Input Types: `ai_embedding` (embedding)
- Output Types: `ai_vectorStore` (vector Store)

### Can Receive From

1. Embeddings Cohere - via `ai_embedding` connection
2. Embeddings AWS Bedrock - via `ai_embedding` connection
3. Embeddings Azure OpenAI - via `ai_embedding` connection
4. Embeddings Google Gemini - via `ai_embedding` connection
5. Embeddings Google Vertex - via `ai_embedding` connection
6. Embeddings Hugging Face Inference - via `ai_embedding` connection
7. Embeddings Mistral Cloud - via `ai_embedding` connection
8. Embeddings OpenAI - via `ai_embedding` connection
9. Embeddings Lemonade - via `ai_embedding` connection
10. Embeddings Ollama - via `ai_embedding` connection

### Can Connect To

1. Vector Store Retriever - via `ai_vectorStore` connection
2. Vector Store Question Answer Tool - via `ai_vectorStore` connection

### Special Requirements

This AI node requires the following special inputs:

- embedding (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Pinecone: Load",
  "type": "nodes-langchain.vectorStorePineconeLoad",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "pineconeIndex": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Postgres Chat Memory

## Basic Information

- Node Type: `nodes-langchain.memoryPostgresChat`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Stores the chat history in Postgres table.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sessionIdType` | options | No | `"fromInput"` | - |
| `sessionKey` | string | No | `""` | The key to use to store session ID in the memory |
| `tableName` | string | No | `"n8n_chat_histories"` | The table name to store the chat history in. If table does not exist, it will be created. |
| `notice` | notice | No | `""` | - |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | - |
| `contextWindowLength` | number | No | `5` | - |

#### Property Details

##### Session ID (`sessionIdType`)

Optional values:
- `fromInput`: Connected Chat Trigger Node - Looks for an input field called 'sessionId' that is coming from a directly connected Chat Trigger
- `customKey`: Define below - Use an expression to reference data in previous nodes or enter static text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_memory` (memory)

### Can Connect To

1. AI Agent - via `ai_memory` connection
2. Chat Memory Manager - via `ai_memory` connection
3. Chat Messages Retriever - via `ai_memory` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Postgres Chat Memory",
  "type": "nodes-langchain.memoryPostgresChat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Postgres PGVector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStorePGVector`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in Postgresql with the PGVector extension

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `tableName` | string | No | `"n8n_vectors"` | The table name to store the vectors in. If table does not exist, it will be created. |
| `embeddingBatchSize` | number | No | `200` | Number of documents to embed in a single batch |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes

##### Options (`options`)

Optional values:
- `undefined`: collection - Collection of vectors
- `undefined`: columnNames - The names of the columns in the PGVector table

##### Options (`options`)

Optional values:
- `undefined`: distanceStrategy - The method to calculate the distance between two vectors
- `undefined`: collection - Collection of vectors
- `undefined`: columnNames - The names of the columns in the PGVector table
- `undefined`: metadata - Metadata to filter the document by

##### Options (`options`)

Optional values:
- `undefined`: distanceStrategy - The method to calculate the distance between two vectors
- `undefined`: collection - Collection of vectors
- `undefined`: columnNames - The names of the columns in the PGVector table
- `undefined`: metadata - Metadata to filter the document by

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Postgres PGVector Store",
  "type": "nodes-langchain.vectorStorePGVector",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "prompt": "",
    "id": ""
  }
}
```

---

## Qdrant Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStoreQdrant`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in a Qdrant collection

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `qdrantCollection` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `embeddingBatchSize` | number | No | `200` | Number of documents to embed in a single batch |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes

##### Options (`options`)

Optional values:
- `undefined`: collectionConfig - JSON options for creating a collection. \<a href="https://qdrant.tech/documentation/concepts/collections"\>Learn more\</a\>.
- `undefined`: contentPayloadKey - The key to use for the content payload in Qdrant. Default is "content".
- `undefined`: metadataPayloadKey - The key to use for the metadata payload in Qdrant. Default is "metadata".

##### Options (`options`)

Optional values:
- `undefined`: searchFilterJson - Filter pageContent or metadata using this \<a href="https://qdrant.tech/documentation/concepts/filtering/" target="\_blank"\>filtering syntax\</a\>
- `undefined`: contentPayloadKey - The key to use for the content payload in Qdrant. Default is "content".
- `undefined`: metadataPayloadKey - The key to use for the metadata payload in Qdrant. Default is "metadata".

##### Options (`options`)

Optional values:
- `undefined`: searchFilterJson - Filter pageContent or metadata using this \<a href="https://qdrant.tech/documentation/concepts/filtering/" target="\_blank"\>filtering syntax\</a\>
- `undefined`: contentPayloadKey - The key to use for the content payload in Qdrant. Default is "content".
- `undefined`: metadataPayloadKey - The key to use for the metadata payload in Qdrant. Default is "metadata".

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Qdrant Vector Store",
  "type": "nodes-langchain.vectorStoreQdrant",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "prompt": "",
    "id": "",
    "qdrantCollection": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Question and Answer Chain

## Basic Information

- Node Type: `nodes-langchain.chainRetrievalQa`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Answer questions about retrieved documents

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `"={{ $json.input }}"` | - |
| `query` | string | Yes | `"={{ $json.chat_input }}"` | - |
| `query` | string | Yes | `"={{ $json.chatInput }}"` | - |
| `text` | string | Yes | `"={{ $json.guardrailsInput }}"` | - |
| `text` | string | Yes | `"={{ $json.chatInput }}"` | - |
| `text` | string | Yes | `""` | - |
| `promptType` | options | No | `"auto"` | - |
| `options` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Source for Prompt (User Message) (`promptType`)

Optional values:
- `auto`: Connected Chat Trigger Node - Looks for an input field called 'chatInput' that is coming from a directly connected Chat Trigger
- `guardrails`: Connected Guardrails Node - Looks for an input field called 'guardrailsInput' that is coming from a directly connected Guardrails Node
- `define`: Define below - Use an expression to reference data in previous nodes or enter static text

##### Options (`options`)

Optional values:
- `undefined`: systemPromptTemplate - Template string used for the system prompt. This should include the variable \`{context}\` for the provided context. For text completion models, you should also include the variable \`{question}\` for the user’s query.
- `undefined`: systemPromptTemplate - Template string used for the system prompt. This should include the variable \`{context}\` for the provided context. For text completion models, you should also include the variable \`{input}\` for the user’s query.
- `undefined`: batching - Batch processing options for rate limiting

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_languageModel` (language Model), `ai_retriever` (retriever)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
- retriever (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Question and Answer Chain",
  "type": "nodes-langchain.chainRetrievalQa",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "={{ $json.chatInput }}",
    "text": ""
  }
}
```

---

## Recursive Character Text Splitter

## Basic Information

- Node Type: `nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Split text into chunks by characters recursively, recommended for most use cases

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `notice` | notice | No | `""` | - |
| `chunkSize` | number | No | `1000` | - |
| `chunkOverlap` | number | No | `0` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: splitCode

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_textSplitter` (text Splitter)

### Can Connect To

1. Binary Input Loader - via `ai_textSplitter` connection
2. JSON Input Loader - via `ai_textSplitter` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Recursive Character Text Splitter",
  "type": "nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Redis Chat Memory

## Basic Information

- Node Type: `nodes-langchain.memoryRedisChat`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Stores the chat history in Redis.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sessionIdType` | options | No | `"fromInput"` | - |
| `sessionKey` | string | No | `"chat_history"` | The key to use to store the memory in the workflow data |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | The key to use to store the memory |
| `sessionKey` | string | No | `""` | The key to use to store session ID in the memory |
| `sessionTTL` | number | No | `0` | For how long the session should be stored in seconds. If set to 0 it will not expire. |
| `notice` | notice | No | `""` | - |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | - |
| `contextWindowLength` | number | No | `5` | - |

#### Property Details

##### Session ID (`sessionIdType`)

Optional values:
- `fromInput`: Connected Chat Trigger Node - Looks for an input field called 'sessionId' that is coming from a directly connected Chat Trigger
- `customKey`: Define below - Use an expression to reference data in previous nodes or enter static text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_memory` (memory)

### Can Connect To

1. AI Agent - via `ai_memory` connection
2. Chat Memory Manager - via `ai_memory` connection
3. Chat Messages Retriever - via `ai_memory` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Redis Chat Memory",
  "type": "nodes-langchain.memoryRedisChat",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Redis Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStoreRedis`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in a Redis vector index

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `redisIndex` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `embeddingBatchSize` | number | No | `200` | Number of documents to embed in a single batch |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes
- `update`: Update Documents - Update documents in vector store by ID

##### Options (`options`)

Optional values:
- `undefined`: keyPrefix - Prefix for Redis keys storing the documents
- `undefined`: overwriteDocuments - Whether existing documents and the index should be overwritten
- `undefined`: metadataKey - The hash key to be used to store the metadata of the document
- `undefined`: contentKey - The hash key to be used to store the content of the document
- `undefined`: vectorKey - The hash key to be used to store the embedding of the document
- `undefined`: ttl - Time-to-live for the documents in seconds

##### Options (`options`)

Optional values:
- `undefined`: metadataFilter - The comma-separated list of words by which to apply additional full-text metadata filtering
- `undefined`: keyPrefix - Prefix for Redis keys storing the documents
- `undefined`: metadataKey - The hash key to be used to store the metadata of the document
- `undefined`: contentKey - The hash key to be used to store the content of the document
- `undefined`: vectorKey - The hash key to be used to store the embedding of the document

##### Options (`options`)

Optional values:
- `undefined`: metadataFilter - The comma-separated list of words by which to apply additional full-text metadata filtering
- `undefined`: keyPrefix - Prefix for Redis keys storing the documents
- `undefined`: metadataKey - The hash key to be used to store the metadata of the document
- `undefined`: contentKey - The hash key to be used to store the content of the document
- `undefined`: vectorKey - The hash key to be used to store the embedding of the document

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Redis Vector Store",
  "type": "nodes-langchain.vectorStoreRedis",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "prompt": "",
    "id": "",
    "redisIndex": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Remove Duplicates

## Basic Information

- Node Type: `nodes-base.removeDuplicates`
- Category: transform
- Package: n8n-nodes-base

### Description

Delete items with matching field values

### Available Operations

### Remove Items Repeated Within Current Input
Remove duplicates from incoming items
- Value: `removeDuplicateInputItems`

### Remove Items Processed in Previous Executions
Deduplicate items already seen in previous executions
- Value: `removeItemsSeenInPreviousExecutions`

### Clear Deduplication History
Wipe the store of previous items
- Value: `clearDeduplicationHistory`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dedupeValue` | string | Yes | `""` | Use an input field (or a combination of fields) that has a unique ID value |
| `operation` | options | No | `"removeDuplicateInputItems"` | - |
| `compare` | options | No | `"allFields"` | The fields of the input items to compare to see if they are the same |
| `logic` | options | No | `"removeItemsWithAlreadySeenKeyValues"` | How to select input items to remove by comparing them with key values previously processed |
| `mode` | options | No | `"cleanDatabase"` | How you want to modify the key values stored on the database. None of these modes removes input items. |
| `options` | collection | No | `{}` | - |
| `fieldsToExclude` | string | No | `""` | Fields in the input to exclude from the comparison |
| `fieldsToCompare` | string | No | `""` | Fields in the input to add to the comparison |
| `incrementalDedupeValue` | number | No | `""` | Use an input field (or a combination of fields) that has an incremental value |
| `dateDedupeValue` | dateTime | No | `""` | Use an input field that has a date value in ISO format |

#### Property Details

##### Operation (`operation`)

Optional values:
- `removeDuplicateInputItems`: Remove Items Repeated Within Current Input - Remove duplicates from incoming items
- `removeItemsSeenInPreviousExecutions`: Remove Items Processed in Previous Executions - Deduplicate items already seen in previous executions
- `clearDeduplicationHistory`: Clear Deduplication History - Wipe the store of previous items

##### Compare (`compare`)

The fields of the input items to compare to see if they are the same

Optional values:
- `allFields`: All Fields
- `allFieldsExcept`: All Fields Except
- `selectedFields`: Selected Fields

##### Keep Items Where (`logic`)

How to select input items to remove by comparing them with key values previously processed

Optional values:
- `removeItemsWithAlreadySeenKeyValues`: Value Is New - Remove all input items with values matching those already processed
- `removeItemsUpToStoredIncrementalKey`: Value Is Higher than Any Previous Value - Works with incremental values, removes all input items with values up to the stored value
- `removeItemsUpToStoredDate`: Value Is a Date Later than Any Previous Date - Works with date values, removes all input items with values up to the stored date

##### Mode (`mode`)

How you want to modify the key values stored on the database. None of these modes removes input items.

Optional values:
- `cleanDatabase`: Clean Database - Clear all values stored for a key in the database

##### Options (`options`)

Optional values:
- `undefined`: disableDotNotation - Whether to disallow referencing child fields using \`parent.child\` in the field name
- `undefined`: removeOtherFields - Whether to remove any fields that are not being compared. If disabled, will keep the values from the first of the duplicates.
- `undefined`: scope - If set to ‘workflow,’ key values will be shared across all nodes in the workflow. If set to ‘node,’ key values will be specific to this node.
- `undefined`: historySize

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Remove Duplicates",
  "type": "nodes-base.removeDuplicates",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dedupeValue": ""
  }
}
```

#### Remove Items Repeated Within Current Input Example
```json
{
  "name": "Remove Duplicates",
  "type": "nodes-base.removeDuplicates",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dedupeValue": "",
    "operation": "removeDuplicateInputItems"
  }
}
```

#### Remove Items Processed in Previous Executions Example
```json
{
  "name": "Remove Duplicates",
  "type": "nodes-base.removeDuplicates",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dedupeValue": "",
    "operation": "removeItemsSeenInPreviousExecutions"
  }
}
```

---

## Reranker Cohere

## Basic Information

- Node Type: `nodes-langchain.rerankerCohere`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Cohere Reranker to reorder documents after retrieval from a vector store by relevance to the given query.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `modelName` | options | No | `"rerank-v3.5"` | The model that should be used to rerank the documents. <a href="https://docs.cohere.com/docs/models">Learn more</a>. |
| `topN` | number | No | `3` | The maximum number of documents to return after reranking |

#### Property Details

##### Model (`modelName`)

The model that should be used to rerank the documents. \<a href="https://docs.cohere.com/docs/models"\>Learn more\</a\>.

Optional values:
- `rerank-v3.5`: rerank-v3.5
- `rerank-english-v3.0`: rerank-english-v3.0
- `rerank-multilingual-v3.0`: rerank-multilingual-v3.0

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_reranker` (reranker)

### Can Connect To

This node has no output, usually used as a workflow endpoint.
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Reranker Cohere",
  "type": "nodes-langchain.rerankerCohere",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## SearXNG

## Basic Information

- Node Type: `nodes-langchain.toolSearXng`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Search in SearXNG

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: numResults
- `undefined`: pageNumber
- `undefined`: language - Defines the language to use. It's a two-letter language code. (e.g., \`en\` for English, \`es\` for Spanish, or \`fr\` for French). Head to \<a href="https://docs.searxng.org/user/search-syntax.html#select-language"\>SearXNG search syntax page\</a\> for more info.
- `undefined`: safesearch - Filter search results of engines which support safe search

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "SearXNG",
  "type": "nodes-langchain.toolSearXng",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Sentiment Analysis

## Basic Information

- Node Type: `nodes-langchain.sentimentAnalysis`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Analyze the sentiment of your text

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `inputText` | string | Yes | `""` | Use an expression to reference data in previous nodes or enter static text |
| `options` | collection | No | `{}` | - |
| `detailedResultsNotice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: categories - A comma-separated list of categories to analyze
- `undefined`: systemPromptTemplate - String to use directly as the system prompt template
- `undefined`: includeDetailedResults - Whether to include sentiment strength and confidence scores in the output
- `undefined`: enableAutoFixing - Whether to enable auto-fixing (may trigger an additional LLM call if output is broken)
- `undefined`: batching - Batch processing options for rate limiting

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_languageModel` (language Model)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Sentiment Analysis",
  "type": "nodes-langchain.sentimentAnalysis",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "inputText": ""
  }
}
```

---

## SerpApi (Google Search)

## Basic Information

- Node Type: `nodes-langchain.toolSerpApi`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Search in Google using SerpAPI

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Optional values:
- `undefined`: gl - Defines the country to use for search. Head to \<a href="https://serpapi.com/google-countries"\>Google countries page\</a\> for a full list of supported countries.
- `undefined`: device - Device to use to get the results
- `undefined`: no_cache - Whether to force SerpApi to fetch the Google results even if a cached version is already present. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month.
- `undefined`: google_domain - Defines the domain to use for search. Head to \<a href="https://serpapi.com/google-domains"\>Google domains page\</a\> for a full list of supported domains.
- `undefined`: hl - Defines the language to use. It's a two-letter language code. (e.g., \`en\` for English, \`es\` for Spanish, or \`fr\` for French). Head to \<a href="https://serpapi.com/google-languages"\>Google languages page\</a\> for a full list of supported languages.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "SerpApi (Google Search)",
  "type": "nodes-langchain.toolSerpApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Simple Memory

## Basic Information

- Node Type: `nodes-langchain.memoryBufferWindow`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Stores in n8n memory, so no credentials required

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sessionIdType` | options | No | `"fromInput"` | - |
| `sessionKey` | string | No | `"chat_history"` | The key to use to store the memory in the workflow data |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | The key to use to store the memory |
| `sessionKey` | string | No | `""` | The key to use to store session ID in the memory |
| `notice` | notice | No | `""` | - |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | - |
| `contextWindowLength` | number | No | `5` | - |

#### Property Details

##### Session ID (`sessionIdType`)

Optional values:
- `fromInput`: Connected Chat Trigger Node - Looks for an input field called 'sessionId' that is coming from a directly connected Chat Trigger
- `customKey`: Define below - Use an expression to reference data in previous nodes or enter static text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_memory` (memory)

### Can Connect To

1. AI Agent - via `ai_memory` connection
2. Chat Memory Manager - via `ai_memory` connection
3. Chat Messages Retriever - via `ai_memory` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Simple Memory",
  "type": "nodes-langchain.memoryBufferWindow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Simple Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStoreInMemory`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

The easiest way to experiment with vector stores, without external setup.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `memoryKey` | resourceLocator | Yes | `{"mode":"list","value":"vector_store_key"}` | The key to use to store the vector memory in the workflow data. These keys are shared between workflows. |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `mode` | options | No | `"retrieve"` | - |
| `memoryKey` | string | No | `"vector_store_key"` | The key to use to store the vector memory in the workflow data. The key will be prefixed with the workflow ID to avoid collisions. |
| `embeddingBatchSize` | number | No | `200` | Number of documents to embed in a single batch |
| `clearStore` | boolean | No | `false` | Whether to clear the store before inserting new data |
| `topK` | number | No | `4` | Number of top results to fetch from vector store |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Simple Vector Store",
  "type": "nodes-langchain.vectorStoreInMemory",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "memoryKey": {
      "mode": "list",
      "value": "vector_store_key"
    },
    "prompt": "",
    "id": ""
  }
}
```

---

## Sort

## Basic Information

- Node Type: `nodes-base.sort`
- Category: transform
- Package: n8n-nodes-base

### Description

Change items order

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `type` | options | No | `"simple"` | The type of sorting to perform |
| `sortFieldsUi` | fixedCollection | No | `{}` | The fields of the input items to sort by |
| `options` | collection | No | `{}` | - |
| `code` | string | No | `"// The two items to compare are in the variables a and b\n\t// Access the fields in a.json and b.json\n\t// Return -1 if a should go before b\n\t// Return 1 if b should go before a\n\t// Return 0 if there's no difference\n\n\tfieldName = 'myField';\n\n\tif (a.json[fieldName] < b.json[fieldName]) {\n\treturn -1;\n\t}\n\tif (a.json[fieldName] > b.json[fieldName]) {\n\treturn 1;\n\t}\n\treturn 0;"` | Javascript code to determine the order of any two items |

#### Property Details

##### Type (`type`)

The type of sorting to perform

Optional values:
- `simple`: Simple
- `random`: Random
- `code`: Code

##### Fields To Sort By (`sortFieldsUi`)

The fields of the input items to sort by

Optional values:
- `undefined`: sortField

##### Options (`options`)

Optional values:
- `undefined`: disableDotNotation - Whether to disallow referencing child fields using \`parent.child\` in the field name

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Sort",
  "type": "nodes-base.sort",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Split Out

## Basic Information

- Node Type: `nodes-base.splitOut`
- Category: transform
- Package: n8n-nodes-base

### Description

Turn a list inside item(s) into separate items

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fieldToSplitOut` | string | Yes | `""` | The name of the input fields to break out into separate items. Separate multiple field names by commas. For binary data, use $binary. |
| `include` | options | No | `"noOtherFields"` | Whether to copy any other fields into the new items |
| `options` | collection | No | `{}` | - |
| `fieldsToInclude` | string | No | `""` | Fields in the input items to aggregate together |

#### Property Details

##### Include (`include`)

Whether to copy any other fields into the new items

Optional values:
- `noOtherFields`: No Other Fields
- `allOtherFields`: All Other Fields
- `selectedOtherFields`: Selected Other Fields

##### Options (`options`)

Optional values:
- `undefined`: disableDotNotation - Whether to disallow referencing child fields using \`parent.child\` in the field name
- `undefined`: destinationFieldName - The field in the output under which to put the split field contents
- `undefined`: includeBinary - Whether to include the binary data in the new items

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Split Out",
  "type": "nodes-base.splitOut",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "fieldToSplitOut": ""
  }
}
```

---

## Structured Output Parser

## Basic Information

- Node Type: `nodes-langchain.outputParserStructured`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Return data in a defined JSON format

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `jsonSchema` | json | Yes | `"{\n  \"type\": \"object\",\n  \"properties\": {\n    \"state\": {\n      \"type\": \"string\"\n    },\n    \"cities\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  }\n}"` | JSON Schema to structure and validate the output against |
| `schemaType` | options | No | `"fromJson"` | How to specify the schema for the function |
| `jsonSchemaExample` | json | No | `"{\n\t\"state\": \"California\",\n\t\"cities\": [\"Los Angeles\", \"San Francisco\", \"San Diego\"]\n}"` | Example JSON object to use to generate the schema |
| `inputSchema` | json | No | `"{\n\t\"type\": \"object\",\n\t\"properties\": {\n\t\t\"state\": {\n\t\t\t\"type\": \"string\"\n\t\t},\n\t\t\"cities\": {\n\t\t\t\"type\": \"array\",\n\t\t\t\"items\": {\n\t\t\t\t\"type\": \"string\"\n\t\t\t}\n\t\t}\n\t}\n}"` | Schema to use for the function |
| `autoFix` | boolean | No | `false` | Whether to automatically fix the output when it is not in the correct format. Will cause another LLM call. |
| `customizeRetryPrompt` | boolean | No | `false` | Whether to customize the prompt used for retrying the output parsing. If disabled, a default prompt will be used. |
| `prompt` | string | No | `"Instructions:\n--------------\n{instructions}\n--------------\nCompletion:\n--------------\n{completion}\n--------------\n\nAbove, the Completion did not satisfy the constraints given in the Instructions.\nError:\n--------------\n{error}\n--------------\n\nPlease try again. Please only respond with an answer that satisfies the constraints laid out in the Instructions:"` | Prompt template used for fixing the output. Uses placeholders: "{instructions}" for parsing rules, "{completion}" for the failed attempt, and "{error}" for the validation error message. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Schema Type (`schemaType`)

How to specify the schema for the function

Optional values:
- `fromJson`: Generate From JSON Example - Generate a schema from an example JSON object
- `manual`: Define using JSON Schema - Define the JSON schema manually

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `ai_outputParser` (output Parser)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

### Can Connect To

1. AI Agent - via `ai_outputParser` connection
2. Auto-fixing Output Parser - via `ai_outputParser` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Structured Output Parser",
  "type": "nodes-langchain.outputParserStructured",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "jsonSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"state\": {\n      \"type\": \"string\"\n    },\n    \"cities\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  }\n}"
  }
}
```

---

## Summarization Chain

## Basic Information

- Node Type: `nodes-langchain.chainSummarization`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Transforms text into a concise summary

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `operationMode` | options | No | `"nodeInputJson"` | How to pass data into the summarization chain |
| `chunkingMode` | options | No | `"simple"` | Chunk splitting strategy |
| `options` | collection | No | `{}` | - |
| `chunkSize` | number | No | `1000` | Controls the max size (in terms of number of characters) of the final document chunk |
| `chunkOverlap` | number | No | `200` | Specifies how much characters overlap there should be between chunks |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Data to Summarize (`operationMode`)

How to pass data into the summarization chain

Optional values:
- `nodeInputJson`: Use Node Input (JSON) - Summarize the JSON data coming into this node from the previous one
- `nodeInputBinary`: Use Node Input (Binary) - Summarize the binary data coming into this node from the previous one
- `documentLoader`: Use Document Loader - Use a loader sub-node with more configuration options

##### Chunking Strategy (`chunkingMode`)

Chunk splitting strategy

Optional values:
- `simple`: Simple (Define Below)
- `advanced`: Advanced - Use a splitter sub-node with more configuration options

##### Options (`options`)

Optional values:
- `undefined`: binaryDataKey - The name of the field in the agent or chain’s input that contains the binary file to be processed
- `undefined`: summarizationMethodAndPrompts
- `undefined`: batching - Batch processing options for rate limiting

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Summarization Chain",
  "type": "nodes-langchain.chainSummarization",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Summarize

## Basic Information

- Node Type: `nodes-base.summarize`
- Category: transform
- Package: n8n-nodes-base

### Description

Sum, count, max, etc. across items

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fieldsToSummarize` | fixedCollection | No | `{"values":[{"aggregation":"count","field":""}]}` | - |
| `options` | collection | No | `{}` | - |
| `fieldsToSplitBy` | string | No | `""` | The name of the input fields that you want to split the summary by |
| `fieldsToSplitBy` | string | No | `""` | The name of the input fields that you want to split the summary by |

#### Property Details

##### Fields to Summarize (`fieldsToSummarize`)

Optional values:
- `undefined`: values

##### Options (`options`)

Optional values:
- `undefined`: continueIfFieldNotFound - Whether to continue if field to summarize can't be found in any items and return single empty item, otherwise an error would be thrown
- `undefined`: disableDotNotation - Whether to disallow referencing child fields using \`parent.child\` in the field name
- `undefined`: outputFormat
- `undefined`: skipEmptySplitFields

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Summarize",
  "type": "nodes-base.summarize",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Supabase Vector Store

## Basic Information

- Node Type: `nodes-langchain.vectorStoreSupabase`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Work with your data in Supabase Vector Store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `toolName` | string | Yes | `""` | Name of the vector store |
| `toolDescription` | string | Yes | `""` | Explain to the LLM what this tool does, a good, specific description would allow LLMs to produce expected results much more often |
| `prompt` | string | Yes | `""` | Search prompt to retrieve matching documents from the vector store using similarity-based ranking |
| `id` | string | Yes | `""` | ID of an embedding entry |
| `tableName` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `mode` | options | No | `"retrieve"` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Operation Mode (`mode`)

Optional values:
- `load`: Get Many - Get many ranked documents from vector store for query
- `insert`: Insert Documents - Insert documents into vector store
- `retrieve`: Retrieve Documents (As Vector Store for Chain/Tool) - Retrieve documents from vector store to be used as vector store with AI nodes
- `retrieve-as-tool`: Retrieve Documents (As Tool for AI Agent) - Retrieve documents from vector store to be used as tool with AI nodes
- `update`: Update Documents - Update documents in vector store by ID

##### Options (`options`)

Optional values:
- `undefined`: queryName - Name of the query to use for matching documents

##### Options (`options`)

Optional values:
- `undefined`: queryName - Name of the query to use for matching documents
- `undefined`: metadata - Metadata to filter the document by

##### Options (`options`)

Optional values:
- `undefined`: queryName - Name of the query to use for matching documents
- `undefined`: metadata - Metadata to filter the document by

##### Options (`options`)

Optional values:
- `undefined`: queryName - Name of the query to use for matching documents

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Supabase Vector Store",
  "type": "nodes-langchain.vectorStoreSupabase",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "toolName": "",
    "toolDescription": "",
    "prompt": "",
    "id": "",
    "tableName": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Supabase: Insert

## Basic Information

- Node Type: `nodes-langchain.vectorStoreSupabaseInsert`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Insert data into Supabase Vector Store index \[https://supabase.com/docs/guides/ai/langchain\]

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `queryName` | string | Yes | `"match_documents"` | Name of the query to use for matching documents |
| `tableName` | resourceLocator | Yes | `{"mode":"list","value":""}` | - |
| `setupNotice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_document` (document), `ai_embedding` (embedding)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- document (optional)
- embedding (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Supabase: Insert",
  "type": "nodes-langchain.vectorStoreSupabaseInsert",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "queryName": "match_documents",
    "tableName": {
      "mode": "list",
      "value": ""
    }
  }
}
```

---

## Text Classifier

## Basic Information

- Node Type: `nodes-langchain.textClassifier`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Classify your text into distinct categories

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `inputText` | string | Yes | `""` | Use an expression to reference data in previous nodes or enter static text |
| `categories` | fixedCollection | No | `{}` | - |
| `options` | collection | No | `{}` | - |

#### Property Details

##### Categories (`categories`)

Optional values:
- `undefined`: categories

##### Options (`options`)

Optional values:
- `undefined`: multiClass
- `undefined`: fallback - What to do with items that don’t match the categories exactly
- `undefined`: systemPromptTemplate - String to use directly as the system prompt template
- `undefined`: enableAutoFixing - Whether to enable auto-fixing (may trigger an additional LLM call if output is broken)
- `undefined`: batching - Batch processing options for rate limiting

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow), `ai_languageModel` (language Model)
- Output Types: `main` (general data flow)
- Output Count: 0 (configurable)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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

### Special Requirements

This AI node requires the following special inputs:

- language Model (required)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Text Classifier",
  "type": "nodes-langchain.textClassifier",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "inputText": ""
  }
}
```

---

## Think Tool

## Basic Information

- Node Type: `nodes-langchain.toolThink`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Invite the AI agent to do some thinking

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `description` | string | Yes | `"Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed."` | The thinking tool's description |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Think Tool",
  "type": "nodes-langchain.toolThink",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "description": "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed."
  }
}
```

---

## Token Splitter

## Basic Information

- Node Type: `nodes-langchain.textSplitterTokenSplitter`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Split text into chunks by tokens

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `chunkSize` | number | No | `1000` | Maximum number of tokens per chunk |
| `chunkOverlap` | number | No | `0` | Number of tokens shared between consecutive chunks to preserve context |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_textSplitter` (text Splitter)

### Can Connect To

1. Binary Input Loader - via `ai_textSplitter` connection
2. JSON Input Loader - via `ai_textSplitter` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Token Splitter",
  "type": "nodes-langchain.textSplitterTokenSplitter",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Vector Store Question Answer Tool

## Basic Information

- Node Type: `nodes-langchain.toolVectorStore`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Answer questions with a vector store

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `name` | string | No | `""` | Name of the data in vector store. This will be used to fill this tool description: Useful for when you need to answer questions about [name]. Whenever you need information about [data description], you should ALWAYS use this. Input should be a fully formed question. |
| `description` | string | No | `""` | Describe the data in vector store. This will be used to fill this tool description: Useful for when you need to answer questions about [name]. Whenever you need information about [data description], you should ALWAYS use this. Input should be a fully formed question. |
| `topK` | number | No | `4` | The maximum number of results to return |
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: `ai_vectorStore` (vector Store), `ai_languageModel` (language Model)
- Output Types: `ai_tool` (tool)

### Can Receive From

1. Anthropic Chat Model - via `ai_languageModel` connection
2. Azure OpenAI Chat Model - via `ai_languageModel` connection
3. AWS Bedrock Chat Model - via `ai_languageModel` connection
4. Cohere Chat Model - via `ai_languageModel` connection
5. DeepSeek Chat Model - via `ai_languageModel` connection
6. Google Gemini Chat Model - via `ai_languageModel` connection
7. Google Vertex Chat Model - via `ai_languageModel` connection
8. Groq Chat Model - via `ai_languageModel` connection
9. Mistral Cloud Chat Model - via `ai_languageModel` connection
10. Lemonade Chat Model - via `ai_languageModel` connection

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection

### Special Requirements

This AI node requires the following special inputs:

- vector Store (optional)
- language Model (required)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Vector Store Question Answer Tool",
  "type": "nodes-langchain.toolVectorStore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Vector Store Retriever

## Basic Information

- Node Type: `nodes-langchain.retrieverVectorStore`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Use a Vector Store as Retriever

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `topK` | number | No | `4` | The maximum number of results to return |

### Connection Guide

### Connection Type

- Input Types: `ai_vectorStore` (vector Store)
- Output Types: `ai_retriever` (retriever)

### Can Receive From

1. In Memory Vector Store Load - via `ai_vectorStore` connection
2. Pinecone: Load - via `ai_vectorStore` connection
3. Supabase: Load - via `ai_vectorStore` connection
4. Zep Vector Store: Load - via `ai_vectorStore` connection

### Can Connect To

1. Question and Answer Chain - via `ai_retriever` connection
2. Contextual Compression Retriever - via `ai_retriever` connection
3. MultiQuery Retriever - via `ai_retriever` connection

### Special Requirements

This AI node requires the following special inputs:

- vector Store (optional)
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Vector Store Retriever",
  "type": "nodes-langchain.retrieverVectorStore",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Vercel AI Gateway Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatVercelAiGateway`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain via Vercel AI Gateway

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"openai/gpt-4o"` | The model which will generate the completion |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: responseFormat
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Vercel AI Gateway Chat Model",
  "type": "nodes-langchain.lmChatVercelAiGateway",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Wikipedia

## Basic Information

- Node Type: `nodes-langchain.toolWikipedia`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Search in Wikipedia

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Wikipedia",
  "type": "nodes-langchain.toolWikipedia",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Wolfram|Alpha

## Basic Information

- Node Type: `nodes-langchain.toolWolframAlpha`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Connects to WolframAlpha's computational intelligence engine.

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `notice` | notice | No | `""` | - |

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_tool` (tool)

### Can Connect To

1. AI Agent - via `ai_tool` connection
2. OpenAI Assistant - via `ai_tool` connection
3. MCP Server Trigger - via `ai_tool` connection
4. Tool Executor - via `ai_tool` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Wolfram|Alpha",
  "type": "nodes-langchain.toolWolframAlpha",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Workflow Retriever

## Basic Information

- Node Type: `nodes-langchain.retrieverWorkflow`
- Category: transform
- Package: @n8n/n8n-nodes-langchain

### Description

Use an n8n Workflow as Retriever

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `workflowId` | string | Yes | `""` | The workflow to execute |
| `workflowJson` | json | Yes | `"\n\n\n"` | The workflow JSON code to execute |
| `workflowId` | workflowSelector | Yes | `""` | - |
| `source` | options | No | `"database"` | Where to get the workflow to execute from |
| `fields` | fixedCollection | No | `{}` | Set the values which should be made available in the workflow |
| `executeNotice` | notice | No | `""` | - |

#### Property Details

##### Source (`source`)

Where to get the workflow to execute from

Optional values:
- `database`: Database - Load the workflow from the database by ID
- `parameter`: Parameter - Load the workflow from a parameter

##### Workflow Values (`fields`)

Set the values which should be made available in the workflow

Optional values:
- `undefined`: values

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_retriever` (retriever)

### Can Connect To

1. Question and Answer Chain - via `ai_retriever` connection
2. Contextual Compression Retriever - via `ai_retriever` connection
3. MultiQuery Retriever - via `ai_retriever` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Workflow Retriever",
  "type": "nodes-langchain.retrieverWorkflow",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "workflowId": "",
    "workflowJson": "\n\n\n"
  }
}
```

---

## xAI Grok Chat Model

## Basic Information

- Node Type: `nodes-langchain.lmChatXAiGrok`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

For advanced usage with an AI chain

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `options` | collection | No | `{}` | Additional options to add |
| `model` | options | No | `"grok-2-vision-1212"` | The model which will generate the completion. <a href="https://docs.x.ai/docs/models">Learn more</a>. |
| `notice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |

#### Property Details

##### Options (`options`)

Additional options to add

Optional values:
- `undefined`: frequencyPenalty - Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim
- `undefined`: maxTokens - The maximum number of tokens to generate in the completion. Most models have a context length of 2048 tokens (except for the newest models, which support 32,768).
- `undefined`: responseFormat
- `undefined`: presencePenalty - Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics
- `undefined`: temperature - Controls randomness: Lowering results in less random completions. As the temperature approaches zero, the model will become deterministic and repetitive.
- `undefined`: timeout - Maximum amount of time a request is allowed to take in milliseconds
- `undefined`: maxRetries - Maximum number of retries to attempt
- `undefined`: topP - Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered. We generally recommend altering this or temperature but not both.

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_languageModel` (language Model)

### Can Connect To

1. AI Agent - via `ai_languageModel` connection
2. Question and Answer Chain - via `ai_languageModel` connection
3. Sentiment Analysis - via `ai_languageModel` connection
4. Information Extractor - via `ai_languageModel` connection
5. Text Classifier - via `ai_languageModel` connection
6. Auto-fixing Output Parser - via `ai_languageModel` connection
7. Contextual Compression Retriever - via `ai_languageModel` connection
8. MultiQuery Retriever - via `ai_languageModel` connection
9. Vector Store Question Answer Tool - via `ai_languageModel` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "xAI Grok Chat Model",
  "type": "nodes-langchain.lmChatXAiGrok",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```

---

## Xata

## Basic Information

- Node Type: `nodes-langchain.memoryXata`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Xata Memory

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sessionId` | string | Yes | `""` | - |
| `sessionIdType` | options | No | `"fromInput"` | - |
| `sessionId` | string | No | `"={{ $json.sessionId }}"` | The key to use to store the memory |
| `sessionKey` | string | No | `""` | The key to use to store session ID in the memory |
| `notice` | notice | No | `""` | - |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | - |
| `contextWindowLength` | number | No | `5` | - |

#### Property Details

##### Session ID (`sessionIdType`)

Optional values:
- `fromInput`: Connected Chat Trigger Node - Looks for an input field called 'sessionId' that is coming from a directly connected Chat Trigger
- `customKey`: Define below - Use an expression to reference data in previous nodes or enter static text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_memory` (memory)

### Can Connect To

1. AI Agent - via `ai_memory` connection
2. Chat Memory Manager - via `ai_memory` connection
3. Chat Messages Retriever - via `ai_memory` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Xata",
  "type": "nodes-langchain.memoryXata",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sessionId": ""
  }
}
```

---

## XML

## Basic Information

- Node Type: `nodes-base.xml`
- Category: transform
- Package: n8n-nodes-base

### Description

Convert data from and to XML

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `dataPropertyName` | string | Yes | `"data"` | Name of the property to which to contains the converted XML data |
| `dataPropertyName` | string | Yes | `"data"` | Name of the property which contains the XML data to convert |
| `mode` | options | No | `"xmlToJson"` | From and to what format the data should be converted |
| `options` | collection | No | `{}` | - |
| `options` | collection | No | `{}` | - |
| `xmlNotice` | notice | No | `""` | - |

#### Property Details

##### Mode (`mode`)

From and to what format the data should be converted

Optional values:
- `jsonToxml`: JSON to XML - Converts data from JSON to XML
- `xmlToJson`: XML to JSON - Converts data from XML to JSON

##### Options (`options`)

Optional values:
- `undefined`: allowSurrogateChars - Whether to allow using characters from the Unicode surrogate blocks
- `undefined`: attrkey - Prefix that is used to access the attributes
- `undefined`: cdata - Whether to wrap text nodes in &lt;!\[CDATA\[ ... \]\]&gt; instead of escaping when necessary. Does not add &lt;!\[CDATA\[ ... \]\]&gt; if it is not required.
- `undefined`: charkey - Prefix that is used to access the character content
- `undefined`: headless - Whether to omit the XML header
- `undefined`: rootName - Root element name to be used

##### Options (`options`)

Optional values:
- `undefined`: attrkey - Prefix that is used to access the attributes
- `undefined`: charkey - Prefix that is used to access the character content
- `undefined`: explicitArray - Whether to always put child nodes in an array if true; otherwise an array is created only if there is more than one
- `undefined`: explicitRoot - Whether to set this if you want to get the root node in the resulting object
- `undefined`: ignoreAttrs - Whether to ignore all XML attributes and only create text nodes
- `undefined`: mergeAttrs - Whether to merge attributes and child elements as properties of the parent, instead of keying attributes off a child attribute object. This option is ignored if ignoreAttrs is true.
- `undefined`: normalize - Whether to trim whitespaces inside text nodes
- `undefined`: normalizeTags - Whether to normalize all tag names to lowercase
- `undefined`: trim - Whether to trim the whitespace at the beginning and end of text nodes

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "XML",
  "type": "nodes-base.xml",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "dataPropertyName": "data"
  }
}
```

---

## Zep

## Basic Information

- Node Type: `nodes-langchain.memoryZep`
- Category: transform
- Package: @n8n/n8n-nodes-langchain
- Requires Credentials: Yes

### Description

Use Zep Memory

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `sessionId` | string | Yes | `""` | - |
| `sessionIdType` | options | No | `"fromInput"` | - |
| `sessionId` | string | No | `"={{ $json.sessionId }}"` | The key to use to store the memory |
| `sessionKey` | string | No | `""` | The key to use to store session ID in the memory |
| `deprecationNotice` | notice | No | `""` | - |
| `notice` | notice | No | `""` | - |
| `supportedVersions` | notice | No | `""` | - |
| `sessionKey` | string | No | `"={{ $json.sessionId }}"` | - |

#### Property Details

##### Session ID (`sessionIdType`)

Optional values:
- `fromInput`: Connected Chat Trigger Node - Looks for an input field called 'sessionId' that is coming from a directly connected Chat Trigger
- `customKey`: Define below - Use an expression to reference data in previous nodes or enter static text

### Connection Guide

### Connection Type

- Input Types: None (this is a trigger or starting node)
- Output Types: `ai_memory` (memory)

### Can Connect To

1. AI Agent - via `ai_memory` connection
2. Chat Memory Manager - via `ai_memory` connection
3. Chat Messages Retriever - via `ai_memory` connection
### JSON Configuration Examples

#### Basic Configuration
```json
{
  "name": "Zep",
  "type": "nodes-langchain.memoryZep",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "sessionId": ""
  }
}
```

---

## Zoho CRM

## Basic Information

- Node Type: `nodes-base.zohoCrm`
- Category: transform
- Package: n8n-nodes-base
- Requires Credentials: Yes

### Description

Consume Zoho CRM API

### Available Operations

### Create
Create an account
- Value: `create`

### Create or Update
Create a new record, or update the current one if it already exists (upsert)
- Value: `upsert`

### Delete
Delete an account
- Value: `delete`

### Get
Get an account
- Value: `get`

### Get Many
Get many accounts
- Value: `getAll`

### Update
Update an account
- Value: `update`

### Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `accountName` | string | Yes | `""` | Name of the account. If a record with this account name exists it will be updated, otherwise a new one will be created. |
| `accountId` | string | Yes | `""` | ID of the account to delete. Can be found at the end of the URL. |
| `accountId` | string | Yes | `""` | ID of the account to retrieve. Can be found at the end of the URL. |
| `accountId` | string | Yes | `""` | ID of the account to update. Can be found at the end of the URL. |
| `contactId` | string | Yes | `""` | ID of the contact to delete |
| `contactId` | string | Yes | `""` | ID of the contact to retrieve |
| `contactId` | string | Yes | `""` | ID of the contact to update |
| `dealName` | string | Yes | `""` | Name of the deal. If a record with this deal name exists it will be updated, otherwise a new one will be created. |
| `stage` | options | Yes | `[]` | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| `dealId` | string | Yes | `""` | ID of the deal to delete |

### Connection Guide

### Connection Type

- Input Types: `main` (general data flow)
- Output Types: `main` (general data flow)

### Can Receive From

1. Webhook - via `main` connection
2. ActiveCampaign Trigger - via `main` connection
3. Acuity Scheduling Trigger - via `main` connection
4. Affinity Trigger - via `main` connection
5. Airtable Trigger - via `main` connection
6. AMQP Trigger - via `main` connection
7. Asana Trigger - via `main` connection
8. Autopilot Trigger - via `main` connection
9. AWS SNS Trigger - via `main` connection
10. Bitbucket Trigger - via `main` connection

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
  "name": "Zoho CRM",
  "type": "nodes-base.zohoCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "accountName": "",
    "accountId": "",
    "contactId": "",
    "dealName": "",
    "stage": [],
    "dealId": ""
  }
}
```

#### Create Example
```json
{
  "name": "Zoho CRM",
  "type": "nodes-base.zohoCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "accountName": "",
    "accountId": "",
    "contactId": "",
    "dealName": "",
    "stage": [],
    "dealId": "",
    "operation": "create"
  }
}
```

#### Create or Update Example
```json
{
  "name": "Zoho CRM",
  "type": "nodes-base.zohoCrm",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "accountName": "",
    "accountId": "",
    "contactId": "",
    "dealName": "",
    "stage": [],
    "dealId": "",
    "operation": "upsert"
  }
}
```
