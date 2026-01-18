# Set

## Basic Information

- Node Type: `nodes-base.set`
- Category: input
- Package: n8n-nodes-base

## Description

Add or edit fields on an input item and optionally remove other fields

## Core Properties

| Property Name | Type | Required | Default | Description |
|---------|------|------|--------|------|
| `fields` | fixedCollection | No | `{}` | Edit existing fields or add new ones to modify the output data |
| `include` | options | No | `"all"` | How to select the fields you want to include in your output items |
| `include` | options | No | `"all"` | How to select the fields you want to include in your output items |
| `mode` | options | No | `"manual"` | - |
| `options` | collection | No | `{}` | - |
| `duplicateItem` | boolean | No | `false` | Whether this item should be duplicated a set number of times |
| `duplicateCount` | number | No | `0` | How many times the item should be duplicated, mainly used for testing and debugging |
| `includeOtherFields` | boolean | No | `false` | Whether to pass to the output all the input fields (along with the fields set in 'Fields to Set') |
| `includeFields` | string | No | `""` | Comma-separated list of the field names you want to include in the output. You can drag the selected fields from the input panel. |
| `excludeFields` | string | No | `""` | Comma-separated list of the field names you want to exclude from the output. You can drag the selected fields from the input panel. |

### Property Details

#### Fields to Set (`fields`)

Edit existing fields or add new ones to modify the output data

Optional values:
- `undefined`: values

#### Include in Output (`include`)

How to select the fields you want to include in your output items

Optional values:
- `all`: All Input Fields - Also include all unchanged fields from the input
- `none`: No Input Fields - Include only the fields specified above
- `selected`: Selected Input Fields - Also include the fields listed in the parameter “Fields to Include”
- `except`: All Input Fields Except - Exclude the fields listed in the parameter “Fields to Exclude”

#### Input Fields to Include (`include`)

How to select the fields you want to include in your output items

Optional values:
- `all`: All - Also include all unchanged fields from the input
- `selected`: Selected - Also include the fields listed in the parameter “Fields to Include”
- `except`: All Except - Exclude the fields listed in the parameter “Fields to Exclude”

#### Mode (`mode`)

Optional values:
- `manual`: Manual Mapping - Edit item fields one by one
- `raw`: JSON - Customize item output with JSON

#### Options (`options`)

Optional values:
- `undefined`: includeBinary - Whether binary data should be included if present in the input item
- `undefined`: stripBinary - Whether binary data should be stripped from the input item. Only applies when "Include Other Input Fields" is enabled.
- `undefined`: ignoreConversionErrors - Whether to ignore field type errors and apply a less strict type conversion
- `undefined`: dotNotation - By default, dot-notation is used in property names. This means that "a.b" will set the property "b" underneath "a" so { "a": { "b": value} }. If that is not intended this can be deactivated, it will then set { "a.b": value } instead.

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
5. Merge - via `main` connection
6. Airtable - via `main` connection
7. Discord - via `main` connection
8. Dropbox - via `main` connection
9. GitHub - via `main` connection
10. Google Drive - via `main` connection
## JSON Configuration Examples

### Basic Configuration
```json
{
  "name": "Set",
  "type": "nodes-base.set",
  "typeVersion": 1,
  "position": [
    250,
    300
  ],
  "parameters": {}
}
```
