# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:27:11 2019

@author: jorge
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav


def gerarGrafico(xt, tempo, PlotTitle, FileTitle,  savepic):
    plt.close('all')
    plt.title(PlotTitle)
    plt.xlabel(r'$t$ (s)', fontsize=18)
    plt.ylabel('Amplitude', fontsize=16)
    plt.plot(tempo, xt)
    plt.grid(True)
    if savepic:
        plt.savefig("./img/"+FileTitle+".png")
    plt.show()

def gerarEspetroAmplitude(xt, fs, PlotTitle, FileTitle,  savepic):
    plt.close('all')
    plt.title(PlotTitle)
    
    new_x = xt[0:len(xt):100]
    xfft = np.fft.fft(new_x)
    N = len(new_x)
    freq1 = np.fft.fftfreq(xfft.shape[-1]) * fs * 10
    x1mag = np.abs(xfft) / N
    
    plt.stem(freq1, x1mag, 'k')
    plt.ylabel('Espectro amplitude')
    plt.xlabel('f(Hz)')
    if savepic:
        plt.savefig("./img/"+FileTitle+".png")
    plt.show()
    
def gerarEspetroFase(xt, fs, PlotTitle, FileTitle,  savepic):
    plt.close('all')
    plt.title(PlotTitle)
    
    new_x = xt[0:len(xt):100]
    xfft = np.fft.fft(new_x)
    freq1 = np.fft.fftfreq(xfft.shape[-1]) * fs * 10
    xfase = np.angle(xfft)
    plt.stem(freq1, xfase, 'k')
    plt.ylabel('Espectro de fase')
    plt.xlabel('f(Hz)')
    if savepic:
        plt.savefig("./img/"+FileTitle+".png")
    plt.show()
    
def gravarWav(xt, fs, FileTitle):
    format = xt.astype('int16')
    wav.write("./sounds/"+FileTitle+".wav", fs, format)
    
#1. Admita que tem o sinal 20000cos(25050t) + 10000sin(22502t). Represente o seu espectro Amplitude e Fase.

Fs = 1/5050

t = np.linspace(-4*Fs,4*Fs, 2000)

x_t1 = 20000 * np.cos(2 * np.pi * 5050 * t)

#gerarGrafico(x_t1, t, "x(t)=20000cos(2pi*5050*t)", True)

x_t2 = 10000 * np.sin(2 * np.pi * 2502 * t)

#gerarGrafico(x_t2, t, "x(t)=10000sin(2pi*2502*t)", True)

xt = x_t1 + x_t2

gerarGrafico(xt, t, "x(t)=20000cos(2pi*5050*t)+10000sin(2pi*2502*t)", "TP1_Q1", True)
gerarEspetroAmplitude(xt, 5050, "Espetro de Amplitude de x(t)","TP1_Q1I", True)
gerarEspetroFase(xt, 5050, "Espetro de Fase de x(t)","TP1_Q1II", True)


print()
print()

#2. Admitindo que faz a amostragem do sinal com uma frequência fs = 8kHz, represente o espectro do sinal amostrado.

Fs = 1/8000

t = np.linspace(-4*Fs,4*Fs, 2000)

x_t1 = 20000 * np.cos(2 * np.pi * 5050 * t)
x_t2 = 10000 * np.sin(2 * np.pi * 2502 * t)

xt = x_t1 + x_t2

gerarGrafico(xt, t, "x(t)=20000cos(2pi*5050*t)+10000sin(2pi*2502*t)", "TP1_Q2", True)
gerarEspetroAmplitude(xt, 8000, "Espetro de Amplitude de x(t)","TP1_Q2I", True)
gerarEspetroFase(xt, 8000, "Espetro de Fase de x(t)","TP1_Q2II", True)

#3. Gere o sinal em Python considerando que tem duração de um segundo.
    #a) Faça a amostragem do sinal com uma frequência fs = 44:1 kHz. Grave o sinal e reproduza o som. Apresente
    #   o seu espectro. Confirme os resultados teóricos da questão 1.
    
Fs = 1/41100    

t = np.arange(0, 1, Fs)

x_t1 = 20000 * np.cos(2 * np.pi * 5050 * t)
x_t2 = 10000 * np.sin(2 * np.pi * 2502 * t)

xt = x_t1 + x_t2

gerarGrafico(xt[:1000], t[:1000], "x(t)=20000cos(2pi*5050*t)+10000sin(2pi*2502*t)", "TP1_Q3A", True) 
gerarEspetroAmplitude(xt, 41100, "Espetro de Amplitude de x(t)","TP1_Q3AI", True)
gerarEspetroFase(xt, 41100, "Espetro de Fase de x(t)","TP1_Q3AII", True)
gravarWav(xt, 41100, "TP1_Q3A_SOUND")
    
    #b) Faça a amostragem do sinal com uma frequência fs = 8 kHz. Grave o sinal e reproduza o som. Apresente
    #   o seu espectro. Conforme os resultados teóricos da questão 2. Tire conclusões. 

Fs = 1/8000   

t = np.arange(0, 1, Fs)

x_t1 = 20000 * np.cos(2 * np.pi * 5050 * t)
x_t2 = 10000 * np.sin(2 * np.pi * 2502 * t)

xt = x_t1 + x_t2

gerarGrafico(xt[:100], t[:100], "x(t)=20000cos(2pi*5050*t)+10000sin(2pi*2502*t)", "TP1_Q3B", True) 
gerarEspetroAmplitude(xt, 8000, "Espetro de Amplitude de x(t)","TP1_Q3BI", True)
gerarEspetroFase(xt, 8000, "Espetro de Fase de x(t)","TP1_Q3BII", True)
gravarWav(xt, 8000, "TP1_Q3B_SOUND")    
    
    
#4. Construa uma função em Python que crie as tabelas com os intervalos de decisao e valores de quanticação para
#   um quanticador uniforme. Esta função tem como parâmetros de entrada o número de bits por amostra (R), o
#   valor máximo a quantificar (Vmax) e o tipo de quanticador (midrse ou midtread). Como parâmetros de saída
#   tem dois Numpy arrays com valores de quanticação e os intervalos de decisão.

def quantificadorUniforme(R, Vmax, tipo):
    #Defenir o número de nívies de quantificação
    L = 2**R
    
    #Definir os intervlaos de quantificação
    delta = (2 * Vmax) / L
    
    if(tipo.lower().strip() == "midrise"):
        iDecisao = np.arange(-Vmax + delta, Vmax + delta, delta)
        vQuantificacao = np.arange(-Vmax + delta / 2, Vmax, delta)
        return iDecisao, vQuantificacao
    elif(tipo.lower().strip() == "midtread"):
        iDecisao = np.arange(-Vmax + delta / 2, Vmax, delta)
        vQuantificacao = np.arange(-Vmax + delta, Vmax + delta, delta)
        return iDecisao, vQuantificacao
    else:
        print("Quantificador desconhecido...")

id, vq = quantificadorUniforme(3, 1 , "midrise")
print("Quantificador 'midrise' -> 3, 1")
print(id)
print(vq)
print()
id, vq = quantificadorUniforme(3, 1 , "midtread")
print("Quantificador 'midtread' -> 3, 1")
print(id)
print(vq)
print()
#5. Construa uma função em Python que dado um Numpy array com as amplitudes de um sinal amostrado, retorne
#   um Numpy array com o sinal quantificado e um Numpy array com o índice dos valores de quantificação usados
#   (vq).
    
def quantificador(xt, R, Vmax, tipo):
    
    sinalQuantificado = np.zeros(len(xt))
    vq = np.zeros(len(xt))
    
    iDecisao, vQuantificado = quantificadorUniforme(R, Vmax, tipo)
    
    for i in range(len(xt)):
        for j in range(len(iDecisao)):
            if(xt[i] < iDecisao[j]):
                sinalQuantificado[i] = vQuantificado[j]
                vq[i] = j
                break
            else:
                sinalQuantificado[i] = vQuantificado[len(iDecisao) - 1]
                vq[i] = len(iDecisao) - 1
    
    return sinalQuantificado, vq
    

    
    
sinal = [0.9, 0.2, -0.25, -0.57, -0.32, 0.11, 0.41, 0.8, 0.92, 1, 0.77, 0.03, -0.41, -0.88]
sq, vq = quantificador(sinal, 3, 1 , "midrise")
print("sinal >")
print(sinal)
print("Sinal Quantificado 'midrise' -> ")
print(sq)
print()
sq, vq = quantificador(sinal, 3, 1 , "midtread")
print("Sinal Quantificado 'midtread' -> ")
print(sq)
print()

def leimi(xt):
    sinal = np.zeros(len(xt))
    
    Vmax = np.max(xt)
    
    for m in range(len(sinal)):
        sinal[m] = (np.log(1 + 255 * abs(m)) / np.log(1 + 255)) * np.sign(m)
    
    return sinal
    
b = leimi(sinal)
print(b)