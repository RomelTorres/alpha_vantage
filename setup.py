from distutils.core import setup

setup(
    name='alpha-vantage',
    version='0.0.1',
    author='R. J. Torres',
    author_email='rtorres@gmail.com',
    license='MIT',
    description='Python module to get stock data from the Alpha Vantage Api',
    long_description=open('README.md').read(),
    install_requires=[
        'simplejson',
        'nose'
    ],
    keywords='stocks market finance alpha-vantage quotes shares currency',
    package_data={
        'alpha-vantage':[],
    }
)
