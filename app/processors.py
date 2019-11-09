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
        marks += string.punctuation + '\r'
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
        while '' in words:
            words.remove('')
    if 'dub' in type:
        list(set(words))
    return words

def declension(UserInput):
    """Функция возвращает список склонений заданного слова, включая само слово.

    """
    result = []
    decls = []
    for word in UserInput:
        words = morph.parse(word.lower())[0].lexeme 
        for element in words:
            (element)
            decl = str(element).split(' ')
            decls.append(decl[-3].replace("'", '').replace(',', ''))
        if word not in decls:
            decls.append(word)
        if len(UserInput) == 1:
            return '\n'.join(decls)
        result.append(decls)
    return '\n'.join(result)

def counter(words):
    """Функция считает количество уникальных слов.
    Возвращает список, в котором первый элемент - количество слов, второй - все слова через пробел.

    """
    result = []
    while len(words) > 0:
        result.append(words[0])               #Добавляем первый элемент списка к результирующему списку
        words = list(set(words) - set(declension(words[0])))  #Удаляем перенесённый элемент и его склонения
    result.insert(0, 'Количество слов - ' + str(len(result)))
    result = '\n'.join(result)
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
    (words)
    res = []
    for i in words:
        res.append(morph.parse(i)[0].normal_form)
    return '\n'.join(res)

def cityremover(UserInput, StopCity = open('stopcity.txt', 'r').read()):
    """Функция получает список слов и удаляет из него города
    """
    result = []
    for words in UserInput:
        words = words.split(' ')
        words = [word for word in words if word not in StopCity]
        words = ' '.join(words)
        result.append(words)
    return '\n'.join(result)

def trim_utm(url):
    """Функция получает ссылку и удаляет из неё utm метки.
    """
    url = url.split('\n')
    result = []
    for url in url:
        if "utm_" not in url:
           return url
        matches = re.findall('(.+\?)([^#]*)(.*)', url)
        if len(matches) == 0:
           return url
        match = matches[0]
        query = match[1]
        sanitized_query = '&'.join([p for p in query.split('&') if not p.startswith('utm_')])
        result.append(match[0]+sanitized_query+match[2])
    return result

def synonym(UserInput):
    """Функция получает список слов и выводит список синонимов.
    """
    result = []
    a = ord('а')
    russ = ''.join([chr(i) for i in range(a,a+32)]) + 'ё '
    for i in UserInput:
        words = 'http://www.serelex.org/find/ru-skipgram-librusec/' + i  #Создание строки для запроса
        words = json.dumps(requests.get(words).json(), ensure_ascii=False).encode('utf8').decode().lower()          #Запрос по api словаря синонимов и декодирование utf8
        for letter in words:                       #Отчистка результата от лишних символов
            if letter not in russ:
                words = words.replace(letter, '').replace('  ', ' ')     #Удаляем лишние прибелы и символы не входящие в русский алфавит
        words = words.split()
        if len(UserInput) == 1:
            return words
        result.append(words)
    return result

def crossminus(UserInput):
    """ Функция получает на вход список фраз и производит добавление слов с префиксом '-' не входящих в данную фразу,
        но входящих в стальные фразы"""
    words = []
    allwords = []
    result = []
    for keys in UserInput:
        keys = keys.split(' ')
        words.append(keys)
    dub = set(functools.reduce(set.__and__, (set(i) for i in words)))
    for key in words:
        allwords += key
    allwords = set(allwords)
    allwords ^= dub
    #print(words)
    #print(allwords)
    for key in words:
        for word in allwords:
            if word not in key:
                key.append('-' + word)
    for i in range(len(words)):
        result.append(' '.join(words[i]))
    return '\n'.join(result)
