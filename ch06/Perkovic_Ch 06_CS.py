__author__ = 'Rolando'
#############################################
### Perkovic Intro to Python              ###
#### CH 6: Containers and Randomness     ####
##### PG 198 CH 6 Case Study            #####
#############################################

import random


def shuffledeck():
    """
    :return: shuffled deck
    """
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}    # suits is a set of 4 unicode symbols: black spade and club,
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}         # and white diamond and heart
    deck = []

    for suit in suits:                                  # Create a deck out of 52 cards
        for rank in ranks:                              # card is the concatenation
            deck.append(rank + ' ' + suit)              # of suit and rank

    random.shuffle(deck)                                # Shuffle the deck and return
    return deck


def dealcard(deck, participant):
    """
    :param deck: deck from shuffledeck() (lst)
    :param participant: the hand of the participant (lst)
    :return: card dealt (added) to participant (a single card id dealt from deck to participant
    """
    card = deck.pop()
    participant.append(card)
    return card


def total(hand):
    """
    :param hand: the hand of the participant (lst)
    :return: value of the hand
    """
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    result = 0
    numaces = 0

    for card in hand:
        result += values[card[0]]       # add up the values of the cards in the hand
        if card[0] == 'A':              # also add up the number of aces
            numaces += 1

    while result > 21 and numaces > 0:  # while value of hand > 21 and there is an ace
        result -= 10                    # in the hand with value 11, convert its value to 1
        numaces -= 1
    return result


def comparehands(house, player):
    """
    :param house: house hand
    :param player: player hand
    :return: compares house and player hands and prints outcome
    """
    housetotal, playertotal = total(house), total(player)

    if housetotal > playertotal:
        print('You lose.')
    elif housetotal < playertotal:
        print('You win.')
    elif housetotal == 21 and 2 == len(house) < len(player):
        print('You lose.')
    elif playertotal == 21 and 2 == len(player) < len(house):
        print('You win.')
    else:
        print('A tie.')


def blackjack():
    """
    :return: simulates the house in the game of blackjack
    """
    deck = shuffledeck()                                    # get shuffled deck

    house = []                                              # house hand
    player = []                                             # player hand

    for i in range(2):                                      # dealing initial hands in 2 rounds
        dealcard(deck, player)                              # deal to player first
        dealcard(deck, house)                               # deal to house second

    print('House:{:>7}{:>7}'.format(house[0], house[1]))    # print hands
    print('  You:{:>7}{:>7}'.format(player[0], player[1]))

    answer = input('Hit or stand? (default: hit): ')
    while answer in {'', 'h', 'hit'}:                       # While user requests additional card, house deals it
        card = dealcard(deck, player)
        print('You got {:>7}'.format(card))

        if total(player) > 21:                              # player total is > 21
            print('You went over... You lose.')
            return

        answer = input('Hit or stand? (default: hit): ')

    while total(house) < 17:                                # house must play the "house rules"
        card = dealcard(deck, house)
        print('House got{:>7}'.format(card))

        if total(house) > 21:                               # house total is > 21
            print('House went over... You win.')
            return

    comparehands(house, player)                             # compare house and player hand and print result

print(blackjack())