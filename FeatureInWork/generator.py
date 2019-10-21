from modifier import mod


def generator(txt1, txt2):
    res = []
    for i in txt1:
        for j in txt2:
            res.append('{0} {1}'.format(i, j))
    return res


txt1 = mod(open('test.txt', 'r').read())
txt2 = mod(open('test1.txt', 'r').read())

print('\n'.join(generator(txt1, txt2)))
