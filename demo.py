#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebe la instalación para el paquetes taller de redes neuronales
informadas por la física del tercer Congreso Colombiano de Matemáticas
Aplicadas e Industriales ejecutando algunos ejemplos.

@author: Nicolás Guarín-Zapata
"""
import numpy as np


## Datos de prueba: Matlab `peaks()`
x, y = np.mgrid[-3:3:150j,-3:3:150j]
z =  3*(1 - x)**2 * np.exp(-x**2 - (y + 1)**2) \
   - 10*(x/5 - x**3 - y**5)*np.exp(-x**2 - y**2) \
   - 1./3*np.exp(-(x + 1)**2 - y**2)

#%% Matplotlib
try:
    msg = "Probando la instalación de Matplotlib"
    print(msg)
    print("="*len(msg))
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.colors import LightSource

    Axes3D
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Create light source object.
    ls = LightSource(azdeg=0, altdeg=65)
    rgb = ls.shade(z, plt.cm.RdYlBu)
    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, linewidth=0,
                           antialiased=False, facecolors=rgb)
    plt.show()
    print("¡Matplotlib está funcionando correctamente!")
except:
    print("¡Matplotlib no está funcionando correctamente!")



#%% Pytorch
try:
    pass
except:
    pass