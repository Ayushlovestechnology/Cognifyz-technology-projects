import requests
from bs4 import BeautifulSoup

def scrape_ndtv_latest_news(url):
    # Fetch the HTML content of the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the news headlines
        headlines = soup.find_all('h2', class_='newsHdng')
        
        # Extract and print the headlines
        for headline in headlines:
            print(headline.text.strip())
    else:
        print("Failed to fetch the webpage.")

# URL of the webpage to scrape
url = "https://www.ndtv.com/latest"

# Call the function to scrape latest news headlines
scrape_ndtv_latest_news(url)
