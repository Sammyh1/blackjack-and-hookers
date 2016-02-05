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


def ace_check(points, aces):
    for i in range(aces):
        if i < (aces - 1):
            points += 1
        elif (points + 11) > 21:
            points += 1
        else:
            points += 11
    return points


def get_hand_score(hand):
    points_total = 0
    no_of_aces = 0
    for card in hand:
        if card[0] in 'TJQK':
            points_total += 10
        elif card[0] == 'A':
            no_of_aces += 1
        else:
            points_total += int(card[0])
    if no_of_aces > 0:
        points_total = ace_check(points_total, no_of_aces)
    return points_total


def card_check(hand):
    score = get_hand_score(hand)
    print(score)


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

        if bet == 0:
            print('You finished the game with %d chips' % p.money)
            break
        p.hand = deal_cards(2)
        print('Your hand is ' + str(p.hand))
        card_check(p.hand)
        dealer_hand = deal_cards(2)
        print('The dealer shows one card of his two, it is the %s' % (dealer_hand[0]))


play()
