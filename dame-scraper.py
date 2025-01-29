import random
import requests
from bs4 import BeautifulSoup

dames = ["Ada Lovelace", "Grace Hopper", "Radia Perlman", "Betty Snyder", "Betty Jean Jennings"]
dame_links = ["https://en.wikipedia.org/wiki/Ada_Lovelace", "https://en.wikipedia.org/wiki/Grace_Hopper", "https://en.wikipedia.org/wiki/Radia_Perlman",
              "https://en.wikipedia.org/wiki/Betty_Holberton", "https://en.wikipedia.org/wiki/Jean_Bartik"]

print("Welcome to Dames of Code - recognising historic (and often forgotten) women in tech.\n\n")

#Generating dame of focus
i = random.randint(0, (len(dames)-1))
print(dames[i], "\n\n")

#Scraping Wikipedia page of dame
url = dame_links[i]
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

refs = soup.find_all('sup')
for ref in refs:
    ref.decompose()

info = soup.find_all('p')
for x in info:
    print(x.text.strip())
    print()

print("Thank you for educating yourself.")