""" Zajmuje sie porownywaniem tesktow """

import numpy as np

class CompareString:
    """ Calculates the similarity of string """

    @staticmethod
    def compare(first: str, second: str) -> int:
        """ Porowuje teksty i zwraca ile znaków jest różnych"""
        return CompareString.Levenshtein_Distance(first, second)

    @staticmethod
    def is_similar(first: str, second: str, strictness: int) -> bool:
        """ Czy teksty sa podobne? """
        return CompareString.Levenshtein_Distance_Opt(first, second, strictness)

    @staticmethod
    def Levenshtein_Distance(first: str, second: str) -> int:
        """ Algorytm, zrodlo: https://pl.wikipedia.org/wiki/Odleg%C5%82o%C5%9B%C4%87_Levenshteina
        int LevenshteinDistance(char s[1..m], char t[1..n])
            declare int d[0..m, 0..n] // niech d będzie tablicą o m+1 wierszach i n+1 kolumnach
            for i from 0 to m
                d[i, 0] := i
            for j from 1 to n
                d[0, j] := j

            for i from 1 to m
                for j from 1 to n
                    if s[i] = t[j] then cost := 0
                                    else cost := 1
                    d[i, j] := minimum(d[i-1, j] + 1,       // usuwanie
                                        d[i, j-1] + 1,       // wstawianie
                                        d[i-1, j-1] + cost)  // zamiana
            return d[m, n]
        """
        first = " " + first
        second = " " + second
        len_first = len(first)
        len_second = len(second)

        arr = np.zeros([len_first, len_second], int)

        arr[:, 0] = range(len_first)
        arr[0, :] = range(len_second)

        for i in range(1,len_first):
            for j in range(1,len_second):
                if first[i] == second[j]:
                    cost = 0
                else:
                    cost = 1
                arr[i,j] = min(arr[i-1, j]+1, arr[i, j-1]+1, arr[i-1, j-1]+cost)

        return arr[len_first-1, len_second-1]

    @staticmethod
    def Levenshtein_Distance_Opt(first: str, second: str, strictness: int) -> bool:
        """ Zoptymalizowany algorytm Levensteina, ktory przerywa dzialanie po przekroczeniu strictness """
        if abs(len(first) - len(second)) > strictness:
            return False

        first = " " + first
        second = " " + second
        len_first = len(first)
        len_second = len(second)

        arr = np.zeros([len_first, len_second], int)

        arr[:, 0] = range(len_first)
        arr[0, :] = range(len_second)

        for i in range(1,len_first):
            for j in range(1,len_second):
                cost = 0 if first[i] == second[j] else 1
                arr[i,j] = min(arr[i-1, j]+1, arr[i, j-1]+1, arr[i-1, j-1]+cost)

                if i == j:
                    if arr[i,j] > strictness:
                        return False

        return arr[len_first-1, len_second-1] <= strictness
