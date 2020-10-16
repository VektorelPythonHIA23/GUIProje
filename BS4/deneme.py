import requests
import time
from bs4 import BeautifulSoup 
HEADERS = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
            }
sayfa = requests.get(r"https://www.sahibinden.com/satilik-daire/ankara-cankaya?pagingOffset={10}",timeout=300,headers = HEADERS)
time.sleep(3)
soup = BeautifulSoup(sayfa.content,"html.parser")
liste1 = soup.findAll("tr",class_="searchResultsItem")
liste2 = soup.findAll("td",class_="searchResultsAttributeValue")
liste3 = soup.findAll("td",class_="searchResultsPriceValue")
liste4 = soup.findAll("td",class_="searchResultsDateValue")
liste5 = soup.findAll("td",class_="searchResultsLocationValue")
listeOda = []
listem2 = []
for i in range(len(liste2)):
    if i % 2==0:
        listem2.append(liste2[i])
    else:
        listeOda.append(liste2[i])

# print(liste1[1].text)
for i in range(len(liste3)):
    # print(liste1[i])
    print(liste3[i].text.replace("\n","").lstrip().split(" ")[0])
    print(liste3[i].text.replace("\n","").lstrip().split(" ")[1])    
    print(listem2[i].text.strip())
    print(listeOda[i].text.strip())
    print(liste4[i].text.strip().replace("\n"," "))
    print(liste5[i].text.strip())
    
