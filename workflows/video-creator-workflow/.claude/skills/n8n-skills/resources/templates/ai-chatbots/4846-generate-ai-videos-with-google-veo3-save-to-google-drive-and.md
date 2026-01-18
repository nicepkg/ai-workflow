# Generate AI Videos with Google Veo3, Save to Google Drive and Upload to YouTube
> **Category**: AI & Chatbots
> **Views**: 155,914
> **Created**: 6/10/2025
## Description
This workflow allows users to generate AI videos using Google Veo3, save them to Google Drive, generate optimized YouTube titles with GPT-4o, and automatically upload them to YouTube with Upload-Post. The entire process is triggered from a Google Sheet that acts as the central interface for input and output.

IT automates video creation, uploading, and tracking, ensuring seamless integration between Google Sheets, Google Drive, Google Veo3, and YouTube.

Benefits of this Workflow

💡 No Code Interface**: Trigger and control the video production pipeline from a simple Google Sheet.
⚙️ Full Automation**: Once set up, the entire video generation and publishing process runs hands-free.
🧠 AI-Powered Creativity**:

  Generates engaging YouTube titles using GPT-4o.
  Leverages advanced generative video AI from Google Veo3.
📁 Cloud Storage & Backup**: Stores all generated videos on Google Drive for safekeeping.
📈 YouTube Ready**: Automatically uploads to YouTube with correct metadata, saving time and boosting visibility.
🧪 Scalable**: Designed to process multiple video prompts by looping through new entries in Google Sheets.
🔒 API-First**: Utilizes secure API-based communication for all services.

How It Works  
Trigger: The workflow can be started manually ("When clicking ‘Test workflow’") or scheduled ("Schedule Trigger") to run at regular intervals (e.g., every 5 minutes).  
Fetch Data: The "Get new video" node retrieves unfilled video requests from a Google Sheet (rows where the "VIDEO" column is empty).  
Video Creation:  
   The "Set data" node formats the prompt and duration from the Google Sheet.  
   The "Create Video" node sends a request to the Fal.run API (Google Veo3) to generate a video based on the prompt.  
Status Check:  
   The "Wait 60 sec." node pauses execution for 60 seconds.  
   The "Get status" node checks the video generation status. If the status is "COMPLETED," the workflow proceeds; otherwise, it waits again.  
Video Processing:  
   The "Get Url Video" node fetches the video URL.  
   The "Generate title" node uses OpenAI (GPT-4.1) to create an SEO-optimized YouTube title.  
   The "Get File Video" node downloads the video file.  
Upload & Update:  
   The "Upload Video" node saves the video to Google Drive.  
   The "HTTP Request" node uploads the video to YouTube via the Upload-Post API.  
   The "Update Youtube URL" and "Update result" nodes update the Google Sheet with the video URL and YouTube link.  

Set Up Steps  
Google Sheet Setup:  
   Create a Google Sheet with columns: PROMPT, DURATION, VIDEO, and YOUTUBE_URL.  
   Share the Sheet link in the "Get new video" node.  

API Keys:  
   Obtain a Fal.run API key (for Veo3) and set it in the "Create Video" node (Header: Authorization: Key YOURAPIKEY).  
   Get an Upload-Post API key (for YouTube uploads) and configure the "HTTP Request" node (Header: Authorization: Apikey YOUR_API_KEY).  

YouTube Upload Configuration:  
   Replace YOUR_USERNAME in the "HTTP Request" node with your Upload-Post profile name.  

Schedule Trigger:  
   Configure the "Schedule Trigger" node to run periodically (e.g., every 5 minutes).  

Need help customizing?  
Contact me for consulting and support or add me on Linkedin. 
## Workflow Structure
# Generate AI Videos with Google Veo3, Save to Google Drive and Upload to YouTube

## Basic Information

- Node count: 15
- Connection count: 14

## Key Nodes

### Triggers
- When clicking ‘Test workflow’ (`n8n-nodes-base.manualTrigger`)
- Schedule Trigger (`n8n-nodes-base.scheduleTrigger`)

### AI Nodes
- Generate title (`@n8n/n8n-nodes-langchain.openAi`)

## All Nodes

| Node Name | Type | Category |
|-----------|------|----------|
| When clicking ‘Test workflow’ | `n8n-nodes-base.manualTrigger` | Trigger |
| Get status | `n8n-nodes-base.httpRequest` | Output |
| Wait 60 sec. | `n8n-nodes-base.wait` | Other |
| Schedule Trigger | `n8n-nodes-base.scheduleTrigger` | Trigger |
| Completed? | `n8n-nodes-base.if` | Transform |
| Update result | `n8n-nodes-base.googleSheets` | Input |
| Set data | `n8n-nodes-base.set` | Transform |
| Get new video | `n8n-nodes-base.googleSheets` | Input |
| Create Video | `n8n-nodes-base.httpRequest` | Output |
| Get Url Video | `n8n-nodes-base.httpRequest` | Output |
| Get File Video | `n8n-nodes-base.httpRequest` | Output |
| Upload Video | `n8n-nodes-base.googleDrive` | Input |
| HTTP Request | `n8n-nodes-base.httpRequest` | Output |
| Generate title | `@n8n/n8n-nodes-langchain.openAi` | AI |
| Update Youtube URL | `n8n-nodes-base.googleSheets` | Input |

## Connections

```
Set data --[main]--> Create Video
Completed? --[main]--> Get Url Video
Completed? --[main]--> Wait 60 sec.
Get status --[main]--> Completed?
Create Video --[main]--> Wait 60 sec.
HTTP Request --[main]--> Update Youtube URL
Upload Video --[main]--> Update result
Wait 60 sec. --[main]--> Get status
Get Url Video --[main]--> Generate title
Get new video --[main]--> Set data
Generate title --[main]--> Get File Video
Get File Video --[main]--> Upload Video
Get File Video --[main]--> HTTP Request
When clicking ‘Test workflow’ --[main]--> Get new video
```

## Workflow Summary

This workflow is triggered by When clicking ‘Test workflow’, Schedule Trigger, uses Generate title for AI processing, goes through 2 transformation step(s), finally outputs to Get status, Create Video, Get Url Video, Get File Video, HTTP Request.
## Author Information
- **Name**: Davide
- **Username**: @n3witalia
- Verified user
## Related Links
- [View this template on n8n.io](https://n8n.io/workflows/4846)
## Complete Workflow JSON
<details>
<summary>Click to expand Workflow JSON</summary>
```json
{
  "id": 4846,
  "meta": {
    "instanceId": "a4bfc93e975ca233ac45ed7c9227d84cf5a2329310525917adaf3312e10d5462",
    "templateCredsSetupCompleted": true
  },
  "name": "Generate AI Videos with Google Veo3, Save to Google Drive and Upload to YouTube",
  "tags": [],
  "nodes": [
    {
      "id": "f1fcb9ab-37aa-44a3-91fc-8480351aa5cd",
      "name": "When clicking ‘Test workflow’",
      "type": "n8n-nodes-base.manualTrigger",
      "position": [
        -220,
        840
      ],
      "parameters": {},
      "typeVersion": 1
    },
    {
      "id": "58194812-a64d-401e-be5e-2f1ba9210557",
      "name": "Get status",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        840,
        840
      ],
      "parameters": {
        "url": "=https://queue.fal.run/fal-ai/veo3/requests/{{ $('Create Video').item.json.request_id }}/status ",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "daOZafXpRXLtoLUV",
          "name": "Fal.run API"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "1e23339c-f829-4426-b4f6-b02add8f8c5e",
      "name": "Wait 60 sec.",
      "type": "n8n-nodes-base.wait",
      "position": [
        660,
        840
      ],
      "webhookId": "490facb8-d0ae-402e-ab59-a87720cf0bdd",
      "parameters": {
        "amount": 60
      },
      "typeVersion": 1.1
    },
    {
      "id": "98ad8a6d-9ded-4f4e-a4ef-b624f7fe7e39",
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [
        -220,
        700
      ],
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes"
            }
          ]
        }
      },
      "typeVersion": 1.2
    },
    {
      "id": "262608c6-e905-4d16-bc52-22b67c1bc298",
      "name": "Sticky Note3",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        -460
      ],
      "parameters": {
        "color": 3,
        "width": 740,
        "height": 280,
        "content": "# Generate AI Videos with Google Veo3, Save to Google Drive and Upload to YouTube\n\nThis workflow allows users to **generate AI videos** using **Google Veo3**, save them to **Google Drive**, generate optimized YouTube titles with GPT-4o, and **automatically upload them to YouTube** . The entire process is triggered from a Google Sheet that acts as the central interface for input and output.\n\nIT automates video creation, uploading, and tracking, ensuring seamless integration between Google Sheets, Google Drive, Google Veo3, and YouTube.\n\n\n\n\n"
      },
      "typeVersion": 1
    },
    {
      "id": "1ea1879e-1e8e-42f9-8b11-7f771cfca2f8",
      "name": "Sticky Note4",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        -140
      ],
      "parameters": {
        "width": 740,
        "height": 200,
        "content": "## STEP 1 - GOOGLE SHEET\nCreate a [Google Sheet like this](https://docs.google.com/spreadsheets/d/1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ/edit?usp=sharing).\n\nPlease insert:\n- in the \"PROMPT\" column the accurate description of the video you want to create\n- in the \"DURATION\" column the lenght of the video you want to create\n\nLeave the \"VIDEO\" column unfilled. It will be inserted by the system once the video has been created"
      },
      "typeVersion": 1
    },
    {
      "id": "8c54b723-d0b9-4d89-8150-975306640a96",
      "name": "Completed?",
      "type": "n8n-nodes-base.if",
      "position": [
        1020,
        840
      ],
      "parameters": {
        "options": {},
        "conditions": {
          "options": {
            "version": 2,
            "leftValue": "",
            "caseSensitive": true,
            "typeValidation": "strict"
          },
          "combinator": "and",
          "conditions": [
            {
              "id": "383d112e-2cc6-4dd4-8985-f09ce0bd1781",
              "operator": {
                "name": "filter.operator.equals",
                "type": "string",
                "operation": "equals"
              },
              "leftValue": "={{ $json.status }}",
              "rightValue": "COMPLETED"
            }
          ]
        }
      },
      "typeVersion": 2.2
    },
    {
      "id": "1135e1f0-b605-4724-a8b3-7f16b9887ef7",
      "name": "Update result",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        860,
        1100
      ],
      "parameters": {
        "columns": {
          "value": {
            "VIDEO": "={{ $('Get Url Video').item.json.video.url }}",
            "row_number": "={{ $('Get new video').item.json.row_number }}"
          },
          "schema": [
            {
              "id": "PROMPT",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PROMPT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DURATION",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "DURATION",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VIDEO",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "VIDEO",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "YOUTUBE_URL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "YOUTUBE_URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "row_number"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/11ebWJvwwXHgvQld9kxywKQUvIoBw6xMa0g0BuIqHDxE/edit#gid=0",
          "cachedResultName": "Foglio1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ/edit?usp=drivesdk",
          "cachedResultName": "Video Google Veo3"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "JYR6a64Qecd6t8Hb",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "8d0ac30d-5a92-487b-aaff-f761bd720293",
      "name": "Set data",
      "type": "n8n-nodes-base.set",
      "position": [
        220,
        840
      ],
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "c713d31f-9abd-496a-ac79-e8e2efe60aa0",
              "name": "prompt",
              "type": "string",
              "value": "={{ $json.PROMPT }}\n\nDuration of the video: {{ $json.DURATION }}"
            }
          ]
        }
      },
      "typeVersion": 3.4
    },
    {
      "id": "ae68690d-c154-4ec9-a5b8-ba95137d2cf4",
      "name": "Sticky Note5",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        520
      ],
      "parameters": {
        "width": 740,
        "height": 100,
        "content": "## STEP 4 - MAIN FLOW\nStart the workflow manually or periodically by hooking the \"Schedule Trigger\" node. It is recommended to set it at 5 minute intervals."
      },
      "typeVersion": 1
    },
    {
      "id": "429ab164-e165-409c-adc7-8a80c25b9f7d",
      "name": "Sticky Note6",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        100
      ],
      "parameters": {
        "width": 740,
        "height": 140,
        "content": "## STEP 2 - GET API KEY (YOURAPIKEY)\nCreate an account [here](https://fal.ai/) and obtain API KEY.\nIn the node \"Create Image\" set \"Header Auth\" and set:\n- Name: \"Authorization\"\n- Value: \"Key YOURAPIKEY\""
      },
      "typeVersion": 1
    },
    {
      "id": "868339d3-e3f0-473b-9f1f-c7c4fe9c9898",
      "name": "Sticky Note7",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        400,
        780
      ],
      "parameters": {
        "width": 180,
        "height": 200,
        "content": "Set API Key created in Step 2"
      },
      "typeVersion": 1
    },
    {
      "id": "44793285-6bb8-471a-a632-e0fe33d2d047",
      "name": "Get new video",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        0,
        840
      ],
      "parameters": {
        "options": {},
        "filtersUI": {
          "values": [
            {
              "lookupColumn": "VIDEO"
            }
          ]
        },
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ/edit#gid=0",
          "cachedResultName": "Foglio1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ/edit?usp=drivesdk",
          "cachedResultName": "Video Google Veo3"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "JYR6a64Qecd6t8Hb",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "7271ea9a-c4f5-4091-8f0f-ef40bb1d94af",
      "name": "Create Video",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        440,
        840
      ],
      "parameters": {
        "url": "https://queue.fal.run/fal-ai/veo3",
        "method": "POST",
        "options": {},
        "jsonBody": "={\n     \"prompt\": \"{{$json.prompt}}\"\n}",
        "sendBody": true,
        "sendHeaders": true,
        "specifyBody": "json",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        }
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "daOZafXpRXLtoLUV",
          "name": "Fal.run API"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "f0cbd048-011e-47ee-8840-af630adf6f85",
      "name": "Get Url Video",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        -220,
        1220
      ],
      "parameters": {
        "url": "=https://queue.fal.run/fal-ai/veo3/requests/{{ $json.request_id }}",
        "options": {},
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "daOZafXpRXLtoLUV",
          "name": "Fal.run API"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "f48cef5b-0609-417b-b4ec-21614397cb07",
      "name": "Get File Video",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        400,
        1220
      ],
      "parameters": {
        "url": "={{ $('Get Url Video').item.json.video.url }}",
        "options": {}
      },
      "typeVersion": 4.2
    },
    {
      "id": "2cde22e1-1b71-4672-80dc-4992c4bdfe5d",
      "name": "Upload Video",
      "type": "n8n-nodes-base.googleDrive",
      "position": [
        680,
        1100
      ],
      "parameters": {
        "name": "={{ $now.format('yyyyLLddHHmmss') }}-{{ $('Get Url Video').item.json.video.file_name }}",
        "driveId": {
          "__rl": true,
          "mode": "list",
          "value": "My Drive"
        },
        "options": {},
        "folderId": {
          "__rl": true,
          "mode": "list",
          "value": "1aHRwLWyrqfzoVC8HoB-YMrBvQ4tLC-NZ",
          "cachedResultUrl": "https://drive.google.com/drive/folders/1aHRwLWyrqfzoVC8HoB-YMrBvQ4tLC-NZ",
          "cachedResultName": "Fal.run"
        }
      },
      "credentials": {
        "googleDriveOAuth2Api": {
          "id": "HEy5EuZkgPZVEa9w",
          "name": "Google Drive account (n3w.it)"
        }
      },
      "typeVersion": 3
    },
    {
      "id": "bf77f692-8a47-4f49-883b-ba045cb39f3b",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "position": [
        680,
        1320
      ],
      "parameters": {
        "url": "https://api.upload-post.com/api/upload",
        "method": "POST",
        "options": {},
        "sendBody": true,
        "contentType": "multipart-form-data",
        "authentication": "genericCredentialType",
        "bodyParameters": {
          "parameters": [
            {
              "name": "title",
              "value": "={{ $('Generate title').item.json.message.content }}"
            },
            {
              "name": "user",
              "value": "YOUR_USERNAME"
            },
            {
              "name": "platform[]",
              "value": "youtube"
            },
            {
              "name": "video",
              "parameterType": "formBinaryData",
              "inputDataFieldName": "data"
            }
          ]
        },
        "genericAuthType": "httpHeaderAuth"
      },
      "credentials": {
        "httpHeaderAuth": {
          "id": "DEE2XGvhGodgbAJh",
          "name": "Upload-post.com API"
        }
      },
      "typeVersion": 4.2
    },
    {
      "id": "0fab9370-c079-40c8-9e87-e9b319e0bee7",
      "name": "Generate title",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "position": [
        20,
        1220
      ],
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "GPT-4O-MINI"
        },
        "options": {},
        "messages": {
          "values": [
            {
              "content": "=Input: {{ $('Get new video').item.json.PROMPT }}"
            },
            {
              "role": "system",
              "content": "You are a YouTube SEO expert specialized in creating engaging and optimized titles.\n\nYour task is to generate an effective title for a YouTube video based on the user's video description.\n\nGUIDELINES:\n- Maximum 60 characters to avoid truncation\n- Use relevant keywords for SEO\n- Make the title catchy and clickable\n- Avoid excessive or misleading clickbait\n- Consider the target audience of the content\n- Use numbers, questions, or power words when appropriate\n- IMPORTANT: Generate the title in the same language as the input description\n\nOUTPUT FORMAT:\nProvide only the title, without additional explanations.\n\nEXAMPLE:\nInput: \"Tutorial video on how to cook perfect pasta carbonara\"\nOutput: \"PERFECT Carbonara in 10 Minutes - Chef's Secrets\""
            }
          ]
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "TefveNaDaMERl1hY",
          "name": "OpenAi account (Eure)"
        }
      },
      "typeVersion": 1.8
    },
    {
      "id": "cf9a58f0-0523-4229-ac2e-42f0f71d5306",
      "name": "Update Youtube URL",
      "type": "n8n-nodes-base.googleSheets",
      "position": [
        860,
        1320
      ],
      "parameters": {
        "columns": {
          "value": {
            "VIDEO": "=",
            "row_number": "={{ $('Get new video').item.json.row_number }}",
            "YOUTUBE_URL": "https://youtu.be/{{ $json.results.youtube.video_id }}"
          },
          "schema": [
            {
              "id": "PROMPT",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "PROMPT",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "DURATION",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "DURATION",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "VIDEO",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "VIDEO",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "YOUTUBE_URL",
              "type": "string",
              "display": true,
              "removed": false,
              "required": false,
              "displayName": "YOUTUBE_URL",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            },
            {
              "id": "row_number",
              "type": "string",
              "display": true,
              "removed": false,
              "readOnly": true,
              "required": false,
              "displayName": "row_number",
              "defaultMatch": false,
              "canBeUsedToMatch": true
            }
          ],
          "mappingMode": "defineBelow",
          "matchingColumns": [
            "row_number"
          ],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {},
        "operation": "update",
        "sheetName": {
          "__rl": true,
          "mode": "list",
          "value": "gid=0",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/11ebWJvwwXHgvQld9kxywKQUvIoBw6xMa0g0BuIqHDxE/edit#gid=0",
          "cachedResultName": "Foglio1"
        },
        "documentId": {
          "__rl": true,
          "mode": "list",
          "value": "1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/1pcoY9N_vQp44NtSRR5eskkL5Qd0N0BGq7Jh_4m-7VEQ/edit?usp=drivesdk",
          "cachedResultName": "Video Google Veo3"
        }
      },
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "JYR6a64Qecd6t8Hb",
          "name": "Google Sheets account"
        }
      },
      "typeVersion": 4.5
    },
    {
      "id": "2f97346c-78df-41fe-b15d-c2af7e9ee680",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        660,
        1260
      ],
      "parameters": {
        "width": 180,
        "height": 200,
        "content": "Set YOUR_USERNAME in Step 3"
      },
      "typeVersion": 1
    },
    {
      "id": "0d6517cb-d2a3-4afe-b163-25311faed711",
      "name": "Sticky Note8",
      "type": "n8n-nodes-base.stickyNote",
      "position": [
        -220,
        280
      ],
      "parameters": {
        "width": 740,
        "height": 200,
        "content": "## STEP 3 - Upload video on Youtube\n- Find your API key in your [Upload-Post Manage Api Keys](https://www.upload-post.com/?linkId=lp_144414&sourceId=n3witalia&tenantId=upload-post-app) 10 FREE uploads per month\n- Set the the \"Auth Header\":\n-- Name: Authorization\n-- Value: Apikey YOUR_API_KEY_HERE\n- Create profiles to manage your social media accounts. The \"Profile\" you choose will be used in the field YOUR_USRNAME (eg. test1 or test2).  "
      },
      "typeVersion": 1
    }
  ],
  "active": false,
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "a358d31a-ae0a-44e0-83e4-0a0df359e143",
  "connections": {
    "Set data": {
      "main": [
        [
          {
            "node": "Create Video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Completed?": {
      "main": [
        [
          {
            "node": "Get Url Video",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Wait 60 sec.",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get status": {
      "main": [
        [
          {
            "node": "Completed?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Create Video": {
      "main": [
        [
          {
            "node": "Wait 60 sec.",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request": {
      "main": [
        [
          {
            "node": "Update Youtube URL",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Upload Video": {
      "main": [
        [
          {
            "node": "Update result",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Wait 60 sec.": {
      "main": [
        [
          {
            "node": "Get status",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Url Video": {
      "main": [
        [
          {
            "node": "Generate title",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get new video": {
      "main": [
        [
          {
            "node": "Set data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Update result": {
      "main": [
        []
      ]
    },
    "Generate title": {
      "main": [
        [
          {
            "node": "Get File Video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get File Video": {
      "main": [
        [
          {
            "node": "Upload Video",
            "type": "main",
            "index": 0
          },
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "When clicking ‘Test workflow’": {
      "main": [
        [
          {
            "node": "Get new video",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```
</details>