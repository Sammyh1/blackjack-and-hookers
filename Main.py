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
    def __init__(self, money):
        self.money = money
        self.hand = []

    def add_money(self, amount):
        self.money += amount

    def lose_money(self, amount):
        self.money -= amount


def ace_check(points, aces):
    """
    sees the number of aces, if there is more than one all but one will be worth one point
    the final (or only ace) will be worth either 1 or, if possible, 11.
    :param points:
    :param aces:
    :return: points
    """
    for i in range(aces):
        if i < (aces - 1):
            points += 1
        elif (points + 11) > 21:
            points += 1
        else:
            points += 11
    return points


def get_score(hand):
    """
    Looks through the cards and adds them up,
    if there are aces sends them to the ace check
    :param hand:
    :return: number of points
    """
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


def deal_cards(number, hand):
    """
    pops a random card out of the deck and appends it to your hand
    does this as many times as the number you enter
    :param number: the number of cards to be dealt
    :param hand: the hand they should be dealt to
    :return a list of random cards of the amount specified:
    """

    for i in range(number):
        hand.append(deck.pop(random.randint(0, len(deck) - 1)))

    return hand


def player_game_on(hand):
    while True:

        try:
            action = int(input('Would you like to stick (0) or twist (1)'))
        except:
            print('please type either a 0 or 1')

        if action == 0:
            return get_score(hand)
        elif action == 1:
            deal_cards(1, hand)
            print('your hand is ' + str(hand))
            score = get_score(hand)
            if score > 21:
                return score
            elif score == 21:
                print('Yay, 21')
                return score
            else:
                print('Your score is ' + str(score))

        else:
            print('please type either a 0 or 1')


def dealers_go(hand):
    score = get_score(hand)
    while True:
        if score < 17:
            deal_cards(1, hand)
            score = get_score(hand)
        else:
            return score


def play():
    p = Player(100)
    while True:
        create_deck()
        try:
            bet = int(input('What is your bet amount? If you want to quit type 0'))
        except:
            print('Please type a number')

        if bet == 0:
            print('You finished the game with %d chips' % p.money)
            break
        p.hand = deal_cards(2, [])
        print('Your hand is ' + str(p.hand))
        score = get_score(p.hand)
        if score == 21:
            print('congratulations, you have black jack')
            p.add_money(bet * 1.5)
            print('You have % chips' % p.money)
        else:
            print('Your score is ' + str(score))
            dealer_hand = deal_cards(2, [])
            print('The dealer shows one card of his two, it is the %s' % (dealer_hand[0]))
            score = player_game_on(p.hand)
            if score > 21:
                p.lose_money(bet)
                print('Your score is: %d. You are bust. You lose your bet. You now have %d chips' % (score, p.money))
            else:
                print('Time for the dealer to have his go')
                dealer_score = dealers_go(dealer_hand)
                print("The dealer's hand is " + str(dealer_hand))
                if dealer_score > 21:
                    p.add_money(bet)
                    print("The dealer is bust. You win your bet. You now have %d chips" % p.money)
                elif dealer_score >= score:
                    p.lose_money(bet)
                    print("The dealer wins. You lose your bet. You now have %d chips" % p.money)
                else:
                    p.add_money(bet)
                    print("You beat the dealer. You win your bet. You now have %d chips" % p.money)


play()
