def generator(txt1, txt2):
    res = []
    for i in txt1:
        for j in txt2:
            res.append('{0} {1}'.format(i, j))
    return res


txt1 = list(set(open('test.txt', 'r').read().lower().split()))
txt2 = list(set(open('test1.txt', 'r').read().lower().split()))

print('\n'.join(generator(txt1, txt2)))