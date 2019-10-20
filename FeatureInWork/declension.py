import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def declension(world):
    world = morph.parse(world.lower())[0].lexeme
    decls = []
    for element in world:
        decl = str(element).split(' ')
        decls.append(decl[-3].strip(',').strip("'"))
    return decls

print(declension(input()))
