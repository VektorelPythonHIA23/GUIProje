import requests
import time
from bs4 import BeautifulSoup

class Emlak1():
    def __init__(self,*args, **kwargs):
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            }
        self.url = "www.google.com"
        for key,value in kwargs.items():
            if key == "adres":
                self.url = value
    
    def veriCek(self,adres):
        self.url = adres
        sayfa = requests.get(self.url,timeout=300,headers = self.headers)
        time.sleep(3)
        soup = BeautifulSoup(sayfa.content,"html.parser")
        # liste1 = soup.findAll("tr",class_="searchResultsItem")
        liste2 = soup.findAll("td",class_="searchResultsAttributeValue")
        liste3 = soup.findAll("td",class_="searchResultsPriceValue")
        liste4 = soup.findAll("td",class_="searchResultsDateValue")
        liste5 = soup.findAll("td",class_="searchResultsLocationValue")
        sonuc = []
        bigSonuc = []
        listeOda = []
        listem2 = []
        for i in range(len(liste2)):
            if i % 2==0:
                listem2.append(liste2[i])
            else:
                listeOda.append(liste2[i])

        for i in range(len(liste3)):
            sonuc = []
            sonuc.append(liste3[i].text.replace("\n","").lstrip().split(" ")[0])
            sonuc.append(liste3[i].text.replace("\n","").lstrip().split(" ")[1])    
            sonuc.append(listem2[i].text.strip())
            sonuc.append(listeOda[i].text.strip())
            sonuc.append(liste4[i].text.strip().replace("\n"," "))
            sonuc.append(liste5[i].text.strip())
            bigSonuc.append(";".join(sonuc)+"\n") 
        return bigSonuc