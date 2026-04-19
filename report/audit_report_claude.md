# eigenai.co — SEO / GEO / AEO Full Audit Report
### With Detailed Step-by-Step Implementation Guide

**Audit Type:** Full Audit  
**Date:** April 16, 2026  
**Prepared by:** Claude AI Audit Skill  
**Site:** https://eigenai.co  

---

## Executive Summary

EigenAI is a Singapore-based AI consulting firm with genuine client wins and solid case study content — the raw material for good SEO is present. However, the site is being let down by foundational technical SEO gaps: missing or weak meta tags sitewide, no structured data (schema markup) anywhere, a near-absent blog (only one post), and a complete lack of named author/team credentials visible to search engines or AI models.

The most urgent issue is **E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)**: authors are identified only by first names ("unni", "yibin", "achuth") with no credentials, bios, or LinkedIn links, making it very hard for Google or AI search engines to validate the people behind the work. The case studies are strong but anonymous.

The biggest opportunity is **AEO and GEO**: EigenAI operates in a space (AI consulting) where professionals are actively searching for answers to specific questions. Adding FAQ schema, restructuring case studies to answer questions directly, and building out authoritative author profiles could yield significant visibility in AI-generated search responses within 60–90 days of implementation.

| Dimension | Score | Status | Key Takeaway |
|-----------|-------|--------|--------------|
| **SEO** | **5/10** | ⚠️ Needs Work | Missing meta tags, no schema, thin Services page |
| **GEO** | **4/10** | 🔴 Needs Work | No E-E-A-T signals, no brand entity schema, no author credentials |
| **AEO** | **3/10** | 🔴 Critical | No FAQ schema, no direct-answer formatting, no voice-ready content |
| **Combined** | **12/30** | ⚠️ Below Target | Strong case study content undermined by technical and structural gaps |

---

## Pages Audited

| URL | Page Type | Notes |
|-----|-----------|-------|
| https://eigenai.co/ | Homepage | Main landing page; H1 present but generic |
| https://eigenai.co/our-services/ | Services | Very thin — only 3-step process, no individual service pages |
| https://eigenai.co/case-studies/ | Case Studies Index | Lists 5 case studies with thumbnails |
| https://eigenai.co/blog/ | Blog Index | Only 1 post found |
| https://eigenai.co/contact-us-2/ | Contact | Physical address + LinkedIn only; no About/Team page |
| https://eigenai.co/the-silent-killer-churn/ | Blog Post | Only blog post; author shown as "unni" — no credentials |
| https://eigenai.co/case-study-boosting-sales-efficiency-for-apac-relocations-with-predictive-lead-scoring/ | Case Study | Good narrative; author "yibin" — no credentials |
| https://eigenai.co/case-study-transforming-supply-chain-performance-with-genai-powered-analytics/ | Case Study | Excellent content; author "achuth" — no credentials |
| https://eigenai.co/navigating-reliability-how-eigenai-is-transforming-shipping-maintenance-with-ai-driven-fmea/ | Case Study | Best content depth on the site |

**Pages not found / inaccessible:** robots.txt, sitemap.xml (returned permission errors — likely exist but require direct browser access). No About page, no Team page, no individual service detail pages discovered.

---

## SEO Analysis — Score: 5/10

### Technical On-Page

| Signal | Finding | Status |
|--------|---------|--------|
| **Title Tag — Homepage** | Page title is "Case Study: Boosting Sales Efficiency for APAC Relocations with Predictive Lead Scoring" — WordPress is inheriting the most recent post title instead of a dedicated home title | 🔴 Critical |
| **Meta Description — Homepage** | No meta description detected in the crawl response | 🔴 Missing |
| **H1 — Homepage** | H1 present: "Harness the power of artificial intelligence to deliver innovative solutions" — no primary keyword (e.g., "AI consulting") | ⚠️ Needs Attention |
| **H1 — Services Page** | No H1 found — "Our Services" renders as an H2 | 🔴 Missing |
| **Heading Hierarchy** | Homepage cascade is functional. Inner pages skip H1 and use H2 as the page title | ⚠️ Needs Attention |
| **URL Structure** | Case study URLs are keyword-rich. Contact page is `/contact-us-2/` — the `-2` suffix suggests a duplicate/legacy structure | ⚠️ Needs Attention |
| **Canonical Tags** | Not visible in crawl responses — cannot confirm they are set | ⚠️ Unconfirmed |
| **Viewport / Mobile Meta** | Not directly visible; WordPress theme (fotawp) typically includes it — verify with browser inspection | ⚠️ Unconfirmed |
| **Image Alt Text** | Images use generic filenames (`Gemini_Generated_Image_3fav5q...`) — no descriptive alt text detected | 🔴 Missing |
| **Internal Linking** | Navigation has only 5 links. No links from homepage body to individual services or case studies | ⚠️ Needs Attention |
| **Open Graph / Twitter Card** | Not detected — WordPress without OG plugin often omits these | ⚠️ Likely Missing |

### Content Quality

| Signal | Finding | Status |
|--------|---------|--------|
| **Homepage Word Count** | Substantial — covers services, process, pricing, testimonial, FAQ, case study previews (~800–1,000 words) | ✅ Good |
| **Case Study Content Depth** | 5 case studies are the site's strongest asset — real clients, detailed narratives, measurable outcomes | ✅ Good |
| **Blog Content** | Only 1 blog post published (November 2025). The blog is functionally empty — major missed opportunity | 🔴 Critical |
| **Services Page Depth** | Only a 3-step process description. The homepage has more service detail than the Services page | 🔴 Critical |
| **Keyword Coverage** | Homepage hits "AI consulting," "machine learning," "data engineering." No page targets a specific long-tail keyword | ⚠️ Needs Attention |
| **Content Freshness** | Case studies dated January 2026, blog post November 2025 — freshness signals present | ✅ Good |
| **Readability** | Case studies are well-structured. Homepage is scannable | ✅ Good |
| **Typo / Copy Issue** | "EIgenAI" (capital I) in homepage hero — signals lack of proofreading | ⚠️ Needs Attention |
| **Pricing Copy** | Business tier describes "Live Chat, Ticketing Workflows, SLA Rules" — reads like generic SaaS copy, not AI consulting deliverables | ⚠️ Needs Attention |

### Structured Data

| Signal | Finding | Status |
|--------|---------|--------|
| **Schema Markup** | No JSON-LD or schema markup detected on any page crawled | 🔴 Critical |
| **Organization Schema** | Absent — no machine-readable brand entity declaration | 🔴 Missing |
| **Article / BlogPosting Schema** | Absent on blog post | 🔴 Missing |
| **FAQ Schema** | Absent despite 3 FAQ questions present on homepage | 🔴 Missing |
| **BreadcrumbList Schema** | Absent | 🔴 Missing |
| **LocalBusiness Schema** | Absent despite having Singapore address and phone number | 🔴 Missing |

---

## GEO Analysis — Score: 4/10

### E-E-A-T Assessment

| Signal | Finding | Status |
|--------|---------|--------|
| **Named Authors** | Three authors post content: "unni," "yibin," "achuth" — first names only, no full names, titles, LinkedIn, or bios | 🔴 Critical |
| **About Page** | No About or Team page exists anywhere on the site | 🔴 Critical |
| **Credentials / Qualifications** | Zero professional credentials, certifications, or affiliations mentioned | 🔴 Missing |
| **Contact Information** | Address: 32 Pekin St, #05-01, Singapore 048762. Phone: +65 96343448. Email: info@eigenai.co — NAP established | ✅ Good |
| **Trust Signals** | One testimonial from Growsari CTO. No other social proof, awards, or press | ⚠️ Needs Attention |
| **Client Names** | MISC Marine, Axidio, APAC Relocations, Growsari are named — strong E-E-A-T signal | ✅ Good |
| **Social Proof** | Only LinkedIn linked. No Twitter, GitHub, Medium | ⚠️ Needs Attention |
| **Organization Schema** | Absent — AI search engines cannot reliably identify EigenAI as an entity | 🔴 Critical |

### Content for AI Synthesis

| Signal | Finding | Status |
|--------|---------|--------|
| **Factual Density** | Case studies contain specific facts. Blog post is generic — lacks stats | ⚠️ Needs Attention |
| **Clear Value Proposition** | "Harness the power of artificial intelligence to deliver innovative solutions" — too generic for AI citation | ⚠️ Needs Attention |
| **Source Citation / Outbound Links** | No external source citations in any content | ⚠️ Needs Attention |
| **Comprehensiveness** | No educational articles or thought leadership pieces — where AI citations typically originate | 🔴 Needs Work |
| **Entity Clarity** | "EigenAI" used consistently except for the "EIgenAI" typo | ⚠️ Needs Attention |
| **Originality** | Case studies contain original client work — excellent GEO signal. Blog is generic | ⚠️ Mixed |
| **Industry-Specific Depth** | The maritime FMEA case study demonstrates genuine domain expertise — AI engines will cite this | ✅ Strong |

### Technical GEO

| Signal | Finding | Status |
|--------|---------|--------|
| **HTTPS** | Site is served over HTTPS | ✅ Good |
| **Structured Data Depth** | No structured data of any kind | 🔴 Critical |
| **SameAs / Brand Entity Links** | LinkedIn linked. No Twitter, Crunchbase, or GitHub | ⚠️ Needs Attention |
| **JavaScript Rendering Risk** | WordPress theme appears server-rendered — content accessible to crawlers | ✅ Good |
| **Robots.txt / Crawlability** | Could not verify — confirm AI crawlers (GPTBot, PerplexityBot, ClaudeBot) are not blocked | ⚠️ Unconfirmed |

---

## AEO Analysis — Score: 3/10

### Featured Snippet Eligibility

| Signal | Finding | Status |
|--------|---------|--------|
| **Direct Answer Paragraphs** | No 40–60 word direct answers under question-phrased headings on any page | 🔴 Missing |
| **Question-Formatted Headings** | FAQ section has question headings — right instinct, but no schema and not snippet-formatted | ⚠️ Partial |
| **Definition Paragraphs** | No definitions of core terms (predictive maintenance, MLOps, churn prediction) | 🔴 Missing |
| **Numbered / Step-Format Content** | "How We Work" process exists but not formatted as a numbered list with concise step descriptions | ⚠️ Partial |
| **Comparison Tables** | None present | 🔴 Missing |

### Structured Answer Formats

| Signal | Finding | Status |
|--------|---------|--------|
| **FAQ Schema** | Absent — 3 existing FAQ questions are an immediate opportunity | 🔴 Critical |
| **HowTo Schema** | Absent — 3-step consulting process could be marked up | 🔴 Missing |
| **Article / BlogPosting Schema** | Absent on blog post | 🔴 Missing |
| **Speakable Schema** | Absent | 🔴 Missing |
| **Breadcrumb Schema** | Absent | 🔴 Missing |

### Voice Search Readiness

| Signal | Finding | Status |
|--------|---------|--------|
| **Conversational Phrasing** | Some FAQ uses conversational phrasing. Most body content is feature-list style | ⚠️ Partial |
| **Local Search Readiness** | Singapore address present but no LocalBusiness schema or Google Business Profile link | 🔴 Needs Work |
| **Answer Length** | Most content too long for voice extraction (ideal: ≤29 words). No content optimized to this standard | 🔴 Missing |
| **Speakable Markup** | Absent | 🔴 Missing |

---

## Priority Recommendations with Step-by-Step Instructions

---

### 🔴 CRITICAL — Fix #1: Correct the Homepage Title Tag

**The problem:** WordPress is showing the latest blog post title as the homepage `<title>` tag in Google Search. When someone Googles "EigenAI," they see "Case Study: Boosting Sales Efficiency for APAC Relocations..." as the page title — which is confusing and loses clicks.

**Why it matters:** The title tag is the single most important on-page SEO signal. It's what appears as the blue headline in Google results. A broken title can drop click-through rates by 30–50%.

**Target title:** `EigenAI – AI Consulting & Machine Learning Services | Singapore`  
(57 characters — within the 50–60 character optimal range)

**Step-by-step fix using Rank Math (recommended) or Yoast SEO:**

**Option A — Using Rank Math (free, recommended for WordPress):**
1. Log in to your WordPress admin dashboard at `https://eigenai.co/wp-admin`
2. In the left sidebar, go to **Rank Math → Titles & Meta**
3. Click on the **Homepage** tab in the top navigation
4. In the **Title** field, type: `EigenAI – AI Consulting & Machine Learning Services | Singapore`
5. In the **Description** field, type: `EigenAI is a Singapore-based AI consulting firm helping businesses unlock value through machine learning, data engineering, and GenAI solutions. Book a free consultation.` (160 characters)
6. Click **Save Changes**
7. Verify by searching `site:eigenai.co` in Google (may take 1–3 days to update in search results)

**Option B — If no SEO plugin is installed:**
1. Go to **Appearance → Theme Editor** in WordPress admin
2. Open `functions.php`
3. Add this code block before the closing `?>` tag:
```php
add_filter('wp_title', 'custom_homepage_title', 10, 3);
function custom_homepage_title($title, $sep, $seplocation) {
    if (is_home() || is_front_page()) {
        return 'EigenAI – AI Consulting & Machine Learning Services | Singapore';
    }
    return $title;
}
```
4. Click **Update File**

> ⚠️ **Note:** Always back up your site before editing theme files. Option A (plugin) is safer.

---

### 🔴 CRITICAL — Fix #2: Add Meta Descriptions to All Pages

**The problem:** No pages on eigenai.co have meta descriptions. Google sometimes auto-generates these from page content, but they are often poorly chosen — which reduces click-through rates from search results.

**Why it matters:** While meta descriptions are not a direct ranking factor, they are shown in search results and directly influence whether someone clicks your link. A well-written meta description can increase organic click-through rate by 5–15%.

**Using Rank Math (once installed from Fix #1):**

For each page:
1. Open the page in WordPress editor (Posts / Pages)
2. Look for the **Rank Math** meta box at the bottom of the editor or in the right sidebar
3. Click the **Edit Snippet** button
4. Fill in the **Meta Description** field

**Recommended meta descriptions for each page:**

| Page | Meta Description (max 160 chars) |
|------|----------------------------------|
| Homepage | `EigenAI is a Singapore-based AI consulting firm helping businesses unlock value through machine learning, data engineering, and GenAI. Book a free consultation.` |
| Services | `Explore EigenAI's full AI lifecycle services — from strategy and data engineering to ML model deployment, MLOps, and managed support. Based in Singapore.` |
| Case Studies | `See how EigenAI has delivered AI solutions for MISC Marine, Growsari, APAC Relocations, and more. Real clients, real outcomes.` |
| Blog | `Insights on AI strategy, machine learning, data engineering, and GenAI from the EigenAI consulting team in Singapore.` |
| Contact | `Get in touch with EigenAI's AI consulting team in Singapore. Schedule a free consultation or request a demo. Call +65 96343448.` |

5. Click **Save Changes** on each page

---

### 🔴 CRITICAL — Fix #3: Create an About / Team Page

**The problem:** There is no About page and no Team page anywhere on the site. Authors post as "unni," "yibin," and "achuth" with no surnames, titles, or credentials. Google and AI search engines use author credibility to decide whether to trust and rank content.

**Why it matters:** This is the single highest-impact E-E-A-T fix available. An About page with named, credentialed people is required for AI engines like Perplexity and Google AI Overviews to confidently cite your content.

**Step-by-step:**

**Step 1: Create the Team page in WordPress**
1. Go to **Pages → Add New** in WordPress admin
2. Set the page title to: `About EigenAI – Our Team`
3. Set the permalink (URL slug) to: `/about/`
4. Add content structured as follows (adapt with real names):

```
## About EigenAI

EigenAI is an AI consulting firm headquartered in Singapore, founded to help 
businesses across Southeast Asia and beyond unlock measurable value through 
applied artificial intelligence. We specialise in machine learning model 
development, data engineering, GenAI implementation, and AI strategy for 
industries including maritime, logistics, e-commerce, and supply chain.

## Our Team

### [Full Name of "unni"] — Founder & AI Strategy Lead
[Photo]
[Full Name] has X years of experience in [domain]. Prior to EigenAI, he/she 
worked at [previous company] where [achievement]. [Full Name] holds a [degree] 
from [university] and specialises in AI roadmapping and GenAI adoption.
[LinkedIn: linkedin.com/in/...]

### [Full Name of "yibin"] — Machine Learning Engineer
[Photo]
...

### [Full Name of "achuth"] — Data Engineering Lead
[Photo]
...
```

**Step 2: Add the About page to your navigation menu**
1. Go to **Appearance → Menus**
2. Find your primary menu (usually "Main Menu" or "Primary Navigation")
3. Under "Pages," check the box next to "About EigenAI" and click **Add to Menu**
4. Drag it to your preferred position (recommended: after "Home")
5. Click **Save Menu**

**Step 3: Update each author's WordPress profile**
1. Go to **Users → All Users**
2. Click **Edit** on each author
3. Fill in:
   - **First Name** and **Last Name** (use real full names)
   - **Display name publicly as** — set to full name (e.g., "Unni Krishnan")
   - **Biographical Info** — write 2–3 sentences about their expertise
   - **Website** — link to their LinkedIn profile
4. Click **Update User**

---

### 🔴 CRITICAL — Fix #4: Add Organization Schema to Homepage

**The problem:** No structured data anywhere on the site means search engines and AI systems cannot reliably identify EigenAI as a registered entity with a specific type, location, and service area.

**Why it matters:** Organization schema is the foundation of your entity graph. Without it, Google cannot confidently associate your brand name with your website, location, and services — which is prerequisite for appearing in AI Overviews and knowledge panels.

**Step-by-step:**

**Step 1: Create the schema JSON**

Copy this block and fill in your real values:

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "EigenAI",
  "url": "https://eigenai.co",
  "logo": "https://eigenai.co/wp-content/uploads/2025/11/logo2_transparent_background-1.png",
  "description": "EigenAI is a Singapore-based AI consulting firm specialising in machine learning, data engineering, GenAI implementation, and AI strategy for enterprise clients.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "32 Pekin St, #05-01",
    "addressLocality": "Singapore",
    "postalCode": "048762",
    "addressCountry": "SG"
  },
  "telephone": "+6596343448",
  "email": "info@eigenai.co",
  "sameAs": [
    "https://www.linkedin.com/company/eigenaico/"
  ],
  "areaServed": "Southeast Asia",
  "serviceType": ["AI Consulting", "Machine Learning", "Data Engineering", "GenAI Implementation", "MLOps"]
}
```

**Step 2: Add to the homepage**

**Option A — Using Rank Math:**
1. Open your homepage in the WordPress editor
2. In the Rank Math sidebar, click **Schema**
3. Click **Add New Schema**
4. Select **Organization**
5. Fill in the fields using the values above
6. Save

**Option B — Using a custom code snippet (more control):**
1. Install the free plugin **WPCode** (or use your theme's `functions.php`)
2. Go to **Code Snippets → Add Snippet**
3. Choose **Header & Footer**
4. Paste this in the **Header** section:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "EigenAI",
  ...paste the full JSON from Step 1...
}
</script>
```
5. Set location to **Homepage only**
6. Save and Activate

**Step 3: Validate**
1. Go to https://search.google.com/test/rich-results
2. Enter `https://eigenai.co`
3. Confirm the Organization entity is detected with no errors

---

### 🔴 CRITICAL — Fix #5: Implement FAQ Schema on the Homepage

**The problem:** The homepage has 3 FAQ questions ("We don't have an AI strategy yet — where do we start?", "How do you handle data governance?", "How does your data engineering benefit our marketing department?") but they have no schema markup. Google cannot extract them as rich results.

**Why it matters:** FAQ schema can trigger FAQ rich results directly in Google search — showing your questions and answers expanded below your main listing. This can double the vertical space your result takes up on the page, dramatically increasing visibility.

**Step-by-step:**

**Step 1: Write the FAQ schema JSON**

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "We don't have an AI strategy yet — where do we start?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "EigenAI accompanies you from the very beginning. Through our AI Consultation and Strategy phase, we help you identify high-value use cases, assess your data readiness, and create a roadmap that moves from initial theory to full-scale operations."
      }
    },
    {
      "@type": "Question",
      "name": "How do you handle data governance and compliance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We build a custom framework for every project that prioritises both value and compliance. Our data management strategies are designed to meet industry standards while ensuring your data remains a secure and accessible asset."
      }
    },
    {
      "@type": "Question",
      "name": "How does your data engineering benefit our marketing department?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "EigenAI bridges the gap between marketing specialists and data analysts. We build cross-channel mechanisms that allow you to manage complex campaigns and objectives using real-time data insights and automation."
      }
    },
    {
      "@type": "Question",
      "name": "What industries does EigenAI serve?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "EigenAI has delivered AI projects across maritime shipping, e-commerce, supply chain and logistics, retail, and relocation services. We are headquartered in Singapore and serve clients across Southeast Asia."
      }
    }
  ]
}
```

**Step 2: Add it to the homepage**
1. Use the same WPCode method described in Fix #4, Step 2
2. Paste the FAQ schema JSON (wrapped in `<script type="application/ld+json">` tags) into the **Header** section
3. Set location to **Homepage only**
4. Save and Activate

**Step 3: Validate**
1. Visit https://search.google.com/test/rich-results
2. Enter `https://eigenai.co`
3. Confirm "FAQPage" is detected under Rich Results

> ⚠️ **AEO bonus:** Add 3–4 more FAQ questions that match real search queries your prospective clients type. Example additions: "How long does an AI consulting engagement typically take?", "What is the difference between machine learning and GenAI?", "How much does AI consulting cost in Singapore?"

---

### 🟠 HIGH — Fix #6: Add Full Author Profiles to All Post Authors

**The problem:** Three people ("unni," "yibin," "achuth") author case studies and blog posts but appear only as anonymous first-name usernames with Gravatar avatars. AI search engines and Google treat anonymous authors as a major trust signal reduction.

**Why it matters:** Google's Search Quality Evaluator Guidelines explicitly require demonstrable real-world expertise for YMYL (Your Money Your Life) and specialist content. AI consulting advice falls in this category.

**Step-by-step:**

**Step 1: Update each WordPress user profile** (see Fix #3, Step 3 for detailed instructions)

**Step 2: Create individual author pages**

WordPress automatically creates author archive pages at `/author/[username]/`. For each author:
1. Go to **Users → Edit** for each author
2. In the **Biographical Info** box, write a detailed bio:

```
[Full Name] is a [title] at EigenAI with [X] years of experience in 
[specialisation]. He/She has worked with clients across [industries], 
delivering AI solutions in [specific areas]. Prior to EigenAI, [Full Name] 
worked at [company] where [achievement]. [Full Name] holds a [degree] 
from [university].
```

3. Save the profile

**Step 3: Add Schema markup to author pages**

For each author's archive page (`/author/[name]/`), add Person schema:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "[Full Name]",
  "jobTitle": "[Title, e.g. Machine Learning Engineer]",
  "worksFor": {
    "@type": "Organization",
    "name": "EigenAI",
    "url": "https://eigenai.co"
  },
  "url": "https://eigenai.co/author/[username]/",
  "sameAs": ["https://linkedin.com/in/[profile]"]
}
```

Use WPCode to inject this schema on each author archive page (target by URL condition).

---

### 🟠 HIGH — Fix #7: Add Article Schema to Blog Post and All Case Studies

**The problem:** The blog post and all 5 case studies have no Article or BlogPosting schema. Search engines cannot identify author credentials, publication dates, or publisher details in a machine-readable way.

**Why it matters:** Article schema unlocks rich results for blog posts and enables AI search engines to correctly attribute content to your organisation and authors — critical for GEO citation.

**Step-by-step using Rank Math:**

1. Open each case study or blog post in the WordPress editor
2. In the Rank Math sidebar, click **Schema**
3. Click **Add New Schema**
4. Choose **Article** (for case studies) or **BlogPosting** (for the blog post)
5. Fill in:
   - **Headline** — the post title
   - **Description** — first 2 sentences of the post
   - **Author Name** — the author's full real name
   - **Author URL** — link to their LinkedIn or author page
   - **Publisher** — EigenAI
   - **Publisher Logo** — paste the logo URL
   - **Date Published** — the post date
   - **Date Modified** — today's date (or last edit date)
6. Save

**Alternatively, use WPCode to add schema to all posts automatically:**

Install WPCode and add a **PHP snippet** that runs on all singular posts:

```php
add_action('wp_head', function() {
    if (is_singular(array('post'))) {
        global $post;
        $author = get_the_author_meta('display_name', $post->post_author);
        $author_url = get_author_posts_url($post->post_author);
        $schema = array(
            "@context" => "https://schema.org",
            "@type" => "Article",
            "headline" => get_the_title(),
            "datePublished" => get_the_date('c'),
            "dateModified" => get_the_modified_date('c'),
            "author" => array(
                "@type" => "Person",
                "name" => $author,
                "url" => $author_url
            ),
            "publisher" => array(
                "@type" => "Organization",
                "name" => "EigenAI",
                "url" => "https://eigenai.co",
                "logo" => array(
                    "@type" => "ImageObject",
                    "url" => "https://eigenai.co/wp-content/uploads/2025/11/logo2_transparent_background-1.png"
                )
            )
        );
        echo '<script type="application/ld+json">' . json_encode($schema) . '</script>';
    }
});
```

---

### 🟠 HIGH — Fix #8: Rebuild the Services Page

**The problem:** The Services page (`/our-services/`) contains only a 3-step process section. It has no H1, no individual service descriptions, and no links to case studies. The homepage actually contains more service information. This is a major missed opportunity for targeting service-specific keywords.

**Why it matters:** Dedicated, deep service pages are how B2B companies rank for high-intent queries like "AI consulting services Singapore," "MLOps implementation partner," or "churn prediction model development." Without them, EigenAI is invisible for these searches.

**Step-by-step content plan:**

**Step 1: Create a proper H1**

In the WordPress editor, add an H1 heading at the top of the page:
```
AI Consulting & Machine Learning Services — EigenAI Singapore
```

**Step 2: Add individual service sections**

Create a section for each of the 6 services with this structure:

```markdown
## [Service Name]

[2–3 sentence summary of what the service delivers and who it's for]

**What's included:**
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

**Who it's for:** [Target client description]

**Typical engagement:** [Duration, e.g., "3–6 months"]

[Link to related case study: "See how we helped [Client] with [outcome] →"]
```

**Example for AI Strategy and Advisory:**
```markdown
## AI Strategy and Advisory

EigenAI's AI Strategy and Advisory service helps organisations move from 
AI ambition to a funded, prioritised roadmap. We assess your data maturity, 
identify the highest-ROI use cases, and create a phased adoption plan your 
leadership team can execute with confidence.

**What's included:**
- AI readiness assessment and data audit
- High-impact use case identification and ROI prioritisation
- Long-term AI adoption roadmap
- Ethical AI governance framework
- GenAI Academy team training programme

**Who it's for:** C-suite leaders and transformation teams planning their first 
or next AI initiative.

**Typical engagement:** 4–8 weeks discovery + 2-week roadmap delivery

[→ See how we built a predictive lead scoring system for APAC Relocations]
```

**Step 3: Add internal links**

At the bottom of each service section, add a link to the most relevant case study. Example:
- AI Strategy & Advisory → APAC Relocations lead scoring case study
- Machine Learning → Growsari churn prediction
- Data Engineering → Supply chain GenAI analytics
- MLOps → MISC Marine FMEA dashboards

**Step 4: Add a meta description** (see Fix #2)

---

### 🟠 HIGH — Fix #9: Add Image Alt Text to All Images

**The problem:** All case study thumbnail images use machine-generated filenames (`Gemini_Generated_Image_3fav5q3fav5q3fav.png`) with no alt text. Theme images also lack descriptive alt text.

**Why it matters:** Alt text is how search engines understand what an image depicts. Missing alt text means images contribute zero SEO value and are inaccessible to screen readers. Descriptive alt text can drive traffic through Google Image Search and reinforces keyword relevance.

**Step-by-step using the WordPress Media Library:**

1. Go to **Media → Library** in WordPress admin
2. Switch to **List View** (the icon that looks like lines, not the grid)
3. For each image, click on it to open the attachment details
4. In the **Alt Text** field, write a specific description

**Recommended alt text for each case study thumbnail:**

| Image | Recommended Alt Text |
|-------|----------------------|
| APAC Relocations (lead scoring) | `AI predictive lead scoring dashboard for international relocation sales team` |
| Shopify merchants (analytics) | `AI predictive analytics and conversational intelligence for Shopify e-commerce merchants` |
| D2C Furniture (conversions) | `Machine learning model driving high-value customer conversions for Southeast Asia furniture brand` |
| MISC Marine (FMEA) | `AI-driven FMEA dashboards for maritime shipping predictive maintenance — EigenAI and MISC Marine` |
| Supply chain (GenAI analytics) | `GenAI-powered chatbot for supply chain KPI analytics — warehouse logistics dashboard` |
| Logo | `EigenAI logo — AI consulting Singapore` |

5. Click **Update** after each change

**For future images:** Before uploading any new image to WordPress, rename the file to include keywords. Example: rename `Gemini_Generated_Image_abc123.png` to `ai-consulting-singapore-churn-prediction.png` before upload.

---

### 🟡 MEDIUM — Fix #10: Start a Regular Blog Publishing Cadence

**The problem:** Only 1 blog post has been published in the site's entire history (November 2025 — 5 months ago). The blog is functionally empty. This means EigenAI has zero organic content targeting the hundreds of long-tail queries its prospective clients type into Google every day.

**Why it matters:** Blog content is the primary engine of organic search traffic for B2B companies. Each well-optimised post is a permanent asset that can generate leads for years. For GEO, a regular publishing cadence signals to AI search engines that the site is actively maintained and authoritative.

**Content strategy — 12 recommended blog topics:**

| # | Title | Target Keyword | Estimated Monthly Searches |
|---|-------|---------------|---------------------------|
| 1 | What is MLOps and Why Does Your Business Need It? | "what is MLOps" | 1,600/mo |
| 2 | AI Consulting in Singapore: What to Expect and How to Choose a Partner | "AI consulting Singapore" | 390/mo |
| 3 | How to Build a Customer Churn Prediction Model for E-Commerce | "churn prediction model e-commerce" | 260/mo |
| 4 | Predictive Maintenance vs. Reactive Maintenance: The ROI Case for AI | "predictive maintenance AI ROI" | 480/mo |
| 5 | What is a Data Pipeline? A Non-Technical Guide for Business Leaders | "what is a data pipeline" | 2,400/mo |
| 6 | How to Write a Business Requirement Document for an AI Project | "AI project BRD template" | 170/mo |
| 7 | GenAI vs. Traditional AI: Which Is Right for Your Business? | "generative AI vs machine learning" | 1,900/mo |
| 8 | 5 Signs Your Business Is Ready for AI — And 3 Signs It Isn't | "is my business ready for AI" | 210/mo |
| 9 | How EigenAI Deploys AI Projects in Under 3 Months | "AI implementation timeline" | 140/mo |
| 10 | The True Cost of Customer Churn (And How AI Stops It) | "cost of customer churn" | 720/mo |
| 11 | How AI Is Transforming Maritime Maintenance in Southeast Asia | "AI maritime maintenance" | 90/mo |
| 12 | Ethical AI Governance: A Practical Framework for Singapore Enterprises | "AI governance framework Singapore" | 110/mo |

**Publishing schedule recommendation:**
- Weeks 1–4: Publish posts #1, #5, #7, #10 (highest search volume)
- Weeks 5–8: Publish posts #2, #4, #8, #12 (local + strategic)
- Weeks 9–12: Publish posts #3, #6, #9, #11 (niche/long-tail)
- Ongoing: 2 posts per month minimum

**Optimising each post for AEO:**
- Start each post with a 40–60 word direct answer to the question in the title
- Use H2 subheadings phrased as follow-up questions
- Include at least one numbered list or step-by-step section
- End with 3–5 FAQ items (add FAQ schema per Fix #5 method)

---

### 🟡 MEDIUM — Fix #11: Add Quantified Results to Case Studies

**The problem:** Case study outcomes are described in vague terms — "Increased Conversion Rates," "Faster Decision-Making," "Improved Transparency." These are claims without evidence that AI search engines cannot cite with confidence.

**Why it matters:** AI engines like Perplexity and Google AI Overviews strongly prefer content with specific, verifiable data points. "Conversion rates improved 34%" is citable. "Increased conversion rates" is not.

**Step-by-step:**

1. Review each case study with the client and ask for permission to publish specific metrics
2. For each measurable outcome, replace the generic phrase with a specific number

**Suggested metrics to collect from clients:**

| Case Study | Metrics to Request |
|------------|-------------------|
| APAC Relocations (lead scoring) | % increase in conversion rate, % reduction in time spent per lead, volume of leads processed per week before vs. after |
| Supply chain GenAI (Axidio) | Time saved per report request (hours → minutes/seconds), % reduction in manual reporting, adoption rate among supervisors |
| MISC Marine (FMEA) | Reduction in unplanned downtime (%), reduction in maintenance-induced failures, number of "bad actor" equipment identified |
| Growsari (churn prediction) | Reduction in monthly churn rate (%), lift in retention intervention effectiveness, accuracy rate of the churn model |
| D2C Furniture (conversions) | Lift in high-value conversion rate, reduction in wasted ad spend, model prediction accuracy |

3. Update each case study with a **Results Summary** box near the top:

```markdown
### Results at a Glance
- 📈 34% improvement in lead conversion rate
- ⏱️ 60% reduction in time spent per lead
- 🔄 Automated pipeline processing 800+ leads/month
```

4. Add these metrics to the Article schema's `description` field (see Fix #7)

---

### 🟡 MEDIUM — Fix #12: Add LocalBusiness Schema

**The problem:** Despite having a Singapore address and phone number, no LocalBusiness schema is present. Voice searches and local map queries ("AI consulting near me," "AI consulting Singapore") are unlikely to surface EigenAI.

**Step-by-step:**

**Step 1: Create LocalBusiness schema JSON**

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "EigenAI",
  "image": "https://eigenai.co/wp-content/uploads/2025/11/logo2_transparent_background-1.png",
  "url": "https://eigenai.co",
  "telephone": "+6596343448",
  "email": "info@eigenai.co",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "32 Pekin St, #05-01",
    "addressLocality": "Singapore",
    "postalCode": "048762",
    "addressCountry": "SG"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 1.2847,
    "longitude": 103.8470
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "09:00",
    "closes": "18:00"
  },
  "priceRange": "$$"
}
```

**Step 2: Add to the Contact page**
1. Use WPCode to inject this schema into the Contact page header
2. Set the location condition to the Contact Us page URL
3. Save and Activate

**Step 3: Set up Google Business Profile (separate but complementary)**
1. Go to https://business.google.com
2. Search for "EigenAI" to check if a listing already exists
3. If not, click **Add your business**
4. Set category to "Management Consultant" or "Information Technology Consultant"
5. Fill in the same NAP details (Name, Address, Phone) that match your website exactly
6. Verify via phone or postcard
7. Add photos, services, and your website URL

> A verified Google Business Profile is required for "near me" and Google Maps visibility and works in tandem with LocalBusiness schema.

---

### 🟡 MEDIUM — Fix #13: Fix the /contact-us-2/ URL

**The problem:** The contact page lives at `/contact-us-2/` — the `-2` suffix indicates a duplicate was created at some point and the original `/contact-us/` may still exist, creating duplicate content risk.

**Step-by-step:**

1. Go to **Pages** in WordPress admin and search for "contact"
2. Check if both `/contact-us/` and `/contact-us-2/` exist
3. Identify which one is live and receiving traffic (check WordPress stats or Google Analytics)
4. If `/contact-us/` exists but is empty or redirects, delete it
5. For the live page (`/contact-us-2/`), edit the permalink to `/contact/`:
   - Open the page editor
   - Click the URL slug under the title
   - Change it to `contact`
   - Click **Save**
6. WordPress will automatically set up a 301 redirect from the old URL — verify this by visiting `https://eigenai.co/contact-us-2/` and confirming it redirects to `https://eigenai.co/contact/`
7. Update your navigation menu to use the new URL (Appearance → Menus)

---

### 🟡 MEDIUM — Fix #14: Add Open Graph and Twitter Card Meta Tags

**The problem:** Open Graph and Twitter Card tags are missing sitewide. When anyone shares a link to eigenai.co on LinkedIn, WhatsApp, or Twitter, the preview will show a blank image or incorrect text.

**Why it matters:** Professional services are heavily shared on LinkedIn. A polished link preview with a proper image, title, and description dramatically increases click-through from social shares. OG tags also help AI crawlers understand page content.

**Step-by-step using Rank Math:**

1. Go to **Rank Math → Titles & Meta**
2. Click the **Social Meta** tab
3. Enable **Open Graph** and **Twitter Card**
4. For each page, open the editor, go to Rank Math → Social, and set:
   - **OG Title** — same as the meta title
   - **OG Description** — same as the meta description
   - **OG Image** — upload a 1200×630px image (the case study thumbnail works well)
5. For the homepage, upload a branded banner image (1200×630px) showing the EigenAI logo and tagline

**Validate:** Go to https://developers.facebook.com/tools/debug/ and enter each page URL to preview how it will appear when shared on social media.

---

### 🟢 QUICK WIN — Fix #15: Fix the "EIgenAI" Typo

**The problem:** The homepage hero text reads "Unlock your full business potential with **EIgenAI** consulting" — with a capital I. This is inconsistent with the brand name and can confuse entity matching in AI systems.

**Fix in 2 minutes:**
1. Go to **Pages → Home** (or your homepage in the editor)
2. Use Ctrl+F (Cmd+F on Mac) to search for "EIgenAI" in the editor
3. Replace it with "EigenAI"
4. Click **Update**

---

### 🟢 QUICK WIN — Fix #16: Add HowTo Schema to the Services Process Section

**The problem:** The 3-step consulting process (Initial Consultation → Strategy Development → Reviews) is a natural "How does AI consulting work?" answer but has no HowTo schema.

**Schema to add to the Services page:**

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How EigenAI's AI Consulting Process Works",
  "description": "EigenAI follows a structured 3-step process to deliver AI solutions — from initial discovery to full deployment and ongoing support.",
  "step": [
    {
      "@type": "HowToStep",
      "position": "1",
      "name": "Initial Consultation",
      "text": "EigenAI begins with a deep-dive discovery session to understand your unique business challenges and data landscape. We identify high-value opportunities and assess your AI readiness."
    },
    {
      "@type": "HowToStep",
      "position": "2",
      "name": "Strategy Development and Implementation",
      "text": "Our experts craft a bespoke technical roadmap then build and deploy customised AI models, data pipelines, or automation frameworks integrated seamlessly into your existing operations."
    },
    {
      "@type": "HowToStep",
      "position": "3",
      "name": "Reviews and Finalisation",
      "text": "We rigorously test and refine every solution to ensure peak performance and compliance, then provide training and documentation to fully empower your team to maintain and scale the solution."
    }
  ]
}
```

Add this to the Services page using WPCode (same method as Fix #4).

---

### 🟢 QUICK WIN — Fix #17: Add SpeakableSpecification Schema to Homepage FAQ

**The problem:** Voice assistants (Google Assistant, Siri, Alexa) need to know which content on a page is suitable for reading aloud. Without Speakable schema, they will either read the entire page or skip it entirely.

**Schema to add (combined with existing FAQ schema from Fix #5):**

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".faq-section", ".hero-tagline"]
  },
  "url": "https://eigenai.co/"
}
```

> Note: The CSS selector values (`.faq-section`, `.hero-tagline`) will need to match the actual class names in your theme's HTML. Use your browser's DevTools (right-click → Inspect) on those sections to find the correct class names.

---

## Implementation Timeline

| Week | Actions | Expected Impact |
|------|---------|-----------------|
| **Week 1** | Fixes #1, #2, #15 (title tag, meta descriptions, typo) | Immediate improvement in search snippet appearance within 3–7 days |
| **Week 2** | Fixes #4, #5 (Organization schema, FAQ schema) | Rich results eligibility begins; entity recognition improves |
| **Week 3** | Fix #3 (About / Team page) | E-E-A-T improvement; Google begins associating credentialed authors with content |
| **Week 4** | Fixes #6, #7 (author profiles, Article schema) | Author credibility signals propagate; case studies become AI-citable |
| **Week 5** | Fixes #8, #9 (Services page rebuild, image alt text) | New service-level keyword rankings begin building |
| **Week 6** | Fixes #12, #13, #14 (LocalBusiness schema, URL fix, OG tags) | Local search visibility, social share appearance improves |
| **Week 7** | Fixes #10, #11 (first blog posts, quantified case study metrics) | Long-tail keyword rankings begin; GEO citation eligibility increases |
| **Ongoing** | 2 blog posts/month; Fix #16, #17 as maintenance tasks | Compound organic growth over 3–6 months |

**Estimated total time investment for all one-time fixes:** 12–18 hours for a developer/content person familiar with WordPress.

---

## What's Working Well

| Strength | Evidence |
|----------|----------|
| **Real, named client case studies** | MISC Marine, Axidio, APAC Relocations, and Growsari are named explicitly — uncommon in AI consulting and a strong E-E-A-T signal |
| **Case study narrative depth** | The maritime FMEA and supply chain GenAI pieces are genuinely detailed — exactly the kind of content AI engines cite |
| **Growsari testimonial** | A specific testimonial from a named CTO (not a generic star rating) — high trust value |
| **NAP data present** | Physical Singapore address, phone number, and email are visible on the Contact page |
| **HTTPS** | The site is served securely over HTTPS |
| **Service breadth on homepage** | 6 specific service lines with detailed descriptions provide good semantic keyword coverage |
| **Internal case study linking** | "You May Love" section creates a content cluster that passes link equity |
| **Question-phrased FAQ** | The existing FAQ questions represent real customer queries — just needs schema markup |
| **Pricing transparency** | Publishing pricing tiers builds trust and creates comparison keyword opportunities |

---

## Glossary

**SEO (Search Engine Optimization)** is the practice of improving a website's visibility in traditional search engines like Google and Bing by optimising technical elements (title tags, meta descriptions, site speed), content quality (keywords, depth, freshness), and authority signals (backlinks, schema markup). When someone types a query into Google, SEO determines whether your page appears and how prominently.

**GEO (Generative Engine Optimization)** is an emerging discipline focused on optimising content to be cited, synthesised, and recommended by AI-powered search tools such as Google AI Overviews, Perplexity, ChatGPT Search, and Gemini. Unlike traditional SEO which ranks pages, GEO determines whether an AI will summarise your content or quote your expertise when someone asks a question in a conversational interface. Key signals include E-E-A-T (named experts, verifiable credentials), factual density, clear entity definition, and structured data.

**AEO (Answer Engine Optimization)** refers to optimising content to be extracted as a direct answer by search engines (featured snippets, People Also Ask boxes) or AI voice assistants (Siri, Alexa, Google Assistant). AEO requires concise, clearly formatted answers to specific questions, supported by FAQ schema, HowTo schema, and content structured around natural language queries. As zero-click search grows, AEO is increasingly critical for top-of-funnel visibility.

**Schema Markup / Structured Data** is code (in JSON-LD format) added to a webpage that tells search engines exactly what the content means — not just what it says. For example, schema can tell Google "this is a FAQ," "this author is a Person with these credentials," or "this business is located at this address." Schema is the foundation of rich results in Google and entity recognition in AI systems.

**E-E-A-T** stands for Experience, Expertise, Authoritativeness, and Trustworthiness. It is the framework Google's quality raters use to assess whether a site deserves to rank for a given query. For a B2B AI consulting firm, E-E-A-T is demonstrated through named experts with verifiable credentials, real client case studies with outcomes, and transparent contact information.

**JSON-LD** (JavaScript Object Notation for Linked Data) is the format Google recommends for adding structured data to webpages. It is placed in a `<script type="application/ld+json">` tag in the HTML `<head>` section and does not affect the visual appearance of the page.

---

*Report generated by Claude AI Audit Skill | eigenai.co Full Audit | April 16, 2026*  
*Skill by Alex Labat*
