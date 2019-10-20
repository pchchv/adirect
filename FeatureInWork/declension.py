import pymorphy2

morph = pymorphy2.MorphAnalyzer()


"""Функция возвращает список склонений заданного слова, включая само слово"""


def declension(word):
    words = morph.parse(word.lower())[0].lexeme          #Создаётся список всех форм слова
    decls = []
    for element in words:                                 #В цикле поэлементно чистим список от лишних данных
        decl = str(element).split(' ')
        decls.append(decl[-3].strip(',').strip("'"))
    if word not in decls:
        decls.append(word)
    return decls

#print(declension(input()))
