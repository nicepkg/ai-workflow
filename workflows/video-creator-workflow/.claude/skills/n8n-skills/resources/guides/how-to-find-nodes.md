# How to Find Nodes

This skill contains complete information for 542 n8n nodes. As an AI assistant, you can use the following tools to efficiently find and read node information.

## 1. Using the Unified Index (INDEX.md)

INDEX.md is the master index for all nodes, providing two ways to search:

### Read Complete Index
```
Read("resources/INDEX.md")
```

Index contents include:
- Find by category: 6 built-in categories (Transform, Input, Output, Trigger, Organization, Misc)
- Community packages: 30+ popular community node packages
- Template index: workflow templates

### Read Specific Sections of the Index

INDEX.md contains location information (starting line number and line count) for all 542 nodes, allowing you to read precisely:

Example: Finding nodes in the "Data Transformation" category
```
# First read the index to understand category contents
Read("resources/INDEX.md", offset=1, limit=100)
```

## 2. Using Read Tool to Precisely Read Node Documentation

### Read High-Priority Nodes (Individual Files)

The top 50 most commonly used nodes have individual files, which can be read directly:

```
# Example: Read Gmail node
Read("resources/output/nodes-base.gmail.md")

# Example: Read Code node
Read("resources/transform/nodes-base.code.md")
```

### Read Low-Priority Nodes (Specific Nodes in Merged Files)

The other 492 nodes are merged in category files. INDEX.md will tell you the starting line number and line count for each node:

```
# Step 1: Find the node's location information from INDEX.md
# Example: Azure Cosmos DB is at line 110 in transform-merged-1.md with 64 lines

# Step 2: Use starting line number and line count to read precisely
Read("resources/transform/transform-merged-1.md", offset=110, limit=64)
```

## 3. Using Glob Tool to Search Files

When you know part of a node name, use Glob to quickly locate files:

```
# Search for node files containing "gmail"
Glob("resources/**/*gmail*.md")

# Search all output-type nodes
Glob("resources/output/*.md")

# Search all trigger nodes
Glob("resources/trigger/*.md")

# Search merged files
Glob("resources/**/*-merged-*.md")
```

## 4. Using Grep Tool to Search Keywords

Search for functional keywords in all resource files:

```
# Search for nodes containing "send email"
Grep("send email", path="resources", output_mode="files_with_matches")

# Search for database-related nodes
Grep("database", path="resources", output_mode="files_with_matches")

# Search webhook-related functionality (show matching content)
Grep("webhook", path="resources", output_mode="content", -n=true, -C=2)

# Search for AI-related nodes
Grep("AI|artificial intelligence", path="resources", output_mode="files_with_matches")
```

## 5. Searching Community Nodes

Community nodes are organized in a dedicated directory:

### Read Community Index
```
Read("resources/community/README.md")
```

### Search Community Packages
```
# Search for WhatsApp-related community nodes
Glob("resources/community/*evolution*.md")
Glob("resources/community/*whatsapp*.md")

# Search for AI-related community nodes
Glob("resources/community/*elevenlabs*.md")
Glob("resources/community/*perplexity*.md")
Glob("resources/community/*tavily*.md")

# Search by keyword in community packages
Grep("voice generation", path="resources/community", output_mode="files_with_matches")
```

## Search Strategy Recommendations

Choose the best search method for different scenarios:

1. User asks about specific services (e.g., "Gmail", "Slack"):
   → Use Glob search: `Glob("resources/**/*gmail*.md")`

2. User asks about functional requirements (e.g., "send email", "database query"):
   → Use Grep to search keywords: `Grep("send email", path="resources")`

3. User asks about node categories (e.g., "what triggers are available"):
   → Read category table in INDEX.md: `Read("resources/INDEX.md", offset=<category_start_line>, limit=<line_count>)`

4. User wants to learn about popular nodes:
   → Read the priority ranking table in INDEX.md

5. User needs workflow examples:
   → Reference the "Common Workflow Patterns" section or resources/templates/ directory

6. User asks about community packages:
   → Read community index: `Read("resources/community/README.md")`
   → Search community packages: `Glob("resources/community/*keyword*.md")`
