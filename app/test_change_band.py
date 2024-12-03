import requests

API_URL = "http://localhost:5000/test/change_band"

def test_change_band(frequency):
    response = requests.post(API_URL, json={"frequency": frequency})
    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: {response.json()}")

if __name__ == "__main__":
    # Example: Change to 14 MHz (20m band)
    test_change_band(14000000)
