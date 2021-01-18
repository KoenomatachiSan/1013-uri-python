import math

VALOR = input("VALOR:").split(" ")

a, b, c = VALOR

MAIOR = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
RESULT = (int(MAIOR) + int(c) + abs(int(MAIOR) - int(c)))/2

print("%d eh o MAIOR" %RESULT)