import re, string


"""Функция получает набор данных от пользователя, чистит данные от лишних знаков и выводит список строк по слову в строке."""


def mod(words):
    words = re.sub('[{}]'.format(re.escape(string.punctuation)), '', words) #удаляем знаки пунктуации
    words = list(set(words.lower().split()))
    return words

#print(modificator(open('test.txt', 'r').read()))