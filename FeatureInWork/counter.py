from declension import declension


"""Функция считает количество уникальных слов"""


def counter(words):
    words = list(set(words.lower().split()))   #Приводим строку к нижнему регистру, разбиваем в список по переносу строки и убираем повторяющиеся слова
    res = []
    while len(words) > 0:
        res.append(words[0])                   #Добавляем первый элемент списка к результирующему списку
        words = list(set(words) - set(declension(words[0])))  #Удаляем перенесённый элемент и его синонимы
    return res

count = counter(open('test.txt', 'r').read())   #В терминал нельзя вбить текст с переносом строки, для теста читаем из файла
print('Количество строк - ' + str(len(count)) + '\n' + str(count))
