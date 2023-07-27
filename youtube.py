import requests
from bs4 import BeautifulSoup

def scrape_news_titles(url):
    try:
        # Send a GET request to the URL
        response = requests.get('https://indianexpress.com/todays-paper/')

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the HTML elements that contain the article titles
            article_titles = soup.find_all('h2', class_='article-title')

            # Extract and print the titles
            for title in article_titles:
                print(title.text.strip())

        else:
            print("Error: Unable to access the website.")

    except requests.exceptions.RequestException as e:
        print("Error: ", e)

if __name__ == "__main__":
    # Replace 'YOUR_NEWS_WEBSITE_URL' with the actual URL of the news website you want to scrape
    news_url = 'YOUR_NEWS_WEBSITE_URL'
    scrape_news_titles(news_url)
