from processors import *

words = modifier(open('/home/jack/Documents/Projects/aDirect/test.txt', 'r').read())
words1 = modifier(open('/home/jack/Documents/Projects/aDirect/test1.txt', 'r').read())
words2 = modifier(open('/home/jack/Documents/Projects/aDirect/test2.txt', 'r').read())

print('\n'.join(str(modifier(str(x))) for x in generator(words, words1, words2)))