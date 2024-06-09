#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebe la instalación para el paquetes taller de redes neuronales
informadas por la física del tercer Congreso Colombiano de Matemáticas
Aplicadas e Industriales ejecutando algunos ejemplos.

@author: Nicolás Guarín-Zapata
"""
import numpy as np


def mensaje(msg):
    msg = "\n\n" + msg
    print(msg)
    print("="*len(msg))

## Datos de prueba: Matlab `peaks()`
x, y = np.mgrid[-3:3:150j,-3:3:150j]
z =  3*(1 - x)**2 * np.exp(-x**2 - (y + 1)**2) \
   - 10*(x/5 - x**3 - y**5)*np.exp(-x**2 - y**2) \
   - 1./3*np.exp(-(x + 1)**2 - y**2)

#%% Matplotlib
try:
    mensaje("Probando la instalación de Matplotlib")
    import matplotlib.pyplot as plt
    from matplotlib.colors import LightSource

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Crea una fuente de luz
    ls = LightSource(azdeg=0, altdeg=65)
    rgb = ls.shade(z, plt.cm.RdYlBu)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1,
                           linewidth=0, antialiased=False,
                           facecolors=rgb)
    print("¡Matplotlib está funcionando correctamente!")

except:
    print("¡Matplotlib no está funcionando correctamente!")



#%% Pytorch
try:
    mensaje("Probando la instalación de PyTorch")
    import torch
    import matplotlib.pyplot as plt
    
    npts = 1000
    X = torch.linspace(-5, 5, npts).view(-1, 1)
    Y = torch.sin(X**2)
    
    
    plt.figure()
    plt.plot(X.numpy(), Y.numpy())
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    print("¡PyTorch está funcionando correctamente!")
    plt.show()
except:
    print("¡PyTorch no está funcionando correctamente!")