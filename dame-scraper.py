import random

dames = ["Ada Lovelace", "Grace Hopper", "Radia Pearlman", "Betty Snyder", "Betty Jean Jennings"]
dame_links = ["https://en.wikipedia.org/wiki/Ada_Lovelace", "https://en.wikipedia.org/wiki/Grace_Hopper", "https://en.wikipedia.org/wiki/Grace_Hopper",
              "https://en.wikipedia.org/wiki/Betty_Holberton", "https://en.wikipedia.org/wiki/Jean_Bartik"]

print("Welcome to Dames of Code - recognising historic (and often forgotten) women in tech.\n\n")

#Generating dame of focus
i = random.randint(0, (len(dames)-1))
print(dames[i], "\n\n")

print("Thank you for educating yourself.")