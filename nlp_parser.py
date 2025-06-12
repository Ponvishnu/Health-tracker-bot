import spacy

nlp = spacy.load("en_core_web_sm")

def parse_health_input(text):
    doc = nlp(text.lower())
    result = {}

    # Keywords to look for
    keywords = {
        'sleep': ['sleep', 'slept', 'napped'],
        'water': ['water', 'drank'],
        'steps': ['walked', 'steps'],
        'exercise': ['run', 'jogged', 'gym', 'workout'],
    }

    # Detect quantity
    quantity = None
    for ent in doc.ents:
        if ent.label_ == 'QUANTITY' or ent.label_ == 'CARDINAL':
            try:
                quantity = float(ent.text)
                break
            except ValueError:
                continue

    for token in doc:
        for key, vals in keywords.items():
            if token.lemma_ in vals or token.text in vals:
                result['metric'] = key
                result['value'] = quantity
                return result

    return {"metric": "unknown", "value": None}
