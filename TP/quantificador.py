# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:09:41 2019

@author: A44615
"""

import numpy as np
import matplotlib.pyplot as plt

class quantificador:
    def __init__(self, sinal, R, tipo):
        self.tipo = tipo
        self.sinal = sinal
        self.r = R
        self.QuantificadorUniforme()
        
    def QuantificadorUniforme(self):
        L = 2**R
        Vmax = np.max(np.abs(self.sinal))
        delta = (2*Vmax) / L
        self.intervalosDecisao = np.where(self.tipo.lower() == "midrise", np.arange(-Vmax + delta, Vmax + delta, delta), np.arange(-Vmax + delta / 2, Vmax, delta))
        self.valoresQuantificacao = np.where(self.tipo.lower() == "midrise", np.arange(-Vmax + delta / 2, Vmax, delta), np.arange(-Vmax + delta, Vmax + delta, delta))

    def getValoresQuantificacao(self):
        return self.valoresQuantificacao
    
    def quantificar(self):
        sinalQuantificado = np.zeros(len(self.sinal))
        vq = np.zeros(len(self.sinal))
        
        for i in range(len(self.sinal)):
            for j in range(len(self.intervalosDecisao)):
                if(sinal[i] < self.intervalosDecisao[j]):
                    sinalQuantificado[i] = self.valoresQuantificacao[j]
                    vq[i] = j
                    break
                else:
                    sinalQuantificado[i] = self.valoresQuantificacao[len(self.intervalosDecisao) - 1]
                    vq[i] = len(self.intervalosDecisao) - 1
        return sinalQuantificado, vq


class ModuloCodificador:
    def __init__(self, sinalCodificado, R):
        self.sinal = sinalCodificado
        self.r = R
        self.codificador()
    
    def codificador(self):
        valores = 2**self.r
        codigos = np.zeros(valores)
        for valor in range(valores):
            codigos[valor] = int(bin(valor)[2:])
        self.codigo = codigos
        
    def codificarSinal(self, indicesQuantificacao):
        codificado = np.zeros(len(indicesQuantificacao))
        
        for indice in range(len(indicesQuantificacao)):
            codificado[indice]= self.codigo[int(indicesQuantificacao[indice])]
        
        return codificado
        
class ModuloDescodificador:
    def __init__(self, sinal, valoresQuantificacao):
        self.sinal = sinal
        self.vQ = valoresQuantificacao

Fs = 8000
n = np.arange(0, 1, 1 / Fs)
R = 3
sinal = 20000 * np.cos(2 * np.pi * 5050 * n) + 10000 * np.sin(2 * np.pi * 2502 * n)

qtf = quantificador(sinal, R, "midrise")


sinalQuantificado, iq = qtf.quantificar()

mCodig = ModuloCodificador(sinalQuantificado, R)

print("MEU")
print(sinalQuantificado[:5])
print()
sinalCodificado = mCodig.codificarSinal(iq)
print(sinalCodificado[:5])