# Introducción a las redes neuronales informadas por la física

![GitHub](https://img.shields.io/github/license/nicoguaro/pinns_mapi-3)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Abrir en Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nicoguaro/pinns_mapi-3/HEAD)
[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nicoguaro/pinns_mapi-3)

Este repositorio contiene materiasl sobre redes neuronales informadas por la física
(PINNs, del inglés Physics-Informed Neural Newtorks) y está pensado para un minicurso
en el marco del tercer Congreso Colombiano de Matemáticas Aplicadas e Industriales (MAPI-3).


## Contenido

 1. [Motivación](#motivación)
 2. [Instalación](#instrucciones-de-instalación)
 3. [Comprobando la instalación](#comprobando-la-instalación)
 4. [Referencias](#referencias)
 5. [Licencia](#licencia)


## Motivación

La modelación de fenómenos físicos mediante ecuaciones diferenciales parciales (EDP) es esencial en varias áreas de las matemáticas puras y aplicadas. Estos modelos describen cómo cambian ciertas cantidades físicas en el espacio y el tiempo, permitiendo abordar problemas cruciales como: predecir comportamientos, optimizar procesos y diseñar soluciones en campos como la química, la biología, la economía y la ingeniería. Dada la complejidad de muchos de estos problemas, encontrar soluciones exactas es a menudo imposible, lo que subraya la necesidad de métodos numéricos efectivos para aproximar las soluciones.

Aunque el análisis numérico clásico ofrece numerosas herramientas para aproximar soluciones de EDP, los recientes avances en la computación científica destacan la importancia de explorar nuevos métodos numéricos que amplíen las aplicaciones. Y además, como matemáticos, es crucial investigar y fortalecer la fundamentación de estos nuevos desarrollos. Por ejemplo, el teorema de aproximación universal establece que las redes neuronales pueden aproximar funciones continuas con gran precisión, abriendo nuevas posibilidades para la modelación matemática. Por otro lado, avances como la diferenciación automática (_autodiff_) permiten calcular derivadas de funciones complejas de manera precisa y eficiente, facilitando la integración de estos métodos en procesos de optimización y entrenamiento de modelos.

Las Physics-Informed Neural Networks (PINNs) son una clase emergente de redes neuronales que incorporan directamente las leyes físicas expresadas mediante EDP en el proceso de aprendizaje. A diferencia de las redes neuronales tradicionales, las PINN utilizan información física para guiar el entrenamiento, imponiendo las EDP como restricciones en la función de pérdida, lo que permite que las redes aprendan soluciones que respeten las leyes físicas subyacentes.

Este curso de teoría e implementación de PINN está diseñado para matemáticos interesados en desarrollar y aplicar métodos numéricos avanzados para resolver problemas descritos por EDP. Durante las dos sesiones, se introducirán los conceptos matemáticos y algorítmicos fundamentales para entender y utilizar PINN, combinando principios físicos con técnicas de aprendizaje automático para resolver problemas clásicos. Los participantes aprenderán a implementar estas metodologías utilizando software de código abierto, facilitando así la extensión del conocimiento adquirido a otros problemas en sus respectivas áreas de estudio. El curso estará organizado en dos partes, cada una compuesta por dos sesiones. En la primera parte, se cubrirán la formulación de problemas físicos mediante EDP y los fundamentos teóricos de las PINN. La segunda parte estará enfocada en la implementación práctica, utilizando herramientas de software y trabajando en ejemplos y ejercicios prácticos.


## Instrucciones de Instalación

Recomendamos usar ``conda`` para instalar los paquetes necesarios para
este tutorial.

Tenga en cuenta también que este tutorial está escrito para Python 3.X.


Cree un entorno conda usando el archivo ``pinn-tutorial.yml`` en la ruta
del repositorio usando

```console
conda env create -f environment.yml
```

Esto creará un entorno conda llamado "pinn-tutorial" con todos los
paquetes requeridos.

Puedes activar el entorno con

```console
conda activate pinn-tutorial
```

## Comprobando la instalación

Después de la instalación puedes comprobar si todo está instalado.

```console
python probar_instalacion.py
```

Para comprobar si todo funciona, ejecute las demostraciones con

```console
python demo.py
```


## Referencias

Existen muchos artículos científicos relacionados con PINNs. A continuación,
compartimos 4 que pueden servir como punto de partida para el tópico.

- Raissi, Maziar, Paris Perdikaris, and George E. Karniadakis.
  ["Physics-informed neural networks: A deep learning framework for solving
  forward and inverse problems involving nonlinear partial differential
  equations."](https://www.sciencedirect.com/science/article/pii/S0021999118307125)
  Journal of Computational physics 378 (2019): 686-707.

- Karniadakis, George Em, et al.
  ["Physics-informed machine learning."](https://doi.org/10.1038/s42254-021-00314-5)
  Nature Reviews Physics 3.6 (2021): 422-440.

- Chuang, Pi-Yueh, and Lorena A. Barba.
  ["Predictive limitations of physics-informed neural networks in vortex shedding."]
  (https://arxiv.org/abs/2306.00230) arXiv preprint arXiv:2306.00230 (2023).

- Krishnapriyan, Aditi, et al. ["Characterizing possible failure modes
  in physics-informed neural networks."](https://arxiv.org/abs/2109.01050)
  Advances in Neural Information Processing Systems 34 (2021): 26548-26560.

## Licencia

Todo el código está bajo licencia MIT y el contenido bajo licencia Creative Commons Attribute.

El contenido de este repositorio está bajo licencia bajo la
[Licencia Creative Commons Attribution 4.0](http://choosealicense.com/licenses/cc-by-4.0/),
y el código fuente que acompaña al contenido tiene 
[Licencia MIT](https://opensource.org/licenses/mit-license.php).
