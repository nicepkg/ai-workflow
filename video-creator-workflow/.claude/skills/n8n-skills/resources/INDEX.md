# n8n Node Resource Index

This index provides quick access to all 545 built-in n8n nodes and 30 community packages.

## Usage Guide

This index contains two ways to search:

1. Find by Category: Browse nodes by functional category
2. Template Index: Browse popular workflow templates

### Instructions for AI Assistants

For nodes in merged files, use line number ranges for precise reading:

```
Read(file_path, offset=starting_line, limit=line_count)
```

Example: Read Azure Cosmos DB node (starting line 110, line count 64)
```
Read("resources/transform/transform-merged-1.md", offset=110, limit=64)
```

## Quick Navigation

- [Find by Category](#find-by-category)
- [Community Packages](#community-packages)
- [Template Index](#template-index)
- [Statistics](#statistics)

---

## Find by Category

### Data Transformation Nodes - 223 nodes

#### High-Priority Nodes (15 individual files)

| Node Name | nodeType | File Path | Description |
|---------|---------|---------|------|
| Code | `nodes-base.code` | transform/nodes-base.code.md | Run custom JavaScript or Python code |
| Function | `nodes-base.function` | transform/nodes-base.function.md | Run custom function code which gets executed once  |
| If | `nodes-base.if` | transform/nodes-base.if.md | Route items to different branches (true/false) |
| Merge | `nodes-base.merge` | transform/nodes-base.merge.md | Merges data of multiple streams once data from bot |
| Gmail | `nodes-base.gmail` | transform/nodes-base.gmail.md | Consume the Gmail API |
| OpenAI | `nodes-base.openAi` | transform/nodes-base.openAi.md | Consume Open AI |
| Action Network | `nodes-base.actionNetwork` | transform/nodes-base.actionNetwork.md | Consume the Action Network API |
| ActiveCampaign | `nodes-base.activeCampaign` | transform/nodes-base.activeCampaign.md | Create and edit data in ActiveCampaign |
| Adalo | `nodes-base.adalo` | transform/nodes-base.adalo.md | Consume Adalo API |
| Agile CRM | `nodes-base.agileCrm` | transform/nodes-base.agileCrm.md | Consume Agile CRM API |
| Airtop | `nodes-base.airtop` | transform/nodes-base.airtop.md | Scrape and control any site with Airtop |
| AI Transform | `nodes-base.aiTransform` | transform/nodes-base.aiTransform.md | Modify data based on instructions written in plain |
| AMQP Sender | `nodes-base.amqp` | transform/nodes-base.amqp.md | Sends a raw-message via AMQP 1.0, executed once pe |
| APITemplate.io | `nodes-base.apiTemplateIo` | transform/nodes-base.apiTemplateIo.md | Consume the APITemplate.io API |
| AWS DynamoDB | `nodes-base.awsDynamoDb` | transform/nodes-base.awsDynamoDb.md | Consume the AWS DynamoDB API |

#### Other Nodes (208 nodes in merged files)

| Node Name | nodeType | File Path | Start Line | Line Count | Description |
|---------|---------|---------|---------|-----|------|
| Aggregate | `nodes-base.aggregate` | transform/transform-merged-2.md | 110 | 61 | Combine a field from many items into a l |
| AI Agent | `nodes-langchain.agent` | transform/transform-merged-2.md | 171 | 57 | Generates an action plan and executes it |
| AI Agent Tool | `nodes-langchain.agentTool` | transform/transform-merged-2.md | 228 | 55 | Generates an action plan and executes it |
| Anthropic | `nodes-langchain.anthropic` | transform/transform-merged-2.md | 283 | 97 | Interact with Anthropic AI models |
| Anthropic Chat Model | `nodes-langchain.lmChatAnthropic` | transform/transform-merged-2.md | 380 | 92 | Language Model Anthropic |
| Auto-fixing Output Parser | `nodes-langchain.outputParserAutofixing` | transform/transform-merged-2.md | 472 | 37 | Deprecated, use structured output parser |
| AWS Bedrock Chat Model | `nodes-langchain.lmChatAwsBedrock` | transform/transform-merged-2.md | 509 | 51 | Language Model AWS Bedrock |
| Azure AI Search Vector Store | `nodes-langchain.vectorStoreAzureAISearch` | transform/transform-merged-2.md | 560 | 68 | Work with your data in Azure AI Search V |
| Azure Cosmos DB | `nodes-base.azureCosmosDb` | transform/transform-merged-1.md | 110 | 64 | Interact with Azure Cosmos DB API |
| Azure OpenAI Chat Model | `nodes-langchain.lmChatAzureOpenAi` | transform/transform-merged-2.md | 628 | 55 | For advanced usage with an AI chain |
| Azure Storage | `nodes-base.azureStorage` | transform/transform-merged-1.md | 174 | 74 | Interact with Azure Storage API |
| BambooHR | `nodes-base.bambooHr` | transform/transform-merged-1.md | 248 | 143 | Consume BambooHR API |
| Basic LLM Chain | `nodes-langchain.chainLlm` | transform/transform-merged-2.md | 683 | 59 | A simple chain to prompt a large languag |
| Binary Input Loader | `nodes-langchain.documentBinaryInputLoader` | transform/transform-merged-2.md | 742 | 52 | Use binary data from a previous step in  |
| Bitwarden | `nodes-base.bitwarden` | transform/transform-merged-1.md | 391 | 110 | Consume the Bitwarden API |
| Brevo | `nodes-base.sendInBlue` | transform/transform-merged-1.md | 501 | 85 | Consume Brevo API |
| Bubble | `nodes-base.bubble` | transform/transform-merged-1.md | 586 | 91 | Consume the Bubble Data API |
| Calculator | `nodes-langchain.toolCalculator` | transform/transform-merged-2.md | 794 | 28 | Make it easier for AI agents to perform  |
| Call n8n Sub-Workflow Tool | `nodes-langchain.toolWorkflow` | transform/transform-merged-2.md | 822 | 46 | Uses another n8n workflow as a tool. All |
| Character Text Splitter | `nodes-langchain.textSplitterCharacterTextSplitter` | transform/transform-merged-2.md | 868 | 31 | Split text into chunks by characters |
| Chat Memory Manager | `nodes-langchain.memoryManager` | transform/transform-merged-2.md | 899 | 71 | Manage chat messages memory and use it i |
| Chat Messages Retriever | `nodes-langchain.memoryChatRetriever` | transform/transform-merged-2.md | 970 | 29 | Retrieve chat messages from memory and u |
| Clockify | `nodes-base.clockify` | transform/transform-merged-1.md | 677 | 70 | Consume Clockify REST API |
| Code Tool | `nodes-langchain.toolCode` | transform/transform-merged-2.md | 999 | 53 | Write a tool in JS or Python |
| Cohere Chat Model | `nodes-langchain.lmChatCohere` | transform/transform-merged-2.md | 1052 | 41 | For advanced usage with an AI chain |
| Cohere Model | `nodes-langchain.lmCohere` | transform/transform-merged-2.md | 1093 | 41 | Language Model Cohere |
| Compare Datasets | `nodes-base.compareDatasets` | transform/transform-merged-1.md | 747 | 72 | Compare two inputs for changes |
| Compression | `nodes-base.compression` | transform/transform-merged-1.md | 819 | 81 | Compress and decompress files |
| Contextual Compression Retriever | `nodes-langchain.retrieverContextualCompression` | transform/transform-merged-2.md | 1134 | 22 | Enhances document similarity search by c |
| Convert to/from binary data | `nodes-base.moveBinaryData` | transform/transform-merged-1.md | 900 | 59 | Move data between binary and JSON proper |
| Copper | `nodes-base.copper` | transform/transform-merged-1.md | 959 | 65 | Consume the Copper API |
| Cortex | `nodes-base.cortex` | transform/transform-merged-1.md | 1024 | 82 | Apply the Cortex analyzer/responder on t |
| crowd.dev | `nodes-base.crowdDev` | transform/transform-merged-1.md | 1106 | 73 | crowd.dev is an open-source suite of com |
| Crypto | `nodes-base.crypto` | transform/transform-merged-1.md | 1179 | 179 | Provide cryptographic utilities |
| Customer Datastore (n8n training) | `nodes-base.n8nTrainingCustomerDatastore` | transform/transform-merged-1.md | 1358 | 56 | Dummy node used for n8n training |
| Customer Messenger (n8n training) | `nodes-base.n8nTrainingCustomerMessenger` | transform/transform-merged-1.md | 1414 | 29 | Dummy node used for n8n training |
| Date & Time | `nodes-base.dateTime` | transform/transform-merged-1.md | 1443 | 150 | Allows you to manipulate date and time v |
| DeepSeek Chat Model | `nodes-langchain.lmChatDeepSeek` | transform/transform-merged-2.md | 1156 | 48 | For advanced usage with an AI chain |
| Default Data Loader | `nodes-langchain.documentDefaultDataLoader` | transform/transform-merged-2.md | 1204 | 82 | Load data from previous step in the work |
| Dropcontact | `nodes-base.dropcontact` | transform/transform-merged-1.md | 1593 | 88 | Find B2B emails and enrich contacts |
| Edit Image | `nodes-base.editImage` | transform/transform-merged-1.md | 1681 | 184 | Edits an image like blur, resize or addi |
| Elastic Security | `nodes-base.elasticSecurity` | transform/transform-merged-1.md | 1865 | 117 | Consume the Elastic Security API |
| Elasticsearch | `nodes-base.elasticsearch` | transform/transform-merged-1.md | 1982 | 70 | Consume the Elasticsearch API |
| Embeddings AWS Bedrock | `nodes-langchain.embeddingsAwsBedrock` | transform/transform-merged-2.md | 1286 | 30 | Use Embeddings AWS Bedrock |
| Embeddings Azure OpenAI | `nodes-langchain.embeddingsAzureOpenAi` | transform/transform-merged-2.md | 1316 | 43 | Use Embeddings Azure OpenAI |
| Embeddings Cohere | `nodes-langchain.embeddingsCohere` | transform/transform-merged-2.md | 1359 | 46 | Use Cohere Embeddings |
| Embeddings Google Gemini | `nodes-langchain.embeddingsGoogleGemini` | transform/transform-merged-2.md | 1405 | 31 | Use Google Gemini Embeddings |
| Embeddings Google Vertex | `nodes-langchain.embeddingsGoogleVertex` | transform/transform-merged-2.md | 1436 | 32 | Use Google Vertex Embeddings |
| Embeddings Hugging Face Inference | `nodes-langchain.embeddingsHuggingFaceInference` | transform/transform-merged-2.md | 1468 | 42 | Use HuggingFace Inference Embeddings |
| Embeddings Lemonade | `nodes-langchain.embeddingsLemonade` | transform/transform-merged-2.md | 1510 | 30 | Use Lemonade Embeddings |
| Embeddings Mistral Cloud | `nodes-langchain.embeddingsMistralCloud` | transform/transform-merged-2.md | 1540 | 41 | Use Embeddings Mistral Cloud |
| Embeddings Ollama | `nodes-langchain.embeddingsOllama` | transform/transform-merged-2.md | 1581 | 30 | Use Ollama Embeddings |
| Embeddings OpenAI | `nodes-langchain.embeddingsOpenAi` | transform/transform-merged-2.md | 1611 | 46 | Use Embeddings OpenAI |
| Evaluation | `nodes-base.evaluation` | transform/transform-merged-1.md | 2052 | 104 | Runs an evaluation |
| Execute Command | `nodes-base.executeCommand` | transform/transform-merged-1.md | 2156 | 29 | Executes a command on the host |
| Execute Sub-workflow | `nodes-base.executeWorkflow` | transform/transform-merged-1.md | 2185 | 78 | Execute another workflow |
| Facebook Graph API | `nodes-base.facebookGraphApi` | transform/transform-merged-1.md | 2263 | 94 | Interacts with Facebook using the Graph  |
| Filter | `nodes-base.filter` | transform/transform-merged-1.md | 2357 | 38 | Remove items matching a condition |
| Freshservice | `nodes-base.freshservice` | transform/transform-merged-1.md | 2395 | 93 | Consume the Freshservice API |
| Freshworks CRM | `nodes-base.freshworksCrm` | transform/transform-merged-1.md | 2488 | 118 | Consume the Freshworks CRM API |
| Function Item | `nodes-base.functionItem` | transform/transform-merged-1.md | 2606 | 29 | Run custom function code which gets exec |
| Git | `nodes-base.git` | transform/transform-merged-1.md | 2635 | 134 | Control git. |
| GitHub Document Loader | `nodes-langchain.documentGithubLoader` | transform/transform-merged-2.md | 1657 | 47 | Use GitHub data as input to this chain |
| Gong | `nodes-base.gong` | transform/transform-merged-1.md | 2769 | 110 | Interact with Gong API |
| Google Ads | `nodes-base.googleAds` | transform/transform-merged-1.md | 2879 | 76 | Use the Google Ads API |
| Google Analytics | `nodes-base.googleAnalytics` | transform/transform-merged-1.md | 2955 | 73 | Use the Google Analytics API |
| Google Cloud Storage | `nodes-base.googleCloudStorage` | transform/transform-merged-1.md | 3028 | 114 | Use the Google Cloud Storage API |
| Google Gemini | `nodes-langchain.googleGemini` | transform/transform-merged-2.md | 1704 | 70 | Interact with Google Gemini AI models |
| Google Gemini Chat Model | `nodes-langchain.lmChatGoogleGemini` | transform/transform-merged-2.md | 1774 | 44 | Chat Model Google Gemini |
| Google Perspective | `nodes-base.googlePerspective` | transform/transform-merged-1.md | 3142 | 59 | Consume Google Perspective API |
| Google Vertex Chat Model | `nodes-langchain.lmChatGoogleVertex` | transform/transform-merged-2.md | 1818 | 46 | Chat Model Google Vertex |
| GoToWebinar | `nodes-base.goToWebinar` | transform/transform-merged-1.md | 3201 | 75 | Consume the GoToWebinar API |
| Grafana | `nodes-base.grafana` | transform/transform-merged-1.md | 3276 | 70 | Consume the Grafana API |
| Groq Chat Model | `nodes-langchain.lmChatGroq` | transform/transform-merged-2.md | 1864 | 41 | Language Model Groq |
| Guardrails | `nodes-langchain.guardrails` | transform/transform-merged-3.md | 18 | 72 | Safeguard AI models from malicious input |
| Hacker News | `nodes-base.hackerNews` | transform/transform-merged-1.md | 3346 | 83 | Consume Hacker News API |
| HighLevel | `nodes-base.highLevel` | transform/transform-merged-1.md | 3429 | 83 | Consume HighLevel API |
| HTML | `nodes-base.html` | transform/transform-merged-1.md | 3512 | 102 | Work with HTML |
| HTML Extract | `nodes-base.htmlExtract` | transform/transform-merged-1.md | 3614 | 52 | Extracts data from HTML |
| Hugging Face Inference Model | `nodes-langchain.lmOpenHuggingFaceInference` | transform/transform-merged-2.md | 1905 | 46 | Language Model HuggingFaceInference |
| In Memory Vector Store Insert | `nodes-langchain.vectorStoreInMemoryInsert` | transform/transform-merged-2.md | 1951 | 30 | Insert data into an in-memory vector sto |
| In Memory Vector Store Load | `nodes-langchain.vectorStoreInMemoryLoad` | transform/transform-merged-2.md | 1981 | 28 | Load embedded data from an in-memory vec |
| Information Extractor | `nodes-langchain.informationExtractor` | transform/transform-merged-2.md | 2009 | 56 | Extract information from text in a struc |
| Item List Output Parser | `nodes-langchain.outputParserItemList` | transform/transform-merged-2.md | 2065 | 37 | Return the results as separate items |
| Jina AI | `nodes-base.jinaAi` | transform/transform-merged-1.md | 3666 | 101 | Interact with Jina AI API |
| JSON Input Loader | `nodes-langchain.documentJsonInputLoader` | transform/transform-merged-2.md | 2102 | 37 | Use JSON data from a previous step in th |
| JWT | `nodes-base.jwt` | transform/transform-merged-1.md | 3767 | 84 | JWT |
| Kafka | `nodes-base.kafka` | transform/transform-merged-1.md | 3851 | 52 | Sends messages to a Kafka topic |
| KoBoToolbox | `nodes-base.koBoToolbox` | transform/transform-merged-1.md | 3903 | 87 | Work with KoBoToolbox forms and submissi |
| LangChain Code | `nodes-langchain.code` | transform/transform-merged-2.md | 2139 | 53 | LangChain Code Node |
| Ldap | `nodes-base.ldap` | transform/transform-merged-1.md | 3990 | 74 | Interact with LDAP servers |
| Lemlist | `nodes-base.lemlist` | transform/transform-merged-1.md | 4064 | 60 | Consume the Lemlist API |
| Lemonade Chat Model | `nodes-langchain.lmChatLemonade` | transform/transform-merged-2.md | 2192 | 45 | Language Model Lemonade Chat |
| Lemonade Model | `nodes-langchain.lmLemonade` | transform/transform-merged-2.md | 2237 | 45 | Language Model Lemonade |
| Limit | `nodes-base.limit` | transform/transform-merged-2.md | 2282 | 39 | Restrict the number of items |
| LoneScale | `nodes-base.loneScale` | transform/transform-merged-1.md | 4124 | 97 | Create List, add / delete items |
| Mailcheck | `nodes-base.mailcheck` | transform/transform-merged-1.md | 4221 | 53 | Consume Mailcheck API |
| Marketstack | `nodes-base.marketstack` | transform/transform-merged-1.md | 4274 | 82 | Consume Marketstack API |
| MCP Client | `nodes-langchain.mcpClient` | transform/transform-merged-2.md | 2321 | 72 | Standalone MCP Client |
| Metabase | `nodes-base.metabase` | transform/transform-merged-1.md | 4356 | 81 | Use the Metabase API |
| Microsoft Entra ID | `nodes-base.microsoftEntra` | transform/transform-merged-1.md | 4437 | 70 | Interact with Microsoft Entra ID API |
| Microsoft Graph Security | `nodes-base.microsoftGraphSecurity` | transform/transform-merged-1.md | 4507 | 88 | Consume the Microsoft Graph Security API |
| Microsoft Outlook | `nodes-base.microsoftOutlook` | transform/transform-merged-1.md | 4595 | 70 | Consume Microsoft Outlook API |
| Microsoft SharePoint | `nodes-base.microsoftSharePoint` | transform/transform-merged-1.md | 4665 | 62 | Interact with Microsoft SharePoint API |
| Milvus Vector Store | `nodes-langchain.vectorStoreMilvus` | transform/transform-merged-2.md | 2393 | 53 | Work with your data in Milvus Vector Sto |
| MISP | `nodes-base.misp` | transform/transform-merged-1.md | 4727 | 77 | Consume the MISP API |
| Mistral AI | `nodes-base.mistralAi` | transform/transform-merged-1.md | 4804 | 89 | Consume Mistral AI API |
| Mistral Cloud Chat Model | `nodes-langchain.lmChatMistralCloud` | transform/transform-merged-2.md | 2446 | 45 | For advanced usage with an AI chain |
| Mocean | `nodes-base.mocean` | transform/transform-merged-1.md | 4893 | 73 | Send SMS and voice messages via Mocean |
| Model Selector | `nodes-langchain.modelSelector` | transform/transform-merged-3.md | 90 | 53 | Use this node to select one of the conne |
| MongoDB Atlas Vector Store | `nodes-langchain.vectorStoreMongoDBAtlas` | transform/transform-merged-2.md | 2491 | 55 | Work with your data in MongoDB Atlas Vec |
| MongoDB Chat Memory | `nodes-langchain.memoryMongoDbChat` | transform/transform-merged-2.md | 2546 | 43 | Stores the chat history in MongoDB colle |
| Monica CRM | `nodes-base.monicaCrm` | transform/transform-merged-1.md | 4966 | 90 | Consume the Monica CRM API |
| Motorhead | `nodes-langchain.memoryMotorhead` | transform/transform-merged-2.md | 2589 | 42 | Use Motorhead Memory |
| MSG91 | `nodes-base.msg91` | transform/transform-merged-1.md | 5056 | 56 | Sends transactional SMS via MSG91 |
| MultiQuery Retriever | `nodes-langchain.retrieverMultiQuery` | transform/transform-merged-2.md | 2631 | 37 | Automates prompt tuning, generates diver |
| n8n | `nodes-base.n8n` | transform/transform-merged-1.md | 5112 | 49 | Handle events and perform actions on you |
| NASA | `nodes-base.nasa` | transform/transform-merged-1.md | 5161 | 100 | Retrieve data from the NASA API |
| Netlify | `nodes-base.netlify` | transform/transform-merged-1.md | 5261 | 95 | Consume Netlify API |
| Odoo | `nodes-base.odoo` | transform/transform-merged-1.md | 5356 | 70 | Consume Odoo API |
| Okta | `nodes-base.okta` | transform/transform-merged-1.md | 5426 | 158 | Use the Okta API |
| Ollama | `nodes-langchain.ollama` | transform/transform-merged-2.md | 2668 | 134 | Interact with Ollama AI models |
| Ollama Chat Model | `nodes-langchain.lmChatOllama` | transform/transform-merged-2.md | 2802 | 58 | Language Model Ollama |
| Ollama Model | `nodes-langchain.lmOllama` | transform/transform-merged-2.md | 2860 | 58 | Language Model Ollama |
| One Simple API | `nodes-base.oneSimpleApi` | transform/transform-merged-1.md | 5584 | 72 | A toolbox of no-code utilities |
| OpenAI | `nodes-langchain.openAi` | transform/transform-merged-2.md | 2918 | 62 | Message an assistant or GPT, analyze ima |
| OpenAI Assistant | `nodes-langchain.openAiAssistant` | transform/transform-merged-2.md | 2980 | 61 | Utilizes Assistant API from Open AI. |
| OpenAI Chat Model | `nodes-langchain.lmChatOpenAi` | transform/transform-merged-2.md | 3041 | 71 | For advanced usage with an AI chain |
| OpenAI Model | `nodes-langchain.lmOpenAi` | transform/transform-merged-2.md | 3112 | 48 | For advanced usage with an AI chain |
| OpenRouter Chat Model | `nodes-langchain.lmChatOpenRouter` | transform/transform-merged-2.md | 3160 | 48 | For advanced usage with an AI chain |
| Perplexity | `nodes-base.perplexity` | transform/transform-merged-1.md | 5656 | 89 | Interact with the Perplexity API to gene |
| Pinecone Vector Store | `nodes-langchain.vectorStorePinecone` | transform/transform-merged-2.md | 3208 | 67 | Work with your data in Pinecone Vector S |
| Pinecone: Insert | `nodes-langchain.vectorStorePineconeInsert` | transform/transform-merged-2.md | 3275 | 32 | Insert data into Pinecone Vector Store i |
| Pinecone: Load | `nodes-langchain.vectorStorePineconeLoad` | transform/transform-merged-2.md | 3307 | 38 | Load data from Pinecone Vector Store ind |
| Pipedrive | `nodes-base.pipedrive` | transform/transform-merged-1.md | 5745 | 88 | Create and edit data in Pipedrive |
| Plivo | `nodes-base.plivo` | transform/transform-merged-1.md | 5833 | 66 | Send SMS/MMS messages or make phone call |
| PostBin | `nodes-base.postBin` | transform/transform-merged-1.md | 5899 | 80 | Consume PostBin API |
| Postgres Chat Memory | `nodes-langchain.memoryPostgresChat` | transform/transform-merged-2.md | 3345 | 42 | Stores the chat history in Postgres tabl |
| Postgres PGVector Store | `nodes-langchain.vectorStorePGVector` | transform/transform-merged-2.md | 3387 | 70 | Work with your data in Postgresql with t |
| Qdrant Vector Store | `nodes-langchain.vectorStoreQdrant` | transform/transform-merged-2.md | 3457 | 69 | Work with your data in a Qdrant collecti |
| Question and Answer Chain | `nodes-langchain.chainRetrievalQa` | transform/transform-merged-2.md | 3526 | 52 | Answer questions about retrieved documen |
| QuickBooks Online | `nodes-base.quickbooks` | transform/transform-merged-1.md | 5979 | 152 | Consume the QuickBooks Online API |
| RabbitMQ | `nodes-base.rabbitmq` | transform/transform-merged-1.md | 6131 | 98 | Sends messages to a RabbitMQ topic |
| Raindrop | `nodes-base.raindrop` | transform/transform-merged-1.md | 6229 | 73 | Consume the Raindrop API |
| Recursive Character Text Splitter | `nodes-langchain.textSplitterRecursiveCharacterTextSplitter` | transform/transform-merged-2.md | 3578 | 40 | Split text into chunks by characters rec |
| Reddit | `nodes-base.reddit` | transform/transform-merged-1.md | 6302 | 100 | Consume the Reddit API |
| Redis Chat Memory | `nodes-langchain.memoryRedisChat` | transform/transform-merged-2.md | 3618 | 44 | Stores the chat history in Redis. |
| Redis Vector Store | `nodes-langchain.vectorStoreRedis` | transform/transform-merged-2.md | 3662 | 77 | Work with your data in a Redis vector in |
| Remove Duplicates | `nodes-base.removeDuplicates` | transform/transform-merged-2.md | 3739 | 103 | Delete items with matching field values |
| Rename Keys | `nodes-base.renameKeys` | transform/transform-merged-1.md | 6402 | 43 | Update item field names |
| Reranker Cohere | `nodes-langchain.rerankerCohere` | transform/transform-merged-2.md | 3842 | 41 | Use Cohere Reranker to reorder documents |
| Respond to Webhook | `nodes-base.respondToWebhook` | transform/transform-merged-1.md | 6445 | 82 | Returns data for Webhook |
| Rundeck | `nodes-base.rundeck` | transform/transform-merged-1.md | 6527 | 72 | Manage Rundeck API |
| SearXNG | `nodes-langchain.toolSearXng` | transform/transform-merged-2.md | 3883 | 40 | Search in SearXNG |
| SecurityScorecard | `nodes-base.securityScorecard` | transform/transform-merged-1.md | 6599 | 146 | Consume SecurityScorecard API |
| SendGrid | `nodes-base.sendGrid` | transform/transform-merged-1.md | 6745 | 87 | Consume SendGrid API |
| Sentiment Analysis | `nodes-langchain.sentimentAnalysis` | transform/transform-merged-2.md | 3923 | 41 | Analyze the sentiment of your text |
| SerpApi (Google Search) | `nodes-langchain.toolSerpApi` | transform/transform-merged-2.md | 3964 | 41 | Search in Google using SerpAPI |
| seven | `nodes-base.sms77` | transform/transform-merged-1.md | 6832 | 80 | Send SMS and make text-to-speech calls |
| SIGNL4 | `nodes-base.signl4` | transform/transform-merged-1.md | 6912 | 77 | Consume SIGNL4 API |
| Simple Memory | `nodes-langchain.memoryBufferWindow` | transform/transform-merged-2.md | 4005 | 42 | Stores in n8n memory, so no credentials  |
| Simple Vector Store | `nodes-langchain.vectorStoreInMemory` | transform/transform-merged-2.md | 4047 | 47 | The easiest way to experiment with vecto |
| Sort | `nodes-base.sort` | transform/transform-merged-2.md | 4094 | 54 | Change items order |
| Split Out | `nodes-base.splitOut` | transform/transform-merged-2.md | 4148 | 49 | Turn a list inside item(s) into separate |
| Splunk | `nodes-base.splunk` | transform/transform-merged-1.md | 6989 | 58 | Consume the Splunk Enterprise API |
| Spreadsheet File | `nodes-base.spreadsheetFile` | transform/transform-merged-1.md | 7047 | 112 | Reads and writes data from a spreadsheet |
| Stackby | `nodes-base.stackby` | transform/transform-merged-1.md | 7159 | 75 | Read, write, and delete data in Stackby |
| Stripe | `nodes-base.stripe` | transform/transform-merged-1.md | 7234 | 81 | Consume the Stripe API |
| Structured Output Parser | `nodes-langchain.outputParserStructured` | transform/transform-merged-2.md | 4197 | 46 | Return data in a defined JSON format |
| Summarization Chain | `nodes-langchain.chainSummarization` | transform/transform-merged-2.md | 4243 | 59 | Transforms text into a concise summary |
| Summarize | `nodes-base.summarize` | transform/transform-merged-2.md | 4302 | 46 | Sum, count, max, etc. across items |
| Supabase Vector Store | `nodes-langchain.vectorStoreSupabase` | transform/transform-merged-2.md | 4348 | 71 | Work with your data in Supabase Vector S |
| Supabase: Insert | `nodes-langchain.vectorStoreSupabaseInsert` | transform/transform-merged-2.md | 4419 | 32 | Insert data into Supabase Vector Store i |
| Supabase: Load | `nodes-langchain.vectorStoreSupabaseLoad` | transform/transform-merged-3.md | 143 | 38 | Load data from Supabase Vector Store ind |
| Switch | `nodes-base.switch` | transform/transform-merged-1.md | 7315 | 58 | Route items depending on defined express |
| Taiga | `nodes-base.taiga` | transform/transform-merged-1.md | 7373 | 70 | Consume Taiga API |
| Tapfiliate | `nodes-base.tapfiliate` | transform/transform-merged-1.md | 7443 | 75 | Consume Tapfiliate API |
| Text Classifier | `nodes-langchain.textClassifier` | transform/transform-merged-2.md | 4451 | 46 | Classify your text into distinct categor |
| TheHive | `nodes-base.theHive` | transform/transform-merged-1.md | 7518 | 96 | Consume TheHive API |
| TheHive 5 | `nodes-base.theHiveProject` | transform/transform-merged-1.md | 7614 | 178 | Consume TheHive 5 API |
| Think Tool | `nodes-langchain.toolThink` | transform/transform-merged-2.md | 4497 | 29 | Invite the AI agent to do some thinking |
| Token Splitter | `nodes-langchain.textSplitterTokenSplitter` | transform/transform-merged-2.md | 4526 | 30 | Split text into chunks by tokens |
| Tool Executor | `nodes-langchain.toolExecutor` | transform/transform-merged-3.md | 181 | 29 | Node to execute tools without an AI Agen |
| TOTP | `nodes-base.totp` | transform/transform-merged-1.md | 7792 | 54 | Generate a time-based one-time password |
| Trello | `nodes-base.trello` | transform/transform-merged-1.md | 7846 | 94 | Create, change and delete boards and car |
| Twake | `nodes-base.twake` | transform/transform-merged-1.md | 7940 | 62 | Consume Twake API |
| Twilio | `nodes-base.twilio` | transform/transform-merged-1.md | 8002 | 72 | Send SMS and WhatsApp messages or make p |
| Unleashed Software | `nodes-base.unleashedSoftware` | transform/transform-merged-1.md | 8074 | 90 | Consume Unleashed Software API |
| urlscan.io | `nodes-base.urlScanIo` | transform/transform-merged-1.md | 8164 | 85 | Provides various utilities for monitorin |
| Vector Store Question Answer Tool | `nodes-langchain.toolVectorStore` | transform/transform-merged-2.md | 4556 | 31 | Answer questions with a vector store |
| Vector Store Retriever | `nodes-langchain.retrieverVectorStore` | transform/transform-merged-2.md | 4587 | 28 | Use a Vector Store as Retriever |
| Vercel AI Gateway Chat Model | `nodes-langchain.lmChatVercelAiGateway` | transform/transform-merged-2.md | 4615 | 48 | For advanced usage with an AI chain via  |
| Weaviate Vector Store | `nodes-langchain.vectorStoreWeaviate` | transform/transform-merged-3.md | 210 | 86 | Work with your data in a Weaviate Cluste |
| Webex by Cisco | `nodes-base.ciscoWebex` | transform/transform-merged-1.md | 8249 | 79 | Consume the Cisco Webex API |
| Webflow | `nodes-base.webflow` | transform/transform-merged-1.md | 8328 | 65 | Consume the Webflow API |
| Wekan | `nodes-base.wekan` | transform/transform-merged-1.md | 8393 | 74 | Consume Wekan API |
| Wikipedia | `nodes-langchain.toolWikipedia` | transform/transform-merged-2.md | 4663 | 28 | Search in Wikipedia |
| Wise | `nodes-base.wise` | transform/transform-merged-1.md | 8467 | 62 | Consume the Wise API |
| Wolfram|Alpha | `nodes-langchain.toolWolframAlpha` | transform/transform-merged-2.md | 4691 | 29 | Connects to WolframAlpha's computational |
| Workflow Retriever | `nodes-langchain.retrieverWorkflow` | transform/transform-merged-2.md | 4720 | 50 | Use an n8n Workflow as Retriever |
| xAI Grok Chat Model | `nodes-langchain.lmChatXAiGrok` | transform/transform-merged-2.md | 4770 | 48 | For advanced usage with an AI chain |
| Xata | `nodes-langchain.memoryXata` | transform/transform-merged-2.md | 4818 | 43 | Use Xata Memory |
| XML | `nodes-base.xml` | transform/transform-merged-2.md | 4861 | 66 | Convert data from and to XML |
| Zep | `nodes-langchain.memoryZep` | transform/transform-merged-2.md | 4927 | 44 | Use Zep Memory |
| Zep Vector Store | `nodes-langchain.vectorStoreZep` | transform/transform-merged-3.md | 296 | 66 | Work with your data in Zep Vector Store |
| Zep Vector Store: Insert | `nodes-langchain.vectorStoreZepInsert` | transform/transform-merged-3.md | 362 | 40 | Insert data into Zep Vector Store index |
| Zep Vector Store: Load | `nodes-langchain.vectorStoreZepLoad` | transform/transform-merged-3.md | 402 | 39 | Load data from Zep Vector Store index |
| Zoho CRM | `nodes-base.zohoCrm` | transform/transform-merged-2.md | 4971 | 74 | Consume Zoho CRM API |

### Input Nodes - 110 nodes

#### High-Priority Nodes (11 individual files)

| Node Name | nodeType | File Path | Description |
|---------|---------|---------|------|
| Set | `nodes-base.set` | input/nodes-base.set.md | Add or edit fields on an input item and optionally |
| Airtable | `nodes-base.airtable` | input/nodes-base.airtable.md | Read, update, write and delete data from Airtable |
| Dropbox | `nodes-base.dropbox` | input/nodes-base.dropbox.md | Access data on Dropbox |
| GitHub | `nodes-base.github` | input/nodes-base.github.md | Consume GitHub API |
| Google Drive | `nodes-base.googleDrive` | input/nodes-base.googleDrive.md | Access data on Google Drive |
| Google Sheets | `nodes-base.googleSheets` | input/nodes-base.googleSheets.md | Read, update and write data to Google Sheets |
| MySQL | `nodes-base.mySql` | input/nodes-base.mySql.md | Get, add and update data in MySQL |
| Postgres | `nodes-base.postgres` | input/nodes-base.postgres.md | Get, add and update data in Postgres |
| Asana | `nodes-base.asana` | input/nodes-base.asana.md | Consume Asana REST API |
| Automizy | `nodes-base.automizy` | input/nodes-base.automizy.md | Consume Automizy API |
| Autopilot | `nodes-base.autopilot` | input/nodes-base.autopilot.md | Consume Autopilot API |

#### Other Nodes (99 nodes in merged files)

| Node Name | nodeType | File Path | Start Line | Line Count | Description |
|---------|---------|---------|---------|-----|------|
| Box | `nodes-base.box` | input/input-merged.md | 109 | 105 | Consume Box API |
| Chargebee | `nodes-base.chargebee` | input/input-merged.md | 214 | 96 | Retrieve data from Chargebee API |
| Cloudflare | `nodes-base.cloudflare` | input/input-merged.md | 310 | 85 | Consume Cloudflare API |
| Contentful | `nodes-base.contentful` | input/input-merged.md | 395 | 94 | Consume Contentful API |
| Convert to File | `nodes-base.convertToFile` | input/input-merged.md | 489 | 105 | Convert JSON data to binary data |
| ConvertKit | `nodes-base.convertKit` | input/input-merged.md | 594 | 77 | Consume ConvertKit API |
| CrateDB | `nodes-base.crateDb` | input/input-merged.md | 671 | 77 | Add and update data in CrateDB |
| Data table | `nodes-base.dataTable` | input/input-merged.md | 748 | 123 | Permanently save data across workflow ex |
| DeepL | `nodes-base.deepL` | input/input-merged.md | 871 | 64 | Translate data using DeepL |
| DHL | `nodes-base.dhl` | input/input-merged.md | 935 | 59 | Consume DHL API |
| Discourse | `nodes-base.discourse` | input/input-merged.md | 994 | 118 | Consume Discourse API |
| Disqus | `nodes-base.disqus` | input/input-merged.md | 1112 | 111 | Access data on Disqus |
| Emelia | `nodes-base.emelia` | input/input-merged.md | 1223 | 79 | Consume the Emelia API |
| Execution Data | `nodes-base.executionData` | input/input-merged.md | 1302 | 52 | Add execution data for search |
| Extract from File | `nodes-base.extractFromFile` | input/input-merged.md | 1354 | 145 | Convert binary data to JSON |
| FileMaker | `nodes-base.filemaker` | input/input-merged.md | 1499 | 107 | Retrieve data from the FileMaker data AP |
| FTP | `nodes-base.ftp` | input/input-merged.md | 1606 | 81 | Transfer files via FTP or SFTP |
| GetResponse | `nodes-base.getResponse` | input/input-merged.md | 1687 | 129 | Consume GetResponse API |
| Ghost | `nodes-base.ghost` | input/input-merged.md | 1816 | 114 | Consume Ghost API |
| GitLab | `nodes-base.gitlab` | input/input-merged.md | 1930 | 70 | Retrieve data from GitLab API |
| Google BigQuery | `nodes-base.googleBigQuery` | input/input-merged.md | 2000 | 114 | Consume Google BigQuery API |
| Google Books | `nodes-base.googleBooks` | input/input-merged.md | 2114 | 79 | Read data from Google Books |
| Google Business Profile | `nodes-base.googleBusinessProfile` | input/input-merged.md | 2193 | 89 | Consume Google Business Profile API |
| Google Calendar | `nodes-base.googleCalendar` | input/input-merged.md | 2282 | 49 | Consume Google Calendar API |
| Google Chat | `nodes-base.googleChat` | input/input-merged.md | 2331 | 77 | Consume Google Chat API |
| Google Cloud Firestore | `nodes-base.googleFirebaseCloudFirestore` | input/input-merged.md | 2408 | 74 | Interact with Google Firebase - Cloud Fi |
| Google Cloud Natural Language | `nodes-base.googleCloudNaturalLanguage` | input/input-merged.md | 2482 | 71 | Consume Google Cloud Natural Language AP |
| Google Cloud Realtime Database | `nodes-base.googleFirebaseRealtimeDatabase` | input/input-merged.md | 2553 | 76 | Interact with Google Firebase - Realtime |
| Google Contacts | `nodes-base.googleContacts` | input/input-merged.md | 2629 | 197 | Consume Google Contacts API |
| Google Docs | `nodes-base.googleDocs` | input/input-merged.md | 2826 | 92 | Consume Google Docs API. |
| Google Slides | `nodes-base.googleSlides` | input/input-merged.md | 2918 | 105 | Consume the Google Slides API |
| Google Tasks | `nodes-base.googleTasks` | input/input-merged.md | 3023 | 86 | Consume Google Tasks API |
| Google Translate | `nodes-base.googleTranslate` | input/input-merged.md | 3109 | 69 | Translate data using Google Translate |
| Google Workspace Admin | `nodes-base.gSuiteAdmin` | input/input-merged.md | 3178 | 116 | Consume Google Workspace Admin API |
| Gotify | `nodes-base.gotify` | input/input-merged.md | 3294 | 82 | Consume Gotify API |
| GraphQL | `nodes-base.graphql` | input/input-merged.md | 3376 | 93 | Makes a GraphQL request and returns the  |
| Grist | `nodes-base.grist` | input/input-merged.md | 3469 | 95 | Consume the Grist API |
| HaloPSA | `nodes-base.haloPSA` | input/input-merged.md | 3564 | 80 | Consume HaloPSA API |
| Harvest | `nodes-base.harvest` | input/input-merged.md | 3644 | 82 | Access data on Harvest |
| Help Scout | `nodes-base.helpScout` | input/input-merged.md | 3726 | 95 | Consume Help Scout API |
| iCalendar | `nodes-base.iCal` | input/input-merged.md | 3821 | 69 | Create iCalendar file |
| Item Lists | `nodes-base.itemLists` | input/input-merged.md | 3890 | 143 | Helper for working with lists of items a |
| Iterable | `nodes-base.iterable` | input/input-merged.md | 4033 | 91 | Consume Iterable API |
| Keap | `nodes-base.keap` | input/input-merged.md | 4124 | 81 | Consume Keap API |
| Kitemaker | `nodes-base.kitemaker` | input/input-merged.md | 4205 | 74 | Consume the Kitemaker GraphQL API |
| Line | `nodes-base.line` | input/input-merged.md | 4279 | 63 | Consume Line API |
| LinkedIn | `nodes-base.linkedIn` | input/input-merged.md | 4342 | 91 | Consume LinkedIn API |
| Magento 2 | `nodes-base.magento2` | input/input-merged.md | 4433 | 80 | Consume Magento API |
| MailerLite | `nodes-base.mailerLite` | input/input-merged.md | 4513 | 97 | Consume MailerLite API |
| Microsoft Dynamics CRM | `nodes-base.microsoftDynamicsCrm` | input/input-merged.md | 4610 | 175 | Consume Microsoft Dynamics CRM API |
| Microsoft Excel 365 | `nodes-base.microsoftExcel` | input/input-merged.md | 4785 | 78 | Consume Microsoft Excel API |
| Microsoft OneDrive | `nodes-base.microsoftOneDrive` | input/input-merged.md | 4863 | 112 | Consume Microsoft OneDrive API |
| Microsoft SQL | `nodes-base.microsoftSql` | input/input-merged.md | 4975 | 75 | Get, add and update data in Microsoft SQ |
| Microsoft Teams | `nodes-base.microsoftTeams` | input/input-merged.md | 5050 | 96 | Consume Microsoft Teams API |
| Microsoft To Do | `nodes-base.microsoftToDo` | input/input-merged.md | 5146 | 65 | Consume Microsoft To Do API. |
| Mindee | `nodes-base.mindee` | input/input-merged.md | 5211 | 85 | Consume Mindee API |
| MongoDB | `nodes-base.mongoDb` | input/input-merged.md | 5296 | 105 | Find, insert and update documents in Mon |
| MQTT | `nodes-base.mqtt` | input/input-merged.md | 5401 | 40 | Push messages to MQTT |
| n8n Form | `nodes-base.form` | input/input-merged.md | 5441 | 116 | Generate webforms in n8n and pass their  |
| Nextcloud | `nodes-base.nextCloud` | input/input-merged.md | 5557 | 74 | Access data on Nextcloud |
| NocoDB | `nodes-base.nocoDb` | input/input-merged.md | 5631 | 78 | Read, update, write and delete data from |
| Npm | `nodes-base.npm` | input/input-merged.md | 5709 | 83 | Consume NPM registry API |
| Onfleet | `nodes-base.onfleet` | input/input-merged.md | 5792 | 96 | Consume Onfleet API |
| OpenWeatherMap | `nodes-base.openWeatherMap` | input/input-merged.md | 5888 | 84 | Gets current and future weather informat |
| Oracle Database | `nodes-base.oracleDatabase` | input/input-merged.md | 5972 | 106 | Get, add and update data in Oracle datab |
| Phantombuster | `nodes-base.phantombuster` | input/input-merged.md | 6078 | 104 | Consume Phantombuster API |
| Philips Hue | `nodes-base.philipsHue` | input/input-merged.md | 6182 | 97 | Consume Philips Hue API |
| PostHog | `nodes-base.postHog` | input/input-merged.md | 6279 | 69 | Consume PostHog API |
| Pushbullet | `nodes-base.pushbullet` | input/input-merged.md | 6348 | 85 | Consume Pushbullet API |
| Pushcut | `nodes-base.pushcut` | input/input-merged.md | 6433 | 63 | Consume Pushcut API |
| Pushover | `nodes-base.pushover` | input/input-merged.md | 6496 | 82 | Consume Pushover API |
| QuestDB | `nodes-base.questDb` | input/input-merged.md | 6578 | 70 | Get, add and update data in QuestDB |
| Quick Base | `nodes-base.quickbase` | input/input-merged.md | 6648 | 49 | Integrate with the Quick Base RESTful AP |
| Read Binary File | `nodes-base.readBinaryFile` | input/input-merged.md | 6697 | 29 | Reads a binary file from disk |
| Read Binary Files | `nodes-base.readBinaryFiles` | input/input-merged.md | 6726 | 29 | Reads binary files from disk |
| Read PDF | `nodes-base.readPDF` | input/input-merged.md | 6755 | 30 | Reads a PDF and extracts its content |
| Read/Write Files from Disk | `nodes-base.readWriteFile` | input/input-merged.md | 6785 | 75 | Read or write files from the computer th |
| Redis | `nodes-base.redis` | input/input-merged.md | 6860 | 90 | Get, send and update data in Redis |
| Respond to Chat | `nodes-langchain.chat` | input/input-merged.md | 6950 | 45 | Send a message to a chat |
| RSS Read | `nodes-base.rssFeedRead` | input/input-merged.md | 6995 | 37 | Reads data from an RSS Feed |
| Sendy | `nodes-base.sendy` | input/input-merged.md | 7032 | 94 | Consume Sendy API |
| Snowflake | `nodes-base.snowflake` | input/input-merged.md | 7126 | 68 | Get, add and update data in Snowflake |
| Spotify | `nodes-base.spotify` | input/input-merged.md | 7194 | 86 | Access public song data via the Spotify  |
| SSH | `nodes-base.ssh` | input/input-merged.md | 7280 | 79 | Execute commands via SSH |
| Start | `nodes-base.start` | input/input-merged.md | 7359 | 28 | Starts the workflow execution from this  |
| Sticky Note | `nodes-base.stickyNote` | input/input-merged.md | 7387 | 31 | Make your workflow easier to understand |
| Stop and Error | `nodes-base.stopAndError` | input/input-merged.md | 7418 | 40 | Throw an error in the workflow |
| Strapi | `nodes-base.strapi` | input/input-merged.md | 7458 | 83 | Consume Strapi API |
| Strava | `nodes-base.strava` | input/input-merged.md | 7541 | 123 | Consume Strava API |
| Supabase | `nodes-base.supabase` | input/input-merged.md | 7664 | 130 | Add, get, delete and update data in a ta |
| TimescaleDB | `nodes-base.timescaleDb` | input/input-merged.md | 7794 | 77 | Add and update data in TimescaleDB |
| Twist | `nodes-base.twist` | input/input-merged.md | 7871 | 78 | Consume Twist API |
| Venafi TLS Protect Cloud | `nodes-base.venafiTlsProtectCloud` | input/input-merged.md | 7949 | 87 | Consume Venafi TLS Protect Cloud API |
| Venafi TLS Protect Datacenter | `nodes-base.venafiTlsProtectDatacenter` | input/input-merged.md | 8036 | 123 | Consume Venafi TLS Protect Datacenter |
| Vonage | `nodes-base.vonage` | input/input-merged.md | 8159 | 67 | Consume Vonage API |
| Yourls | `nodes-base.yourls` | input/input-merged.md | 8226 | 78 | Consume Yourls API |
| YouTube | `nodes-base.youTube` | input/input-merged.md | 8304 | 165 | Consume YouTube API |
| Zammad | `nodes-base.zammad` | input/input-merged.md | 8469 | 77 | Consume the Zammad API |
| Zoom | `nodes-base.zoom` | input/input-merged.md | 8546 | 121 | Consume Zoom API |

### Output Nodes - 99 nodes

#### High-Priority Nodes (15 individual files)

| Node Name | nodeType | File Path | Description |
|---------|---------|---------|------|
| HTTP Request | `nodes-base.httpRequest` | output/nodes-base.httpRequest.md | Makes an HTTP request and returns the response dat |
| Discord | `nodes-base.discord` | output/nodes-base.discord.md | Sends data to Discord |
| Notion | `nodes-base.notion` | output/nodes-base.notion.md | Consume Notion API |
| S3 | `nodes-base.s3` | output/nodes-base.s3.md | Sends data to any S3-compatible service |
| Slack | `nodes-base.slack` | output/nodes-base.slack.md | Consume Slack API |
| Telegram | `nodes-base.telegram` | output/nodes-base.telegram.md | Sends data to Telegram |
| Affinity | `nodes-base.affinity` | output/nodes-base.affinity.md | Consume Affinity API |
| AWS Lambda | `nodes-base.awsLambda` | output/nodes-base.awsLambda.md | Invoke functions on AWS Lambda |
| AWS SNS | `nodes-base.awsSns` | output/nodes-base.awsSns.md | Sends data to AWS SNS |
| AWS Certificate Manager | `nodes-base.awsCertificateManager` | output/nodes-base.awsCertificateManager.md | Sends data to AWS Certificate Manager |
| AWS Cognito | `nodes-base.awsCognito` | output/nodes-base.awsCognito.md | Sends data to AWS Cognito |
| AWS Comprehend | `nodes-base.awsComprehend` | output/nodes-base.awsComprehend.md | Sends data to Amazon Comprehend |
| AWS ELB | `nodes-base.awsElb` | output/nodes-base.awsElb.md | Sends data to AWS ELB API |
| AWS IAM | `nodes-base.awsIam` | output/nodes-base.awsIam.md | Interacts with Amazon IAM |
| AWS Rekognition | `nodes-base.awsRekognition` | output/nodes-base.awsRekognition.md | Sends data to AWS Rekognition |

#### Other Nodes (84 nodes in merged files)

| Node Name | nodeType | File Path | Start Line | Line Count | Description |
|---------|---------|---------|---------|-----|------|
| AWS SES | `nodes-base.awsSes` | output/output-merged.md | 94 | 72 | Sends data to AWS SES |
| AWS SQS | `nodes-base.awsSqs` | output/output-merged.md | 166 | 73 | Sends messages to AWS SQS |
| AWS Textract | `nodes-base.awsTextract` | output/output-merged.md | 239 | 55 | Sends data to Amazon Textract |
| AWS Transcribe | `nodes-base.awsTranscribe` | output/output-merged.md | 294 | 110 | Sends data to AWS Transcribe |
| AwsS3 | `nodes-base.awsS3` | output/output-merged.md | 404 | 66 | Sends data to AWS S3 |
| Bannerbear | `nodes-base.bannerbear` | output/output-merged.md | 470 | 89 | Consume Bannerbear API |
| Baserow | `nodes-base.baserow` | output/output-merged.md | 559 | 107 | Consume the Baserow API |
| Beeminder | `nodes-base.beeminder` | output/output-merged.md | 666 | 106 | Consume Beeminder API |
| Bitly | `nodes-base.bitly` | output/output-merged.md | 772 | 109 | Consume Bitly API |
| Brandfetch | `nodes-base.Brandfetch` | output/output-merged.md | 881 | 90 | Consume Brandfetch API |
| CircleCI | `nodes-base.circleCi` | output/output-merged.md | 971 | 94 | Consume CircleCI API |
| Clearbit | `nodes-base.clearbit` | output/output-merged.md | 1065 | 96 | Consume Clearbit API |
| ClickUp | `nodes-base.clickUp` | output/output-merged.md | 1161 | 73 | Consume ClickUp API (Beta) |
| Cockpit | `nodes-base.cockpit` | output/output-merged.md | 1234 | 102 | Consume Cockpit API |
| Coda | `nodes-base.coda` | output/output-merged.md | 1336 | 78 | Consume Coda API |
| CoinGecko | `nodes-base.coinGecko` | output/output-merged.md | 1414 | 112 | Consume CoinGecko API |
| Customer.io | `nodes-base.customerIo` | output/output-merged.md | 1526 | 76 | Consume Customer.io API |
| DebugHelper | `nodes-base.debugHelper` | output/output-merged.md | 1602 | 70 | Causes problems intentionally and genera |
| Demio | `nodes-base.demio` | output/output-merged.md | 1672 | 105 | Consume the Demio API |
| Drift | `nodes-base.drift` | output/output-merged.md | 1777 | 104 | Consume Drift API |
| E-goi | `nodes-base.egoi` | output/output-merged.md | 1881 | 112 | Consume E-goi API |
| E2E Test | `nodes-base.e2eTest` | output/output-merged.md | 1993 | 63 | Dummy node used for e2e testing |
| ERPNext | `nodes-base.erpNext` | output/output-merged.md | 2056 | 91 | Consume ERPNext API |
| Flow | `nodes-base.flow` | output/output-merged.md | 2147 | 124 | Consume Flow API |
| Freshdesk | `nodes-base.freshdesk` | output/output-merged.md | 2271 | 135 | Consume Freshdesk API |
| Home Assistant | `nodes-base.homeAssistant` | output/output-merged.md | 2406 | 62 | Consume Home Assistant API |
| HTTP Request Tool | `nodes-langchain.toolHttpRequest` | output/output-merged.md | 2468 | 90 | Makes an HTTP request and returns the re |
| HubSpot | `nodes-base.hubspot` | output/output-merged.md | 2558 | 90 | Consume HubSpot API |
| Humantic AI | `nodes-base.humanticAi` | output/output-merged.md | 2648 | 81 | Consume Humantic AI API |
| Hunter | `nodes-base.hunter` | output/output-merged.md | 2729 | 80 | Consume Hunter API |
| Intercom | `nodes-base.intercom` | output/output-merged.md | 2809 | 70 | Consume Intercom API |
| Invoice Ninja | `nodes-base.invoiceNinja` | output/output-merged.md | 2879 | 66 | Consume Invoice Ninja API |
| Jenkins | `nodes-base.jenkins` | output/output-merged.md | 2945 | 109 | Consume Jenkins API |
| Jira Software | `nodes-base.jira` | output/output-merged.md | 3054 | 82 | Consume Jira Software API |
| Linear | `nodes-base.linear` | output/output-merged.md | 3136 | 68 | Consume Linear API |
| LingvaNex | `nodes-base.lingvaNex` | output/output-merged.md | 3204 | 57 | Consume LingvaNex API |
| Mailchimp | `nodes-base.mailchimp` | output/output-merged.md | 3261 | 121 | Consume Mailchimp API |
| Mailgun | `nodes-base.mailgun` | output/output-merged.md | 3382 | 36 | Sends an email via Mailgun |
| Mailjet | `nodes-base.mailjet` | output/output-merged.md | 3418 | 72 | Consume Mailjet API |
| Mandrill | `nodes-base.mandrill` | output/output-merged.md | 3490 | 128 | Consume Mandrill API |
| Markdown | `nodes-base.markdown` | output/output-merged.md | 3618 | 91 | Convert data between Markdown and HTML |
| Matrix | `nodes-base.matrix` | output/output-merged.md | 3709 | 67 | Consume Matrix API |
| Mattermost | `nodes-base.mattermost` | output/output-merged.md | 3776 | 78 | Sends data to Mattermost |
| Mautic | `nodes-base.mautic` | output/output-merged.md | 3854 | 94 | Consume Mautic API |
| MCP Client Tool | `nodes-langchain.mcpClientTool` | output/output-merged.md | 3948 | 92 | Connect tools from an MCP Server |
| Medium | `nodes-base.medium` | output/output-merged.md | 4040 | 90 | Consume Medium API |
| MessageBird | `nodes-base.messageBird` | output/output-merged.md | 4130 | 79 | Sends SMS via MessageBird |
| Monday.com | `nodes-base.mondayCom` | output/output-merged.md | 4209 | 102 | Consume Monday.com API |
| Netscaler ADC | `nodes-base.citrixAdc` | output/output-merged.md | 4311 | 106 | Consume Netscaler ADC API |
| OpenThesaurus | `nodes-base.openThesaurus` | output/output-merged.md | 4417 | 60 | Get synonmns for German words using the  |
| Orbit | `nodes-base.orbit` | output/output-merged.md | 4477 | 76 | Consume Orbit API |
| Oura | `nodes-base.oura` | output/output-merged.md | 4553 | 71 | Consume Oura API |
| Paddle | `nodes-base.paddle` | output/output-merged.md | 4624 | 97 | Consume Paddle API |
| PagerDuty | `nodes-base.pagerDuty` | output/output-merged.md | 4721 | 66 | Consume PagerDuty API |
| PayPal | `nodes-base.payPal` | output/output-merged.md | 4787 | 90 | Consume PayPal API |
| Peekalink | `nodes-base.peekalink` | output/output-merged.md | 4877 | 58 | Consume the Peekalink API |
| ProfitWell | `nodes-base.profitWell` | output/output-merged.md | 4935 | 77 | Consume ProfitWell API |
| QuickChart | `nodes-base.quickChart` | output/output-merged.md | 5012 | 80 | Create a chart via QuickChart |
| RocketChat | `nodes-base.rocketchat` | output/output-merged.md | 5092 | 86 | Consume RocketChat API |
| Salesforce | `nodes-base.salesforce` | output/output-merged.md | 5178 | 86 | Consume Salesforce API |
| Salesmate | `nodes-base.salesmate` | output/output-merged.md | 5264 | 93 | Consume Salesmate API |
| SeaTable | `nodes-base.seaTable` | output/output-merged.md | 5357 | 82 | Read, update, write and delete data from |
| Segment | `nodes-base.segment` | output/output-merged.md | 5439 | 94 | Consume Segment API |
| Send Email | `nodes-base.emailSend` | output/output-merged.md | 5533 | 83 | Sends an email using SMTP protocol |
| Sentry.io | `nodes-base.sentryIo` | output/output-merged.md | 5616 | 58 | Consume Sentry.io API |
| ServiceNow | `nodes-base.serviceNow` | output/output-merged.md | 5674 | 76 | Consume ServiceNow API |
| Shopify | `nodes-base.shopify` | output/output-merged.md | 5750 | 94 | Consume Shopify API |
| Spontit | `nodes-base.spontit` | output/output-merged.md | 5844 | 71 | Consume Spontit API |
| Storyblok | `nodes-base.storyblok` | output/output-merged.md | 5915 | 58 | Consume Storyblok API |
| SyncroMSP | `nodes-base.syncroMsp` | output/output-merged.md | 5973 | 70 | Manage contacts, tickets and more from S |
| Todoist | `nodes-base.todoist` | output/output-merged.md | 6043 | 168 | Consume Todoist API |
| TravisCI | `nodes-base.travisCi` | output/output-merged.md | 6211 | 104 | Consume TravisCI API |
| Uplead | `nodes-base.uplead` | output/output-merged.md | 6315 | 65 | Consume Uplead API |
| uProc | `nodes-base.uproc` | output/output-merged.md | 6380 | 441 | Consume uProc API |
| UptimeRobot | `nodes-base.uptimeRobot` | output/output-merged.md | 6821 | 85 | Consume UptimeRobot API |
| Vero | `nodes-base.vero` | output/output-merged.md | 6906 | 78 | Consume Vero API |
| WhatsApp Business Cloud | `nodes-base.whatsApp` | output/output-merged.md | 6984 | 59 | Access WhatsApp API |
| WooCommerce | `nodes-base.wooCommerce` | output/output-merged.md | 7043 | 113 | Consume WooCommerce API |
| Wordpress | `nodes-base.wordpress` | output/output-merged.md | 7156 | 66 | Consume Wordpress API |
| Write Binary File | `nodes-base.writeBinaryFile` | output/output-merged.md | 7222 | 37 | Writes a binary file to disk |
| X (Formerly Twitter) | `nodes-base.twitter` | output/output-merged.md | 7259 | 49 | Consume the X API |
| Xero | `nodes-base.xero` | output/output-merged.md | 7308 | 76 | Consume Xero API |
| Zendesk | `nodes-base.zendesk` | output/output-merged.md | 7384 | 82 | Consume Zendesk API |
| Zulip | `nodes-base.zulip` | output/output-merged.md | 7466 | 82 | Consume Zulip API |

### Trigger Nodes - 108 nodes

#### High-Priority Nodes (9 individual files)

| Node Name | nodeType | File Path | Description |
|---------|---------|---------|------|
| Webhook | `nodes-base.webhook` | trigger/nodes-base.webhook.md | Starts the workflow when a webhook is called |
| ActiveCampaign Trigger | `nodes-base.activeCampaignTrigger` | trigger/nodes-base.activeCampaignTrigger.md | Handle ActiveCampaign events via webhooks |
| Acuity Scheduling Trigger | `nodes-base.acuitySchedulingTrigger` | trigger/nodes-base.acuitySchedulingTrigger.md | Handle Acuity Scheduling events via webhooks |
| Affinity Trigger | `nodes-base.affinityTrigger` | trigger/nodes-base.affinityTrigger.md | Handle Affinity events via webhooks |
| Airtable Trigger | `nodes-base.airtableTrigger` | trigger/nodes-base.airtableTrigger.md | Starts the workflow when Airtable events occur |
| AMQP Trigger | `nodes-base.amqpTrigger` | trigger/nodes-base.amqpTrigger.md | Listens to AMQP 1.0 Messages |
| Asana Trigger | `nodes-base.asanaTrigger` | trigger/nodes-base.asanaTrigger.md | Starts the workflow when Asana events occur. |
| Autopilot Trigger | `nodes-base.autopilotTrigger` | trigger/nodes-base.autopilotTrigger.md | Handle Autopilot events via webhooks |
| AWS SNS Trigger | `nodes-base.awsSnsTrigger` | trigger/nodes-base.awsSnsTrigger.md | Handle AWS SNS events via webhooks |

#### Other Nodes (99 nodes in merged files)

| Node Name | nodeType | File Path | Start Line | Line Count | Description |
|---------|---------|---------|---------|-----|------|
| Bitbucket Trigger | `nodes-base.bitbucketTrigger` | trigger/trigger-merged.md | 109 | 53 | Handle Bitbucket events via webhooks |
| Box Trigger | `nodes-base.boxTrigger` | trigger/trigger-merged.md | 162 | 83 | Starts the workflow when Box events occu |
| Brevo Trigger | `nodes-base.sendInBlueTrigger` | trigger/trigger-merged.md | 245 | 74 | Starts the workflow when Brevo events oc |
| Cal.com Trigger | `nodes-base.calTrigger` | trigger/trigger-merged.md | 319 | 61 | Handle Cal.com events via webhooks |
| Calendly Trigger | `nodes-base.calendlyTrigger` | trigger/trigger-merged.md | 380 | 52 | Starts the workflow when Calendly events |
| Chargebee Trigger | `nodes-base.chargebeeTrigger` | trigger/trigger-merged.md | 432 | 69 | Starts the workflow when Chargebee event |
| Chat Trigger | `nodes-langchain.chatTrigger` | trigger/trigger-merged.md | 501 | 114 | Runs the workflow when an n8n generated  |
| ClickUp Trigger | `nodes-base.clickUpTrigger` | trigger/trigger-merged.md | 615 | 80 | Handle ClickUp events via webhooks (Beta |
| Clockify Trigger | `nodes-base.clockifyTrigger` | trigger/trigger-merged.md | 695 | 37 | Listens to Clockify events |
| ConvertKit Trigger | `nodes-base.convertKitTrigger` | trigger/trigger-merged.md | 732 | 52 | Handle ConvertKit events via webhooks |
| Copper Trigger | `nodes-base.copperTrigger` | trigger/trigger-merged.md | 784 | 53 | Handle Copper events via webhooks |
| Cron | `nodes-base.cron` | trigger/trigger-merged.md | 837 | 38 | Triggers the workflow at a specific time |
| crowd.dev Trigger | `nodes-base.crowdDevTrigger` | trigger/trigger-merged.md | 875 | 39 | Starts the workflow when crowd.dev event |
| Customer.io Trigger | `nodes-base.customerIoTrigger` | trigger/trigger-merged.md | 914 | 69 | Starts the workflow on a Customer.io upd |
| Email Trigger (IMAP) | `nodes-base.emailReadImap` | trigger/trigger-merged.md | 983 | 61 | Triggers the workflow when a new email i |
| Emelia Trigger | `nodes-base.emeliaTrigger` | trigger/trigger-merged.md | 1044 | 42 | Handle Emelia campaign activity events v |
| Error Trigger | `nodes-base.errorTrigger` | trigger/trigger-merged.md | 1086 | 28 | Triggers the workflow when another workf |
| Eventbrite Trigger | `nodes-base.eventbriteTrigger` | trigger/trigger-merged.md | 1114 | 62 | Handle Eventbrite events via webhooks |
| Execute Workflow Trigger | `nodes-base.executeWorkflowTrigger` | trigger/trigger-merged.md | 1176 | 55 | Helpers for calling other n8n workflows. |
| Facebook Lead Ads Trigger | `nodes-base.facebookLeadAdsTrigger` | trigger/trigger-merged.md | 1231 | 45 | Handle Facebook Lead Ads events via webh |
| Facebook Trigger | `nodes-base.facebookTrigger` | trigger/trigger-merged.md | 1276 | 57 | Starts the workflow when Facebook events |
| Figma Trigger (Beta) | `nodes-base.figmaTrigger` | trigger/trigger-merged.md | 1333 | 41 | Starts the workflow when Figma events oc |
| Flow Trigger | `nodes-base.flowTrigger` | trigger/trigger-merged.md | 1374 | 41 | Handle Flow events via webhooks |
| Form.io Trigger | `nodes-base.formIoTrigger` | trigger/trigger-merged.md | 1415 | 40 | Handle form.io events via webhooks |
| Formstack Trigger | `nodes-base.formstackTrigger` | trigger/trigger-merged.md | 1455 | 39 | Starts the workflow on a Formstack form  |
| GetResponse Trigger | `nodes-base.getResponseTrigger` | trigger/trigger-merged.md | 1494 | 54 | Starts the workflow when GetResponse eve |
| Github Trigger | `nodes-base.githubTrigger` | trigger/trigger-merged.md | 1548 | 96 | Starts the workflow when Github events o |
| GitLab Trigger | `nodes-base.gitlabTrigger` | trigger/trigger-merged.md | 1644 | 59 | Starts the workflow when GitLab events o |
| Gmail Trigger | `nodes-base.gmailTrigger` | trigger/trigger-merged.md | 1703 | 62 | Fetches emails from Gmail and starts the |
| Google Business Profile Trigger | `nodes-base.googleBusinessProfileTrigger` | trigger/trigger-merged.md | 1765 | 38 | Fetches reviews from Google Business Pro |
| Google Calendar Trigger | `nodes-base.googleCalendarTrigger` | trigger/trigger-merged.md | 1803 | 47 | Starts the workflow when Google Calendar |
| Google Drive Trigger | `nodes-base.googleDriveTrigger` | trigger/trigger-merged.md | 1850 | 83 | Starts the workflow when Google Drive ev |
| Google Sheets Trigger | `nodes-base.googleSheetsTrigger` | trigger/trigger-merged.md | 1933 | 67 | Starts the workflow when Google Sheets e |
| Gumroad Trigger | `nodes-base.gumroadTrigger` | trigger/trigger-merged.md | 2000 | 42 | Handle Gumroad events via webhooks |
| Help Scout Trigger | `nodes-base.helpScoutTrigger` | trigger/trigger-merged.md | 2042 | 47 | Starts the workflow when Help Scout even |
| HubSpot Trigger | `nodes-base.hubspotTrigger` | trigger/trigger-merged.md | 2089 | 42 | Starts the workflow when HubSpot events  |
| Interval | `nodes-base.interval` | trigger/trigger-merged.md | 2131 | 41 | Triggers the workflow in a given interva |
| Invoice Ninja Trigger | `nodes-base.invoiceNinjaTrigger` | trigger/trigger-merged.md | 2172 | 54 | Starts the workflow when Invoice Ninja e |
| Jira Trigger | `nodes-base.jiraTrigger` | trigger/trigger-merged.md | 2226 | 103 | Starts the workflow when Jira events occ |
| Jotform Trigger | `nodes-base.jotFormTrigger` | trigger/trigger-merged.md | 2329 | 31 | Handle Jotform events via webhooks |
| Kafka Trigger | `nodes-base.kafkaTrigger` | trigger/trigger-merged.md | 2360 | 50 | Consume messages from a Kafka topic |
| Keap Trigger | `nodes-base.keapTrigger` | trigger/trigger-merged.md | 2410 | 30 | Starts the workflow when Infusionsoft ev |
| KoBoToolbox Trigger | `nodes-base.koBoToolboxTrigger` | trigger/trigger-merged.md | 2440 | 49 | Process KoBoToolbox submissions |
| Lemlist Trigger | `nodes-base.lemlistTrigger` | trigger/trigger-merged.md | 2489 | 90 | Handle Lemlist events via webhooks |
| Linear Trigger | `nodes-base.linearTrigger` | trigger/trigger-merged.md | 2579 | 50 | Starts the workflow when Linear events o |
| Local File Trigger | `nodes-base.localFileTrigger` | trigger/trigger-merged.md | 2629 | 62 | Triggers a workflow on file system chang |
| LoneScale Trigger | `nodes-base.loneScaleTrigger` | trigger/trigger-merged.md | 2691 | 29 | Trigger LoneScale Workflow |
| Mailchimp Trigger | `nodes-base.mailchimpTrigger` | trigger/trigger-merged.md | 2720 | 61 | Handle Mailchimp events via webhooks |
| MailerLite Trigger | `nodes-base.mailerLiteTrigger` | trigger/trigger-merged.md | 2781 | 47 | Starts the workflow when MailerLite even |
| Mailjet Trigger | `nodes-base.mailjetTrigger` | trigger/trigger-merged.md | 2828 | 43 | Handle Mailjet events via webhooks |
| Manual Chat Trigger | `nodes-langchain.manualChatTrigger` | trigger/trigger-merged.md | 2871 | 29 | Runs the flow on new manual chat message |
| Manual Trigger | `nodes-base.manualTrigger` | trigger/trigger-merged.md | 2900 | 28 | Runs the flow on clicking a button in n8 |
| Mautic Trigger | `nodes-base.mauticTrigger` | trigger/trigger-merged.md | 2928 | 47 | Handle Mautic events via webhooks |
| MCP Server Trigger | `nodes-langchain.mcpTrigger` | trigger/trigger-merged.md | 2975 | 41 | Expose n8n tools as an MCP Server endpoi |
| Microsoft OneDrive Trigger | `nodes-base.microsoftOneDriveTrigger` | trigger/trigger-merged.md | 3016 | 76 | Trigger for Microsoft OneDrive API. |
| Microsoft Outlook Trigger | `nodes-base.microsoftOutlookTrigger` | trigger/trigger-merged.md | 3092 | 96 | Fetches emails from Microsoft Outlook an |
| Microsoft Teams Trigger | `nodes-base.microsoftTeamsTrigger` | trigger/trigger-merged.md | 3188 | 48 | Triggers workflows in n8n based on event |
| MQTT Trigger | `nodes-base.mqttTrigger` | trigger/trigger-merged.md | 3236 | 39 | Listens to MQTT events |
| n8n Form Trigger | `nodes-base.formTrigger` | trigger/trigger-merged.md | 3275 | 80 | Generate webforms in n8n and pass their  |
| n8n Trigger | `nodes-base.n8nTrigger` | trigger/trigger-merged.md | 3355 | 39 | Handle events and perform actions on you |
| Netlify Trigger | `nodes-base.netlifyTrigger` | trigger/trigger-merged.md | 3394 | 42 | Handle netlify events via webhooks |
| Notion Trigger | `nodes-base.notionTrigger` | trigger/trigger-merged.md | 3436 | 40 | Starts the workflow when Notion events o |
| Onfleet Trigger | `nodes-base.onfleetTrigger` | trigger/trigger-merged.md | 3476 | 58 | Starts the workflow when Onfleet events  |
| PayPal Trigger | `nodes-base.payPalTrigger` | trigger/trigger-merged.md | 3534 | 29 | Handle PayPal events via webhooks |
| Pipedrive Trigger | `nodes-base.pipedriveTrigger` | trigger/trigger-merged.md | 3563 | 137 | Starts the workflow when Pipedrive event |
| Postgres Trigger | `nodes-base.postgresTrigger` | trigger/trigger-merged.md | 3700 | 64 | Listens to Postgres messages |
| Postmark Trigger | `nodes-base.postmarkTrigger` | trigger/trigger-merged.md | 3764 | 45 | Starts the workflow when Postmark events |
| Pushcut Trigger | `nodes-base.pushcutTrigger` | trigger/trigger-merged.md | 3809 | 29 | Starts the workflow when Pushcut events  |
| RabbitMQ Trigger | `nodes-base.rabbitmqTrigger` | trigger/trigger-merged.md | 3838 | 50 | Listens to RabbitMQ messages |
| Redis Trigger | `nodes-base.redisTrigger` | trigger/trigger-merged.md | 3888 | 38 | Subscribe to redis channel |
| RSS Feed Trigger | `nodes-base.rssFeedReadTrigger` | trigger/trigger-merged.md | 3926 | 28 | Starts a workflow when an RSS feed is up |
| Salesforce Trigger | `nodes-base.salesforceTrigger` | trigger/trigger-merged.md | 3954 | 56 | Fetches data from Salesforce and starts  |
| Schedule Trigger | `nodes-base.scheduleTrigger` | trigger/trigger-merged.md | 4010 | 36 | Triggers the workflow on a given schedul |
| SeaTable Trigger | `nodes-base.seaTableTrigger` | trigger/trigger-merged.md | 4046 | 49 | Starts the workflow when SeaTable events |
| Shopify Trigger | `nodes-base.shopifyTrigger` | trigger/trigger-merged.md | 4095 | 102 | Handle Shopify events via webhooks |
| Simulate Trigger | `nodes-base.simulateTrigger` | trigger/trigger-merged.md | 4197 | 31 | Simulate a trigger node |
| Slack Trigger | `nodes-base.slackTrigger` | trigger/trigger-merged.md | 4228 | 56 | Handle Slack events via webhooks |
| SSE Trigger | `nodes-base.sseTrigger` | trigger/trigger-merged.md | 4284 | 28 | Triggers the workflow when Server-Sent E |
| Strava Trigger | `nodes-base.stravaTrigger` | trigger/trigger-merged.md | 4312 | 54 | Starts the workflow when Strava events o |
| Stripe Trigger | `nodes-base.stripeTrigger` | trigger/trigger-merged.md | 4366 | 188 | Handle Stripe events via webhooks |
| SurveyMonkey Trigger | `nodes-base.surveyMonkeyTrigger` | trigger/trigger-merged.md | 4554 | 79 | Starts the workflow when Survey Monkey e |
| Taiga Trigger | `nodes-base.taigaTrigger` | trigger/trigger-merged.md | 4633 | 55 | Handle Taiga events via webhook |
| Telegram Trigger | `nodes-base.telegramTrigger` | trigger/trigger-merged.md | 4688 | 56 | Starts the workflow on a Telegram update |
| TheHive 5 Trigger | `nodes-base.theHiveProjectTrigger` | trigger/trigger-merged.md | 4744 | 72 | Starts the workflow when TheHive events  |
| TheHive Trigger | `nodes-base.theHiveTrigger` | trigger/trigger-merged.md | 4816 | 75 | Starts the workflow when TheHive events  |
| Toggl Trigger | `nodes-base.togglTrigger` | trigger/trigger-merged.md | 4891 | 36 | Starts the workflow when Toggl events oc |
| Trello Trigger | `nodes-base.trelloTrigger` | trigger/trigger-merged.md | 4927 | 29 | Starts the workflow when Trello events o |
| Twilio Trigger | `nodes-base.twilioTrigger` | trigger/trigger-merged.md | 4956 | 38 | Starts the workflow on a Twilio update |
| Typeform Trigger | `nodes-base.typeformTrigger` | trigger/trigger-merged.md | 4994 | 40 | Starts the workflow on a Typeform form s |
| Venafi TLS Protect Cloud Trigger | `nodes-base.venafiTlsProtectCloudTrigger` | trigger/trigger-merged.md | 5034 | 30 | Starts the workflow when Venafi events o |
| Webex by Cisco Trigger | `nodes-base.ciscoWebexTrigger` | trigger/trigger-merged.md | 5064 | 136 | Starts the workflow when Cisco Webex eve |
| Webflow Trigger | `nodes-base.webflowTrigger` | trigger/trigger-merged.md | 5200 | 44 | Handle Webflow events via webhooks |
| WhatsApp Trigger | `nodes-base.whatsAppTrigger` | trigger/trigger-merged.md | 5244 | 52 | Handle WhatsApp events via webhooks |
| Wise Trigger | `nodes-base.wiseTrigger` | trigger/trigger-merged.md | 5296 | 40 | Handle Wise events via webhooks |
| WooCommerce Trigger | `nodes-base.wooCommerceTrigger` | trigger/trigger-merged.md | 5336 | 49 | Handle WooCommerce events via webhooks |
| Workable Trigger | `nodes-base.workableTrigger` | trigger/trigger-merged.md | 5385 | 44 | Starts the workflow when Workable events |
| Workflow Trigger | `nodes-base.workflowTrigger` | trigger/trigger-merged.md | 5429 | 39 | Triggers based on various lifecycle even |
| Wufoo Trigger | `nodes-base.wufooTrigger` | trigger/trigger-merged.md | 5468 | 30 | Handle Wufoo events via webhooks |
| Zendesk Trigger | `nodes-base.zendeskTrigger` | trigger/trigger-merged.md | 5498 | 58 | Handle Zendesk events via webhooks |

### Organization Nodes - 4 nodes

#### Other Nodes (4 nodes in merged files)

| Node Name | nodeType | File Path | Start Line | Line Count | Description |
|---------|---------|---------|---------|-----|------|
| No Operation, do nothing | `nodes-base.noOp` | organization/organization-merged.md | 14 | 20 | No Operation |
| Simulate | `nodes-base.simulate` | organization/organization-merged.md | 34 | 42 | Simulate a node |
| Split In Batches | `nodes-base.splitInBatches` | organization/organization-merged.md | 76 | 37 | Split data into batches and iterate over |
| Wait | `nodes-base.wait` | organization/organization-merged.md | 113 | 109 | Wait before continue with execution |

### Miscellaneous Nodes - 1 nodes

#### Other Nodes (1 nodes in merged files)

| Node Name | nodeType | File Path | Start Line | Line Count | Description |
|---------|---------|---------|---------|-----|------|
| EvaluationTrigger.node.ee.js | `nodes-base.` | misc/misc-merged.md | 11 | 15 |  |

---

## Community Packages

Popular community-developed node packages (30 packages).

| Package Name | Category | File Path | Description |
|--------------|----------|-----------|-------------|
| n8n-nodes-evolution-api | Communication | community/n8n-nodes-evolution-api.md | A Evolution API é um hub de canais com foco no Wha |
| n8n-nodes-kommo | Utilities | community/n8n-nodes-kommo.md | n8n node for Kommo Api |
| n8n-nodes-mcp | AI Tools | community/n8n-nodes-mcp.md | MCP nodes for n8n  |
| n8n-nodes-elevenlabs | AI Tools | community/n8n-nodes-elevenlabs.md | Complete implementation of ElevenLabs AI voice gen |
| n8n-nodes-pdfkit | Document | community/n8n-nodes-pdfkit.md | Node for using PDFKit to tranform images into PDF, |
| n8n-nodes-chatwoot | Communication | community/n8n-nodes-chatwoot.md | This is an n8n community node. It lets you use Cha |
| @elevenlabs/n8n-nodes-elevenlabs | AI Tools | community/elevenlabs-n8n-nodes-elevenlabs.md | Official ElevenLabs node for n8n |
| n8n-nodes-globals | Utilities | community/n8n-nodes-globals.md | N8N community node that allows users to create glo |
| n8n-nodes-powerbi | Utilities | community/n8n-nodes-powerbi.md | n8n nodes for integration with Power BI APIs |
| n8n-nodes-evolution-api-media-downloader | Communication | community/n8n-nodes-evolution-api-media-downloader.md | Download Media from Evolution API data message |
| n8n-nodes-text-manipulation | Data Processing | community/n8n-nodes-text-manipulation.md | This node allows to modify texts. |
| n8n-nodes-datastore | Data Processing | community/n8n-nodes-datastore.md | Datastore for n8n within the workflow |
| @apify/n8n-nodes-apify | Utilities | community/apify-n8n-nodes-apify.md | n8n nodes for Apify |
| @mendable/n8n-nodes-firecrawl | Web Scraping | community/mendable-n8n-nodes-firecrawl.md | Firecrawl node for n8n |
| n8n-nodes-zohozeptomail | AI Tools | community/n8n-nodes-zohozeptomail.md | This is an n8n community node. It lets you use Zoh |
| @tavily/core | Utilities | community/tavily-core.md | Official JavaScript library for Tavily. |
| n8n-nodes-cronlytic | Utilities | community/n8n-nodes-cronlytic.md | n8n community node for Cronlytic advanced cron sch |
| @splainez/n8n-nodes-phonenumber-parser | AI Tools | community/splainez-n8n-nodes-phonenumber-parser.md | Parse a phone number and return its information |
| n8n-nodes-serpapi | Web Scraping | community/n8n-nodes-serpapi.md | Official n8n node for SerpApi |
| n8n-nodes-n8ntools-uazapi | Communication | community/n8n-nodes-n8ntools-uazapi.md | N8N Tools - Uazapi: Complete Uazapi integration -  |
| @reportei/n8n-nodes-reportei | Utilities | community/reportei-n8n-nodes-reportei.md | n8n nodes for integrating with Reportei |
| @devlikeapro/n8n-nodes-chatwoot | Communication | community/devlikeapro-n8n-nodes-chatwoot.md | n8n node to connect with ChatWoot |
| n8n-nodes-instagram-integrations | Utilities | community/n8n-nodes-instagram-integrations.md | N8N nodes for Instagram API integration with OAuth |
| n8n-nodes-megaapi | Communication | community/n8n-nodes-megaapi.md | N8N Community Node for MegaAPI WhatsApp automation |
| n8n-nodes-tavily | AI Tools | community/n8n-nodes-tavily.md | Tavily is a search engine tailored for AI agents,  |
| @watzon/n8n-nodes-perplexity | AI Tools | community/watzon-n8n-nodes-perplexity.md | n8n node to interact with the Perplexity AI API |
| @brave/n8n-nodes-brave-search | Web Scraping | community/brave-n8n-nodes-brave-search.md | A n8n node for the Brave Search API |
| n8n-nodes-youtube-transcription-kasha | Utilities | community/n8n-nodes-youtube-transcription-kasha.md | A custom n8n node for fetching YouTube video trans |
| @tavily/n8n-nodes-tavily | Web Scraping | community/tavily-n8n-nodes-tavily.md | A community node for n8n to integrate Tavily API f |
| n8n-nodes-pdforge | AI Tools | community/n8n-nodes-pdforge.md | pdf noodle (previously pdforge) automates PDF Gene |

For detailed information, see [community/README.md](community/README.md).

---

## Template Index

Popular workflow templates are located in the `templates/` directory, categorized by functionality:

- [AI & Chatbots](templates/ai-chatbots/) - AI agents, chatbot-related templates
- [Social Media](templates/social-media/) - Social media automation templates
- [Data Processing](templates/data-processing/) - Data transformation and processing templates
- [Communication](templates/communication/) - Communication tool integration templates

For detailed template lists, please refer to the README.md file in each subdirectory.

---

## Statistics

- Total built-in nodes: 545
- High-priority nodes: 50 (individual files)
- Low-priority nodes: 495 (merged files)
- Merged file count: 8
- Community packages: 30

### Nodes by Category

- Data Transformation Nodes: 223 nodes (high-priority: 15, other: 208)
- Input Nodes: 110 nodes (high-priority: 11, other: 99)
- Output Nodes: 99 nodes (high-priority: 15, other: 84)
- Trigger Nodes: 108 nodes (high-priority: 9, other: 99)
- Organization Nodes: 4 nodes (high-priority: 0, other: 4)
- Miscellaneous Nodes: 1 nodes (high-priority: 0, other: 1)

- Last updated: 2025-12-30
