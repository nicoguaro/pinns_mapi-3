"""
Comprueba la instalación de los paquetes taller de redes neuronales
informadas por la física del tercer Congreso Colombiano de Matemáticas
Aplicadas e Industriales.

Este archivo se basa en el siguiente script:
    
    https://github.com/gforsyth/numba_tutorial_scipy2017/blob/master/check_install.py

que es publicado bajo licencia del MIT por Gilbert Forsyth y Lorena Barba.
"""
import importlib
import sys
from warnings import warn

onpy2 = False

try:
    assert sys.version_info >= (3,0)
    import importlib.util
except AssertionError:
    warn('This tutorial is written for Python 3.  Legacy Python is not explicitly supported.')
    onpy2 = True

def tuple_version(version):
    return tuple(int(x) for x in version.strip('<>+-=.').split('.'))

def check_versions():
    version_trouble=False
    mpl = importlib.import_module('matplotlib')
    mpl_version = tuple_version(mpl.__version__)
    if mpl_version < (2, 0, 0):
        print('Please update matplotlib to version 2.0.0 or higher')
        version_trouble=True

    return version_trouble

def main():
    required_modules = ['numpy', 'matplotlib', 'jupyter', 'scipy',
                        'vtk', 'IPython', 'jupyter', 'mayavi',
                        'yt', 'ipyvolume', 'spyder', 'PyQt5']
    
    missing_modules = []
    for mod in required_modules:
        if not onpy2:
            spec = importlib.util.find_spec(mod)
            if spec is None:
                missing_modules.append(mod)
        else:
            try:
                importlib.import_module(mod)
            except ImportError:
                missing_modules.append(mod)

    if missing_modules:
        print('The following modules are required but not installed:')
        print('    {}'.format(', '.join(missing_modules)))
        print('\nYou can install them using conda by running:')
        print('\n    conda install {}'.format(' '.join(missing_modules)))
        print('\nOr you can install them using pip by running:')
        print('\n    pip install {}'.format(' '.join(missing_modules)))
    else:
        if check_versions():
            print('All packages are installed but at least one needs updating')
        else:
            print('Everything looks good!')

if __name__ == '__main__':
    main()