# Introducción a las redes neuronales informadas por la física

Este repositorio contiene materiasl sobre redes neuronales informadas por la física
(PINNs, del inglés Physics-Informed Neural Newtorks) y está pensado para un minicurso
en el marco del tercer Congreso Colombiano de Matemáticas Aplicadas e Industriales (MAPI-3).


## Contenido

 1. [Motivación](#motivación)
 2. [Instalación](#instrucciones-de-instalación)
 3. [Comprobando la instalación](#comprobando-la-instalación)

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
conda env create -f pinn-tutorial.yml
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

## Licencia

Todo el código está bajo licencia MIT y el contenido bajo licencia Creative Commons Attribute.

El contenido de este repositorio está bajo licencia bajo la
[Licencia Creative Commons Attribution 4.0](http://choosealicense.com/licenses/cc-by-4.0/),
y el código fuente que acompaña al contenido tiene 
[Licencia MIT](https://opensource.org/licenses/mit-license.php).
