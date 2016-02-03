import random
import itertools

SUITS = 'cdhs'
RANKS = '23456789TJQKA'


def create_deck():
    global SUITS
    global RANKS
    global deck
    deck = list(''.join(card) for card in itertools.product(RANKS, SUITS))


class Player(object):
    def __init__(self, money, hand=None):
        self.money = money
        self.hand = hand

    def add_money(self, amount):
        self.money += amount


def deal_cards(number):
    """
    pops a random car out of the deck and appends it to your hand
    does this as many times as the number you enter
    :param number:
    :return a list of random cards of the amount specified:
    """
    hand = []
    for i in range(number):
        hand.append(deck.pop(random.randint(0, len(deck) - 1)))

    return hand


def play():
    create_deck()
    p = Player(100)
    while True:
        try:
            bet = int(input('What is your bet amount? If you want to quit type 0'))
        except:
            print('Please type a number')
        p.hand = deal_cards(2)
        dealer_hand = deal_cards(2)
        print('The dealer shows one card of his two, it is the %s' % (dealer_hand[0]))


play()
