from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..application.seo_geo_aeo_agent import run_research

app = FastAPI(title="Terms API", description="A FastAPI application using hexagonal architecture")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4173", "http://127.0.0.1:4173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from Terms API!"}

@app.get("/search-terms/{website}")
def get_search_terms(website: str, n: int = 10, model: str = "nvidia/nemotron-3-super-120b-a12b:free", context: str = ""):
    terms = run_research(website, n, model, context)
    return {"website": website, "terms": terms}