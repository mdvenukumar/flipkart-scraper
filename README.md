# Flipkart Scraper

Flipkart Scraper is a Python library designed for extracting detailed product information from Flipkart. This library utilizes web scraping techniques to gather data such as title, price, rating, number of reviews, and description from a given Flipkart product URL.




## Installation

### 1. Prerequisites

Before installing Flipkart Scraper, make sure you have the following prerequisites installed on your system:

- Python (version 3.6 and above)
- pip (Python package installer)

### 2. Install Flipkart Scraper
Use pip to install Flipkart Scraper:
```bash
pip install flipkart-scraper
```
### 3. Verify Installation
You can verify the installation by running the following command
```bash
flipkart-scraper --version
```


## Usage/Examples

### To use Flipkart Scraper, follow these simple steps:

```python
from thevk.flipkartscraper import FlipkartScraper

# Replace the URL with the Flipkart product you want to scrape
url = "https://www.flipkart.com/some-product"

# Initialize the FlipkartScraper with the provided URL
scraper = FlipkartScraper(url)
```



## In-Built Methods:
### 1. get_title()
This method returns the title of the product.
```python
title = scraper.get_title()
print("Title:", title)
```
### 2. get_price()
This method returns the price of the product
```python
price = scraper.get_price()
print("Price:", price)
```
### 3. get_rating()
This method returns the rating of the product.
```python
rating = scraper.get_rating()
print("Rating:", rating)
```
### 4. get_num_reviews()
This method returns the number of reviews for the product.
```python
num_reviews = scraper.get_num_reviews()
print("Number of Reviews:", num_reviews)
```
### 5. get_description()
This method returns the description of the product.
```python
description = scraper.get_description()
print("Description:", description)
```
## Acknowledgements

- [Requests](https://docs.python-requests.org/en/latest/) - HTTP library for Python
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - HTML parsing library for Python



## About the Author

Hi there! 👋 I'm Durga Venu Kumar Mutyala, the author of Flipkart Scraper. I'm passionate about AI, Automation and many more.

## Contact

- **Email:** thevk22@gmail.com
- **LinkedIn:** [Durga Venu Kumar Mutyala](https://www.linkedin.com/in/venukumarmd/)
- **Twitter:** [@thevk22](https://twitter.com/thevk22)

Feel free to reach out if you have any questions, suggestions, or just want to connect. I'd love to hear from you!


Happy coding! 🚀




## Contributing to Flipkart Scraper

Contributions are always welcome!

Thank you for considering contributing to Flipkart Scraper! Your contributions help make this project better.

## Code of Conduct

This project and everyone participating in it are governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [your email or a moderation contact].

## How to Contribute

### 1. Fork the repository to your GitHub account.
### 2. Clone the forked repository to your local machine.

```bash
git clone https://github.com/yourusername/flipkart-scraper.git
cd flipkart-scraper
```
### 3. Create a new branch for your feature or bug fix.
```bash
git checkout -b feature/your-feature
```
#### Make your changes and ensure they are working as expected.
### 4. Commit your changes.

```bash
git commit -m "Add your feature or fix"
```
### 5. Push the changes to your GitHub repository.
```bash
git push origin feature/your-feature
```