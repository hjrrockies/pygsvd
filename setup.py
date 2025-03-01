import sys
from setuptools import setup, Extension, find_packages
import numpy as np

define_args = '-DBUILD_WITH_PYTHON3' if sys.version.startswith('3') else ''
gsvd_extension = Extension(
                    '_gsvd',
                    ['src/_gsvd.c'],
                    include_dirs=[np.get_include(),
                            '/opt/homebrew/Cellar/lapack/3.12.1/include'
                        ],
                    library_dirs=[
                            '/opt/homebrew/Cellar/lapack/3.12.1/lib'
                            ],
                    libraries=['lapacke'],
                    extra_compile_args = [define_args])

setup(
        name='pygsvd',
        version='0.0.2',
        author='Benjamin Naecker',
        author_email='bnaecker@fastmail.com',
        packages=find_packages(),
        ext_modules=[gsvd_extension],
        install_requires=['numpy>=1.11'],
        py_modules=['pygsvd'],
    )
