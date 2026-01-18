# Usage Guide

## 1. File Structure Navigation

### Directory Structure

```
resources/
├── INDEX.md                     # Unified index (contains line number info for all nodes)
├── compatibility-matrix.md      # Node compatibility matrix
├── transform/                   # Data transformation nodes
│   ├── README.md                # 18 nodes overview
│   ├── nodes-base.code.md       # High-priority individual files
│   ├── nodes-base.function.md
│   └── transform-merged-*.md    # Low-priority merged files
├── input/                       # Data input nodes
│   ├── README.md                # 12 nodes
│   └── ...
├── output/                      # Data output nodes
│   ├── README.md                # 16 nodes
│   └── ...
├── trigger/                     # Trigger nodes
│   ├── README.md                # 10 nodes
│   └── ...
├── organization/                # Organization management nodes
│   ├── README.md                # 1 nodes
│   └── ...
├── misc/                        # Miscellaneous nodes
│   ├── README.md                # 1 nodes
│   └── ...
├── community/                   # Community package nodes
│   ├── README.md                # Community packages index (30+ packages)
│   ├── ai-tools.md              # AI tools category
│   ├── communication.md         # Communication category
│   └── *.md                     # Individual package files
└── templates/                   # Workflow templates
    ├── README.md                # Templates overview
    ├── ai-chatbots/             # AI & chatbot templates
    ├── social-media/            # Social media templates
    ├── data-processing/         # Data processing templates
    └── communication/           # Communication & collaboration templates
```

### High-Priority vs Low-Priority Nodes

- High-priority (top 50): Individual files, filename format `nodes-base.{nodeType}.md`
  - Example: `resources/transform/nodes-base.code.md`
  - Read the complete file directly using the Read tool

- Low-priority (other 492): Merged in `*-merged-*.md` files
  - Example: `resources/transform/transform-merged-1.md`
  - Use INDEX.md to find line numbers, then use Read tool's offset/limit parameters to read specific ranges

## 2. Complete Tool Usage Instructions

### Read Tool

Purpose: Read file contents

Complete read:
```
Read("resources/INDEX.md")
Read("resources/transform/nodes-base.code.md")
```

Precise read (using starting line number and line count):
```
Read("resources/transform/transform-merged-1.md", offset=110, limit=64)
```

### Glob Tool

Purpose: Search for files matching a pattern

Common patterns:
```
Glob("resources/**/*{keyword}*.md")    # Search for files containing keyword
Glob("resources/transform/*.md")      # Search all files in a specific category
Glob("resources/**/*-merged-*.md")    # Search all merged files
```

### Grep Tool

Purpose: Search for keywords in file contents

Basic search:
```
Grep("{keyword}", path="resources", output_mode="files_with_matches")
```

Advanced search:
```
# Show matching content and line numbers
Grep("{keyword}", path="resources", output_mode="content", -n=true, -C=2)

# Use regular expressions
Grep("email|mail", path="resources", output_mode="files_with_matches")

# Limit search to specific category
Grep("{keyword}", path="resources/transform", output_mode="files_with_matches")
```

### INDEX.md Query Method

INDEX.md is the most important navigation tool, recommended to use first:

1. First read INDEX.md to understand overall structure
2. Find target nodes based on categories
3. Record node's file path, starting line number, and line count
4. Use Read tool to precisely read node content

## 3. Decision Flow Guide

### Scenario 1: User Asks About a Specific Service Node

Example: "How do I use the Gmail node?"

Decision flow:
```
1. Use Glob for quick location
   Glob("resources/**/*gmail*.md")

2. If an individual file is found, read it directly
   Read("resources/output/nodes-base.gmail.md")

3. If in a merged file, check INDEX.md first
   → Find starting line number and line count
   → Use offset/limit to read
```

### Scenario 2: User Asks About Functional Requirements

Example: "I need a node to send emails"

Decision flow:
```
1. Use Grep to search keywords
   Grep("send email|send mail", path="resources", output_mode="files_with_matches")

2. Get a list of candidate nodes
   → Gmail, SendGrid, SMTP, etc.

3. Read detailed documentation for relevant nodes
   → Compare functional differences
   → Recommend the most suitable node
```

### Scenario 3: User Asks About Node Categories

Example: "What trigger nodes are available?"

Decision flow:
```
1. Read the trigger category section in INDEX.md
   Read("resources/INDEX.md")
   → Find "## Find by Category" > "### Trigger"

2. Or directly read the category README
   Read("resources/trigger/README.md")

3. Provide node list and brief descriptions
```

### Scenario 4: User Needs Workflow Examples

Example: "How do I build an AI chatbot?"

Decision flow:
```
1. First check the "Common Workflow Patterns" section
   → Look for relevant patterns

2. Check the template library
   Read("resources/templates/ai-chatbots/README.md")

3. Combine with node documentation
   → AI Agent node
   → OpenAI node
   → Vector Store node
```

### Scenario 5: User Asks About Community Packages

Example: "What community nodes are available for WhatsApp?"

Decision flow:
```
1. Read community nodes index
   Read("resources/community/README.md")

2. Search for specific packages
   Glob("resources/community/*whatsapp*.md")
   Glob("resources/community/*evolution*.md")
   Grep("whatsapp", path="resources/community", output_mode="files_with_matches")

3. Read detailed package documentation
   Read("resources/community/n8n-nodes-evolution-api.md")
   Read("resources/community/n8n-nodes-megaapi.md")
```

## 4. Best Practices and Considerations

### Search Strategy

1. Prioritize using INDEX.md for a global view
   - Understand node categorization and priorities
   - Quickly locate target nodes

2. Leverage Grep for function-oriented searches
   - When users describe needs rather than specific node names
   - Keyword searches can quickly find candidate nodes

3. Use Glob for filename searches
   - When you know part of a node name
   - Faster than Grep

4. Leverage starting line number and line count reading
   - Merged files can be very large (thousands of lines)
   - Use offset/limit to read only the needed portions
   - Save token usage

### Node Selection Recommendations

1. Prioritize recommending high-priority nodes
   - High usage = more stable, more complete documentation
   - Better community support

2. Check node compatibility
   - Read resources/compatibility-matrix.md
   - Or check the "Connection Guide" section in node documentation

3. Reference actual templates
   - The templates/ directory contains real-world use cases
   - Learn how nodes are combined

### Common Pitfalls

1. Don't always read complete merged files
   - Merged files can have thousands of lines
   - Should use INDEX.md to find line numbers, then read precisely

2. Pay attention to node naming format
   - File format: `nodes-base.{nodeType}.md`
   - nodeType is usually lowercase with hyphens
   - Example: `nodes-base.httpRequest.md` (not `http-request`)

3. Distinguish between trigger and action nodes
   - Triggers can only be placed at the beginning of workflows
   - Webhook nodes are also a type of trigger

4. Check node versions
   - Some nodes have multiple versions
   - Documentation will note version numbers and differences
