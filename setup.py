from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    long_description = 'Python module to get stock data from the Alpha Vantage Api'

setup(
    name='alpha_vantage',
    version='2.1.2',
    author='Romel J. Torres',
    author_email='romel.torres@gmail.com',
    license='MIT',
    description='Python module to get stock data from the Alpha Vantage Api',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/RomelTorres/alpha_vantage',
    install_requires=[
        'requests'
    ],
    test_requires=[
        'nose',
        'requests_mock'
    ],
    extras_requires={
        'pandas': ['pandas'],
    },
    keywords=['stocks', 'market', 'finance', 'alpha_vantage', 'quotes',
              'shares'],
    packages=find_packages(
        exclude=['helpers', 'test_alpha_vantage', 'images']),
    package_data={
        'alpha_vantage': [],
    }
)
