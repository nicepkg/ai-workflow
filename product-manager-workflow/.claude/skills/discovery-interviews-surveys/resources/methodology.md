# Discovery Interviews & Surveys - Advanced Methodology

## 1. Jobs-to-be-Done (JTBD) Switch Interviews

**When to use**: Understanding why users switch products, identifying hiring/firing triggers.

**Process**:
1. Recruit recent switchers (adopted product in last 3-6 months—memory is fresh)
2. Reconstruct timeline from first thought to current state (forces of progress)
3. Identify push (problems with old solution), pull (attraction to new), anxiety (concerns about new), habit (inertia keeping old)

**Forces of progress framework**:
- **Push**: What problems pushed you away from old solution?
- **Pull**: What attracted you to new solution?
- **Anxiety**: What concerns almost stopped you?
- **Habit**: What kept you using old solution despite problems?

**Key questions**:
- "When did you first realize [old solution] wasn't working?" (First thought—passive)
- "What event made you start actively looking?" (Trigger—active)
- "What did you consider? How did you evaluate?" (Consideration)
- "What almost made you not switch?" (Anxiety)
- "What was the deciding factor?" (Decision moment)

**Output**: Hiring triggers, firing triggers, evaluation criteria, anxieties, decision drivers.

---

## 2. Kano Analysis (Feature Prioritization)

**When to use**: Deciding which features to build based on satisfaction impact.

**Categories**:
- **Must-have** (basic): Dissatisfaction if absent, no extra satisfaction if present
- **Performance** (linear): More is better—satisfaction increases linearly
- **Delight** (exciter): Big satisfaction if present, no dissatisfaction if absent
- **Indifferent**: No impact either way
- **Reverse**: Some users want it, others don't

**Survey approach**:
For each feature, ask 2 questions:
1. "How would you feel if [feature] WAS present?" (Functional)
   - I like it / I expect it / I'm neutral / I can tolerate it / I dislike it
2. "How would you feel if [feature] WAS NOT present?" (Dysfunctional)
   - I like it / I expect it / I'm neutral / I can tolerate it / I dislike it

**Classification matrix**: Cross-reference functional vs dysfunctional responses to categorize feature.

**Prioritization**:
1. Must-haves first (absence causes dissatisfaction)
2. Performance features second (linear satisfaction gain)
3. Delighters third (differentiation, but not required)

---

## 3. Thematic Coding for Interview Analysis

**Process**:
1. **Familiarization**: Read all transcripts once without coding
2. **Open coding**: Highlight interesting quotes, note initial themes (bottom-up)
3. **Axial coding**: Group codes into broader themes
4. **Selective coding**: Identify core themes, relationships between themes
5. **Frequency counting**: How many participants mentioned each theme?
6. **Saturation check**: Did new interviews reveal new themes, or just confirm existing?

**Rigor techniques**:
- **Inter-rater reliability**: Two coders independently code subset, compare agreement
- **Negative case analysis**: Actively look for quotes that contradict main themes
- **Thick description**: Provide rich context, not just quotes
- **Audit trail**: Document coding decisions

**Software tools**: NVivo, Atlas.ti, or spreadsheet with color-coding.

---

## 4. Statistical Analysis for Surveys

**Descriptive statistics**:
- **Central tendency**: Mean, median, mode
- **Spread**: Standard deviation, range, interquartile range
- **Distribution**: Histogram, check for normality

**Inferential statistics**:
- **t-test**: Compare means between two groups (e.g., users vs non-users)
- **ANOVA**: Compare means across 3+ groups
- **Chi-square**: Test association between categorical variables
- **Correlation**: Relationship between two continuous variables (Pearson's r)

**Sample size requirements**:
- **Minimum for statistical power**: n ≥ 30 per segment
- **Margin of error**: ±5% at 95% confidence requires n ≈ 400 (for population > 10K)
- **For small populations**: Use finite population correction

**Segmentation**:
- Divide sample by demographics, behavior, or attitudes
- Compare segments on key metrics (e.g., satisfaction, willingness to pay)
- Ensure each segment has n ≥ 30 for valid comparisons

---

## 5. Bias Mitigation Techniques

**Common biases**:
- **Confirmation bias**: Seeking evidence that confirms pre-existing beliefs
- **Leading questions**: Telegraphing desired answer
- **Social desirability bias**: Participants say what they think you want to hear
- **Selection bias**: Non-representative sample
- **Recency bias**: Overweighting recent experiences
- **Hindsight bias**: Rewriting history post-hoc

**Mitigation strategies**:
1. **Avoid leading questions**: Bad: "Don't you think our UI is confusing?" Good: "Walk me through using this feature."
2. **Focus on behavior, not attitudes**: Bad: "Do you value security?" Good: "Tell me about the last time security mattered in your decision."
3. **Use concrete examples**: Bad: "How important is speed?" Good: "Show me your current workflow. Where do you wait?"
4. **Recruit diverse sample**: Include detractors, not just enthusiasts. Screen for demographics and behaviors.
5. **Blind analysis**: Analyze data without knowing which participant is which (if possible).
6. **Pre-register hypotheses**: Document what you expect to find before data collection.

---

## 6. Participant Recruitment Strategies

**Approaches**:

**For existing users**:
- **In-app invite**: Email or in-app message to random sample
- **Behavior-triggered**: Invite after specific action (e.g., canceled subscription, completed onboarding)
- **Support tickets**: Recruit from users who contacted support
- **Incentive**: Gift card, product credits, donation to charity

**For non-users/prospects**:
- **User testing platforms**: UserTesting, Respondent, User Interviews
- **Social media**: LinkedIn, Twitter, Facebook groups
- **Snowball sampling**: Ask interviewees to refer others
- **Panel providers**: Qualtrics, Prolific (for surveys)
- **Community forums**: Reddit, Slack communities, Discord

**Screening**:
- Use short survey (3-5 questions) to qualify
- Check for disqualifiers (competitors, never used category, outside target)
- Over-recruit by 20-30% to account for no-shows

**Sample size guidance**:
- **Qualitative interviews**: 5-15 (themes emerge by interview 5-8, saturation by 12-15)
- **Quantitative surveys**: 100+ for basic stats, 400+ for ±5% margin of error, 30+ per segment for comparisons

---

## 7. Interview Facilitation Best Practices

**Before interview**:
- Review objectives and guide
- Set up recording (with participant permission)
- Prepare backup note-taking system
- Join 5 min early to check tech

**During interview**:
- **Active listening**: Focus on what they say, not your next question
- **Follow the energy**: If they get excited or frustrated, dig deeper
- **Embrace silence**: Pause 3-5 seconds after asking. Let them think.
- **Use mirroring**: Repeat last few words to encourage elaboration
- **Ask "why" sparingly**: Can sound accusatory. Use "What prompted..." "What mattered..."
- **Probe with "tell me more"**: When they hint at something interesting
- **Show don't tell**: Ask to screen-share, demonstrate, show artifacts (spreadsheets, tools)
- **Watch non-verbal**: Hesitation, confusion, workarounds reveal truth

**After interview**:
- Debrief: Write 3-5 key takeaways immediately
- Save recording and transcript
- Thank participant, send compensation
- Update sampling tracker (did they fit profile? Any biases?)

---

## 8. Survey Design Best Practices

**Question types**:
- **Likert scale** (1-5 agreement): "I am satisfied with [product]"
- **Semantic differential** (bipolar): Fast [1-7] Slow
- **Multiple choice** (single select): "Which do you prefer?"
- **Checkbox** (multi-select): "Which of these have you used?"
- **Ranking**: "Rank these features 1-5"
- **Open-ended**: "What is the biggest challenge you face?"
- **Matrix**: Rows = items, columns = rating scale

**Order effects**:
- Start with engaging, easy questions (not demographics)
- Group related questions
- Randomize option order (except ordered scales)
- Put demographics at end
- Avoid fatigue: Keep surveys < 10 min (15-20 questions)

**Response scales**:
- **5-point** (standard): Very dissatisfied, Dissatisfied, Neutral, Satisfied, Very satisfied
- **Odd vs even**: Odd (5-point) allows neutral, even (4-point) forces choice
- **Labeled vs numeric**: Fully labeled preferred for clarity

**Pilot testing**:
- Test with 5-10 people before launch
- Check for confusing questions, technical issues, time to complete
- Iterate based on feedback

---

## 9. Continuous Discovery Practices

**Weekly interview cadence**:
- Schedule 3-5 customer conversations per week (15-30 min each)
- Rotate team members (product, design, eng)
- Focus rotates based on current priorities (new features, onboarding, retention, etc.)

**Process**:
1. **Recruiting**: Automated email to random sample, quick scheduling link
2. **Conducting**: Lightweight interview guide, record main points
3. **Sharing**: Post key quotes/insights in shared Slack channel or doc
4. **Synthesis**: Monthly review of patterns across all conversations

**Benefits**:
- Continuous learning loop
- Early problem detection
- Relationship building with customers
- Team alignment (everyone hears customer voice)

**Tools**: Calendly for scheduling, Zoom for calls, Dovetail or Notion for notes.

---

## 10. Mixed Methods Approach

**Sequential**:
- Phase 1 (Qual): Interviews to discover problems and generate hypotheses (n=10-15)
- Phase 2 (Quant): Survey to validate findings at scale (n=100-500)

**Example**:
- Interviews: "Users mention pricing confusion" (theme in 8/12 interviews)
- Survey: Test hypothesis—"65% of users find pricing page confusing" (validated at scale)

**Concurrent**:
- Run interviews and surveys simultaneously
- Use interviews for depth (why), surveys for breadth (how many)

**Triangulation**:
- Interviews: What users say
- Surveys: What users report
- Analytics: What users do
- Convergence across methods = high confidence

---

## 11. Ethical Considerations

**Informed consent**:
- Explain research purpose, how data will be used
- Get explicit permission to record
- Allow opt-out at any time

**Privacy**:
- Anonymize participant data in reports (use P1, P2, etc.)
- Store recordings securely, delete after transcription (or per policy)
- Don't share personally identifiable information

**Compensation**:
- Fair compensation for time ($50-150 for 60 min interview, $10-25 for survey)
- Offer choice (gift card, donation, product credit)
- Pay promptly (within 1 week)

**Vulnerable populations**:
- Extra care with children, elderly, disabled, marginalized groups
- May require IRB approval for academic/medical research
