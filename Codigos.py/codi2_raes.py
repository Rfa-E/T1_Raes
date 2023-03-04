"""
Analitzar el senyal del fitxer wav
"""

import numpy as np

import matplotlib.pyplot as plt

import soundfile as sf

import sounddevice as sd

from numpy.fft import fft  

x_r, fm = sf.read('so1_raes.wav')       # Llegim el fitxer

T = (1/fm)*len(x_r)
Tm=1/fm 

L = int(fm * T) 
t=Tm*np.arange(L)

#Representació dels 5 períodes
fx=fm/2 
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide
plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.
sd.play(x_r, fm) 

#FFT
N=5000
X_r=fft(x_r[0:Ls],N) 
k=np.arange(N)                        # Vector amb els valors 0≤  k<N
plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X_r))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X_r)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()   