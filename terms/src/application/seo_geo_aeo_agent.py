"""
Search Term Research Agent
==========================
Pass a website → get back the N most popular search terms + why each ranks there.

Install
-------
uv add langchain langchain-openai langchain-community python-dotenv rich pydantic

Environment (.env)
------------------
OPENROUTER_API_KEY=sk-or-...   # https://openrouter.ai/keys

Usage
-----
python query_research_agent.py apacrelocation.com
python query_research_agent.py apacrelocation.com -n 20
python query_research_agent.py apacrelocation.com --model anthropic/claude-sonnet-4-6
"""

from __future__ import annotations

import json
import os
from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from rich.console import Console
from rich.table import Table

load_dotenv()
console = Console()

DEFAULT_MODEL = "nvidia/nemotron-super-49b-v1:free"

SYSTEM_PROMPT = """
You are an SEO expert. Given a website, find the most popular search terms
people use to find it.

Steps:
1. Search for the website name / brand to understand what it does.
2. Search for the industry + services to find common search terms.
3. Search for competitor or related terms people use in this niche.

Then return a ranked list of search terms from most to least popular.
For each term, include a short reason (1 sentence) explaining why it ranks
at that position — e.g. high search volume, strong brand match, competitor
gap, or long-tail intent.
"""


# ── Structured output schema ──────────────────────────────────────────────────

class SearchTerm(BaseModel):
    term: str = Field(description="The search term people use to find this site")
    reason: str = Field(description="One sentence explaining why this term ranks at this position")


class SearchTermList(BaseModel):
    terms: List[SearchTerm] = Field(description="Ranked list of search terms, most popular first")


# ── Model & agent ─────────────────────────────────────────────────────────────

def _make_model(model_id: str) -> ChatOpenAI:
    return ChatOpenAI(
        model=model_id,
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
        temperature=0,
    )


@tool
def web_search(query: str) -> str:
    """Search the web and return results."""
    return DuckDuckGoSearchRun().run(query)


def build_agent(model_id: str):
    model = _make_model(model_id)
    return create_agent(
        model=model,
        tools=[web_search],
        system_prompt=SYSTEM_PROMPT,
        response_format=ToolStrategy(SearchTermList),  # ✅ typed structured output
    )


# ── Research runner ───────────────────────────────────────────────────────────

def run_research(website: str, n: int = 10, model: str = DEFAULT_MODEL, context: str = "") -> list[SearchTerm]:
    if not website.startswith("http"):
        website = f"https://{website}"

    domain = website.replace("https://", "").replace("http://", "").rstrip("/")

    agent = build_agent(model)

    content = (
        f"""Understand the business of the Website: {domain}\n.
        Find its competitors and the industry it operates in.\n
        Return the top {n} search terms people use to find this site, 
        with a reason for each term's ranking position."
    )
    if context.strip():
        content += f"\n\nContext: {context.strip()}"

    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": content,
        }]
    })

    # ✅ structured_response is populated by create_agent when response_format is set
    output: SearchTermList = result["structured_response"]
    terms = output.terms[:n]

    _print_table(terms, domain)
    return terms


# ── Display ───────────────────────────────────────────────────────────────────

def _print_table(terms: list[SearchTerm], domain: str) -> None:
    t = Table(title=f"Top search terms · {domain}", show_lines=True)
    t.add_column("#",           style="dim",        width=4)
    t.add_column("Search Term", style="bold white",  min_width=30)
    t.add_column("Why it ranks here", style="grey70")
    for i, item in enumerate(terms, 1):
        t.add_row(str(i), item.term, item.reason)
    console.print(t)


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Find top search terms for a website")
    p.add_argument("website", help="e.g. apacrelocation.com")
    p.add_argument("-n", type=int, default=10, help="Number of terms (default: 10)")
    p.add_argument("--model", default=DEFAULT_MODEL)
    args = p.parse_args()

    terms = run_research(args.website, args.n, args.model)

    with open("search_terms.json", "w") as f:
        json.dump(
            [{"term": t.term, "reason": t.reason} for t in terms],
            f,
            indent=2,
        )
    console.print("\n[dim]Saved → search_terms.json[/]")