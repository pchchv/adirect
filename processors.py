import re
import string
import requests
import json
from itertools import product
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import functools

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
    if 'cities' in type:
        words = CityRemover(words)
    if '+prep' in type:
        for word in words.strip().split('\n'):
            if word[0] == '+' and 'PREP' or 'CONJ' in morph.parse(word[1:])[0].tag.POS:
                words.replace(word, word[1:])

    #Минус слова

    if marks != '':
        words = re.sub('[{}]'.format(re.escape(marks)), '', words) #удаляем знаки пунктуации
    words = list(words.lower().split('\n'))
    if words[-1] == '':
        words.remove(words[-1])
    if 'pass' in type:
        for el in words:
            if el == '':
                words.replace(el)
    if 'dub' in type:
        list(set(words))
    return words

def declension(UserInput):
    """Функция возвращает список склонений заданного слова, включая само слово.

    """
    result = []
    decls = []
    if type(UserInput) == str:
        UserInput = UserInput.replace('\n', ' ').split(' ')
    for word in UserInput:
        words = morph.parse(word.lower())[0].lexeme          #Создаётся список всех форм слова
        for element in words:
            decl = str(element).split(' ')
            decls.append(decl[-3])
        if word not in decls:
            decls.append(word)
        if len(UserInput) == 1:
            return decls
        result.append(decls)
    return result

def counter(words):
    """Функция считает количество уникальных слов.
    Возвращает список, в котором первый элемент - количество слов, второй - все слова через пробел.

    """
    res = []
    while len(words) > 0:
        res.append(words[0])                  #Добавляем первый элемент списка к результирующему списку
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
    result = '\n'.join(res)
    return result

def lemma(words):
    """Функция получает список слов и выводит список нормальных форм

    """
    res = []
    for i in words:
        res.append(morph.parse(i)[0].normal_form)
    return res

def CityRemover(UserInput, StopCity = open('StopCity.txt', 'r').read()):
    """Функция получает список слов и удаляет из него города
    """
    words = UserInput.split('\n')
    words = [word for word in words if word.lower() not in StopCity]
    result = '\n'.join(words)
    return result

def trim_utm(url):
    """Функция получает ссылку и удаляет из неё utm метки.
    """
    if "utm_" not in url:
        return url
    matches = re.findall('(.+\?)([^#]*)(.*)', url)
    if len(matches) == 0:
        return url
    match = matches[0]
    query = match[1]
    sanitized_query = '&'.join([p for p in query.split('&') if not p.startswith('utm_')])
    return match[0]+sanitized_query+match[2]

def synonym(UserInput):
    """Функция получает список слов и выводит список синонимов.
    """
    result = []
    a = ord('а')
    russ = ''.join([chr(i) for i in range(a,a+32)]) + 'ё '
    for i in UserInput:
        words = 'http://ltmaggie.informatik.uni-hamburg.de/jobimviz/ws/api/russianTrigram/jo/similar/' + i  #Создание строки для запроса
        words = json.dumps(requests.get(words).json(), ensure_ascii=False).encode('utf8').decode().lower()          #Запрос по api словаря синонимов и декодирование utf8
        for letter in words:                       #Отчистка результата от лишних символов
            if letter not in russ:
                words = words.replace(letter, '').replace('  ', ' ')     #Удаляем лишние прибелы и символы не входящие в русский алфавит
        words = words.split()
        if len(UserInput) == 1:
            return words
        result.append(words)
    return result

def CrossMinus(UserInput):
    words = []
    allwords = []
    for keys in UserInput:
        keys = keys.lower().split(' ')
        keys = lemma(keys)
        words.append(keys)
    dub = set(functools.reduce(set.__and__, (set(i) for i in words)))
    for key in words:
        allwords += key
    allwords = set(allwords)
    allwords ^= dub
    for key in words:
        for word in allwords:
            if word not in key:
                key.append('-' + word)
    return words
