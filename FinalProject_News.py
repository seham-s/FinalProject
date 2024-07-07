# to interact with the New York Times API by sending requests and receiving responses.
import requests 

# Sets up the base URL and stores the API key
class NYTAPI:
    def __init__(self, api_key): 
        self.base_url = "https://api.nytimes.com/svc/topstories/v2/" 
        self.api_key = api_key 

# Sends requests to the NYT API and prints article details.
    def fetch_top_stories(self, section='home'): 
        endpoint = f"{self.base_url}{section}.json"
        params = {'api-key': self.api_key}

# Sends a request to the NYT API and retrieves the response.
        response = requests.get(endpoint, params=params) 

# For the response code
        if response.status_code == 200:
            data = response.json() #convert the jason response into python dictionary
            articles = data.get('results', []) # Retrieves the list of articles or returns an empty list if not found.

            if articles:
                print(f"Recent Articles in '{section}':\n")
                for article in articles:
                    print(f"Title: {article['title']}")
                    print(f"Abstract: {article['abstract']}")
                    print(f"URL: {article['url']}")
                    print("-" * 40)
            else:
                print(f"No articles found in '{section}'.")
        else:
            print(f"Failed to fetch articles. Status code: {response.status_code}")

if __name__ == "__main__": # Ensures the code runs only when the script is executed directly, not when imported as a module.
    api_key = '1SIAsQGTDlMSA6CRxWhq6JTCHSok3qMG'  
    nyt_api = NYTAPI(api_key)
    section = input("Enter section (e.g., arts, business, sports): ").lower()  # Prompt user to input the section
    nyt_api.fetch_top_stories(section)

# site used for the API https://developer.nytimes.com/docs/top-stories-product/1/routes/%7Bsection%7D.json/get