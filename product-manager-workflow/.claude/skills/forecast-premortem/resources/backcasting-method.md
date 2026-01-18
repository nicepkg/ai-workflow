# Backcasting Method

## Temporal Reasoning from Future to Present

**Backcasting** is the practice of starting from a future state and working backward to identify the path that led there.

**Contrast with forecasting:**
- **Forecasting:** Present → Future (What will happen?)
- **Backcasting:** Future → Present (How did this happen?)

---

## The Structured Backcasting Process

### Phase 1: Define the Future State

**Step 1.1: Set the resolution date**
- When will you know if the prediction came true?
- Be specific: "December 31, 2025"

**Step 1.2: State the outcome as a certainty**
- Don't say "might fail" or "probably fails"
- Say "HAS failed" or "DID fail"
- Use past tense

**Step 1.3: Emotional calibration**
- How surprising is this outcome?
  - Shocking → You were very overconfident
  - Expected → Appropriate confidence
  - Inevitable → You were underconfident

---

### Phase 2: Construct the Timeline

**Step 2.1: Work backward in time chunks**

Start at resolution date, work backward in intervals:

**For 2-year prediction:**
- Resolution date (final failure)
- 6 months before (late-stage warning)
- 1 year before (mid-stage problems)
- 18 months before (early signs)
- Start date (initial conditions)

**For 6-month prediction:**
- Resolution date
- 1 month before
- 3 months before
- Start date

---

**Step 2.2: Fill in each time chunk**

For each period, ask:
- What was happening at this time?
- What decisions were made?
- What external events occurred?
- What warning signs appeared?

**Template:**
```
[Date]: [Event that occurred]
Effect: [How this contributed to failure]
Warning sign: [What would have indicated this was coming]
```

---

### Phase 3: Identify Causal Chains

**Step 3.1: Map the causal structure**

```
Initial condition → Trigger event → Cascade → Failure
```

**Example:**
```
Team overworked → Key engineer quit → Lost 3 months → Missed deadline → Funding fell through → Failure
```

---

**Step 3.2: Classify causes**

| Type | Description | Example |
|------|-------------|---------|
| **Necessary** | Without this, failure wouldn't happen | Regulatory ban |
| **Sufficient** | This alone causes failure | Founder death |
| **Contributing** | Makes failure more likely | Market downturn |
| **Catalytic** | Speeds up inevitable failure | Competitor launch |

---

**Step 3.3: Find the "brittle point"**

**Question:** Which single event, if prevented, would have avoided failure?

This is your **critical dependency** and highest-priority monitoring target.

---

### Phase 4: Narrative Construction

**Step 4.1: Write the headlines**

Imagine you're a journalist covering this failure. What headlines mark the timeline?

**Example:**
- "Startup X raises $10M Series A" (12 months before)
- "Startup X faces regulatory scrutiny" (9 months before)
- "Key executive departs Startup X" (6 months before)
- "Startup X misses Q3 targets" (3 months before)
- "Startup X shuts down, cites regulatory pressure" (resolution)

---

**Step 4.2: Write the obituary**

"Startup X failed because..."

Complete this sentence with a single, clear causal narrative. Force yourself to be concise.

**Good:**
"Startup X failed because regulatory uncertainty froze customer adoption, leading to missed revenue targets and inability to raise Series B."

**Bad (too vague):**
"Startup X failed because of various challenges."

---

**Step 4.3: The insider vs outsider narrative**

**Insider view:** What would the founders say?
- "We underestimated regulatory risk"
- "We hired too slowly"
- "We ran out of runway"

**Outsider view:** What would analysts say?
- "82% of startups in this space fail due to regulation"
- "Classic execution failure"
- "Unit economics never made sense"

**Compare:** Does your insider narrative match outsider base rates?

---

## Narrative vs Quantitative Backcasting

### Narrative Backcasting

**Strengths:**
- Rich, detailed stories
- Reveals unknown unknowns
- Good for complex systems

**Weaknesses:**
- Subject to narrative fallacy
- Can feel too "real" and bias you
- Hard to quantify

**Use when:**
- Complex, multi-causal failures
- Human/organizational factors dominate
- Need to surface blind spots

---

### Quantitative Backcasting

**Strengths:**
- Precise probability estimates
- Aggregates multiple failure modes
- Less subject to bias

**Weaknesses:**
- Requires data
- Can miss qualitative factors
- May feel mechanical

**Use when:**
- Statistical models exist
- Multiple independent failure modes
- Need to calculate confidence intervals

---

## Advanced Technique: Multiple Backcast Paths

### Generate 3-5 Different Failure Narratives

Instead of one story, create multiple:

**Path 1: Internal Execution Failure**
- Team burned out
- Product quality suffered
- Customers churned
- Revenue missed
- Funding dried up

**Path 2: External Market Shift**
- Competitor launched free tier
- Market commoditized
- Margins compressed
- Unit economics broke
- Shutdown

**Path 3: Regulatory Kill**
- New law passed
- Business model illegal
- Forced shutdown

**Path 4: Black Swan**
- Pandemic
- Supply chain collapse
- Force majeure

---

### Aggregate the Paths

**Calculate probability for each path:**
- Path 1 (Internal): 40%
- Path 2 (Market): 30%
- Path 3 (Regulatory): 20%
- Path 4 (Black Swan): 10%

**Total failure probability:** 100% (since we assumed failure)

**Insight:** But in reality, your prediction gives 25% failure. This means you're underestimating by 75 percentage points, OR these paths are not independent.

**Adjustment:**
If paths are partially overlapping (e.g., internal failure AND market shift), use:
```
P(A or B) = P(A) + P(B) - P(A and B)
```

---

## Temporal Reasoning Techniques

### The "Newspaper Test"

**Method:**
For each time period, imagine you're reading a newspaper from that date.

**What headlines would you see?**
- Macro news (economy, politics, technology)
- Industry news (competitors, regulations, trends)
- Company news (your specific case)

**This forces you to think about:**
- External context, not just internal execution
- Leading indicators, not just lagging outcomes

---

### The "Retrospective Interview"

**Method:**
Imagine you're interviewing someone 1 year after failure.

**Questions:**
- "Looking back, when did you first know this was in trouble?"
- "What was the moment of no return?"
- "If you could go back, what would you change?"
- "What signs did you ignore?"

**This reveals:**
- Early warning signals you should monitor
- Critical decision points
- Hindsight that can become foresight

---

### The "Parallel Universe" Technique

**Method:**
Create two timelines:

**Timeline A: Success**
What had to happen for success?

**Timeline B: Failure**
What happened instead?

**Divergence point:**
Where do the timelines split? That's your critical uncertainty.

---

## Common Backcasting Mistakes

### Mistake 1: Being Too Vague

**Bad:** "Things went wrong and it failed."
**Good:** "Q3 2024: Competitor X launched free tier. Q4 2024: We lost 30% of customers. Q1 2025: Revenue dropped below runway. Q2 2025: Failed to raise Series B. Q3 2025: Shutdown."

**Fix:** Force yourself to name specific events and dates.

---

### Mistake 2: Only Internal Causes

**Bad:** "We executed poorly."
**Good:** "We executed poorly AND market shifted AND regulation changed."

**Fix:** Use PESTLE framework to ensure external factors are considered.

---

### Mistake 3: Hindsight Bias

**Bad:** "It was always obvious this would fail."
**Good:** "In retrospect, these warning signs were present, but at the time they were ambiguous."

**Fix:** Acknowledge that foresight ≠ hindsight. Don't pretend everything was obvious.

---

### Mistake 4: Single-Cause Narratives

**Bad:** "Failed because of regulation."
**Good:** "Regulation was necessary but not sufficient. Also needed internal execution failure and market downturn to actually fail."

**Fix:** Multi-causal explanations are almost always more accurate.

---

## Integration with Forecasting

### How Backcasting Improves Forecasts

**Before Backcasting:**
- Forecast: 80% success
- Reasoning: Strong team, good market, solid plan
- Confidence interval: 70-90%

**After Backcasting:**
- Identified failure modes: Regulatory (20%), Execution (15%), Market (10%), Black Swan (5%)
- Total failure probability from backcasting: 50%
- **Realized:** Current 80% is too high
- **Adjusted forecast:** 60% success
- **Adjusted CI:** 45-75% (wider, reflecting uncertainty)

---

## Practical Workflow

### Quick Backcast (15 minutes)

1. **State outcome:** "It failed."
2. **One-sentence cause:** "Failed because..."
3. **Three key events:** Timeline points
4. **Probability check:** Does failure narrative feel >20% likely?
5. **Adjust:** If yes, lower confidence.

---

### Rigorous Backcast (60 minutes)

1. Define future state and resolution date
2. Create timeline working backward in chunks
3. Write detailed narrative for each period
4. Identify causal chains (necessary, sufficient, contributing)
5. Generate 3-5 alternative failure paths
6. Estimate probability of each path
7. Aggregate and compare to current forecast
8. Adjust probability and confidence intervals
9. Set monitoring signposts
10. Document assumptions

---

**Return to:** [Main Skill](../SKILL.md#interactive-menu)
