export interface Morphology {
  Mood?: string;
  Number?: string;
  Person?: string;
  Tense?: string;
  VerbForm?: string;
}

export interface LookupResponse {
  word: string;
  lemma: string | null;
  pos: string | null;
  morphology: Morphology;
}

export interface ErrorResponse {
  error: string;
}
