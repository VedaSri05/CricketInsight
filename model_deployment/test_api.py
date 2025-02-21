import requests

# Define the API URL
url = "http://127.0.0.1:5000/predict"

# Sample player stats
sample_data = {
    "total_matches": 250,
    "innings": 240,
    "average_score": 45.2,
    "strike_rate": 89.5,
    "highest_score": 180,
    "fours": 1200,
    "sixes": 150,
    "fifties": 60,
    "hundreds": 25
}

# Send POST request
response = requests.post(url, json=sample_data)

# Print response
print("Response:", response.json())
