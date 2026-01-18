# Merge

## Basic Information

- Node Type: `nodes-base.merge`
- Category: transform
- Package: n8n-nodes-base

## Description

Merges data of multiple streams once data from both is available

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `query` | string | Yes | `"SELECT * FROM input1 LEFT JOIN input2 ON input1.name = input2.id"` | Input data available as tables with corresponding number, e.g. input1, input2 |
| `mode` | options | No | `"append"` | How input data should be merged |
| `combineBy` | options | No | `"combineByFields"` | How input data should be merged |
| `numberInputs` | options | No | `2` | The number of data inputs you want to merge. The node waits for all connected inputs to be executed. |
| `mergeByFields` | fixedCollection | No | `{"values":[{"field1":"","field2":""}]}` | Specify the fields to use for matching input items |
| `joinMode` | options | No | `"keepMatches"` | How to select the items to send to output |
| `numberInputs` | options | No | `2` | The number of data inputs you want to merge. The node waits for all connected inputs to be executed. |
| `numberInputs` | options | No | `2` | The number of data inputs you want to merge. The node waits for all connected inputs to be executed. |
| `numberInputs` | options | No | `2` | The number of data inputs you want to merge. The node waits for all connected inputs to be executed. |
| `options` | collection | No | `{}` | - |

### Property Details

#### Mode (`mode`)

How input data should be merged

Optional values:
- `append`: Append - Output items of each input, one after the other
- `combine`: Combine - Merge matching items together
- `combineBySql`: SQL Query - Write a query to do the merge
- `chooseBranch`: Choose Branch - Output data from a specific branch, without modifying it

#### Combine By (`combineBy`)

How input data should be merged

Optional values:
- `combineByFields`: Matching Fields - Combine items with the same field values
- `combineByPosition`: Position - Combine items based on their order
- `combineAll`: All Possible Combinations - Every pairing of every two items (cross join)

#### Number of Inputs (`numberInputs`)

The number of data inputs you want to merge. The node waits for all connected inputs to be executed.

Optional values:
- `2`: 2
- `3`: 3
- `4`: 4
- `5`: 5
- `6`: 6
- `7`: 7
- `8`: 8
- `9`: 9
- `10`: 10

#### Fields to Match (`mergeByFields`)

Specify the fields to use for matching input items

Optional values:
- `undefined`: values

#### Output Type (`joinMode`)

How to select the items to send to output

Optional values:
- `keepMatches`: Keep Matches - Items that match, merged together (inner join)
- `keepNonMatches`: Keep Non-Matches - Items that don't match
- `keepEverything`: Keep Everything - Items that match merged together, plus items that don't match (outer join)
- `enrichInput1`: Enrich Input 1 - All of input 1, with data from input 2 added in (left join)
- `enrichInput2`: Enrich Input 2 - All of input 2, with data from input 1 added in (right join)

#### Number of Inputs (`numberInputs`)

The number of data inputs you want to merge. The node waits for all connected inputs to be executed.

Optional values:
- `2`: 2
- `3`: 3
- `4`: 4
- `5`: 5
- `6`: 6
- `7`: 7
- `8`: 8
- `9`: 9
- `10`: 10

#### Number of Inputs (`numberInputs`)

The number of data inputs you want to merge. The node waits for all connected inputs to be executed.

Optional values:
- `2`: 2
- `3`: 3
- `4`: 4
- `5`: 5
- `6`: 6
- `7`: 7
- `8`: 8
- `9`: 9
- `10`: 10

#### Number of Inputs (`numberInputs`)

The number of data inputs you want to merge. The node waits for all connected inputs to be executed.

Optional values:
- `2`: 2
- `3`: 3
- `4`: 4
- `5`: 5
- `6`: 6
- `7`: 7
- `8`: 8
- `9`: 9
- `10`: 10

#### Options (`options`)

Optional values:
- `undefined`: clashHandling
- `undefined`: fuzzyCompare - Whether to tolerate small type differences when comparing fields. E.g. the number 3 and the string '3' are treated as the same.

## Connection Guide

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
6. Airtable - via `main` connection
7. Discord - via `main` connection
8. Dropbox - via `main` connection
9. GitHub - via `main` connection
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "Merge",
  "type": "nodes-base.merge",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {
    "query": "SELECT * FROM input1 LEFT JOIN input2 ON input1.name = input2.id"
  }
}
```
