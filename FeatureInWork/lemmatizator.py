from modifier import mod
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def lemma(words):
    res = []
    for i in words:
        res.append(morph.parse(i)[0].normal_form)
    return(set(res))

#print('\n'.join(lemma(mod(open('test.txt', 'r').read()))))
