import re
import spacy

# Load spaCy NER model
nlp = spacy.load("en_core_web_sm")

# PII patterns for masking
PII_PATTERNS = {
    "email": r"[\w\.-]+@[\w\.-]+\.\w+",
    "phone_number": r"(?:\+91[\-\s]?)?[6-9]\d{9}",
    "dob": r"\b(?:\d{1,2}[/-]){2}\d{2,4}\b",
    "aadhar_num": r"\b(?!91)\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d{4}[\s-]?){4}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/?([0-9]{2}|[0-9]{4})\b"
}

def mask_pii(text):
    entities = []
    replacements = []
    seen = set()

    priority_order = [
        "email",
        "phone_number",
        "dob",
        "aadhar_num",
        "credit_debit_no",
        "cvv_no",
        "expiry_no"
    ]

    for entity_type in priority_order:
        pattern = PII_PATTERNS[entity_type]
        for match in re.finditer(pattern, text):
            start, end = match.span()
            if (start, end) in seen:
                continue
            seen.add((start, end))
            replacement = f"[{entity_type}]"
            replacements.append((start, end, replacement))
            entities.append({
                "position": [start, end],
                "classification": entity_type,
                "entity": match.group()
            })

    # Full Name Detection
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            start, end = ent.start_char, ent.end_char
            if (start, end) not in seen:
                replacement = "[full_name]"
                replacements.append((start, end, replacement))
                entities.append({
                    "position": [start, end],
                    "classification": "full_name",
                    "entity": ent.text
                })
                seen.add((start, end))

    # Apply all replacements (right to left so index shifts don't affect earlier spans)
    replacements.sort(key=lambda x: x[0], reverse=True)
    masked_text = text
    for start, end, replacement in replacements:
        masked_text = masked_text[:start] + replacement + masked_text[end:]

    return masked_text, entities

