import re
import string
from itertools import product
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def modifier(words, type):
    """Функция получает набор данных от пользователя, чистит данные от лишних знаков и выводит список строк по слову в строке.
    На данный момент реализованна только функция отчистки от всех знаков.

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
        for i in words:
            i.title()
    if 'cities' in type:
        CityRemover(words)
        if type == 'cities':
            result = ' '.join(words)
            return result

    #Минус слова

    #Пустые строки

    #Удалить + в предлогах

    words = re.sub('[{}]'.format(re.escape(marks)), '', words) #удаляем знаки пунктуации
    words = list(set(words.lower().split()))
    result = ' '.join(words)
    return words

def declension(word):
    """Функция возвращает список склонений заданного слова, включая само слово.

    """
    words = morph.parse(word.lower())[0].lexeme          #Создаётся список всех форм слова
    decls = []
    for element in words:                                 #В цикле поэлементно чистим список от лишних данных
        decl = str(element).split(' ')
        decls.append(decl[-3].strip(',').strip("'"))
    if word not in decls:
        decls.append(word)
    return decls

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
    result = ' '.join(res)
    return result

def CityRemover(KeyWords, StopCity = open('StopCity.txt', 'r').read()):
    """Функция получает список слов и удаляет из него города
    """
    KeyWords = KeyWords.split()
    Keywords = [word for word in KeyWords if word.lower() not in StopCity]
    result = ' '.join(KeyWords)
    return result
