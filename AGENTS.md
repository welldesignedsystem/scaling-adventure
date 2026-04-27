# Scaling Adventure - AI Agent Instructions

## Project Overview
This is a **skills-first repository** for SEO/GEO/AEO optimization integrated with VS Code/Copilot chat. It provides automated audit and analysis capabilities for websites and search performance through self-contained skill methodologies.

**Important**: This is NOT a traditional Python application. Skills run directly in Copilot chat, triggered by user questions like "audit my site" or "check my rankings". The skills are methodology documents (markdown) that orchestrate browser automation and web fetching tools.

## Technology Stack
- **Python 3.12+** (pinned in `.python-version`, managed with `uv`)
- **Skills architecture** in `.github/skills/` for modular capabilities
- **Report generation**: Markdown reports to `report/` folder → Optional DOCX conversion via Pandoc
- **Browser automation**: Playwright for page capture and SERP analysis
- **Copilot integration**: Skills trigger from chat using Copilot's built-in tools

## Key Directories
- `.github/skills/` - Skill methodologies (markdown-based, not Python code)
- `report/` - Generated audit/analysis reports (markdown format)
- `output/` - Converted documents (DOCX format, via Pandoc)
- `misc/` - Supporting files (diagrams, templates) — currently empty

## Getting Started

### Installation
```bash
# Install dependencies (currently empty, but uv manages the environment)
uv sync
```

### Using Skills
Skills are **triggered from Copilot chat**, not from command line. Examples:
- "Audit my website at example.com"
- "Check my rankings for 'web development'"
- "Analyze my SEO"
- "Compare my site against competitors"

Skills use Copilot's built-in tools (`fetch_webpage`, Playwright browser automation, workspace file creation).

### Report Conversion (Optional)
Convert generated markdown reports to DOCX format using Pandoc:
```bash
mkdir -p output && for file in report/*.md; do pandoc "$file" -o "output/$(basename "$file" .md).docx"; done
```

### Generate Diagrams (Optional)
Create PlantUML diagrams (requires Docker):
```bash
docker run -v $(pwd):/data plantuml/plantuml -tsvg misc/mindmap.puml
```

## Architecture Decisions
- **Skills-first design**: Each capability is a self-contained skill with detailed methodology
- **Markdown output**: All reports saved as markdown for easy review and conversion
- **Web-based analysis**: Skills analyze live websites using fetch/page capture tools
- **Structured reporting**: Tables, checklists, and actionable recommendations
- **Copilot-native**: Skills integrate with VS Code's Copilot chat interface, not as Python code

## Skill Architecture & Integration

### What Are Skills?
Skills are **methodology documents** (markdown files in `.github/skills/`) that define audit or analysis processes. They:
- Include step-by-step procedures with decision points
- Use Copilot's built-in tools (fetch, browser automation, file creation)
- Generate structured reports (markdown) saved to workspace
- Can be triggered by specific user questions or keywords

### Available Skills

#### 1. SEO/GEO/AEO Audit (`seo-geo-aeo/SKILL.md`)
**When triggered**: "audit my site", "check my SEO", "optimize for AI search", etc.

**Methodology**:
1. Ask user for audit scope (Quick 2-3 min vs Full 5-10 min)
2. Fetch target URL and key pages (Homepage, About, Services, Blog, FAQ, Contact)
3. Analyze **SEO signals**: title tags, meta descriptions, heading structure, content quality, schema markup, internal links
4. Analyze **GEO signals** (AI search): E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness), author credentials, entity clarity, structured data depth
5. Analyze **AEO signals** (Answer engines): featured snippet patterns, FAQ schema, HowTo markup, voice search readiness
6. Generate scores (1-10) for each dimension

**Outputs**:
- **Chat**: Summary table with scores + top 3 priorities
- **Workspace**: `AUDIT_REPORT_[domain]_[date].md` with detailed signal-by-signal analysis
- **Optional**: Convert to DOCX via Pandoc

#### 2. SEO Search Performance (`seo-search-performance/SKILL.md`)
**When triggered**: "check my rankings", "analyze SERP for X", "who are my competitors?", etc.

**Methodology**:
1. Ask user for analysis scope (Quick top 10 vs Full deep-dive)
2. Use browser automation to search keywords on Google
3. Capture top 10-20 organic results with titles, descriptions, positions, ratings
4. Identify featured snippets, knowledge panels, PAA (People Also Ask) boxes
5. Analyze top 10 competing domains and their average positions
6. Score visibility, competition intensity, AEO presence, GEO integration

**Outputs**:
- **Chat**: Metrics table + top 3 competitors with details
- **Workspace**: `SERP_ANALYSIS_[keywords]_[date].md` with ranking tables and competitor analysis
- **Optional**: Convert to DOCX via Pandoc

## Skill Development Conventions
When creating or updating skills:
- **Skill structure**: Each skill is a standalone `.md` file with YAML frontmatter defining name, description, trigger phrases
- **Methodology sections**: Include clear step-by-step processes with decision points
- **Output formats**: All output as markdown saved to `report/` folder
- **Report naming**: Use consistent pattern: `[TYPE]_[SUBJECT]_[DATE].md` (e.g., `AUDIT_REPORT_example.com_2025-04-22.md`)
- **Error handling**: Graceful degradation when web content is inaccessible
- **User confirmation**: Ask for scope/complexity level before proceeding with analysis

## Common Patterns
- **Fetch-first approach**: Always fetch live data before analysis
- **Parallel processing**: Use multiple Copilot tools in parallel when possible  
- **User confirmation**: Ask for audit scope/type before proceeding
- **Workspace integration**: Save reports to workspace for easy reference and archival
- **Markdown-to-DOCX**: All reports are markdown; users can convert via Pandoc
- **Scoring rubrics**: Use consistent 1-10 scale for dimensions (e.g., SEO, GEO, AEO scores)

## Testing & Validation
- **Manual testing**: Run skills in Copilot chat to verify functionality
- **Output validation**: Check generated reports in `report/` folder for completeness and accuracy
- **Browser integration**: Test with actual web searches and page captures
- **Report conversion**: Verify Pandoc conversion from markdown to DOCX works correctly
- **Sandbox testing**: Use test URLs before running audits on production sites

## Integration Configuration
### VS Code Settings
The `.vscode/settings.json` enables automatic approval for Playwright browser tools:
```json
{
  "chat.tools.autoApprove": ["playwright/*"]
}
```
This allows skills to use browser automation without prompting for approval on each action.

### Python Environment
- Python 3.12+ (locked in `.python-version`)
- `uv` manages the virtual environment and dependencies
- Currently no external dependencies; project is in early stage
- To add dependencies: Update `pyproject.toml` and run `uv sync`

### External Tool Requirements
- **Pandoc**: Required for DOCX conversion (install via `apt install pandoc` or `brew install pandoc`)
- **Docker**: Required for PlantUML diagram generation
- **Chrome/Chromium**: Used by Playwright for browser automation

## Potential Pitfalls
- **Web access limitations**: Some sites may block automated access or require authentication
- **SERP volatility**: Search results change frequently; always include timestamps in reports
- **Rate limiting**: Respect search engine terms of service when automating searches
- **Large outputs**: Truncate or paginate when generating extensive reports to avoid overwhelming chat
- **Timezone handling**: Record timezone context in audit reports for consistent reference
- **Accessibility**: Ensure reports are accessible; use proper markdown formatting and alt text

## Development Environment Setup
- **VS Code Extensions**: Ensure GitHub Copilot and related extensions are installed
- **Copilot Chat**: Enable chat functionality (required for skills to work)
- **Python Setup**: Use `uv sync` to create virtual environment
- **Browser Tools**: Playwright is called from skills; ensure Chrome/Chromium is installed
- **Report Generation**: Install Pandoc for DOCX conversion support
- **File Permissions**: Ensure `report/` and `output/` directories are writable

## For AI Agents: Key Facts for Productivity
1. **Skills-first architecture**: All capabilities are markdown methodology documents, not Python code
2. **Copilot-native execution**: Skills run in Copilot chat, triggered by user questions
3. **No production code**: There is no `main.py` or traditional application entry point
4. **Zero dependencies currently**: The project is in early stage; `pyproject.toml` has no external packages
5. **Fetch-based approach**: Skills use `fetch_webpage` and browser automation, not APIs
6. **Report outputs**: All generated files go to `report/` (markdown) and `output/` (DOCX)
7. **Naming convention**: Reports use format `[TYPE]_[SUBJECT]_[DATE].md` for organization
8. **Scoring system**: Consistent 1-10 scale used for all SEO/GEO/AEO dimensions
9. **Browser automation**: Playwright used for SERP analysis and page capture; auto-approved in VS Code
10. **Markdown reports**: All outputs are markdown-first; DOCX is optional via Pandoc conversion

## Related Documentation
- [README.md](README.md) - Report conversion and build commands
- [.github/skills/](https://github.com/user/scaling-adventure/tree/main/.github/skills/) - Individual skill methodologies
- [pyproject.toml](pyproject.toml) - Project configuration (Python 3.12+, currently no dependencies)