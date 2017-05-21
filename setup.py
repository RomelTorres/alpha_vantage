from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='alpha_vantage',
    version='0.1.6',
    author='Romel J. Torres',
    author_email='romel.torres@gmail.com',
    license='MIT',
    description='Python module to get stock data from the Alpha Vantage Api',
    long_description=long_description,
    url = 'https://github.com/RomelTorres/alpha_vantage',
    install_requires=[
        'simplejson',
        'pandas',
        'nose'
    ],
    keywords=['stocks', 'market', 'finance', 'alpha_vantage', 'quotes',
    'shares'],
    packages= find_packages(exclude=['helpers','test_alpha_vantage', 'images']),
    package_data={
        'alpha_vantage':[],
    }
)
