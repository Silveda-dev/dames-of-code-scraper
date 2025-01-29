import random
import requests
from bs4 import BeautifulSoup

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
finished = False

def dame_finder():
    global finished

    #Escape if all dames have been viewed
    if finished:
        print("You have viewed all dames in the dataset - thank you for your dedication.")
    else:
        #Generating dame of focus
        chosen_dame = random.randint(0, (len(dames)-1)) 
        print(dames[chosen_dame], "\n\n")

        #Scraping Wikipedia page of dame
        url = dame_links[chosen_dame]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        refs = soup.find_all('sup')
        for ref in refs:
            ref.decompose()

        info = soup.find_all('p')
        i = 0
        for x in info:
            print(x.text.strip())
            print()
            i += 1
            if i >= 5:
                break
        
        print("You can find out more at: ", dame_links[chosen_dame])
        print()
    
        #Removing selected dames to prevent repeats
        if len(dames) > 1:
            del dames[chosen_dame]
            del dame_links[chosen_dame]
        else:
            finished = True

        return True

print("Welcome to Dames of Code - recognising historic (and often forgotten) women in tech.\n\n")

cont = True

while cont:
    cont = dame_finder()
    if cont:
        check = input("Do you wish to find out about another dame (y/n)? ")
        if check == 'n' or check == 'N' or check == 'no' or check == 'No':
            cont = False

print("Thank you for educating yourself.")