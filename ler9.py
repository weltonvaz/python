from sympy import divisor_count

def isPrime(x):
    return divisor_count(x) == 2

file = open('pi_27.txt', 'r')
digits = file.read()
groups = []

for i in range(0, len(digits), 9):
    groups.append(digits[i:i+9])
print(groups)
    