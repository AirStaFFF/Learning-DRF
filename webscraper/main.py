from bs4 import BeautifulSoup
import requests


search = input("Enter search term:")
params = {"string": search}

r = requests.get("https://allegro.pl/listing", params=params)
print(r.url)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
results = soup.find("section", {"class": "_9c44d_3pyzl"})
print("results", results)
links = results.findAll("article")
print("links", links)

for link in links:
    item_block = link.find("a", {"class": "_w7z6o"})
    item_link = item_block.attrs['href']
    item_text = item_block.text

    if item_link and item_text:
        print(item_link)
        print(item_text)

        print("Parrent:", item_block.parent.parent.parent)