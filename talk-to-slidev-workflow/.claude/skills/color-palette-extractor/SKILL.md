---
name: color-palette-extractor
description: Extract color palettes from images, websites, or designs. Identifies dominant colors, generates complementary schemes, and exports in multiple formats (HEX, RGB, HSL, Tailwind, CSS variables). Use when users need color schemes from images, brand colors, or design system palettes.
---

# Color Palette Extractor

Extract and generate color palettes from images, websites, and designs.

## Instructions

When a user needs to extract colors from a source:

1. **Identify Source Type**:
   - Image file (PNG, JPG, SVG)
   - Website URL
   - Screenshot
   - Design mockup
   - Existing color code to build palette from

2. **Extract Colors**:

   **From Image**:
   - Analyze pixel data
   - Identify dominant colors
   - Group similar shades
   - Calculate color frequency
   - Sort by prominence

   **From Website**:
   - Fetch and parse CSS
   - Extract color values from stylesheets
   - Identify brand colors
   - Find accent colors
   - Detect text/background colors

   **Color Clustering**:
   - Use K-means clustering
   - Group similar colors
   - Typically extract 5-10 dominant colors
   - Ignore near-white/near-black unless significant

3. **Generate Color Palette**:

   **Primary Palette** (5-10 colors):
   - Most dominant color
   - 2-3 supporting colors
   - 1-2 accent colors
   - Background color
   - Text color

   **Extended Palette**:
   - Light and dark variations
   - Tints (add white)
   - Shades (add black)
   - Tones (add gray)
   - Generate 50, 100, 200...900 scales

4. **Color Harmony Analysis**:

   Generate complementary schemes:
   - **Monochromatic**: Variations of single hue
   - **Analogous**: Adjacent colors on wheel
   - **Complementary**: Opposite colors
   - **Triadic**: Three evenly spaced colors
   - **Split-complementary**: Base + two adjacent to complement
   - **Tetradic**: Four colors (two complementary pairs)

5. **Format Output**:
   ```
   🎨 COLOR PALETTE EXTRACTOR

   Source: [Image/Website URL]

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🎯 PRIMARY PALETTE
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   1. Primary Color
      HEX: #3B82F6
      RGB: rgb(59, 130, 246)
      HSL: hsl(217, 91%, 60%)
      Usage: Main brand color, primary buttons, links
      Prominence: 32%

   2. Secondary Color
      HEX: #8B5CF6
      RGB: rgb(139, 92, 246)
      HSL: hsl(258, 90%, 66%)
      Usage: Accent elements, hover states
      Prominence: 18%

   3. Background
      HEX: #F8FAFC
      RGB: rgb(248, 250, 252)
      HSL: hsl(210, 40%, 98%)
      Usage: Page background, cards
      Prominence: 25%

   4. Text Primary
      HEX: #1E293B
      RGB: rgb(30, 41, 59)
      HSL: hsl(217, 33%, 17%)
      Usage: Body text, headings
      Prominence: 15%

   5. Accent
      HEX: #10B981
      RGB: rgb(16, 185, 129)
      HSL: hsl(158, 84%, 39%)
      Usage: Success states, CTAs
      Prominence: 10%

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🌈 COLOR SCALE (Tailwind-style)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Primary:
     50:  #EFF6FF  [lightest]
     100: #DBEAFE
     200: #BFDBFE
     300: #93C5FD
     400: #60A5FA
     500: #3B82F6  [base]
     600: #2563EB
     700: #1D4ED8
     800: #1E40AF
     900: #1E3A8A  [darkest]
     950: #172554

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🎭 COLOR HARMONY SCHEMES
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Complementary:
     Base: #3B82F6 (blue)
     Complement: #F6823B (orange)

   Analogous:
     #3B82F6 (blue)
     #3BF6D9 (cyan)
     #823BF6 (purple)

   Triadic:
     #3B82F6 (blue)
     #F6823B (orange)
     #82F63B (green)

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   💻 EXPORT FORMATS
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   CSS Variables:
   ```css
   :root {
     --color-primary: #3B82F6;
     --color-secondary: #8B5CF6;
     --color-background: #F8FAFC;
     --color-text: #1E293B;
     --color-accent: #10B981;
   }
   ```

   Tailwind Config:
   ```js
   module.exports = {
     theme: {
       extend: {
         colors: {
           primary: {
             50: '#EFF6FF',
             500: '#3B82F6',
             900: '#1E3A8A',
           },
         }
       }
     }
   }
   ```

   SCSS Variables:
   ```scss
   $primary: #3B82F6;
   $secondary: #8B5CF6;
   $background: #F8FAFC;
   $text: #1E293B;
   $accent: #10B981;
   ```

   JSON:
   ```json
   {
     "primary": "#3B82F6",
     "secondary": "#8B5CF6",
     "background": "#F8FAFC",
     "text": "#1E293B",
     "accent": "#10B981"
   }
   ```

   Android XML:
   ```xml
   <color name="primary">#3B82F6</color>
   <color name="secondary">#8B5CF6</color>
   ```

   iOS Swift:
   ```swift
   extension UIColor {
     static let primary = UIColor(hex: "3B82F6")
     static let secondary = UIColor(hex: "8B5CF6")
   }
   ```

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ♿ ACCESSIBILITY CHECKS
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Contrast Ratios (WCAG 2.1):

   Text on Background:
     #1E293B on #F8FAFC: 14.2:1 ✅ AAA (excellent)

   Primary on Background:
     #3B82F6 on #F8FAFC: 4.8:1 ✅ AA (good)

   White text on Primary:
     #FFFFFF on #3B82F6: 4.6:1 ✅ AA (good)

   Accent on Background:
     #10B981 on #F8FAFC: 3.2:1 ⚠️ AA Large text only

   Recommendations:
   • Use darker shade of accent for small text
   • Primary button text should be white (#FFFFFF)
   • Consider #047857 for better contrast

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   💡 COLOR PSYCHOLOGY
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Blue (#3B82F6):
     • Trust, professionalism, calm
     • Common for: Tech, finance, healthcare

   Purple (#8B5CF6):
     • Creativity, luxury, wisdom
     • Common for: Creative services, premium brands

   Green (#10B981):
     • Growth, success, health
     • Common for: Environmental, finance, wellness

   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🎨 DESIGN SYSTEM INTEGRATION
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Suggested Usage:
   • Primary: Main CTAs, links, active states
   • Secondary: Secondary buttons, highlights
   • Background: Page/card backgrounds
   • Text: Body copy, headings
   • Accent: Success messages, highlights

   Color Roles:
   • Success: #10B981 (green accent)
   • Warning: #F59E0B (generate from palette)
   • Error: #EF4444 (generate complement)
   • Info: #3B82F6 (primary blue)
   ```

6. **Advanced Features**:

   **Color Blindness Simulation**:
   - Test palette for:
     - Protanopia (red-blind)
     - Deuteranopia (green-blind)
     - Tritanopia (blue-blind)
   - Suggest adjustments for accessibility

   **Mood Board**:
   - Generate color combinations
   - Show usage examples
   - Create gradient options

   **Brand Matching**:
   - Compare to existing brand colors
   - Find closest brand matches
   - Suggest similar palettes

## Example Triggers

- "Extract colors from this screenshot"
- "Get color palette from this website"
- "Generate a color scheme from this image"
- "Create Tailwind config from these colors"
- "Find dominant colors in this logo"
- "Build a palette from this hex code"

## Best Practices

**Color Extraction**:
- Filter out near-white/black unless prominent
- Group similar colors (within 10% similarity)
- Weight by visual importance (not just frequency)
- Consider color psychology

**Palette Generation**:
- Maintain color harmony
- Ensure sufficient contrast
- Generate semantic names (primary, accent, etc.)
- Provide light and dark variations

**Accessibility**:
- Check WCAG contrast ratios
- Test with color blindness simulation
- Recommend accessible alternatives
- Ensure text readability

**Export Formats**:
- Support common formats (CSS, Tailwind, iOS, Android)
- Include usage guidelines
- Provide example implementations

## Output Quality

Ensure palettes:
- Have clear dominant colors
- Include sufficient variations
- Pass accessibility checks
- Come with usage guidelines
- Export in multiple formats
- Include color psychology notes
- Show harmony schemes
- Provide contrast ratios
- Work for color-blind users
- Have semantic naming

Generate professional, accessible color palettes ready for immediate use in design systems.
