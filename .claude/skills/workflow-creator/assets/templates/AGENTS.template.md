# {{WORKFLOW_NAME}} - AI Instructions

You are a {{ROLE_DESCRIPTION}} assistant. Help users through the complete workflow using the installed skills.

## Workflow Overview

This workflow covers the {{DOMAIN}} pipeline:
```
{{PIPELINE_SUMMARY}}
```
<!-- Example: Intake → Discovery → Definition → Prioritization → Delivery → Launch → Review -->

## Available Skills

{{SKILLS_BY_STAGE}}
<!--
Format each stage like this:

### Stage 0: Stage Name
- **skill-name**: Brief description

### Stage 1: Stage Name
- **skill-name**: Brief description
- **skill-name**: Brief description
-->

## Skill Usage Guidelines

{{SKILL_USAGE_GUIDELINES}}
<!--
Format like this:

### When user mentions [trigger topic]
1. Use `skill-name` first to [action]
2. Suggest next steps based on [criteria]

### When user needs [task type]
1. Use `skill-name` for [purpose]
2. Use `skill-name` for [purpose]
-->

## Recommended Sequences

{{RECOMMENDED_SEQUENCES}}
<!--
Format like this:

### Sequence Name (Purpose)
```
skill1 → skill2 → skill3 → skill4
```

### Another Sequence
```
skill1 → skill2 → skill3
```
-->

## Output Standards

{{OUTPUT_STANDARDS}}
<!--
Format like this:

### Output Type Name
- Bullet point for standard
- Another standard
- Another standard

### Another Output Type
- Standard format requirement
- Quality requirement
-->

## Quality Gates

{{QUALITY_GATES}}
<!--
Format like this:

### Before Phase A → Phase B
- [ ] Checkpoint item
- [ ] Another checkpoint

### Before Phase B → Phase C
- [ ] Checkpoint item
-->
