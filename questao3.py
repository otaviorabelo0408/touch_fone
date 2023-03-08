from numpy import (linspace, sin, arange, absolute, pi, exp)
from matplotlib.pyplot import (plot, show, title, xlabel, ylabel, stem)
from statistics import mean
from scipy import io


def dft(lista):
    aux = list()
    for k in range(len(lista)):
        soma = 0
        for n in range(len(lista)):
            soma += lista[n] * exp((1j * (-2) * pi * k * n) / len(lista))
        aux.append(soma)
    return aux


def touch_fone(lista):
    numero = ""
    linha = [697, 770, 852, 940]
    coluna = [1209, 1336, 1477]
    matriz = []
    frequenciasl = []
    frequenciasc = []
    for m in range(8):
        matriz.append(list(lista[m * int(len(lista)/8):int((m + 1) * len(lista)/8)]))
    dfts = []
    for o in range(8):
        dfts.append(list(absolute(dft(matriz[o]))))
        dfts[o] = (dfts[o][:int(len(matriz[o]) / 2)])
    for p in range(8):
        for freql in linha:
            if dfts[p][freql] > 500:
                frequenciasl.append(freql)
    for q in range(8):
        for freqc in coluna:
            if dfts[q][freqc] > 500:
                frequenciasc.append(freqc)
    for i in range(8):
        if frequenciasl[i] == 697:
            if frequenciasc[i] == 1209:
                numero = numero + '1'
            elif frequenciasc[i] == 1336:
                numero = numero + '2'
            else:
                numero = numero + '3'
        elif frequenciasl[i] == 770:
            if frequenciasc[i] == 1209:
                numero = numero + '4'
            elif frequenciasc[i] == 1336:
                numero = numero + '5'
            else:
                numero = numero + '6'
        elif frequenciasl[i] == 852:
            if frequenciasc[i] == 1209:
                numero = numero + '7'
            elif frequenciasc[i] == 1336:
                numero = numero + '8'
            else:
                numero = numero + '9'
        else:
            numero = numero + '0'
    return numero


dic = io.loadmat("touch_fone.mat")
sinal = dic['x']
sinal = sinal.ravel()

print(touch_fone(sinal))
