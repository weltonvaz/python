#/usr/bin/env python
#coding: utf-8
import os
os.system('clear')

import math

def triangular_numero(n):
    x = (math.sqrt(8 * n + 1) - 1) / 2
    if x - int(x) > 0:
        return "Não é Triangular"
    return "É Triangular"
    

n = int(input("Digite um número: "))
print (triangular_numero(n))
