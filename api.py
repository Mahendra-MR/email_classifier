from flask import Flask, request, jsonify
from models import load_model
from utils import mask_pii

app = Flask(__name__)
model = load_model()

@app.route('/classify', methods=['POST'])
def classify_email():
    data = request.get_json()
    input_email = data.get("email", "")

    masked_email, entities = mask_pii(input_email)
    category = model.predict([masked_email])[0]

    response = {
        "input_email_body": input_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

    return jsonify(response)
