#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

a = 1
n = 3
print(a,end=' ')
for x in range(0,7):
	a = a + (n**x)
	print(a,end=' ')
print()
