import requests
from bs4 import BeautifulSoup

url = 'https://www.countdown.co.nz/shop/productdetails?stockcode=58643&name=countdown-fresh-tomatoes-cherry'

# Send a request to the website and get its HTML content
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/'
}

response = requests.get(url, headers=headers)
print(response)
html_content = response.content
print(html_content)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the item name and price using their respective HTML elements
item_name = soup.find('div', {'class': 'product-detail-header'}).h1.text.strip()
price = soup.find('div', {'class': 'product-price'}).span.text.strip()

# Print the results
print(f"Item Name: {item_name}")
print(f"Price: {price}")