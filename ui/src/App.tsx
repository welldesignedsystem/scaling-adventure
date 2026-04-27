import { useState } from "react";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

interface SearchTerm {
  term: string;
  reason: string;
}

const normalizeWebsite = (input: string) =>
  input.trim().replace(/^https?:\/\//, "").replace(/\/$/, "");

function App() {
  const [website, setWebsite] = useState("");
  const [count, setCount] = useState(10);
  const [context, setContext] = useState("");
  const [terms, setTerms] = useState<SearchTerm[]>([]);
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");
  const [error, setError] = useState("");

  const fetchTerms = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError("");
    setTerms([]);

    const normalized = normalizeWebsite(website);
    if (!normalized) {
      setError("Please enter a website or domain.");
      return;
    }

    setStatus("loading");
    try {
      const params = new URLSearchParams();
      params.set("n", count.toString());
      if (context.trim()) {
        params.set("context", context.trim());
      }

      const response = await fetch(
        `${apiBaseUrl}/search-terms/${encodeURIComponent(normalized)}?${params.toString()}`
      );

      if (!response.ok) throw new Error(`API returned ${response.status}`);

      const data = await response.json();
      if (!Array.isArray(data.terms)) throw new Error("Unexpected API response format.");

      setTerms(data.terms);
      setStatus("success");
    } catch (err) {
      setStatus("error");
      setError(err instanceof Error ? err.message : "Something went wrong.");
    }
  };

  return (
    <div className="page-shell">
      <header className="hero-card">
        <h1>Search Term Explorer</h1>
        <p>Enter a website or domain and query the backend API for the top search terms people use to find it.</p>
      </header>

      <main className="content-grid">
        <section className="panel">
          <form onSubmit={fetchTerms} className="form-grid">
            <label>
              Website or domain
              <input
                value={website}
                onChange={(e) => setWebsite(e.target.value)}
                placeholder="example.com or https://example.com"
                autoFocus
              />
            </label>

            <label>
              Number of terms
              <input
                type="number"
                min={1}
                max={25}
                value={count}
                onChange={(e) => setCount(Number(e.target.value))}
              />
            </label>

            <label>
              Context (optional)
              <textarea
                value={context}
                onChange={(e) => setContext(e.target.value)}
                placeholder="E.g., 'B2B SaaS for project management' or 'Focus on enterprise solutions'"
                rows={4}
              />
            </label>

            <button type="submit" className="submit-button" disabled={status === "loading"}>
              {status === "loading" ? "Loading…" : "Fetch terms"}
            </button>

            {status === "error" && <div className="alert">{error}</div>}
          </form>
        </section>

        <section className="panel results-panel">
          <div className="results-header">
            <h2>Search terms</h2>
            <span className="tag">API: {apiBaseUrl}</span>
          </div>

          {status === "idle" && (
            <div className="empty-state">Enter a site and click Fetch terms to begin.</div>
          )}

          {status === "loading" && (
            <div className="empty-state">Researching search terms, this may take a minute…</div>
          )}

          {status === "success" && terms.length === 0 && (
            <div className="empty-state">No terms returned. Try a different site.</div>
          )}

          {terms.length > 0 && (
            <table className="terms-table">
              <thead>
                <tr>
                  <th className="col-rank">#</th>
                  <th className="col-term">Search Term</th>
                  <th className="col-reason">Why It Ranks</th>
                </tr>
              </thead>
              <tbody>
                {terms.map((item, index) => (
                  <tr key={`${item.term}-${index}`}>
                    <td className="col-rank">{index + 1}</td>
                    <td className="col-term">{item.term}</td>
                    <td className="col-reason">{item.reason}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;