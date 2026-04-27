---
name: analyze-serp
description: Analyze actual search engine results, rankings, competitors, and ratings for SEO, AEO, and GEO optimization
---

# SEO Search Performance Analysis Skill for Copilot & VS Code

## Purpose
Automatically analyze actual search engine results for websites and projects, measuring real-world performance, competitor analysis, and optimization opportunities for Search Engine Optimization (SEO), Answer Engine Optimization (AEO), and Generative Engine Optimization (GEO). Generate structured performance reports with rankings, ratings, competitor insights, and actionable recommendations directly within Copilot and VS Code.

## When to Use
- User provides keywords, domain, or queries and wants to see actual search rankings and performance
- Checking how your site performs against competitors in real search results
- Analyzing featured snippets, local pack results, or AI-generated answers
- Measuring SEO effectiveness with actual SERP data
- Identifying common search terms and queries for a niche
- Comparing ratings and visibility across competitors
- Answer "how do I rank for X?", "check my search results", "who are my competitors?", "analyze SERP for keywords"

Trigger phrases:
- "check my search rankings"
- "analyze SERP for [keywords]"
- "who are my competitors in search"
- "measure SEO performance"
- "featured snippet analysis"
- "local search results"

## Integration with VS Code/Copilot

### Quick Integration Points
1. **Browser automation**: Use browser tools to perform actual searches and capture SERP data
2. **Generate reports as Markdown**: Output findings as markdown files in the workspace for easy reference
3. **Create performance dashboards**: Generate tables and charts showing rankings over time
4. **Link to optimization tasks**: Create checklists for improving rankings

### Output Formats
- **Inline Chat Summary**: Brief overview of key metrics and top findings (2-3 minutes)
- **Workspace Report**: Detailed markdown file with tables, competitor analysis, and recommendations
- **Performance Tables**: Structured data showing positions, ratings, features for each result

## Analysis Methodology

### Step 1: Define Search Scope
Ask the user: **"What keywords or queries would you like to analyze? Would you like a Quick Analysis (top 10 results — 2-3 minutes) or Full Analysis (multiple queries, competitor deep-dive — 5-10 minutes)?"**

Wait for explicit confirmation. No exceptions.

### Step 2: Perform Searches and Capture Data
**Phase 2a: Execute searches**
- Use browser automation to search specified keywords on Google (or other engines if specified)
- Capture top 10-20 organic results, featured snippets, local pack, knowledge panels
- For each result: URL, title, description, position, rating (if available), features (rich snippets, etc.)

**Phase 2b: Identify competitors and patterns**
- Analyze top 10 results to identify common domains/competitors
- Extract common search terms from titles and descriptions
- Note AEO elements: featured snippets, PAA boxes, knowledge panels
- Capture GEO elements: AI-generated answers, entity mentions

**Phase 2c: Gather ratings and metrics**
- For each result, check for star ratings, review counts
- Note structured data indicators (rich snippets for recipes, products, etc.)
- Capture local business information if applicable

### Step 3: Analyze Performance

#### Ranking Analysis
- Position of target domain(s) for each query
- Average position across queries
- Presence in featured snippets, local pack, etc.

#### Competitor Analysis
- Top 10 domains appearing most frequently
- Their average positions and features
- Common content types and strategies

#### Query Analysis
- Most common terms in titles/descriptions
- Question-based queries (AEO opportunities)
- Long-tail vs. short-tail distribution

#### Rating Analysis
- Average ratings for top results
- Correlation between ratings and positions
- Review counts and their impact

### Step 4: Score & Assess

Score performance metrics:
- **Visibility Score**: Based on average position (1-10, higher better)
- **Competitive Score**: Based on market share in top 10 (1-10, higher better)
- **AEO Score**: Based on featured snippet presence (1-10, higher better)
- **GEO Score**: Based on AI answer integration (1-10, higher better)

## Reporting in VS Code

### Chat Summary (Inline)
Keep brief and data-driven:
```
🔍 Search Performance Analysis for "[keywords]"

Queries analyzed: [count]
Analysis date: [date]

| Metric | Score | Summary |
|--------|-------|---------|
| Visibility | X/10 | [Target domain] ranks avg position Y |
| Competition | X/10 | Top competitor: [domain] with Z% share |
| AEO | X/10 | [X] featured snippets captured |
| GEO | X/10 | [X] AI answers present |

**Top Competitors:**
1. [Domain] - Avg position: X, Rating: Y/Z
2. [Domain] - Avg position: X, Rating: Y/Z
3. [Domain] - Avg position: X, Rating: Y/Z

**Key Opportunities:**
1. [Specific action] — [why it matters]
2. [Specific action] — [why it matters]
3. [Specific action] — [why it matters]
```

### Workspace Report (Markdown)
Create a `SERP_ANALYSIS_[keywords]_[date].md` file in workspace with:
- Executive summary with key metrics
- Detailed ranking tables for each query
- Competitor analysis with ratings and features
- Common search terms frequency analysis
- AEO/GEO opportunities identified
- Actionable recommendations

### Table Formats
**Ranking Table:**
| Position | Domain | Title | Rating | Features |
|----------|--------|-------|--------|----------|
| 1 | example.com | Title... | 4.5/5 | Featured Snippet |
| 2 | competitor.com | Title... | 4.2/5 | Rich Snippet |

**Competitor Overview:**
| Domain | Avg Position | Appearance Count | Avg Rating | Key Features |
|--------|--------------|-----------------|------------|--------------|
| competitor1.com | 2.3 | 8/10 | 4.7 | Local Pack, Reviews |
| competitor2.com | 4.1 | 6/10 | 4.3 | Featured Snippet |

## Best Practices

### Accuracy First
- Use actual browser searches to capture real SERP data
- Include date/timestamp in all reports (SERP data changes frequently)
- Note search location/device settings used

### Comprehensive Coverage
- Analyze multiple related queries for broader insights
- Include both organic and featured results
- Capture ratings and review data where available

### Actionable Insights
- Link findings to specific optimization opportunities
- Prioritize high-impact, low-competition keywords
- Suggest content strategies based on competitor analysis

### Privacy and Ethics
- Respect search engine terms of service
- Don't attempt to manipulate or game search results
- Use data for legitimate optimization purposes only

## Usage Examples

**User**: "check my search rankings for 'best coffee shops'"
```
1. Ask: Quick or Full Analysis?
2. Perform search in browser, capture top 10 results
3. Analyze positions, competitors, ratings
4. Present summary with competitor table
5. Generate detailed report with recommendations
```

**User**: "who are my competitors for 'web development services'"
```
Focus on B2B analysis:
- Identify top agencies and their positioning
- Analyze ratings and review counts
- Note portfolio/portfolio features in snippets
- Suggest differentiation strategies
```

**User**: "analyze SERP for featured snippets"
```
Emphasize AEO:
- Count featured snippets across queries
- Analyze question patterns
- Identify opportunities for FAQ/HowTo content
- Recommend structured data implementation
```

## Key Differences from Site Audit Skill

1. **External Focus**: Analyzes search results, not internal site structure
2. **Competitive Intelligence**: Identifies and analyzes competitors
3. **Real-time Data**: Uses live browser searches for current SERP data
4. **Performance Metrics**: Focuses on rankings, visibility, and market position
5. **Query-based**: Starts with keywords rather than URLs

## Important Principles

1. **Search the actual queries**: Use real searches to get authentic data
2. **Analyze the ecosystem**: Look at competitors, not just target site
3. **Provide context**: Explain what metrics mean and how to improve them
4. **Time-sensitive**: SERP data changes; always include analysis date
5. **Action-oriented**: Every insight should lead to a concrete optimization step