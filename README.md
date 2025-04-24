#  Email Classification for Support Team

This project implements an intelligent email classification system for a support team. It classifies support requests into categories (e.g., Billing Issues, Technical Support) and ensures that all personally identifiable information (PII) is masked **before processing** using non-LLM techniques. The system is exposed as a Flask API and is compliant with strict output format requirements.


##  Objective

- Classify incoming support emails into predefined categories.
- Mask all PII before classification.
- Use regex and spaCy (non-LLM) for PII masking.
- Provide strict JSON output format as required.
- Deploy as an API for real-time usage.


##  Masked PII Fields

The system detects and masks the following fields:
- Full Name (`full_name`)
- Email Address (`email`)
- Phone Number (`phone_number`)
- Date of Birth (`dob`)
- Aadhaar Card Number (`aadhar_num`)
- Credit/Debit Card Number (`credit_debit_no`)
- CVV Number (`cvv_no`)
- Card Expiry Number (`expiry_no`)

**Example:**

**Input:**
Hello, my name is John Doe. My email is john.doe@example.com and my CVV is 123.

**Masked:**
Hello, my name is [full_name]. My email is [email] and my CVV is [cvv_no].


##  Tech Stack

- Python
- scikit-learn (Naive Bayes Classifier)
- Regex
- spaCy (`en_core_web_sm`)
- Flask (REST API)
- Pandas
- JSON


##  Project Structure
email_classifier/ ├── app.py # Main API entry ├── api.py # API route logic ├── models.py # Model training/loading ├── utils.py # PII masking logic ├── run_on_csv.py # Run classifier + masking on full dataset ├── test_api.py # Sample local API test ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── masked_and_classified_results.json # Output file from full dataset run ├── model/ │ └── saved_model.pkl # Trained classification model └── data/ └── combined_emails_with_natural_pii.csv # Input dataset



##  Setup Instructions

```bash
git clone <your-repo-url>
cd email_classifier
python -m venv env
source env/bin/activate        # On Windows use: env\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm


##  Usage

Run the API locally:
```bash
python app.py

Test API using:
```bash
python test_api.py

Process the full dataset:
```bash
python run_on_csv.py

This will generate the following output file:
masked_and_classified_results.json


## API Format
POST /classify

Request Body:
{
  "email": "Hi, I'm Arjun Mehra. You can reach me at arjun@xyz.com or call +919876543210."
}s
Response:
{
  "input_email_body": "Hi, I'm Arjun Mehra...",
  "list_of_masked_entities": [
    {
      "position": [9, 21],
      "classification": "full_name",
      "entity": "Arjun Mehra"
    },
    {
      "position": [47, 62],
      "classification": "email",
      "entity": "arjun@xyz.com"
    },
    {
      "position": [72, 85],
      "classification": "phone_number",
      "entity": "+919876543210"
    }
  ],
  "masked_email": "Hi, I'm [full_name]. You can reach me at [email] or call [phone_number].",
  "category_of_the_email": "Incident"
}



 Output File
The result of processing the full dataset is saved in:
masked_and_classified_results.json




