# Local Chatbot with Retrieval Augmented Generation (RAG)
> **Category**: AI & Chatbots
> **Views**: 28,717
> **Created**: 6/23/2025
## Description
Build a 100% local RAG with n8n, Ollama and Qdrant. This agent uses a semantic database (Qdrant) to answer questions about PDF files.

Tutorial

Click here to view the YouTube Tutorial

How it works
Build a chatbot that answers based on documents you provide it (Retrieval Augmented Generation). You can upload as many PDF files as you want to the Qdrant database. The chatbot will use its retrieval tool to fetch the chunks and use them to answer questions.

Installation
Install n8n + Ollama + Qdrant using the Self-hosted AI starter kit
Make sure to install Llama 3.2 and mxbai-embed-large as embeddings model.

How to use it
First run the "Data Ingestion" part and upload as many PDF files as you want
Run the Chatbot and start asking questions about the documents you uploaded

## Workflow Structure
# Local Chatbot with Retrieval Augmented Generation (RAG)

## Basic Information

- Node count: 11
- Connection count: 9

## Key Nodes

### Triggers
- On form submission (`n8n-nodes-base.formTrigger`)
- When chat message received (`@n8n/n8n-nodes-langchain.chatTrigger`)

### AI Nodes
- Qdrant Vector Store (`@n8n/n8n-nodes-langchain.vectorStoreQdrant`)
- Embeddings Ollama (`@n8n/n8n-nodes-langchain.embeddingsOllama`)
- Default Data Loader (`@n8n/n8n-nodes-langchain.documentDefaultDataLoader`)
- Recursive Character Text Splitter (`@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`)
- AI Agent (`@n8n/n8n-nodes-langchain.agent`)
- Ollama Chat Model (`@n8n/n8n-nodes-langchain.lmChatOllama`)
- Simple Memory (`@n8n/n8n-nodes-langchain.memoryBufferWindow`)
- Qdrant Vector Store1 (`@n8n/n8n-nodes-langchain.vectorStoreQdrant`)
- Embeddings Ollama1 (`@n8n/n8n-nodes-langchain.embeddingsOllama`)

## All Nodes

| Node Name | Type | Category |
|-----------|------|----------|
| On form submission | `n8n-nodes-base.formTrigger` | Trigger |
| Qdrant Vector Store | `@n8n/n8n-nodes-langchain.vectorStoreQdrant` | AI |
| Embeddings Ollama | `@n8n/n8n-nodes-langchain.embeddingsOllama` | AI |
| Default Data Loader | `@n8n/n8n-nodes-langchain.documentDefaultDataLoader` | AI |
| Recursive Character Text Splitter | `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter` | AI |
| When chat message received | `@n8n/n8n-nodes-langchain.chatTrigger` | Trigger |
| AI Agent | `@n8n/n8n-nodes-langchain.agent` | AI |
| Ollama Chat Model | `@n8n/n8n-nodes-langchain.lmChatOllama` | AI |
| Simple Memory | `@n8n/n8n-nodes-langchain.memoryBufferWindow` | AI |
| Qdrant Vector Store1 | `@n8n/n8n-nodes-langchain.vectorStoreQdrant` | AI |
| Embeddings Ollama1 | `@n8n/n8n-nodes-langchain.embeddingsOllama` | AI |

## Connections

```
Simple Memory --[ai_memory]--> AI Agent
Embeddings Ollama --[ai_embedding]--> Qdrant Vector Store
Ollama Chat Model --[ai_languageModel]--> AI Agent
Embeddings Ollama1 --[ai_embedding]--> Qdrant Vector Store1
On form submission --[main]--> Qdrant Vector Store
Default Data Loader --[ai_document]--> Qdrant Vector Store
Qdrant Vector Store1 --[ai_tool]--> AI Agent
When chat message received --[main]--> AI Agent
Recursive Character Text Splitter --[ai_textSplitter]--> Default Data Loader
```

## Workflow Summary

This workflow is triggered by On form submission, When chat message received, uses Qdrant Vector Store, Embeddings Ollama, Default Data Loader, Recursive Character Text Splitter, AI Agent, Ollama Chat Model, Simple Memory, Qdrant Vector Store1, Embeddings Ollama1 for AI processing.
## Author Information
- **Name**: Thomas Janssen
- **Username**: @thomasjanssen-tech
- Verified user
## Related Links
- [View this template on n8n.io](https://n8n.io/workflows/5148)
## Complete Workflow JSON
<details>
<summary>Click to expand Workflow JSON</summary>
```json
{
  "id": 5148,
  "meta": {
    "instanceId": "558d88703fb65b2d0e44613bc35916258b0f0bf983c5d4730c00c424b77ca36a",
    "templateCredsSetupCompleted": true
  },
  "name": "Local Chatbot with Retrieval Augmented Generation (RAG)",
  "tags": [],
  "nodes": [
    {
      "id": "a00e5b5b-1cc1-4272-9790-8ffde3c92efb",
      "name": "On form submission",
      "type": "n8n-nodes-base.formTrigger",
      "position": [
        0,
        0
      ],
      "webhookId": "4e1e20d4-f759-42c8-8439-87b93f43aa7c",
      "parameters": {
        "options": {},
        "formTitle": "Add your file here",
        "formFields": {
          "values": [
            {
              "fieldType": "file",
              "fieldLabel": "File",
              "requiredField": true,
              "acceptFileTypes": ".pdf"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "1218186e-a93e-4e05-b47e-a395f28cf5f9",
      "name": "Qdrant Vector Store",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreQdrant",
      "position": [
        220,
        0
      ],
      "parameters": {
        "mode": "insert",
        "options": {},
        "qdrantCollection": {
          "__rl": true,
          "mode": "id",
          "value": "rag_collection"
        }
      },
      "credentials": {
        "qdrantApi": {
          "id": "sFfERYppMeBnFNeA",
          "name": "Local QdrantApi database"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "9c7fb858-b571-4626-b976-d3e1995c464b",
      "name": "Embeddings Ollama",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOllama",
      "position": [
        60,
        220
      ],
      "parameters": {
        "model": "mxbai-embed-large:latest"
      },
      "credentials": {
        "ollamaApi": {
          "id": "xHuYe0MDGOs9IpBW",
          "name": "Local Ollama service"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "af14443b-ae01-48dc-8552-5ded7a27fce2",
      "name": "Default Data Loader",
      "type": "@n8n/n8n-nodes-langchain.documentDefaultDataLoader",
      "position": [
        360,
        220
      ],
      "parameters": {
        "options": {},
        "dataType": "binary"
      },
      "typeVersion": 1
    },
    {
      "id": "660380c5-63da-4404-98e6-f9c0ee9aaa90",
      "name": "Recursive Character Text Splitter",
      "type": "@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter",
      "position": [
        460,
        440
      ],
      "parameters": {
        "options": {},
        "chunkSize": 200,
        "chunkOverlap": 50
      },
      "typeVersion": 1
    },
    {
      "id": "49dbe387-751f-4a2e-8803-290bc2c06ec5",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -140,
        -100
      ],
      "parameters": {
        "color": 3,
        "width": 840,
        "height": 700,
        "content": "## Data Ingestion\n**Add data to the semantic database"
      },
      "typeVersion": 1
    },
    {
      "id": "45683271-af59-41d0-9e69-af721d566661",
      "name": "When chat message received",
      "type": "@n8n/n8n-nodes-langchain.chatTrigger",
      "position": [
        940,
        -20
      ],
      "webhookId": "5e56a263-3a40-44bd-bc9d-1cfb3bc2a87d",
      "parameters": {
        "options": {}
      },
      "typeVersion": 1.1
    },
    {
      "id": "af562588-2e8c-4c0b-b041-d6fc8c0affd0",
      "name": "AI Agent",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [
        1220,
        -20
      ],
      "parameters": {
        "options": {
          "systemMessage": "You are a helpful assistant. You have access to a tool to retrieve data from a semantic database to answer questions. Always provide arguments when you execute the tool"
        }
      },
      "typeVersion": 2
    },
    {
      "id": "4d924b4a-fe07-4606-8385-613d6ea14991",
      "name": "Ollama Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOllama",
      "position": [
        1060,
        220
      ],
      "parameters": {
        "options": {}
      },
      "credentials": {
        "ollamaApi": {
          "id": "xHuYe0MDGOs9IpBW",
          "name": "Local Ollama service"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "de87b7bb-6fec-4d8f-a77a-25bc3a30a038",
      "name": "Simple Memory",
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "position": [
        1260,
        220
      ],
      "parameters": {},
      "typeVersion": 1.3
    },
    {
      "id": "16261539-5218-4df1-8b14-915dd3377167",
      "name": "Qdrant Vector Store1",
      "type": "@n8n/n8n-nodes-langchain.vectorStoreQdrant",
      "position": [
        1540,
        240
      ],
      "parameters": {
        "mode": "retrieve-as-tool",
        "options": {},
        "toolName": "retriever",
        "toolDescription": "Retrieve data from a semantic database to answer questions",
        "qdrantCollection": {
          "__rl": true,
          "mode": "id",
          "value": "rag_collection"
        }
      },
      "credentials": {
        "qdrantApi": {
          "id": "sFfERYppMeBnFNeA",
          "name": "Local QdrantApi database"
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "57d3be1d-73cd-4464-a3f3-7dd4a3157cdf",
      "name": "Embeddings Ollama1",
      "type": "@n8n/n8n-nodes-langchain.embeddingsOllama",
      "position": [
        1460,
        440
      ],
      "parameters": {
        "model": "mxbai-embed-large:latest"
      },
      "credentials": {
        "ollamaApi": {
          "id": "xHuYe0MDGOs9IpBW",
          "name": "Local Ollama service"
        }
      },
      "typeVersion": 1
    },
    {
      "id": "5919cc58-05f4-42c8-aada-3782a16574d9",
      "name": "Sticky Note1",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        740,
        -100
      ],
      "parameters": {
        "color": 4,
        "width": 1200,
        "height": 700,
        "content": "## RAG Chatbot\n**Chat with your data"
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "895c0261-fbf5-4bb6-9581-4cea3c4d20bd",
  "connections": {
    "Simple Memory": {
      "ai_memory": [
        [
          {
            "node": "AI Agent",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings Ollama": {
      "ai_embedding": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "Ollama Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Embeddings Ollama1": {
      "ai_embedding": [
        [
          {
            "node": "Qdrant Vector Store1",
            "type": "ai_embedding",
            "index": 0
          }
        ]
      ]
    },
    "On form submission": {
      "main": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Default Data Loader": {
      "ai_document": [
        [
          {
            "node": "Qdrant Vector Store",
            "type": "ai_document",
            "index": 0
          }
        ]
      ]
    },
    "Qdrant Vector Store1": {
      "ai_tool": [
        [
          {
            "node": "AI Agent",
            "type": "ai_tool",
            "index": 0
          }
        ]
      ]
    },
    "When chat message received": {
      "main": [
        [
          {
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Recursive Character Text Splitter": {
      "ai_textSplitter": [
        [
          {
            "node": "Default Data Loader",
            "type": "ai_textSplitter",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
</details>