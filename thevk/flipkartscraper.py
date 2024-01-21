import requests
from bs4 import BeautifulSoup

class FlipkartScraper:
    def __init__(self, url):
        self.url = url
        self.html_content = self.fetch_html()

        if not self.html_content:
            print("Initialization failed. Check the provided URL.")

        self.soup = BeautifulSoup(self.html_content, 'html.parser')
        self.product_info = self.get_product_info()

    def fetch_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: Unable to fetch HTML content. Status code: {response.status_code}")
            return None

    def get_product_info(self):
        title_element = self.soup.find('span', {'class': 'B_NuCI'})
        title = title_element.get_text().strip() if title_element else None

        price_element = self.soup.find('div', {'class': '_30jeq3'})
        price = price_element.get_text().strip() if price_element else None

        rating_element = self.soup.find('div', {'class': '_3LWZlK'})
        rating = rating_element.text if rating_element else None

        num_reviews_element = self.soup.find('span', {'class': '_2_R_DZ'})
        num_reviews = num_reviews_element.text if num_reviews_element else None

        description_element = self.soup.find('div', {'class': '_1mXcCf'})
        description = description_element.get_text().strip() if description_element else None

        return {'title': title, 'price': price, 'rating': rating, 'num_reviews': num_reviews, 'description': description}

    def get_title(self):
        return self.product_info.get('title', 'Title not found')

    def get_price(self):
        return self.product_info.get('price', 'Price not found')

    def get_rating(self):
        return self.product_info.get('rating', 'Rating not found')

    def get_num_reviews(self):
        return self.product_info.get('num_reviews', 'Number of Reviews not found')

    def get_description(self):
        return self.product_info.get('description', 'Description not found')
