import sympy
import csv

with open('divisores.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Número', 'Número de Divisores', 'Divisores'])

    for i in range(2, 1000001):
        divisors = sympy.divisors(i)
        divisors_str = ', '.join(str(divisor) for divisor in divisors)
        writer.writerow([i, sympy.divisor_count(i), divisors_str])

