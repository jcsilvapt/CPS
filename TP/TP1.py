# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:32:50 2019

@author: uTk99
"""

import numpy as np
import matplotlib.pyplot as plt

class GerarSinal():
    def __init__(self, FS, tempoDeSinal):
        print("Sinal gerado x(t)=20000cos(2pi5050t)+10000sin(2pi2502t)")
        print("Frequência de Amostragem: " + str(FS))
        self.fs = FS
        self.tempo = tempoDeSinal
        
    def gerarPlotSinal(self):
        t = np.arange(0, self.tempo, 1/self.fs)
        sinal = 20000*np.cos(2*np.pi*5050*t) + 10000 * np.sin(2*np.pi*2502*t)
        plt.plot(t, sinal)
        plt.grid(True)
        plt.show()
        
    def amostrarSinal(self, FS):
        n = np.arange(0, 1, 1/FS)
        sinal = 20000*np.cos(2*np.pi*5050*n) + 10000 * np.sin(2*np.pi*2502*n)
        plt.stem(n[:50], sinal[:50], use_line_collection=True)
        plt.grid(True)
        plt.show()
        
sinal = GerarSinal(8000, 10)
sinal.amostrarSinal(44615)