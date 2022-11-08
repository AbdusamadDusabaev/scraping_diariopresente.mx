import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv


fields = ["Date", "Title", "URL"]
with open("diariopresente.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(fields)

headers = {"user-agent": UserAgent().chrome}
domain = "https://www.diariopresente.mx"
categories = ["sucesos", "villahermosa", "tabasco", "mexico", "politica", "mundo",
              "deportes", "espectaculos", "cultura", "sociales", "actualidad"]
for category in categories:
    url = f"https://www.diariopresente.mx/{category}"
    response = requests.get(url=url, headers=headers)
    bs_object = BeautifulSoup(response.content, "lxml")
    articles_block = bs_object.find_all(name="section", class_="inner-page-contents")[-1]
    articles = articles_block.find_all(name="div", class_="col-lg-12 listado")
    for article in articles:
        link = domain + article.find(name="div", class_="pic seccionlistado").a["href"]
        title = article.find(name="div", class_="pic seccionlistado").a["title"]
        date = article.find(name="div", class_="info").find_all(name="span")[-1].text.strip()
        result = [date, title, link]
        with open("diariopresente.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(result)
