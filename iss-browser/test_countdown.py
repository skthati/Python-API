import requests

url = "https://www.countdown.co.nz/shop/productdetails?stockcode=58643&name=countdown-fresh-tomatoes-cherry"

response = requests.get(url)

print(response.text())