#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read,
#and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

#

import pandas as pd
import numpy as np
import random
import sys


# I was surprised to find our there was no function in python for weighted sampling.
# I found the following function on the o'reilly website


def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    item = ''
    item_probability = 1

    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability: break

    return item


# Takes file path and the number of words to generate as arguments
def markovTextGenerator(filePath, numberOfWords):
    with open(filePath, 'r') as myfile:
        data=myfile.read().replace('\n', '')

        # split into a list by spaces
        words = data.split(' ')

        # remove any empty strings
        words = [w for w in words if len(w.strip()) > 0]

        # create data frame with current word and next word
        wordDf = pd.DataFrame([words[i-1:i+1] for i in range(1,len(words))], columns=['w_1','w_2'])

        # calculate current word counts in the document
        wordDf['w_1_count'] = wordDf.groupby(['w_1'])['w_1'].transform('count')

        # group by current word and next word to calculate count occurrences of current word
        # and next word appearing together
        wordDf['w_2_count'] = wordDf.groupby(['w_1','w_2'])['w_2'].transform('count')

        # calculate conditional probability of next word occurrence given current word
        wordDf['probability'] = wordDf.w_2_count / wordDf.w_1_count

        # pick a random current word from the list of words
        currentWord = wordDf.loc[random.randint(0,len(wordDf)),'w_1']

        for i in range(numberOfWords):
            # get slice where current word is w_1
            w = wordDf[wordDf['w_1'] == currentWord]

            # if no rows returned, that means there were no words after that word in original document
            if w.empty:
                # reset chain when no next words were found
                currentWord = wordDf.loc[random.randint(0,len(wordDf)),'w_1']
                w = wordDf[wordDf['w_1'] == currentWord]

            # pick next word using probabilities given current word
            next_word = random_pick(w['w_2'], w['probability'])
            print(' '+ next_word, end='')
            currentWord = next_word

        print('')

def main():
    if len(sys.argv) < 2:
        print('Invalid arguments entered. Usage:\n python markov.py <input file path> <# of words>')

    markovTextGenerator(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()
