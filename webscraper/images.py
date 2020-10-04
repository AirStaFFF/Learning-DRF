from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import time
import os

def StartSearch():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()
    result = requests.get("http://bing.com/images/search", params=params)

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    print("STATUS:", result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for link in links:
        try:
            img_url = link.attrs['href']
            image_request = requests.get(img_url)
            title = img_url.split('/')[-1]
            print(f"Status img {title}", image_request.status_code)
            path = f"./{dir_name}/{title}"
            try:
                image = Image.open(BytesIO(image_request.content))
                image.save(path, image.format)
            except:
                print('Could not save')

            time.sleep(1)
        except:
            print("Could not request")

    StartSearch()


StartSearch()
