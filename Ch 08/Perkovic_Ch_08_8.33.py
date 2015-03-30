__author__ = 'Rolando'


# define globals for cards

# ranks and suits are Deck class variables
RANKS = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}

# suits is a set of 4 unicode symbols representing the 4 suits
SUITS = {'\u2660', '\u2661', '\u2662', '\u2663'}

# values of cards
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


class Card:
    """ Represents a playing card
    """

    def __init__(self, rank, suit):
        """ Initiates rank and suit of playing card
        """
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        """ Return rank
        """
        return self.rank

    def get_suit(self):
        """ Return suit
        """
        return self.suit

    def __eq__(self, other):
        """ self == other if rank and suit are the same
        """
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        """ self > other (suit hierarchy: spade > heart > diamond > club
        """
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank > other.rank

    def __ge__(self, other):
        """ self >= other
        """
        if self.rank == other.rank:
            return self.suit <= other.suit
        return self.rank >= other.rank

    def __lt__(self, other):
        """ self < other
        """
        if self.rank == other.rank:
            return self.suit > other.suit
        return self.rank < other.rank

    def __le__(self, other):
        """ self <= other
        """
        if self.rank == other.rank:
            return self.suit >= other.suit
        return self.rank <= other.suit

    def __repr__(self):
        """ return canonical string representation of Card(rank, suit)
        """
        return "Card('{}', '{}')".format(self.rank, self.suit)


class Hand:
    """ Represents a hand of playing cards
    """

    def __init__(self, p_id=''):
        """ Constructor - hand
        """
        self.id = p_id
        self.hand = []

    def add_card(self, card):
        """ Takes a Card and adds it to the Hand
        """
        self.hand.append(card)
        return card

    def show_hand(self):
        """ Displays player hand
        """
        print(self.id + ':', end=' ')
        for card in self.hand:
            print(card.get_rank(), card.get_suit(), end='   ')

    def total(self):
        """ Takes the hand and returns total value
        """

        result = 0
        num_aces = 0

        for card in self.hand:
            result += VALUES[card.get_rank()[0]]       # add up the values of the cards in the hand
            if card.get_rank()[0] == 'A':              # also add up the number of aces
                num_aces += 1

        while result > 21 and num_aces > 0:
            result -= 10
            num_aces -= 1
        return result

    def __len__(self):
        return len(self.hand)

    def __getitem__(self, key):
        return self.hand[key]

    def __setitem__(self, key, item):
        self.hand[key] = item

    def __contains__(self, key):
        return key in self.hand

import random


class Deck:
    """ Represents a deck of 52 cards
    """

    def __init__(self, card_list=None):
        """ Create a deck using a list of input cards or
            initialize a deck of 52 cards if None
        """
        if card_list is None:
            self.deck = []
            for suit in SUITS:
                for rank in RANKS:
                    self.deck.append(Card(rank, suit))

        else:
            self.deck = card_list

    def deal_card(self):
        """ Deal (pop and return) card from the top of deck
        """
        return self.deck.pop()

    def shuffle(self):
        """ Shuffle the deck
        """
        random.shuffle(self.deck)

    def __eq__(self, other):
        """ Returns True if deck and other have same items; else False
        """
        return self.deck == other.deck

    def __len__(self):
        """ Returns number of items in deck
        """
        return len(self.deck)

    def __repr__(self):
        """ Return canonical string representation of deck
        """
        return 'Deck({})'.format(self.deck)


class BlackJack:
    """
    """

    def play(self):
        # create and shuffle deck
        deck = Deck()
        deck.shuffle()

        # create initial hands
        house = Hand('House')
        player = Hand('Player')

        # deal cards to hands (2 cards per hand)
        for i in range(2):
            player.add_card(deck.deal_card())
            house.add_card(deck.deal_card())

        player.show_hand()
        house.show_hand()

        print('\n')

        answer = input('Hit or stand? (default: hit): ')

        while answer in {'hit', 'h', ''}:
            card = str(player.add_card(deck.deal_card()))
            print('You got {:>7}'.format(card))

            if player.total() > 21:
                print('You went over... You lose.')
                return

            answer = input('Hit or stand? (default: hit): ')

        while house.total() < 17:
            card = str(house.add_card(deck.deal_card()))
            print('House got {:>7}'.format(card))

            if house.total() > 21:
                print('House went over... You win.')
                return

        self.compare_hands(house, player)

    def compare_hands(self, house, player):
        """
        """

        house_total, player_total = house.total(), player.total()

        if house_total > player_total:
            print('You lose.')
        elif house_total < player_total:
            print('You win.')
        elif house_total == 21 and 2 == len(house) < len(player):
            print('You lose.')
        elif player_total == 21 and 2 == len(player) < len(house):
            print('You win.')
        else:
            print('A tie.')

# bj = BlackJack()
# bj.play()
