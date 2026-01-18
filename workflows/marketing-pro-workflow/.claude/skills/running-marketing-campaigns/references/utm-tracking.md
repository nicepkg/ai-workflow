# UTM Parameters & Campaign Tracking

Standards, naming conventions, and GA4 alignment for accurate campaign attribution.

## Contents

- [The Five UTM Parameters](#the-five-utm-parameters)
- [Naming Convention Standards](#naming-convention-standards)
- [GA4 Channel Alignment](#ga4-channel-alignment)
- [Common Mistakes](#common-mistakes)
- [Dynamic Parameters for Ads](#dynamic-parameters-for-ads)
- [QR Code Tracking](#qr-code-tracking)
- [UTM Governance](#utm-governance)

---

## The Five UTM Parameters

### Parameter Reference

| Parameter | Purpose | Required | Position |
|-----------|---------|----------|----------|
| utm_source | WHERE traffic originates | ✅ Yes | 1st |
| utm_medium | HOW traffic arrives | ✅ Yes | 2nd |
| utm_campaign | Specific marketing initiative | ✅ Yes | 3rd |
| utm_term | Paid search keywords | ❌ Optional | 4th |
| utm_content | Differentiates similar content | ❌ Optional | 5th |

### utm_source (Required)

| Channel | Recommended Values |
|---------|-------------------|
| Google | `google` |
| Facebook | `facebook` |
| Instagram | `instagram` |
| LinkedIn | `linkedin` |
| Twitter/X | `twitter` or `x` |
| TikTok | `tiktok` |
| Email | `newsletter`, `klaviyo`, `mailchimp` |
| QR code | `qr` |
| Partner | `partner-name` |

### utm_medium (Required)

| Medium Type | Recommended Values |
|-------------|-------------------|
| Paid search | `cpc`, `ppc` |
| Paid social | `paid-social`, `cpc` |
| Organic social | `social`, `organic-social` |
| Email | `email` |
| Display ads | `display`, `banner`, `cpm` |
| Affiliate | `affiliate` |
| Referral | `referral` |

### utm_campaign (Required)

**Naming pattern:** `[type]-[name]-[date/version]`

| Example | Meaning |
|---------|---------|
| `spring-sale-2025` | Seasonal promotion |
| `product-launch-v2` | Product launch, version 2 |
| `webinar-seo-basics-mar25` | Webinar campaign |

### utm_content (Optional)

| Example | Use Case |
|---------|----------|
| `header-cta` | CTA in header |
| `sidebar-banner` | Banner placement |
| `blue-button` | Button variant |
| `link-1`, `link-2` | Multiple links in email |

---

## Naming Convention Standards

### Critical Formatting Rules

| Rule | Correct | Incorrect |
|------|---------|-----------|
| **Always lowercase** | `facebook` | `Facebook`, `FACEBOOK` |
| **No spaces** | `spring-sale` | `spring sale` |
| **Use hyphens** | `product-launch` | `product_launch` |
| **No special characters** | `q1-2025` | `q1/2025`, `q1&2025` |

**GA4 is case-sensitive.** `Facebook`, `facebook`, and `FACEBOOK` track as three different sources.

### URL Structure

```
https://example.com/landing-page
?utm_source=facebook
&utm_medium=paid-social
&utm_campaign=spring-sale-2025
&utm_content=carousel-ad-1
```

**Key rules:**
- First parameter starts with `?`
- Subsequent parameters use `&`
- No spaces anywhere

---

## GA4 Channel Alignment

UTM parameters must align with GA4's default channel definitions.

### Default Channel Groupings

| Channel | Source Match | Medium Match |
|---------|--------------|--------------|
| **Paid Search** | Google, Bing search sites | `cpc`, `ppc`, `paid.*` |
| **Paid Social** | Social network sites | `cpc`, `ppc`, `paid-social` |
| **Organic Social** | Social network sites | `social`, `organic-social` |
| **Email** | Any | `email`, `e-mail`, `e_mail` |
| **Affiliates** | Any | `affiliate` |
| **Referral** | Any | `referral` |
| **Display** | Any | `display`, `banner`, `cpm` |

### Email Configuration

| Parameter | Acceptable Values |
|-----------|-------------------|
| utm_medium | `email`, `e-mail`, `e_mail` |
| utm_source | Any (newsletter, klaviyo, etc.) |

---

## Common Mistakes

### Mistake Checklist

| Mistake | Problem | Fix |
|---------|---------|-----|
| **Inconsistent case** | `Facebook` ≠ `facebook` | Always lowercase |
| **Spaces in values** | URL breaks | Use hyphens |
| **Swapped source/medium** | Misattribution | Source = WHO, Medium = HOW |
| **Tagged internal links** | Overwrites attribution | Never tag internal navigation |
| **Missing `?`** | Parameters not recognized | Always start with `?` |
| **Using `&` for first param** | First parameter ignored | First uses `?` |

### Internal Link Warning

**Never tag internal links.** When a user clicks an internal link with UTM parameters:
- Original source is overwritten
- Session may restart
- Attribution is destroyed

### Troubleshooting "Direct" Traffic

| Check | Solution |
|-------|----------|
| UTMs present in URL? | Verify links include parameters |
| Correct `?` and `&` usage? | First param `?`, rest `&` |
| Redirects stripping UTMs? | Test final destination URL |

---

## Dynamic Parameters for Ads

### Meta (Facebook/Instagram) Ads

```
utm_source={{site_source_name}}
&utm_medium=paid-social
&utm_campaign={{campaign.name}}
&utm_content={{adset.name}}-{{ad.name}}
```

| Parameter | Dynamic Value | Output Example |
|-----------|---------------|----------------|
| `{{site_source_name}}` | Platform | `fb`, `ig` |
| `{{campaign.name}}` | Campaign name | `spring-sale-2025` |
| `{{adset.name}}` | Ad set name | `lookalike-1pct` |
| `{{ad.name}}` | Ad name | `carousel-v1` |

### Google Ads (ValueTrack)

```
utm_source=google
&utm_medium=cpc
&utm_campaign={campaignid}
&utm_content={creative}
&utm_term={keyword}
```

| Parameter | Dynamic Value |
|-----------|---------------|
| `{campaignid}` | Campaign ID |
| `{creative}` | Ad ID |
| `{keyword}` | Keyword triggered |
| `{matchtype}` | Match type (b, p, e) |

**Note:** If Google Ads auto-tagging is enabled, avoid UTMs to prevent duplicate data.

### LinkedIn Ads

```
utm_source=linkedin
&utm_medium=paid-social
&utm_campaign={campaign_name}
&utm_content={creative_name}
```

### TikTok Ads

```
utm_source=tiktok
&utm_medium=paid-social
&utm_campaign=__CAMPAIGN_NAME__
&utm_content=__AID_NAME__
```

---

## QR Code Tracking

Without UTMs, QR scans appear as "Direct" traffic.

### QR Code UTM Template

```
utm_source=qr
&utm_medium=offline
&utm_campaign=[campaign-name]
&utm_content=[placement]
```

### QR Code Placements

| Placement | utm_content Value |
|-----------|-------------------|
| Product packaging | `packaging` |
| Business card | `business-card` |
| Flyer | `flyer-[location]` |
| Billboard | `billboard-[location]` |
| Event booth | `event-[name]` |
| Print ad | `print-[publication]` |

---

## UTM Governance

### Team Documentation Template

```markdown
# UTM Naming Standards - [Company Name]

## Approved Sources
- google, facebook, instagram, linkedin, twitter
- newsletter, [email-tool-name]
- partner-[name]

## Approved Mediums
- cpc, paid-social, social, email, display, affiliate, referral

## Campaign Naming Convention
Pattern: [type]-[name]-[date]
Types: promo, launch, event, content, retarget

## Examples
- promo-black-friday-nov24
- launch-product-v2-q1
- event-webinar-seo-mar25
```

### Monthly Audit Checklist

- [ ] Review GA4 for "Unassigned" traffic
- [ ] Check for case inconsistencies
- [ ] Verify new campaigns follow standards
- [ ] Update documentation
- [ ] Test sample URLs from active campaigns

---

## Quick Reference

### UTM Parameter Cheat Sheet

```
?utm_source=[where-from]
&utm_medium=[how-arrived]
&utm_campaign=[which-campaign]
&utm_content=[which-variant]    (optional)
&utm_term=[which-keyword]       (optional)
```

### Copy-Paste Templates

**Email campaign:**
```
?utm_source=newsletter&utm_medium=email&utm_campaign=[campaign-name]&utm_content=[link-position]
```

**Paid social (Facebook):**
```
?utm_source=facebook&utm_medium=paid-social&utm_campaign=[campaign-name]&utm_content=[ad-name]
```

**Organic social (LinkedIn):**
```
?utm_source=linkedin&utm_medium=social&utm_campaign=[campaign-name]
```

**QR code:**
```
?utm_source=qr&utm_medium=offline&utm_campaign=[campaign-name]&utm_content=[placement]
```

### Validation Checklist

- [ ] All lowercase
- [ ] No spaces (hyphens only)
- [ ] Source/medium not swapped
- [ ] First parameter uses `?`
- [ ] Subsequent parameters use `&`
- [ ] URL works in incognito
- [ ] Not applied to internal links
