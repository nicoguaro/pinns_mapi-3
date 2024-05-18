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
    warn('Este tutorial está pensado para Python 3.')
    onpy2 = True

def tuple_version(version):
    return tuple(int(x) for x in version.strip('<>+-=.').split('.'))

def check_versions():
    version_trouble = False
    
    modules_names = ['numpy', 'scipy', 'matplotlib', 'jupyterlab', 'pytorch',
               'sympy']
    versions = [(3, 12), (1, 26), (1, 13), (3, 8), (4, 2), (2, 2), (1, 12)]

    for module_name, version in zip(modules_names, versions):
        module = importlib.import_module(module_name)
        module_version = tuple_version(module.__version__)
        if module_version < version:
            print(f'Por favor actualiza {module_name} a la versión {version[0].version[1]} o mayor')
            version_trouble = True

    return version_trouble


def main():
    required_modules = ['numpy', 'matplotlib', 'jupyterlab', 'scipy',
                        'pytorch', 'sympy']
    
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
        print('Los siguientes módulos se requieren pero no están instalados:')
        print('    {}'.format(', '.join(missing_modules)))
        print('\nLos puede instalar usando conda ejecutando:')
        print('\n    conda install {}'.format(' '.join(missing_modules)))
        print('\nO puede instalarlo usando pip ejecutando:')
        print('\n    pip install {}'.format(' '.join(missing_modules)))
    else:
        if check_versions():
            print('Todos los paquetes están instalados pero al menos uno necesita acualización')
        else:
            print('¡Todo parece estar bien!')

if __name__ == '__main__':
    main()