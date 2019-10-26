from processors import *

words = modifier(open('test.txt', 'r').read(), 'all')
words1 = modifier(open('test1.txt', 'r').read(), 'all')
words2 = modifier(open('test2.txt', 'r').read(), 'all')

print(counter(words2))
#print(words)
#print(CityRemover(words))
#print('\n'.join(generator(words, words1, words2)))
