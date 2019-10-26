#без функции оставляю навсякий случай
# KeyWords = open('keywords.txt', 'r').read()
# StopCity = open('StopCity.txt', 'r').read()
# KeyWordswords = KeyWords.split()
#
# resultwords  = [word for word in KeyWordswords if word.lower() not in StopCity]
# result = ' '.join(resultwords)
#
# print(result)


def CityRemover(KeyWords, StopCity):
    KeyWordswords = KeyWords.split()
    resultwords = [word for word in KeyWordswords if word.lower() not in StopCity]
    result = ' '.join(resultwords)
    return result

KeyWords = open('keywords.txt', 'r').read()
StopCity = open('StopCity.txt', 'r').read()

print(CityRemover(KeyWords, StopCity))