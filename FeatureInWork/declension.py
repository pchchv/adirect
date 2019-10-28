import pymorphy2

morph = pymorphy2.MorphAnalyzer()


"""Функция возвращает список склонений заданного слова, включая само слово"""


#UserInput = modifier(open('test.txt', 'r').read())
#UserInput = 'айфон'

def declension(UserInput):
    result = []
    if type(UserInput) == str:
        UserInput = UserInput.split(' ')
    for word in UserInput:
        words = morph.parse(word.lower())[0].lexeme          #Создаётся список всех форм слова
        decls = []
        for element in words:
            decl = str(element).split(' ')
            decls.append(decl[-3])
        if word not in decls:
            decls.append(word)
        result.append(decls)
    return result

#print(declension(UserInput))
