import requests
import time
from bs4 import BeautifulSoup as BSP
HEADERS = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            }
r = requests.get(r"https://www.sahibinden.com",timeout=300,headers = HEADERS)
time.sleep(4)
kaynak = BSP(r.content,"lxml")
print(kaynak.title)
liste = kaynak.find_all("li")
for item in liste:
    print(liste.get("a",attrs={"class":"successfulSales"}))