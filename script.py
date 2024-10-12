 
import subprocess

def read_api_keys(filename):
    """Reads API keys from the given file."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def test_api_key(api_key):
    """Tests if the API key is valid by calling Google Maps API using curl."""
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address=New+York&key={api_key}"
    try:
        # Use curl to make the API request
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True,
            text=True,
            timeout=10
        )
        response = result.stdout
        # Check if the response contains "error_message"
        if '"error_message"' not in response:
            return True  # Valid API key
        else:
            return False  # Invalid API key
    except subprocess.TimeoutExpired:
        print(f"Request timed out for key: {api_key}")
        return False

def main():
    api_keys = read_api_keys("api.txt")
    valid_keys = []

    print("Testing API keys...\n")
    for key in api_keys:
        if test_api_key(key):
            print(f"✅ Valid API Key: {key}")
            valid_keys.append(key)
        else:
            print(f"❌ Invalid API Key: {key}")

    if valid_keys:
        print("\nSummary of Working API Keys:")
        for key in valid_keys:
            print(key)
    else:
        print("\nNo valid API keys found.")

if __name__ == "__main__":
    main()
