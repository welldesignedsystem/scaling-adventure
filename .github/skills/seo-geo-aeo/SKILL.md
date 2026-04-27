---
name: audit-seo-geo-aeo
description: Audit websites for Search Engine Optimization (SEO), Generative Engine Optimization (GEO), and Answer Engine Optimization (AEO)
---

# SEO / GEO / AEO Audit Skill for Copilot & VS Code

## Purpose
Automatically audit websites and projects for Search Engine Optimization (SEO), Generative Engine Optimization (GEO), and Answer Engine Optimization (AEO) directly within Copilot and VS Code. Generate structured audit reports and actionable recommendations without leaving your editor.

## When to Use
- User provides a URL, domain, or website name and asks about search performance, SEO issues, or visibility
- Developer wants to audit their own project's public website
- Checking SEO readiness before deploying a new feature or redesign
- Optimizing for AI-powered search engines (Perplexity, ChatGPT Search, Google AI Overviews, Gemini)
- Comparing your site against competitor URLs
- Answer "why isn't my site ranking?", "check my SEO", "optimize for AI search", "audit my site"

Trigger phrases:
- "audit my site"
- "check my SEO"
- "why isn't my site ranking"
- "optimize for AI search"
- "GEO audit"
- "featured snippet optimization"

## Integration with VS Code/Copilot

### Quick Integration Points
1. **Fetch directly from browser**: Use the `fetch_webpage` tool to pull HTML, meta tags, schema markup
2. **Generate reports as Markdown**: Output findings as markdown files in the workspace for easy reference
3. **Create actionable checklists**: Generate VS Code-compatible checklist tasks
4. **Link findings to code**: Create tasks linked to specific files/lines where changes are needed

### Output Formats
- **Inline Chat Report**: Brief summary in Copilot chat (1-2 minutes)
- **Workspace Report**: Detailed markdown file saved to workspace for review
- **Quick Checklist**: TODO items that can be tracked in VS Code

## Audit Methodology

### Step 1: Confirm Audit Scope
Ask the user: **"Would you like a Quick Audit (overview + top issues — 2-3 minutes) or Full Audit (comprehensive analysis — 5-10 minutes)?"**

Wait for explicit confirmation. No exceptions.

### Step 2: Gather Data
**Phase 2a: Discover site structure**
- Fetch the provided URL's complete HTML
- Extract all meta tags, schema markup, headings, links, navigation
- Discover `robots.txt` and `sitemap.xml` to understand site structure

**Phase 2b: Crawl key pages** (in parallel when possible)
- About / Team page (E-E-A-T signals)
- Services / Products page (content depth, keywords)
- Case Studies / Portfolio (social proof, trust)
- Blog / Resources page (content strategy, AEO)
- Contact / Location page (NAP data)
- FAQ page (featured snippet potential)

Quick Audit: Homepage + up to 6 high-signal pages  
Full Audit: All meaningful pages (skip only Privacy, Terms, login pages, beyond page 2 archives)

**Phase 2c: Handle inaccessible content**
- If URL fails: confirm accessibility with user, offer framework audit
- If individual pages fail: note in findings, continue with available data

### Step 3: Analyze Signals

#### SEO Signals (Traditional Search Engine Optimization)
**Technical On-Page:**
- Title tag: Present? Length 50-60 chars? Contains primary keyword? Unique across site?
- Meta description: Present? Length 150-160 chars? Contains CTA? Engaging?
- Heading hierarchy: H1 unique and present? H2/H3 logical and keyword-relevant?
- URL structure: Clean, readable, keyword-relevant?
- Canonical tag: Present and self-referencing?
- Robots meta: Indexable? No accidental noindex?
- Mobile viewport meta: Present?
- Image alt text: Descriptive and keyword-relevant?
- Internal links: Present with descriptive anchor text?
- Open Graph / Twitter Cards: Present for social sharing?

**Content Quality:**
- Word count: Substantial (500+ for most pages, 1500+ for pillar content)?
- Keyword signals: Primary topic clear? Semantic related terms present?
- Freshness: Publication/update dates visible?
- Readability: Scannable with subheadings, short paragraphs, bullets?

**Structured Data:**
- Schema markup present? (JSON-LD, microdata)
- Types detected: Organization, LocalBusiness, Article, Product, FAQ, HowTo, BreadcrumbList?
- Schema validity: Syntactically correct and complete?

#### GEO Signals (Generative Engine Optimization)
Optimizes for AI-powered search engines (Perplexity, ChatGPT Search, Google AI Overviews, Gemini).

**E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness):**
- Author information: Named authors with credentials?
- About page: Who runs it? Background and qualifications?
- Contact information: Phone, address, email accessible?
- Trust signals: Testimonials, awards, certifications, press mentions?
- Organization schema: Brand entity declared clearly (name, logo, URL, social profiles)?

**Content for AI Synthesis:**
- Factual density: Specific facts, statistics, data AI can cite?
- Clear claims: Core argument/value prop stated plainly at top?
- Source citation: References to authoritative external sources?
- Comprehensiveness: Fully addresses topic or leaves questions unanswered?
- Entity clarity: Brand/person/place named clearly and consistently?
- Originality signals: Clear POV, original data, unique perspective?

**Technical GEO:**
- Structured data depth: Rich, specific types (Author, Dataset, ClaimReview, SpeakableSpecification)?
- HTTPS / security: Secure site?
- Clean crawlability: No robots.txt blocks, JavaScript doesn't block crawlers?
- Same-as / brand entity links: Social profile links from site (strengthens entity graph)?

#### AEO Signals (Answer Engine Optimization)
Optimizes for featured snippets, People Also Ask, and voice search.

**Featured Snippet Eligibility:**
- Direct answer paragraphs: Key question answered in 40-60 word paragraph below question heading?
- Definition patterns: Clear "X is..." definition sentences?
- List content: Numbered steps or bulleted lists?
- Table content: Comparison tables?

**Structured Answer Formats:**
- FAQ schema: Present and correctly structured?
- HowTo schema: Step-by-step processes marked up?
- Question-phrased headings: Natural question language in H2/H3?
- Speakable schema: SpeakableSpecification markup for voice-friendly sections?

**Voice Search Readiness:**
- Conversational language: Natural, conversational phrasing?
- Long-tail question coverage: Addresses who/what/when/where/why/how questions?
- Local signals: NAP data, local schema, location mentions (if applicable)?

### Step 4: Score & Assess

Score each category 1-10:
- **1-3**: Critical issues — site likely penalized or invisible
- **4-5**: Below average — significant missed opportunities
- **6-7**: Decent foundation — specific improvements needed
- **8-9**: Strong — minor refinements available
- **10**: Exemplary — model implementation

## Reporting in VS Code

### Chat Report (Inline)
Keep brief and scannable:
```
🔍 [Site Name] — [Quick/Full] SEO/GEO/AEO Audit

Pages reviewed: [count]
Audit date: [date]

| Dimension | Score | Status | Summary |
|-----------|-------|--------|---------|
| SEO | X/10 | [Needs Work / On Track / Strong] | [One sentence] |
| GEO | X/10 | [Needs Work / On Track / Strong] | [One sentence] |
| AEO | X/10 | [Needs Work / On Track / Strong] | [One sentence] |

**Top 3 Priorities:**
1. [Specific action] — [why it matters]
2. [Specific action] — [why it matters]
3. [Specific action] — [why it matters]

**Biggest Strength:**
[One sentence with specific evidence]
```

### Workspace Report (Markdown)
Create a `AUDIT_REPORT_[domain]_[date].md` file in workspace with:
- Executive summary
- Detailed findings by category (SEO, GEO, AEO)
- Pages audited (list)
- Signal-by-signal analysis
- Priority recommendations matrix
- What's working well
- Next steps

### Checklist Format
Generate a checklist as markdown comments or VS Code task items:
```markdown
## SEO Fixes
- [ ] Update title tags to 50-60 characters
- [ ] Add missing meta descriptions
- [ ] Fix H1 hierarchy on [specific pages]

## GEO Improvements
- [ ] Add author schema markup
- [ ] Expand About page with credentials
- [ ] Add organizational schema

## AEO Optimization
- [ ] Create FAQ schema for FAQ page
- [ ] Convert [section] to question-answer format
- [ ] Add Speakable markup to key sections
```

## Best Practices

### Specificity First
- Never flag "missing" content unless you've confirmed it doesn't exist
- Quote actual text when illustrating problems
- Reference exact page URLs and headings
- Don't suggest adding "Team page" if one exists but is low-quality — evaluate what's there

### Be Honest About Limitations
Some signals require external tools:
- **Core Web Vitals** → Google PageSpeed Insights
- **Backlink profile** → Ahrefs, SEMrush, Moz
- **Domain authority** → Third-party tools
- **Mobile rendering** → Google Mobile-Friendly Test
- **JavaScript rendering** → Playwright or headless browser testing

### Calibrate Tone
- If site is in good shape, say so — don't manufacture problems
- If serious issues exist, communicate urgency appropriately
- Explain GEO/AEO if the user seems unfamiliar (1-2 sentences max)

### Make Every Recommendation Actionable
- Link findings to specific pages/sections
- Prioritize by impact and effort
- Include examples of what good looks like
- Suggest next steps for learning more

## Usage Examples

**User**: "audit my website example.com"
```
1. Ask: Quick or Full Audit?
2. Fetch example.com + key pages in parallel
3. Analyze signals across all 3 dimensions
4. Present scores and top 3 priorities in chat
5. Generate detailed markdown report in workspace
6. Offer next steps: "Would you like to dig deeper into any area?"
```

**User**: "check my SEO for site:myproject.dev"
```
Same process, but contextualize for a dev project:
- Is the project docs/homepage crawlable?
- Are code examples in snippets indexed?
- Does it have proper meta tags?
- Is there structured data for tutorials or API docs?
```

**User**: "optimize my site for AI search"
```
Focus heavily on GEO:
- E-E-A-T signals (author info, credentials, trust)
- Factual density and originality
- Entity clarity
- Prioritize GEO over traditional SEO if user goal is AI visibility
```

## Key Differences from Agency Version

1. **No Word/PDF generation**: Output markdown files for VS Code, not .docx
2. **Integrated in chat**: Full audit happens in Copilot chat, not external tools
3. **Workspace-linked**: Generate files saved to workspace for easy reference
4. **Developer context**: Suggestions frame around "before pushing to production", "add to your build checklist"
5. **Code-focused**: If auditing a dev project, relate findings to actual code/config files
6. **Faster output**: Quick Audits emphasize speed; Full Audits still thorough but VS Code-friendly

## Important Principles

1. **Audit the whole site**: URL provided is starting point, not the whole picture
2. **Crawl before concluding**: Never skip fetching key pages
3. **Be specific and honest**: Reference actual observed findings
4. **Make reports actionable**: Every finding should lead to a concrete next step
5. **Respect user's time**: Balance thoroughness with brevity for chat context
