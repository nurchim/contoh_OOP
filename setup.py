from setuptools import setup, find_packages

from my_pip_package import __version__

extra_math = [
    'returns-decorator',
]

extra_bin = [
    *extra_math,
]

extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='contoh',
    version=__version__,
    description='A tutorial for creating pip packages.',

    url='https://github.com/nurchim/contoh_OOP',
    author='Nurchim',
    author_email='nurchim@udb.ac.id',

    packages=find_packages(exclude=['tests', 'tests.*']),

    extras_require={
        'math': extra_math,

        'bin': extra_bin,

        'test': extra_test,
        'dev': extra_dev,

        'ci': extra_ci,
    },

    entry_points={
        'console_scripts': [
            'add=contoh.math:cmd_add',
        ],
    },

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
