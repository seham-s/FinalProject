import requests

class NYTAPI:
    def __init__(self, api_key_file):
        self.base_url = "https://api.nytimes.com/svc/topstories/v2/"
        # Read the API key from a file
        with open(api_key_file, 'r') as file:
            self.api_key = file.read().strip()

    def fetch_top_stories(self, section='home'):
        endpoint = f"{self.base_url}{section}.json"
        params = {'api-key': self.api_key}

        # Sends a request to the NYT API and retrieves the response.
        response = requests.get(endpoint, params=params)

        # Check the response code
        if response.status_code == 200:
            data = response.json()  # Convert the JSON response into a Python dictionary
            articles = data.get('results', [])  # Retrieves the list of articles or returns an empty list if not found.

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

if __name__ == "__main__":
    # Provide the path to the file containing your API key
    api_key_file = 'NYTKey.txt'
    nyt_api = NYTAPI(api_key_file)
    section = input("Enter section (e.g., arts, business, sports): ").lower()  # Prompt user to input the section
    nyt_api.fetch_top_stories(section)