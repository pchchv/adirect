def counter(words):
    return list(set(words.lower().split()))
keywords1 = counter(open('test.txt', 'r').read())
keywords2 = counter(open('test1.txt', 'r').read())
for i in keywords1: #раскладываем первый список
    for j in keywords2: #раскладываем второй список
        print('{0} {1}'.format(i, j))
