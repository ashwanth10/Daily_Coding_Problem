"""
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[('a', 'a', 0.9), ('a', 'b', 0.075), ('a', 'c', 0.025), ('b', 'a', 0.15), ('b', 'b', 0.8), ('b', 'c', 0.05), ('c', 'a', 0.25), ('c', 'b', 0.25), ('c', 'c', 0.5)]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""
import numpy as np

def main():
    steps = count = int(raw_input("enter no. of steps\n"))
    probabilites = input("enter the probabilites?\n")

    row_length = len(probabilites[0])

    matrix = []
    row = []
    for item in probabilites:
        row.append(item[2])
        if len(row) == 3:
            matrix.append(row)
            row = []

    T = np.matrix(matrix)
    I = np.matrix([[1.0] + [0] * (row_length - 1)])

    while(steps > 0):
        steps -= 1
        I = I * T

    print(I * count)

if __name__ == '__main__':
    main()