import { useState } from "react";
import type { KeyboardEvent } from "react";

import { lookupWord } from "./api";
import type { LookupResponse } from "./types";


function App() {
  const [word, setWord] = useState("");
  const [result, setResult] = useState<LookupResponse | null>(null);
  const [lastLookup, setLastLookup] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);


  async function handleLookup() {
    const trimmedWord = word.trim();

    if (!trimmedWord) {
      setError("Please enter a word.");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const data = await lookupWord(trimmedWord);

      setResult(data);
      setLastLookup(trimmedWord);
    } catch (err) {
      setResult(null);
      setError(
        err instanceof Error
          ? err.message
          : "Something went wrong.",
      );
    } finally {
      setLoading(false);
    }
  }


  function handleKeyDown(event: KeyboardEvent<HTMLInputElement>) {
    if (event.key === "Enter") {
      void handleLookup();
    }
  }


  return (
    <main className={`app ${darkMode ? "dark" : "light"}`}>
      <header className="header">
        <h1>Lemma Lookup</h1>

        <button
          type="button"
          className="mode-button"
          onClick={() => setDarkMode((current) => !current)}
        >
          {darkMode ? "Light" : "Dark"}
        </button>
      </header>

      <div className="lookup">
        <input
          type="text"
          value={word}
          onChange={(event) => setWord(event.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Enter a German word"
          aria-label="German word"
        />

        <button
          type="button"
          onClick={() => void handleLookup()}
          disabled={loading}
        >
          {loading ? "Looking up..." : "Lookup"}
        </button>
      </div>

      {lastLookup && (
        <p className="last-lookup">
          Last lookup: <strong>{lastLookup}</strong>
        </p>
      )}

      {error && (
        <div className="error" role="alert">
          {error}
        </div>
      )}

      {result && (
        <section className="result">
          <h2>Word information</h2>

          <dl>
            <div>
              <dt>Lemma</dt>
              <dd>{result.lemma ?? "—"}</dd>
            </div>

            <div>
              <dt>Word type</dt>
              <dd>{result.pos ?? "—"}</dd>
            </div>

            <div>
              <dt>Form</dt>
              <dd>{result.word}</dd>
            </div>
          </dl>

          <h2>Morphology</h2>

          <dl>
            {Object.entries(result.morphology).map(([key, value]) => (
              <div key={key}>
                <dt>{key}</dt>
                <dd>{value}</dd>
              </div>
            ))}
          </dl>
        </section>
      )}
    </main>
  );
}

export default App;
