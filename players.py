### gracze ###

class Player:
    def __init__(self, number, bot=False):
        self.number = number
        self.bot = bot
        self.score = 0
        self.sources = {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0, "GOLD": 0}
        self.cards = {"WHITE": 0, "BLUE": 0, "GREEN": 0, "RED": 0, "BLACK": 0}
        self.reserved = []
    
    def print_score(self):
        print("ZASOBY GRACZA:", self.number)
        print("biały:", self.sources["WHITE"])
        print("niebieski:", self.sources["BLUE"])
        print("zielony:", self.sources["GREEN"])
        print("czerwony:", self.sources["RED"])
        print("czarny:", self.sources["BLACK"])

    def jocker(self): # zamiana dżokerów w inną walutę
        white = int(input("biały: "))
        blue = int(input("niebieski: "))
        green = int(input("zielony: "))
        red = int(input("czerwony: "))
        black = int(input("czarny: "))

        #sprawdzenie czy gracz posiada wystarczającą ilość złotych znaczników
        if self.sources["GOLD"] - (white + blue + green + red + black) < 0:
            print("nie stać cię gościu!!!")
            return -1

        self.sources["WHITE"] += white
        self.sources["BLUE"] += blue
        self.sources["GREEN"] += green
        self.sources["RED"] += red
        self.sources["BLACK"] += black
        self.sources["GOLD"] -= (white + blue + green + red + black)

    def buy(self, card):
        # sprawdzenie czy można zakupić kartę
        if (self.sources["WHITE"] + self.cards["WHITE"] - card.cost["WHITE"] < 0 or
            self.sources["BLUE"] + self.cards["BLUE"] - card.cost["BLUE"] < 0 or
            self.sources["GREEN"] + self.cards["GREEN"] - card.cost["GREEN"] < 0 or
            self.sources["RED"] + self.cards["RED"] - card.cost["RED"] < 0 or
            self.sources["BLACK"] + self.cards["BLACK"] - card.cost["BLACK"] < 0):
            print("nie stac cie gosicu!!!")
            return -1

        self.sources["WHITE"] -= max(card.cost["WHITE"] - self.cards["WHITE"], 0)
        self.sources["BLUE"] -= max(card.cost["BLUE"] - self.cards["BLUE"], 0)
        self.sources["GREEN"] -= max(card.cost["GREEN"] - self.cards["GREEN"], 0)
        self.sources["RED"] -= max(card.cost["RED"] - self.cards["RED"], 0)
        self.sources["BLACK"] -= max(card.cost["BLACK"] - self.cards["BLACK"], 0)

        self.score += card.prestige
        self.cards[card.color] += 1
    
    def reservation(self, card):
        # sprawdzenie czy można zarezerwować kartę
        if len(self.reserved) > 3:
            print("nie możesz już rezerwować typie!!!")
            return -1

        self.sources["GOLD"] += 1
        self.reserved.append(card)





