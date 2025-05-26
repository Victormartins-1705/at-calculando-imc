
import statistics

numeros = [5, 8, 12, 14, 17, 20, 22, 24, 27, 30, 33, 35, 38, 40]

media1 = statistics.mean(numeros)
mediana1 = statistics.median(numeros)
print("Média (modo 1):", media1)
print("Mediana (modo 1):", mediana1)

import statistics as st
media2 = st.mean(numeros)
mediana2 = st.median(numeros)
print("Média (modo 2):", media2)
print("Mediana (modo 2):", mediana2)

from statistics import mean, median
media3 = mean(numeros)
mediana3 = median(numeros)
print("Média (modo 3):", media3)
print("Mediana (modo 3):", mediana3)

from statistics import *
media4 = mean(numeros)
mediana4 = median(numeros)
print("Média (modo 4):", media4)
print("Mediana (modo 4):", mediana4)
