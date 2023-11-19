# find words which have length greater than 6
words = ['cherry', 'elderberry', 'banana', 'nimbuerr']


def len_words(word):
    return len(word) > 6


op = list(filter(len_words, words))
print(op)
