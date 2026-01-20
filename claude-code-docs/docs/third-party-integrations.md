---
source: https://code.claude.com/docs/en/third-party-integrations
title: Enterprise deployment overview
---

Organizations can deploy Claude Code through Anthropic directly or through a cloud provider. This page helps you choose the right configuration.

## [​](#compare-deployment-options) Compare deployment options

For most organizations, Claude for Teams or Claude for Enterprise provides the best experience. Team members get access to both Claude Code and Claude on the web with a single subscription, centralized billing, and no infrastructure setup required.
**Claude for Teams** is self-service and includes collaboration features, admin tools, and billing management. Best for smaller teams that need to get started quickly.
**Claude for Enterprise** adds SSO and domain capture, role-based permissions, compliance API access, and managed policy settings for deploying organization-wide Claude Code configurations. Best for larger organizations with security and compliance requirements.
Learn more about [Team plans](https://support.claude.com/en/articles/9266767-what-is-the-team-plan) and [Enterprise plans](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan).
If your organization has specific infrastructure requirements, compare the options below:

| Feature | Claude for Teams/Enterprise | Anthropic Console | Amazon Bedrock | Google Vertex AI | Microsoft Foundry |
| --- | --- | --- | --- | --- | --- |
| Best for | Most organizations (recommended) | Individual developers | AWS-native deployments | GCP-native deployments | Azure-native deployments |
| Billing | **Teams:** $150/seat (Premium) with PAYG available **Enterprise:** [Contact Sales](https://claude.com/contact-sales) | PAYG | PAYG through AWS | PAYG through GCP | PAYG through Azure |
| Regions | Supported [countries](https://www.anthropic.com/supported-countries) | Supported [countries](https://www.anthropic.com/supported-countries) | Multiple AWS [regions](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) | Multiple GCP [regions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) | Multiple Azure [regions](https://azure.microsoft.com/en-us/explore/global-infrastructure/products-by-region/) |
| Prompt caching | Enabled by default | Enabled by default | Enabled by default | Enabled by default | Enabled by default |
| Authentication | Claude.ai SSO or email | API key | API key or AWS credentials | GCP credentials | API key or Microsoft Entra ID |
| Cost tracking | Usage dashboard | Usage dashboard | AWS Cost Explorer | GCP Billing | Azure Cost Management |
| Includes Claude on web | Yes | No | No | No | No |
| Enterprise features | Team management, SSO, usage monitoring | None | IAM policies, CloudTrail | IAM roles, Cloud Audit Logs | RBAC policies, Azure Monitor |

Select a deployment option to view setup instructions:

- [Claude for Teams or Enterprise](/docs/en/iam#claude-for-teams-or-enterprise-recommended)
- [Anthropic Console](/docs/en/iam#claude-console-authentication)
- [Amazon Bedrock](/docs/en/amazon-bedrock)
- [Google Vertex AI](/docs/en/google-vertex-ai)
- [Microsoft Foundry](/docs/en/microsoft-foundry)

## [​](#configure-proxies-and-gateways) Configure proxies and gateways

Most organizations can use a cloud provider directly without additional configuration. However, you may need to configure a corporate proxy or LLM gateway if your organization has specific network or management requirements. These are different configurations that can be used together:

- **Corporate proxy**: Routes traffic through an HTTP/HTTPS proxy. Use this if your organization requires all outbound traffic to pass through a proxy server for security monitoring, compliance, or network policy enforcement. Configure with the `HTTPS_PROXY` or `HTTP_PROXY` environment variables. Learn more in [Enterprise network configuration](/docs/en/network-config).
- **LLM Gateway**: A service that sits between Claude Code and the cloud provider to handle authentication and routing. Use this if you need centralized usage tracking across teams, custom rate limiting or budgets, or centralized authentication management. Configure with the `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, or `ANTHROPIC_VERTEX_BASE_URL` environment variables. Learn more in [LLM gateway configuration](/docs/en/llm-gateway).

The following examples show the environment variables to set in your shell or shell profile (`.bashrc`, `.zshrc`). See [Settings](/docs/en/settings) for other configuration methods.

### [​](#amazon-bedrock) Amazon Bedrock

- Corporate proxy
- LLM Gateway

Route Bedrock traffic through your corporate proxy by setting the following [environment variables](/docs/en/settings#environment-variables):

```bash
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

Route Bedrock traffic through your LLM gateway by setting the following [environment variables](/docs/en/settings#environment-variables):

```bash
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1

# Configure LLM gateway
export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # If gateway handles AWS auth
```

### [​](#microsoft-foundry) Microsoft Foundry

- Corporate proxy
- LLM Gateway

Route Foundry traffic through your corporate proxy by setting the following [environment variables](/docs/en/settings#environment-variables):

```bash
# Enable Microsoft Foundry
export CLAUDE_CODE_USE_FOUNDRY=1
export ANTHROPIC_FOUNDRY_RESOURCE=your-resource
export ANTHROPIC_FOUNDRY_API_KEY=your-api-key  # Or omit for Entra ID auth

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

Route Foundry traffic through your LLM gateway by setting the following [environment variables](/docs/en/settings#environment-variables):

```bash
# Enable Microsoft Foundry
export CLAUDE_CODE_USE_FOUNDRY=1

# Configure LLM gateway
export ANTHROPIC_FOUNDRY_BASE_URL='https://your-llm-gateway.com'
export CLAUDE_CODE_SKIP_FOUNDRY_AUTH=1  # If gateway handles Azure auth
```

### [​](#google-vertex-ai) Google Vertex AI

- Corporate proxy
- LLM Gateway

Route Vertex AI traffic through your corporate proxy by setting the following [environment variables](/docs/en/settings#environment-variables):

```bash
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

Route Vertex AI traffic through your LLM gateway by setting the following [environment variables](/docs/en/settings#environment-variables):

```bash
# Enable Vertex
export CLAUDE_CODE_USE_VERTEX=1

# Configure LLM gateway
export ANTHROPIC_VERTEX_BASE_URL='https://your-llm-gateway.com/vertex'
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1  # If gateway handles GCP auth
```

Use `/status` in Claude Code to verify your proxy and gateway configuration is applied correctly.

## [​](#best-practices-for-organizations) Best practices for organizations

### [​](#invest-in-documentation-and-memory) Invest in documentation and memory

We strongly recommend investing in documentation so that Claude Code understands your codebase. Organizations can deploy CLAUDE.md files at multiple levels:

- **Organization-wide**: Deploy to system directories like `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) for company-wide standards
- **Repository-level**: Create `CLAUDE.md` files in repository roots containing project architecture, build commands, and contribution guidelines. Check these into source control so all users benefit

Learn more in [Memory and CLAUDE.md files](/docs/en/memory).

### [​](#simplify-deployment) Simplify deployment

If you have a custom development environment, we find that creating a “one click” way to install Claude Code is key to growing adoption across an organization.

### [​](#start-with-guided-usage) Start with guided usage

Encourage new users to try Claude Code for codebase Q&A, or on smaller bug fixes or feature requests. Ask Claude Code to make a plan. Check Claude’s suggestions and give feedback if it’s off-track. Over time, as users understand this new paradigm better, then they’ll be more effective at letting Claude Code run more agentically.

### [​](#configure-security-policies) Configure security policies

Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration. [Learn more](/docs/en/security).

### [​](#leverage-mcp-for-integrations) Leverage MCP for integrations

MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs. We recommend that one central team configures MCP servers and checks a `.mcp.json` configuration into the codebase so that all users benefit. [Learn more](/docs/en/mcp).
At Anthropic, we trust Claude Code to power development across every Anthropic codebase. We hope you enjoy using Claude Code as much as we do.

## [​](#next-steps) Next steps

Once you’ve chosen a deployment option and configured access for your team:

1. **Roll out to your team**: Share installation instructions and have team members [install Claude Code](/docs/en/setup) and authenticate with their credentials.
2. **Set up shared configuration**: Create a [CLAUDE.md file](/docs/en/memory) in your repositories to help Claude Code understand your codebase and coding standards.
3. **Configure permissions**: Review [security settings](/docs/en/security) to define what Claude Code can and cannot do in your environment.