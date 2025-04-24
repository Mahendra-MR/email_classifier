import requests

url = "http://127.0.0.1:5000/classify"

payload = {
    "email": "Subject: Billing Problem\n\nMy name is Arjun Mehra. I have been charged twice for the same transaction. Please check the details and let me know. You can reach me at arjunmehra@example.com or call at +919876543210."
}

response = requests.post(url, json=payload)

print("Response from API:\n", response.json())
