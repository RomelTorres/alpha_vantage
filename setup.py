from distutils.core import setup

setup(
    name='alpha_vantage',
    version='0.1.4',
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
    package_data={
        'alpha_vantage':[],
    }
)
