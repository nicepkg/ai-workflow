---
name: product-strategy
version: "2.0.0"
description: Master product strategy, market analysis, competitive positioning, and long-term product vision. Define business models and craft go-to-market strategies that drive success.
sasmp_version: "1.3.0"
bonded_agent: 01-strategy-vision
bond_type: PRIMARY_BOND
parameters:
  - name: market_context
    type: string
    required: true
    description: Market veya ürün hakkında context
  - name: analysis_type
    type: string
    enum: [tam_sam_som, competitive, positioning, business_model]
retry_logic:
  max_attempts: 3
  backoff: exponential
logging:
  level: info
  hooks: [start, complete, error]
---

# Product Strategy & Vision Skill

Master the art of strategic product thinking. Define winning market positions, identify opportunities, and create compelling visions that guide your entire organization.

## Part 1: Market Analysis Framework

### Market Definition
**TAM (Total Addressable Market)**
- Total revenue opportunity in your market
- Definition: All potential customers who need your solution
- Calculation: (Target customer base) × (avg. contract value)
- Example: B2B SaaS for small business = 5M SMBs × $5K = $25B TAM

**SAM (Serviceable Available Market)**
- Market you can realistically capture
- Definition: Segments you can reach with your go-to-market
- Usually 5-20% of TAM
- More useful for planning

**SOM (Serviceable Obtainable Market)**
- Realistic market share in first 3-5 years
- Definition: What you can actually win with realistic execution
- Usually 1-5% of SAM
- Use for revenue projections

### Competitive Landscape

**Direct Competitors**
- Products serving same customer with same use case
- Examples: Slack vs Teams, Figma vs Adobe XD

**Indirect Competitors**
- Solutions to same problem, different approach
- Examples: Slack vs email, Google Forms vs Typeform

**Alternative Solutions**
- Build in-house, spreadsheets, manual processes
- Often biggest competitor for new categories

**Analyze Each:**
- Product capabilities matrix
- Pricing and positioning
- Target customer segment
- Go-to-market approach
- Strengths and weaknesses
- Market share and growth
- Recent funding/momentum

### Market Trends & Timing

**Questions to Answer:**
- Is the market growing or shrinking?
- What's driving growth?
- Are there macroeconomic tailwinds?
- What regulatory changes are coming?
- Is technology making solutions possible now?
- Are buyers ready to adopt?

**Market Readiness**
- Have customers already tried solutions?
- Are there early adopters?
- Is there pent-up demand?
- Are budget allocations available?

## Part 2: Positioning Strategy

### Value Proposition
Define what you offer that's different and better:

**Template:**
```
For [target customer]
Who [customer need/problem]
The [product name]
Is [product category]
That [key benefit]
Unlike [alternative]
Our product [unique differentiator]
```

**Example (Slack):**
```
For teams that need communication
Who struggle with fragmented tools (email, Skype, etc)
Slack is a messaging platform
That brings all communication into one place
Unlike email (which is async and scattered)
Our product is focused on searchable history and integrations
```

### Positioning Pillars

**3-5 core pillars** that define your position:

1. **Speed** - Faster than alternatives
2. **Ease of Use** - Simpler than competitors
3. **Integration** - Connects to tools they already use
4. **Security** - Enterprise-grade security
5. **Cost** - Better ROI than alternatives

Rate yourself vs competitors on each pillar.

### Target Customer Profile

**Ideal Customer (ICP):**
- Company size (employees, revenue)
- Industry vertical
- Job titles of decision makers
- Annual spend budget
- Current tech stack
- Growth stage (startup, growth, enterprise)

**Why they'll buy:**
- Main pain point you solve
- Secondary pain points
- How success is measured
- What failure looks like

## Part 3: Business Model Design

### Revenue Model Options

**SaaS (Software as a Service)**
- Monthly/annual recurring revenue
- Per user, per seat, per feature tier
- High gross margin (70-80%)
- Pros: Predictable, high LTV
- Cons: Long sales cycle

**Freemium**
- Free tier with limited features
- Paid upgrades for power users
- Good for user acquisition
- Challenge: Converting free to paid

**One-Time Purchase**
- Perpetual license
- Lower LTV than SaaS
- Better for enterprise deals
- Outdated for most categories

**Usage-Based**
- Pay for what you use (GB, API calls, etc)
- Good for variable workloads
- Challenge: Revenue unpredictability

**Marketplace/Commission**
- Take percentage of transactions
- Examples: Stripe, Uber, Airbnb
- High volume, lower margins
- Network effects critical

**Hybrid Models**
- Combine multiple (e.g., SaaS base + usage overage)
- More complex but often optimal

### Pricing Strategy

**Value-Based Pricing**
- Price based on value delivered, not cost
- Most profitable approach
- Requires understanding ROI for customer

**Tiered Pricing**
- Starter, Professional, Enterprise
- Good for catering to different segments
- Prevent feature parity issues

**Per-Seat Pricing**
- Charge per user
- Easy to understand
- Can limit adoption (too expensive for large teams)

**Usage-Based Pricing**
- Charge per API call, GB storage, etc.
- Scales with customer growth
- Harder to predict revenue

**Freemium Conversion Rate**
- Typical: 2-5% free to paid
- Higher for B2B (5-10%)
- Lower for consumer (0.5-2%)

## Part 4: Go-To-Market Strategy

### GTM Channel Selection

**Direct Sales**
- Your team sells to customers
- Best for: High ACV (>$10K), complex product
- Typical sales cycle: 3-6 months
- Cost: High ($200K+/rep + quota)

**Self-Service / Freemium**
- Customers discover and sign up themselves
- Best for: Low ACV (<$1K), self-explanatory
- Typical sales cycle: Minutes to days
- Cost: Low (marketing focused)

**Sales Development (SMB)**
- SDR/AE team for SMB segment
- Typical ACV: $2K-$20K
- Sales cycle: 1-3 months
- More efficient than enterprise

**Channels & Partnerships**
- Resellers, integrations, platforms
- Example: App store, Zapier, AWS Marketplace
- Lower customer acquisition cost
- Channel partnership challenges

### Customer Acquisition Strategy

**CAC (Customer Acquisition Cost)**
- Total sales & marketing spend / new customers
- Target: CAC payback in 12-18 months

**LTV (Lifetime Value)**
- Average revenue × average customer lifetime
- Target: LTV > 3x CAC

**Metrics Formula:**
```
Monthly Revenue Per Customer × Gross Margin %
÷ Monthly Churn Rate
= LTV

Example:
$1000 MRR × 80% / 5% churn = $16,000 LTV
If CAC = $5,000: LTV/CAC = 3.2x ✓
```

### Launch Strategy Timeline

**Option 1: Stealth Launch**
- Build in secret, launch with big bang
- Risk: Misaligned with market needs
- Reward: Surprise, buzz, no competitive pressure

**Option 2: Open Beta**
- Limited availability, lots of transparency
- Risk: Slower growth initially
- Reward: Feedback, hype building, press coverage

**Option 3: Enterprise Sales**
- Deep relationships with early customers
- Risk: Takes longer to scale
- Reward: Higher validation, valuable feedback

## Part 5: Pitching Your Strategy

### Executive Pitch Template (30 minutes)

**1. The Opportunity** (5 min)
- Market size (TAM/SAM/SOM)
- Market growth rate
- Why now (timing)

**2. The Problem** (5 min)
- Customer pain point(s)
- How it's solved today
- Why current solutions are inadequate

**3. Your Solution** (5 min)
- What you're building
- Why you're different
- Key competitive advantages

**4. The Business** (5 min)
- Target customer segment
- Go-to-market strategy
- Revenue model and pricing
- Unit economics projection

**5. The Team** (3 min)
- Why are you uniquely capable
- Relevant background
- Advisors and supporters

**6. The Ask** (2 min)
- How much you're raising
- How you'll use it
- 18-month milestones

### Elevator Pitch (2 minutes)

"[Product] helps [target customer] [solve problem/achieve goal]. Unlike [alternative], we [unique differentiator], which results in [customer benefit]. We're focused on [market segment] and building [key capability]."

## Part 6: Strategy Decisions & Trade-offs

### Key Strategic Questions

1. **Horizontal vs Vertical?**
   - Horizontal: Serve many industries
   - Vertical: Dominate one industry deeply
   - Decision factors: Market size, competition, expertise

2. **High-Touch vs Self-Service?**
   - Impacts CAC, LTV, scaling ability
   - Decision: Customer value + ACV

3. **Niche vs Broad?**
   - Start narrow, expand over time
   - Better to dominate niche than lose in broad market

4. **Premium vs Budget?**
   - Premium: Higher margin, slower growth
   - Budget: Lower margin, faster growth
   - Rarely can do both

5. **First Mover vs Fast Follower?**
   - First mover: Build market, education, but risk
   - Fast follower: Learn from others, better execution
   - Category size matters

## Part 7: Strategy Refinement

### Strategy Review Cadence

**Quarterly:**
- Progress vs. plan
- Competitive changes
- Customer feedback
- Market evolution
- Tactical adjustments

**Annually:**
- Full strategy refresh
- Market assumptions review
- Competitive repositioning
- Long-term vision update

### When to Pivot

**Signs you need a strategic pivot:**
- Low customer demand for current strategy
- Major competitive threat
- Market conditions changed significantly
- Better opportunity emerged
- Team capabilities misaligned
- Unit economics don't work

## Troubleshooting

### Yaygın Hatalar & Çözümler

| Hata | Olası Sebep | Çözüm |
|------|-------------|-------|
| TAM/SAM hesaplama hatası | Yanlış multiplier | Assumptions'ları document et |
| Positioning belirsiz | Çok fazla segment | Single ICP focus |
| Business model sürdürülebilir değil | Unit economics negatif | LTV/CAC analizi |
| GTM channel ineffective | Yanlış channel seçimi | A/B test channels |

### Debug Checklist

```
[ ] TAM/SAM/SOM varsayımları documented mı?
[ ] Competitive matrix güncel mi?
[ ] Value proposition tested mi?
[ ] Pricing sensitivity analyzed mı?
[ ] GTM channel hypothesis validated mı?
```

### Recovery Procedures

1. **Market Size Uncertainty** → Scenario analysis (3 cases)
2. **Positioning Confusion** → Customer interviews for validation
3. **Business Model Issues** → Unit economics deep dive

---

**Master strategy thinking and position your product for long-term success!**
