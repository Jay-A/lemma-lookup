import type { ErrorResponse, LookupResponse } from "./types";

const API_BASE_URL = "https://lemma-lookup.onrender.com/api";

export async function lookupWord(word: string): Promise<LookupResponse> {
  const response = await fetch(
    `${API_BASE_URL}/lookup/?word=${encodeURIComponent(word)}`,
  );

  if (!response.ok) {
    const error: ErrorResponse = await response.json();
    throw new Error(error.error);
  }

  return response.json() as Promise<LookupResponse>;
}
