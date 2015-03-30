__author__ = 'Rolando'

import random

class Craps:
    """
    """

    def __init__(self):
        """
        """

        # first roll
        self.rounds = 1
        d1 = random.randrange(1, 7)
        d2 = random.randrange(1, 7)
        self.first_result = d1 + d2

        print('Round {} Throw total: {}'.format(self.rounds, self.first_result))

        if self.first_result in {7, 11}:
            print('You won!')
        elif self.first_result in {2, 3, 12}:
            print('You lost!')
        else:
            print('Throw for Point.')
            self.for_point()

    def for_point(self):
        """
        """
        # consecutive rolls
        d1 = random.randrange(1, 7)
        d2 = random.randrange(1, 7)
        next_result = d1 + d2
        self.rounds += 1

        print('Round {} Throw total: {}'.format(self.rounds, next_result))

        if next_result == 7:
            print('You lost')
        elif next_result == self.first_result:
            print('You won')
        else:
            print('Throw for Point.')
            self.for_point()

crap = Craps()