from Deck import Deck
from Game import Game

if __name__ == '__main__':
    g = Game()
    g.start_game()

    for pl in g.players:
        print(pl)

    # d = Deck()
    #
    # print(len(d))
    # card = d.get_card()
    # print(card)
    # print(len(d))
