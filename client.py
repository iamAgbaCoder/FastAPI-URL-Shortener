import requests

# Replace with the URL of your FastAPI application
BASE_URL = "http://127.0.0.1:8000"

# Function to shorten a URL
def shorten_url(long_url):
    payload = {"long_url": long_url}
    response = requests.post(f"{BASE_URL}/shorten/", json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['short_url']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to redirect to the original URL
def redirect_to_original_url(short_url):
    response = requests.get(f"{BASE_URL}/{short_url}")
    if response.status_code == 200:
        data = response.json()
        return data['short_url']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

if __name__ == "__main__":
    long_url = "https://www.example.com"
    # long_url = input("[PROMPT] ==> Enter long URL: ")
    
    # Shorten a URL
    short_url = shorten_url(long_url)
    if short_url:
        print(f"Shortened URL: {short_url}")
    
    # Redirect to the original URL
    if short_url:
        original_url = redirect_to_original_url(short_url)
        if original_url:
            print(f"Redirecting to: {original_url}")
