# n8n-nodes-evolution-api

## Basic Information

- Package: `n8n-nodes-evolution-api`
- Category: 💬 Communication & Messaging
- Version: 1.0.4
- Maintainer: oriondesign
- npm: [View Package](https://www.npmjs.com/package/n8n-nodes-evolution-api)
- Repository: [View Source](https://github.com/oriondesign2015/n8n-nodes-evolution-api)

## Description

A Evolution API é um hub de canais com foco no WhatsApp

## Installation

```
n8n-nodes-evolution-api
```

## Nodes (1)

### Evolution API

- Node Type: `n8n-nodes-evolution-api.evolutionApi`
- Version: 1
- Requires Credentials: Yes

Interact with Evolution API

#### Available Operations

- **Criar Instancia** (`instance-basic`)
  Cria uma nova Instancia
- **Conectar Instancia** (`instance-connect`)
  Gera a conexão de uma Instancia (QR ou Base64)
- **Buscar Instancia** (`fetch-instances`)
  Busca e lista as Instancias criadas
- **Definir Comportamento** (`instance-settings`)
  Define o comportamento da instancia
- **Definir Presença** (`set-presence`)
  Define a presença na instancia
- **Definir/Buscar Proxy** (`set-proxy`)
  Define um Proxy na instancia
- **Reiniciar Instancia** (`restart-instance`)
  Reinicia o socket da Instancia
- **Desconectar Instancia** (`logout-instance`)
  Desconecta o WhatsApp da Instancia
- **Deletar Instancia** (`delete-instance`)
  Deleta uma Instancia

#### Core Properties

| Property | Type | Required | Default |
|----------|------|----------|---------|
| `action` | options | Yes | `"add"` |
| `action` | options | Yes | `"not_announcement"` |
| `url` | string | Yes | `""` |
| `presence` | options | Yes | `"available"` |
| `options_display` | fixedCollection | Yes | `{"metadataValues":[]}` |
| `keyType` | options | Yes | `"email"` |
| `searchMethod` | options | Yes | `"inviteCode"` |
| `expiration` | options | Yes | `0` |
| `botType` | options | Yes | `"chatBot"` |
| `archive` | options | Yes | `true` |

#### Connection

- Input Types: `main`
- Output Types: `main`

#### Example Configuration

```json
{
  "name": "Evolution API",
  "type": "n8n-nodes-evolution-api.evolutionApi",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "action": "not_announcement",
    "url": "",
    "presence": "available",
    "options_display": {
      "metadataValues": []
    },
    "operation": "instance-basic"
  }
}
```

---

---

[← Back to Community Nodes Index](README.md)
