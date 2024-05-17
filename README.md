# Introducción a las redes neuronales informadas por la física

Este repositorio contiene materiasl sobre redes neuronales informadas por la física
(PINNs, del inglés Physics-Informed Neural Newtorks) y está pensado para un minicurso
en el marco del tercer Congreso Colombiano de Matemáticas Aplicadas e Industriales (MAPI-3).


**Contenidos**

 1. [Installación](##instrucciones-de-instalacion)
 3. [Checking the installation](##comprobando-la-instalacion)


## Instrucciones de Instalación

Recomendamos usar ``conda`` para instalar los paquetes necesarios para
este tutorial.

Tenga en cuenta también que este tutorial está escrito para Python 3.X.


Cree un entorno conda usando el archivo ``pinn-tutorial.yml`` en la ruta
del repositorio usando

```console
conda env create -f pinn.yml
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
