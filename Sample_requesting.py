import requests

# API endpoint URL
url = "http://localhost:5000/generate_clickbait"

# Seed text and number of words
seed_text = "Amazing secrets"
num_words = 5

# Create the JSON payload
payload = {
    "seed_text": seed_text,
    "num_words": num_words
}

# Send the POST request
response = requests.post(url, json=payload)

# Get the generated text from the response
generated_text = response.json()["generated_text"]

# Print the generated text
print("Generated Text:", generated_text)
