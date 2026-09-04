import spacy


MODEL_NAME = "de_core_news_sm"

nlp = spacy.load(MODEL_NAME)


def lookup_word(word: str) -> dict:
    """
    Analyze a German word with spaCy and return structured information.
    """
    doc = nlp(word)

    if not doc:
        return {
            "word": word,
            "lemma": None,
            "pos": None,
            "morphology": {},
        }

    token = doc[0]

    return {
        "word": token.text,
        "lemma": token.lemma_,
        "pos": token.pos_,
        "morphology": {
            key: values
            for key, values in token.morph.to_dict().items()
        },
    }


