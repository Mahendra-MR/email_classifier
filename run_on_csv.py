# run_on_csv.py

import pandas as pd
from models import load_model
from utils import mask_pii
import json

df = pd.read_csv("data/combined_emails_with_natural_pii.csv")
model = load_model()

results = []

for idx, row in df.iterrows():
    input_text = row["email"]
    masked_email, entities = mask_pii(input_text)
    category = model.predict([masked_email])[0]

    result = {
        "input_email_body": input_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

    results.append(result)
    print(json.dumps(result, indent=2, ensure_ascii=False))  # ← optional for console view

# Save to file for submission & GitHub
with open("masked_and_classified_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ Done: Output saved to masked_and_classified_results.json")
