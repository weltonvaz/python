#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def happy(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1, 7) if number < 10 else happy(next_)

n = int(input("Digite um número: "))

print ("O número %d é um feliz(True)/Infeliz(False) --> %s " %(n,happy(n)))
