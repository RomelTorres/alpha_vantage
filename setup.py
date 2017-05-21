from setuptools import setup, find_packages
from os import path

setup(
    name='alpha_vantage',
    version='0.1.7',
    author='Romel J. Torres',
    author_email='romel.torres@gmail.com',
    license='MIT',
    description='Python module to get stock data from the Alpha Vantage Api',
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
