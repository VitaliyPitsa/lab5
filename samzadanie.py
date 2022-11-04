#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
средний балл студентов в группе
"""


def beg(**keywords):
    summa = 0
    n = len(keywords)
    max = keywords["Виталик"]
    for kw in keywords:
        summa = summa + keywords[kw]
        if keywords[kw] > max:
            max = keywords[kw]
    print("Средний балл студентов в группе - ", round(summa / n, 2))
    print("Максимальный балл - ", max)


if __name__ == "__main__":
    beg(
        Вася=60.1,
        Виталик=62.3,
        Адам=62.7,
        Вова=59.5,
        Дина=65.8,
    )