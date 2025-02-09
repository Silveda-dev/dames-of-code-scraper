import random
import requests
from bs4 import BeautifulSoup
from flask import Flask
from markupsafe import Markup

#Flask constructor using name of current module
app = Flask(__name__)

dames = ["Ada Lovelace", "Grace Hopper", "Radia Perlman", "Betty Holberton (nee Snyder)", "Betty Jean Jennings",
         "Kathleen 'Kay' Antonelli (nee McNulty)", "Marlyn Meltzer (nee Wescoff)", "Frances Spence (nee Bilas)",
         "Ruth Teitelbaum (nee Lichterman)", "Mary Hawes", "Jean E. Sammet", "Milly Koss", "St. Jude (aka Jude Milhon)",
         "Pamela Hardt-English", "Elizabeth 'Jake' Feinler", "Dame Wendy Hall", "Karen Catlin", "Cathy Marshall", "Jaime Levy"]
dame_links = ["https://en.wikipedia.org/wiki/Ada_Lovelace", "https://en.wikipedia.org/wiki/Grace_Hopper", "https://en.wikipedia.org/wiki/Radia_Perlman",
              "https://en.wikipedia.org/wiki/Betty_Holberton", "https://en.wikipedia.org/wiki/Jean_Bartik", "https://en.wikipedia.org/wiki/Kathleen_Antonelli",
              "https://en.wikipedia.org/wiki/Marlyn_Meltzer", "https://en.wikipedia.org/wiki/Frances_Spence", "https://en.wikipedia.org/wiki/Ruth_Teitelbaum",
              "https://en.wikipedia.org/wiki/Mary_K._Hawes", "https://en.wikipedia.org/wiki/Jean_E._Sammet", "https://en.wikipedia.org/wiki/Milly_Koss",
              "https://en.wikipedia.org/wiki/Jude_Milhon", "https://en.wikipedia.org/wiki/Pamela_Hardt-English", "https://en.wikipedia.org/wiki/Elizabeth_J._Feinler",
              "https://en.wikipedia.org/wiki/Wendy_Hall", "https://en.wikipedia.org/wiki/Karen_Catlin", "https://en.wikipedia.org/wiki/Cathy_Marshall_(hypertext_developer)",
              "https://en.wikipedia.org/wiki/Jaime_Levy"]

def dame_finder():
    scraped_dame = '<h1 class="title">Dames of Code</h1>'
    scraped_dame += '<h3>Recognising significant (and often forgotten) women in technology</h3>'

    #Generating dame of focus
    chosen_dame = random.randint(0, (len(dames)-1)) 
    scraped_dame += "<h2 class='name'>"
    scraped_dame += dames[chosen_dame]
    scraped_dame += "</h2>"

    #Scraping Wikipedia page of dame
    url = dame_links[chosen_dame]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    #Removes Wikipedia in-text citations (e.g. [1])
    refs = soup.find_all('sup')
    for ref in refs:
        ref.decompose()

    info = soup.find_all('p')
    i = 0
    current_para = ""

    #Adds each of the first five paragraphs with appropriate line breaks
    for x in info:
        current_para = x.text.strip()
        if current_para != "":
            scraped_dame += current_para
            scraped_dame += "<br/><br/>"
        i += 1
        if i >= 5:
            break

    #Inserts link to scraped page for more information    
    scraped_dame += "You can find out more at: "
    scraped_dame += '<a href="' + dame_links[chosen_dame] + '" target="_blank">'
    scraped_dame += dame_links[chosen_dame]
    scraped_dame += "</a><br/><br/>"
    
    #Creates 'regenerate' button which refreshes the page when clicked on, triggering a new dame to be shown
    scraped_dame += "<button id='reload' onclick='javascript:window.location.reload();'>Generate Another</button>"

    return scraped_dame

#Binding default URL '/' to the dame_scraper function
@app.route('/')
def dame_scraper():
    #Markup ensures that HTML formatting is preserved
    return Markup(dame_finder())

#Driver function
if __name__ == '__main__':
    #Runs app on local development server
    app.run()