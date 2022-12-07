import requests

from random import randint

import pyfiglet

from termcolor import colored

def art_name(name, color):
    asciii = pyfiglet.figlet_format(name)
    colored_name = colored(asciii, color=color)
    print(colored_name)


art_name("Dad Jokes 3000", "blue")

joke_theme = input("What's the joke theme?")

url = "https://icanhazdadjoke.com/search?term=" + joke_theme

jsonn = requests.get(url, headers={"Accept":"application/json"})

teste = jsonn.json()

total_jokes = teste["total_jokes"]


handling = teste['results']

joke_number = randint(0, total_jokes)

print(handling[joke_number]["joke"])


