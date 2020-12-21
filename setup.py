from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except IOError:
    long_description = 'Python module to get stock data from the Alpha Vantage Api'

setup(
    name='alpha_vantage',
    version='2.3.1',
    author='Romel J. Torres',
    author_email='romel.torres@gmail.com',
    license='MIT',
    description='Python module to get stock data from the Alpha Vantage Api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    url='https://github.com/RomelTorres/alpha_vantage',
    install_requires=[
        'aiohttp',
        'requests'
    ],
    test_requires=[
        'aioresponses',
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
