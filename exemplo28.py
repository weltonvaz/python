#/usr/bin/env python
#coding: utf-8
import os
os.system('clear')
__author__ = 'welton'

num1 = int(input("Digite um número: "))

if(num1 > 10):
    print ("O valor é maior do que 10!")
else:
    if (num1 > 5):
        print("O numero é menor do que 10 mas maior do que 5!")
        if (num1 == 7):
            print("O número é iqual a 7.0")
        else:
            print("O valor é menor do que 5.0")
