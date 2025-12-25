import requests
import json
import sys

# Define the endpoint
url = "http://127.0.0.1:8000/analyze"

# Construct the payload mimicking a request from the Rails app
payload = {
    "query": "Show me the sales for the last 30 days",
    "shop_domain": "demo-store.myshopify.com",
    "access_token": "mock_access_token_123"
}

print(f"Sending POST request to {url}...")
print(f"Payload: {json.dumps(payload, indent=2)}\n")

try:
    # Send the request
    response = requests.post(url, json=payload)
    
    # Check if request was successful
    if response.status_code == 200:
        print("✅ SUCCESS! Server responded with 200 OK.")
        print("Response Body:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"❌ FAILED. Status Code: {response.status_code}")
        print("Response Text:")
        print(response.text)

except requests.exceptions.ConnectionError:
    print("❌ ERROR: Could not connect to the server. Is uvicorn running on port 8000?")
except Exception as e:
    print(f"❌ ERROR: An unexpected error occurred: {e}")
