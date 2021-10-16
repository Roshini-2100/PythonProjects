import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.amazon.in/s?k=rings&ref=nb_sb_noss_1")

soup =BeautifulSoup(req.content, "html.parser")

res = soup.title

print(soup.get_text())
