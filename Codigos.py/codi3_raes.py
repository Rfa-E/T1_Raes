"""
Representacio del modul de la Transformada de Fourier en dB
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd
from numpy.fft import fft
import os

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=fm/2                              # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so3_raes.wav', x, fm)      # Escriptura del senyal a un fitxer en format wav
Tx=1/fx                              # Període del senyal
Ls=int(fm*5*Tx)                      # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.
sd.play(x,fm)

N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                # Vector amb els valors 0≤  k<N
X_dB = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N         #Calcul de la fk, pels valors de l'eix d'abscisses
plt.figure(1)
plt.subplot(211)   
plt.plot(fk,X_dB[0:N//2+1])  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                  
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')              
plt.show() 