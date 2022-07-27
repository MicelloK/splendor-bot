### karty ###

class Card:
    def __init__(self, type=0, color=None, prestige=0, cost={"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0}):
        self.type = type
        self.color = color
        self.prestige = prestige
        self.cost = cost

    def print(self): # wyświetla informacje o karcie
        if self.color == "WHITE": color = "biały"
        elif self.color == "BLUE": color = "niebieski"
        elif self.color == "GREEN": color = "zielony" 
        elif self.color == "RED": color = "czerwony"
        elif self.color == "BLACK": color = "czarny"
        else: 
            print("nieprawidlowo wpisany kolor")
            return -1

        print("#### KARTA POZIOMU", self.type, "####")
        print("Kolor:", color)
        print("Punkty prestizu:", self.prestige)
        print("KOSZT:")
        print("biały", self.cost["WHITE"])
        print("niebieski", self.cost["BLUE"])
        print("zielony", self.cost["GREEN"])
        print("czerwony", self.cost["RED"])
        print("czarny", self.cost["BLACK"])
        print("#########################")

def find_card(type, color, prestige, cost):
    if type == 1:
        cards = green_cards
    elif type == 2:
        cards = yellow_cards
    elif type == 3:
        cards = blue_cards
    else:
        print("nie ma takiego poziomu kart")
        return -1

    for x in cards:
        if x.color == color and x.prestige == prestige and x.cost == cost:
            return x
    return -1

def add_card(table):
    type = int(input("Podaj poziom karty: "))
    color = input("Podaj kolor karty: ")
    prestige = int(input("Podaj prestiż karty: "))
    print("KOSZT")
    white = int(input("biały: "))
    blue = int(input("niebieski: "))
    green = int(input("zielony: "))
    red = int(input("czerwony: "))
    black = int(input("czarny: "))
    cost = {"WHITE": white, "BLUE": blue, "GREEN": green, "RED": red, "BLACK": black}

    card = find_card(type, color, prestige, cost)

    if card != -1: table[type-1].append(card)
    else: 
        print("Nie ma takiej karty!!!")
        return -1

def remove_card(table, card):
    if card in table[card.type-1]:
        table[card.type-1].remove(card)
    else:
        print("nie ma takiej karty na stole!!!")
        return -1

# karty poziomu pierwszego
green_cards = [ # postaci: kolor, prestiż, koszt (white, blue, green, red, black)
    Card(1, 'WHITE', 1, {"WHITE": 0, "BLUE": 0, "GREEN": 4, "RED": 0, "BLACK": 0}),
    Card(1, 'WHITE', 0, {"WHITE": 0, "BLUE": 2, "GREEN": 0, "RED": 0, "BLACK": 2}),
    Card(1, 'WHITE', 0, {"WHITE": 0, "BLUE": 1, "GREEN": 1, "RED": 1, "BLACK": 1}),
    Card(1, 'WHITE', 0, {"WHITE": 3, "BLUE": 1, "GREEN": 0, "RED": 0, "BLACK": 1}),
    Card(1, 'WHITE', 0, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 2, "BLACK": 1}),
    Card(1, 'WHITE', 0, {"WHITE": 0, "BLUE": 1, "GREEN": 2, "RED": 1, "BLACK": 1}),
    Card(1, 'WHITE', 0, {"WHITE": 0, "BLUE": 3, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(1, 'WHITE', 0, {"WHITE": 0, "BLUE": 2, "GREEN": 2, "RED": 0, "BLACK": 1}),
    Card(1, 'BLUE', 1, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 4, "BLACK": 0}),
    Card(1, 'BLUE', 0, {"WHITE": 1, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 2}),
    Card(1, 'BLUE', 0, {"WHITE": 0, "BLUE": 1, "GREEN": 3, "RED": 1, "BLACK": 0}),
    Card(1, 'BLUE', 0, {"WHITE": 1, "BLUE": 0, "GREEN": 2, "RED": 2, "BLACK": 0}),
    Card(1, 'BLUE', 0, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 3}),
    Card(1, 'BLUE', 0, {"WHITE": 1, "BLUE": 0, "GREEN": 1, "RED": 1, "BLACK": 1}),
    Card(1, 'BLUE', 0, {"WHITE": 1, "BLUE": 0, "GREEN": 1, "RED": 2, "BLACK": 1}),
    Card(1, 'BLUE', 0, {"WHITE": 0, "BLUE": 0, "GREEN": 2, "RED": 0, "BLACK": 2}),
    Card(1, 'GREEN', 1, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 4}),
    Card(1, 'GREEN', 0, {"WHITE": 1, "BLUE": 3, "GREEN": 1, "RED": 0, "BLACK": 0}),
    Card(1, 'GREEN', 0, {"WHITE": 0, "BLUE": 2, "GREEN": 0, "RED": 2, "BLACK": 0}),
    Card(1, 'GREEN', 0, {"WHITE": 0, "BLUE": 1, "GREEN": 0, "RED": 2, "BLACK": 2}),
    Card(1, 'GREEN', 0, {"WHITE": 1, "BLUE": 1, "GREEN": 0, "RED": 1, "BLACK": 2}),
    Card(1, 'GREEN', 0, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 3, "BLACK": 0}),
    Card(1, 'GREEN', 0, {"WHITE": 2, "BLUE": 1, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(1, 'GREEN', 0, {"WHITE": 1, "BLUE": 1, "GREEN": 0, "RED": 1, "BLACK": 1}),
    Card(1, 'RED', 1, {"WHITE": 4, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(1, 'RED', 0, {"WHITE": 2, "BLUE": 0, "GREEN": 1, "RED": 0, "BLACK": 2}),
    Card(1, 'RED', 0, {"WHITE": 2, "BLUE": 0, "GREEN": 0, "RED": 2, "BLACK": 0}),
    Card(1, 'RED', 0, {"WHITE": 3, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(1, 'RED', 0, {"WHITE": 2, "BLUE": 1, "GREEN": 1, "RED": 0, "BLACK": 1}),
    Card(1, 'RED', 0, {"WHITE": 1, "BLUE": 0, "GREEN": 0, "RED": 1, "BLACK": 3}),
    Card(1, 'RED', 0, {"WHITE": 1, "BLUE": 1, "GREEN": 1, "RED": 0, "BLACK": 1}),
    Card(1, 'RED', 0, {"WHITE": 0, "BLUE": 2, "GREEN": 1, "RED": 0, "BLACK": 0}),
    Card(1, 'BLACK', 1, {"WHITE": 0, "BLUE": 4, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(1, 'BLACK', 0, {"WHITE": 2, "BLUE": 0, "GREEN": 2, "RED": 0, "BLACK": 0}),
    Card(1, 'BLACK', 0, {"WHITE": 0, "BLUE": 0, "GREEN": 2, "RED": 1, "BLACK": 0}),
    Card(1, 'BLACK', 0, {"WHITE": 1, "BLUE": 1, "GREEN": 1, "RED": 1, "BLACK": 0}),
    Card(1, 'BLACK', 0, {"WHITE": 1, "BLUE": 2, "GREEN": 1, "RED": 1, "BLACK": 0}),
    Card(1, 'BLACK', 0, {"WHITE": 2, "BLUE": 2, "GREEN": 0, "RED": 1, "BLACK": 0}),
    Card(1, 'BLACK', 0, {"WHITE": 0, "BLUE": 0, "GREEN": 1, "RED": 3, "BLACK": 1}),
    Card(1, 'BLACK', 0, {"WHITE": 0, "BLUE": 0, "GREEN": 3, "RED": 0, "BLACK": 0}),
]

# karty poziomu drugiego
yellow_cards = [ # postaci: kolor, prestiż, koszt (white, blue, green, red, black)
    Card(2, 'WHITE', 3, {"WHITE": 6, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(2, 'WHITE', 2, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 5, "BLACK": 3}),
    Card(2, 'WHITE', 2, {"WHITE": 0, "BLUE": 0, "GREEN": 1, "RED": 4, "BLACK": 2}),
    Card(2, 'WHITE', 2, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 5, "BLACK": 0}),
    Card(2, 'WHITE', 1, {"WHITE": 2, "BLUE": 3, "GREEN": 0, "RED": 3, "BLACK": 0}),
    Card(2, 'WHITE', 1, {"WHITE": 0, "BLUE": 0, "GREEN": 3, "RED": 2, "BLACK": 2}),
    Card(2, 'BLUE', 3, {"WHITE": 0, "BLUE": 6, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(2, 'BLUE', 2, {"WHITE": 2, "BLUE": 0, "GREEN": 1, "RED": 0, "BLACK": 4}),
    Card(2, 'BLUE', 2, {"WHITE": 5, "BLUE": 3, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(2, 'BLUE', 2, {"WHITE": 0, "BLUE": 5, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(2, 'BLUE', 1, {"WHITE": 0, "BLUE": 2, "GREEN": 3, "RED": 0, "BLACK": 3}),
    Card(2, 'BLUE', 1, {"WHITE": 0, "BLUE": 2, "GREEN": 2, "RED": 3, "BLACK": 0}),
    Card(2, 'GREEN', 3, {"WHITE": 0, "BLUE": 0, "GREEN": 6, "RED": 0, "BLACK": 0}),
    Card(2, 'GREEN', 2, {"WHITE": 0, "BLUE": 5, "GREEN": 3, "RED": 0, "BLACK": 0}),
    Card(2, 'GREEN', 2, {"WHITE": 4, "BLUE": 2, "GREEN": 0, "RED": 0, "BLACK": 1}),
    Card(2, 'GREEN', 2, {"WHITE": 0, "BLUE": 0, "GREEN": 5, "RED": 0, "BLACK": 0}),
    Card(2, 'GREEN', 1, {"WHITE": 3, "BLUE": 0, "GREEN": 2, "RED": 3, "BLACK": 0}),
    Card(2, 'GREEN', 1, {"WHITE": 2, "BLUE": 3, "GREEN": 0, "RED": 0, "BLACK": 2}),
    Card(2, 'RED', 3, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 6, "BLACK": 0}),
    Card(2, 'RED', 2, {"WHITE": 3, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 5}),
    Card(2, 'RED', 2, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 5}),
    Card(2, 'RED', 2, {"WHITE": 1, "BLUE": 4, "GREEN": 2, "RED": 0, "BLACK": 0}),
    Card(2, 'RED', 1, {"WHITE": 0, "BLUE": 3, "GREEN": 2, "RED": 0, "BLACK": 3}),
    Card(2, 'RED', 1, {"WHITE": 2, "BLUE": 0, "GREEN": 0, "RED": 2, "BLACK": 3}),
    Card(2, 'BLACK', 3, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 6}),
    Card(2, 'BLACK', 2, {"WHITE": 5, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(2, 'BLACK', 2, {"WHITE": 0, "BLUE": 0, "GREEN": 5, "RED": 3, "BLACK": 0}),
    Card(2, 'BLACK', 2, {"WHITE": 0, "BLUE": 1, "GREEN": 4, "RED": 2, "BLACK": 0}),
    Card(2, 'BLACK', 1, {"WHITE": 3, "BLUE": 0, "GREEN": 3, "RED": 0, "BLACK": 2}),
    Card(2, 'BLACK', 1, {"WHITE": 3, "BLUE": 2, "GREEN": 2, "RED": 0, "BLACK": 0}),
]

# karty poziomu trzeciego
blue_cards = [ # postaci: kolor, prestiż, koszt (white, blue, green, red, black)
    Card(3, 'WHITE', 5, {"WHITE": 3, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 7}),
    Card(3, 'WHITE', 4, {"WHITE": 3, "BLUE": 0, "GREEN": 0, "RED": 3, "BLACK": 6}),
    Card(3, 'WHITE', 4, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 7}),
    Card(3, 'WHITE', 3, {"WHITE": 0, "BLUE": 3, "GREEN": 3, "RED": 5, "BLACK": 3}),
    Card(3, 'BLUE', 5, {"WHITE": 7, "BLUE": 3, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(3, 'BLUE', 4, {"WHITE": 7, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(3, 'BLUE', 4, {"WHITE": 6, "BLUE": 3, "GREEN": 0, "RED": 0, "BLACK": 3}),
    Card(3, 'BLUE', 3, {"WHITE": 3, "BLUE": 0, "GREEN": 3, "RED": 3, "BLACK": 5}),
    Card(3, 'GREEN', 5, {"WHITE": 0, "BLUE": 7, "GREEN": 3, "RED": 0, "BLACK": 0}),
    Card(3, 'GREEN', 4, {"WHITE": 0, "BLUE": 7, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Card(3, 'GREEN', 4, {"WHITE": 3, "BLUE": 6, "GREEN": 3, "RED": 0, "BLACK": 0}),
    Card(3, 'GREEN', 3, {"WHITE": 5, "BLUE": 3, "GREEN": 3, "RED": 0, "BLACK": 3}),
    Card(3, 'RED', 5, {"WHITE": 0, "BLUE": 0, "GREEN": 7, "RED": 3, "BLACK": 0}),
    Card(3, 'RED', 4, {"WHITE": 0, "BLUE": 0, "GREEN": 7, "RED": 0, "BLACK": 0}),
    Card(3, 'RED', 4, {"WHITE": 0, "BLUE": 3, "GREEN": 6, "RED": 3, "BLACK": 0}),
    Card(3, 'RED', 3, {"WHITE": 3, "BLUE": 5, "GREEN": 3, "RED": 0, "BLACK": 3}),
    Card(3, 'BLACK', 5, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 7, "BLACK": 3}),
    Card(3, 'BLACK', 4, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 7, "BLACK": 0}),
    Card(3, 'BLACK', 4, {"WHITE": 0, "BLUE": 0, "GREEN": 3, "RED": 6, "BLACK": 3}),
    Card(3, 'BLACK', 3, {"WHITE": 3, "BLUE": 3, "GREEN": 5, "RED": 3, "BLACK": 0}),
]


### arystokraci ###

class Aristocrat:
    def __init__(self, prestige, cost):
        self.prestige = prestige
        self.cost = cost
    
    def print(self):
        print("### ARYSTOKRATA ###")
        print("KOSZT:")
        print("biały:", self.cost["WHITE"])
        print("niebieski:", self.cost["BLUE"])
        print("zielony:", self.cost["GREEN"])
        print("czerwony:", self.cost["RED"])
        print("czarny:", self.cost["BLACK"])
        print("####################")

def find_aristocrat(cost):
    for x in aristocrats:
        if x.cost == cost:
            return x
    return -1

aristocrats = [
    Aristocrat(3, {"WHITE": 3, "BLUE": 3, "GREEN": 3, "RED": 0, "BLACK": 0}),
    Aristocrat(3, {"WHITE": 4, "BLUE": 4, "GREEN": 0, "RED": 0, "BLACK": 0}),
    Aristocrat(3, {"WHITE": 3, "BLUE": 3, "GREEN": 0, "RED": 0, "BLACK": 3}),
    Aristocrat(3, {"WHITE": 0, "BLUE": 0, "GREEN": 3, "RED": 3, "BLACK": 3}),
    Aristocrat(3, {"WHITE": 0, "BLUE": 4, "GREEN": 4, "RED": 0, "BLACK": 0}),
    Aristocrat(3, {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 4, "BLACK": 4}),
    Aristocrat(3, {"WHITE": 0, "BLUE": 0, "GREEN": 4, "RED": 4, "BLACK": 0}),
    Aristocrat(3, {"WHITE": 0, "BLUE": 3, "GREEN": 3, "RED": 3, "BLACK": 0}),
    Aristocrat(3, {"WHITE": 3, "BLUE": 0, "GREEN": 0, "RED": 3, "BLACK": 3}),
    Aristocrat(3, {"WHITE": 4, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 4})
]



