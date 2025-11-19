import requests
from bs4 import BeautifulSoup

url = input("Enter URL: ")

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("a"):
    print(link.get("href"))
