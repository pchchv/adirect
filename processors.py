import re
import string
from itertools import product
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def modifier(words, type):
    """Функция получает набор данных от пользователя, чистит данные от знаков и выводит список строк по слову в строке.
    Параметр type содержит информацию какие знаки удалять.

    """
    marks = ''
    if 'all' in type:
        marks = string.punctuation
    if 'quotes' in type:
        marks += '[“”‘«»„“]'
    if 'exclamation_mark' in type:
        marks += '!'
    if 'space' in type:
        marks += '   '
    if 'plus' in type:   #Удаляет все +
        marks += '+'
    if 'uppercase' in type:
        for word in words:
            words.title()
        if type == 'uppercase':
            result = ' '.join(words)
    if 'cities' in type:
        CityRemover(words)
        if type == 'cities':
            result = ' '.join(words)
    if '+prep' in type:
        for word in words.strip().split('\n'):
            if word[0] == '+' and 'PREP' or 'CONJ' in morph.parse(word[1:])[0].tag.POS:
                words.replace(word, word[1:])


    #Минус слова

    #Пустые строки

    #Удалить + в предлогах
    if marks != '':
        words = re.sub('[{}]'.format(re.escape(marks)), '', words) #удаляем знаки пунктуации
    words = list(words.lower().split('\n'))
    if 'pass' in type:
        for el in words:
            if el == '':
                words.replace(el)
    if 'dub' in type:
        list(set(words))
    result = ' '.join(words)
    return result

def declension(UserInput):
    """Функция возвращает список склонений заданного слова, включая само слово.

    """
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

def counter(words):
    """Функция считает количество уникальных слов.
    Возвращает список, в котором первый элемент - количество слов, второй - все слова через пробел.

    """
    res = []
    while len(words) > 0:
        res.append(words[0])                   #Добавляем первый элемент списка к результирующему списку
        words = list(set(words) - set(declension(words[0])))  #Удаляем перенесённый элемент и его склонения
    result = ['Количество слов - ' + str(len(res))]
    result.append(' '.join(res))
    return result

def generator(*words):
    """Функция получает на вход от 2 до 10 списков, и выводит список сочетаний эллементов входных списков.

    """
    genwords = list(product(*words))
    res = []
    for i in genwords:
        res.append(' '.join(i))
    result = ' '.join(res)
    return result

def lemma(words):
    """Функция получает список слов и выводит список нормальных форм

    """
    res = []
    for i in words:
        res.append(morph.parse(i)[0].normal_form)
    return res

def CityRemover(KeyWords, StopCity = open('StopCity.txt', 'r').read()):
    """Функция получает список слов и удаляет из него города
    """
    KeyWords = KeyWords.split()
    Keywords = [word for word in KeyWords if word.lower() not in StopCity]
    result = ' '.join(KeyWords)
    return result
