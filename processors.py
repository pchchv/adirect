import re
import string
from itertools import product
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def modifier(words):
    """Функция получает набор данных от пользователя, чистит данные от лишних знаков и выводит список строк по слову в строке.
    На данный момент реализованна только функция отчистки от всех знаков.

    """
    words = re.sub('[{}]'.format(re.escape(string.punctuation)), '', words) #удаляем знаки пунктуации
    words = list(set(words.lower().split()))
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
    """Функция считает количество уникальных слов

    """
    res = []
    while len(words) > 0:
        res.append(words[0])                   #Добавляем первый элемент списка к результирующему списку
        words = list(set(words) - set(declension(words[0])))  #Удаляем перенесённый элемент и его склонения
    return res

def generator(*words):
    """Функция получает на вход от 2 до 10 списков, и выводит список сочетаний эллементов входных списков.

    """
    res = list(product(*words))
    return res

def lemma(words):
    """Функция получает список слов и выводит список нормальных форм

    """
    res = []
    for i in words:
        res.append(morph.parse(i)[0].normal_form)
    return(set(res))