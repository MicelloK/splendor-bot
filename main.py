### SILNIK DO GRY SPLENDOR ###

from cards import *
import os

def create_table():
    table = [[], [], []]
    for i in range(3):
        print("karty poziomu", i+1)
        card_in_table = 0
        while card_in_table < 4:
            if add_card(table) != -1:
                card_in_table += 1
    return table

def print_table(table):
    os.system('cls')
    print('\n', "KARTY POZIOMU PIERWSZEGO:", sep="")
    for x in table[0]:
        x.print()
    print('\n', "KARTY POZIOMU DRUGIEGO:", sep="")
    for x in table[1]:
        x.print()
    print('\n', "KARTY POZIOMU TRZECIEGO:", sep="")
    for x in table[2]:
        x.print()


def init_game():
    global GAMEOVER, table
    table = create_table()
    GAMEOVER = False
init_game()

while not GAMEOVER:
    pass

