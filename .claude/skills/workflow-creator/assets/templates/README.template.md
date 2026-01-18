<div align="center">

# {{EMOJI}} {{WORKFLOW_NAME}}

### **{{TAGLINE}}**

[← Back to AI Workflow](../README.md)

[简体中文](./README_cn.md) | English

</div>

---

## 🎯 Who Is This For?

{{TARGET_USERS}}
<!-- Example:
- **Role 1** - Use case description
- **Role 2** - Use case description
- **Role 3** - Use case description
-->

---

## ⚡ Quick Install

```bash
# Install all {{SKILL_COUNT}} skills with one command
npx add-skill nicepkg/ai-workflow/{{WORKFLOW_DIR}}

# Or install specific skills
npx add-skill nicepkg/ai-workflow/{{WORKFLOW_DIR}} --skill {{EXAMPLE_SKILL}}
```

---

## 📦 Skills Included ({{SKILL_COUNT}})

{{SKILLS_BY_STAGE}}
<!--
Format each stage like this:

### 0️⃣ Stage Name
| Skill | What It Does |
|:------|:-------------|
| `skill-name` | Brief description of what this skill does |

### 1️⃣ Next Stage
| Skill | What It Does |
|:------|:-------------|
| `skill-name` | Brief description |
-->

---

## 🔄 Complete Pipeline ({{STAGE_COUNT}} Stages)

```
{{PIPELINE_ASCII}}
```
<!--
Format like this:

Stage 0: Stage Name
└── skill-name → What it does

Stage 1: Stage Name
├── skill-name → What it does
├── skill-name → What it does
└── skill-name → What it does

Stage 2: Stage Name
├── skill-name → What it does
└── skill-name → What it does
-->

---

## 💡 Example Workflows

{{EXAMPLE_WORKFLOWS}}
<!--
Format each example like this:

### Workflow Name
```
1. "First prompt to AI"
2. "Second prompt to AI"
3. "Third prompt to AI"
```
-->

---

## 🔗 Skill Combinations

| Goal | Skill Chain |
|:-----|:------------|
{{SKILL_COMBINATIONS}}
<!--
| **Goal Name** | skill1 → skill2 → skill3 → skill4 |
-->

---

## 📄 License

MIT © [nicepkg](https://github.com/nicepkg)

<div align="center">

**[⬆ Back to Main Project](../README.md)**

</div>
