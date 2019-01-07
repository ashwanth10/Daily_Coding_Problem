"""
This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1.Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
from random import random
import bisect

class NumberGenerator():

    def __init__(self, numbers, probabilities):
        assert sum(probabilities) == 1

        self._numbers = numbers
        self._cum_probability = list()
        cur_cum_probability = 0
        for probability in probabilities:
            cur_cum_probability += probability
            self._cum_probability.append(cur_cum_probability)

    def generate_number(self):
        rand = random()
        index = bisect.bisect_left(self._cum_probability, rand)
        return self._numbers[index]


def main():
    numbers = map(int, raw_input("Enter the numbers?\n").split())
    probabilities = map(float, raw_input("Enter their probabilites?\n").split())

    ng = NumberGenerator(numbers, probabilities)

    while(raw_input("Get number?\n") in ['Y', 'y']):
        print(ng.generate_number())
    print('Bye!\n')

if __name__ == '__main__':
    main()