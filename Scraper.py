import requests as re
from bs4 import BeautifulSoup
import json
import os
import csv
import urllib.parse


url="https://books.toscrape.com/"
ses=re.Session()
ses.headers.update({"User-Agent": "Mozilla/5.0"})
books_data=[]

while True:
    try:
         r=ses.get(url,timeout=20)
         #print("length of this is",len(r.text))
    except re.exceptions.Timeout:
         print("excedded limited time")
    r.encoding=r.apparent_encoding
    html=r.text
    soup=BeautifulSoup(html,"html.parser")

    page=soup.find("li",class_="current").text.strip()
    #print("page number is",page)
    
    book=soup.find_all("article",class_="product_pod")
    
    
    for lo in book:
        tit=lo.find("h3").find("a")["title"]
        pri=lo.find("p",class_="price_color").text.strip()
        ava=lo.find("p",class_="instock availability").text.strip()
        books={"title":tit,
               "price":pri,
               "availibilty":ava}
        books_data.append(books)
        
        
    next_btn=soup.find("li",class_="next")
    if not next_btn:
        break
    
    next_page=next_btn.find("a")["href"]
    url=urllib.parse.urljoin(url,next_page)
    
with open("pra.csv","w",newline="",encoding="utf-8") as f:
    writer= csv.DictWriter(
        f,
        fieldnames=["title","price","availibilty"]
    )
    
    writer.writeheader()
    writer.writerows(books_data)
    
print("csv printed sucesfully")

with open("pra.json","w",encoding="utf-8") as f:
    json.dump(books_data,f,indent=4)
    
print("JSON saved successfully")

    
    

    

