import requests
import time

# Function to fetch the first 100 Solana tokens from Dexscreener API
def fetch_solana_tokens():
    url = "https://api-v3.raydium.io/"
    
    # Send request to the API
    response = requests.get(url)
    
    # Check if the response is valid
    if response.status_code == 200:
        data = response.json()
        
  

# Function to print tokens in a loop
def print_tokens():
    while True:
        tokens = fetch_solana_tokens()
        
        if tokens:
            print("\nNew Tokens:\n")
            for token in tokens:
                name = token.get("name", "N/A")
                ca = token.get("address", "N/A")  # Get the contract address
                
                print(f"+ {name} ({ca})")
        
        # Wait for 10 seconds before checking again
        print("\nWaiting for the next check...\n")
        time.sleep(10)

# Start the process
if __name__ == "__main__":
    print("Starting Solana token monitor...\n")
    print_tokens()
