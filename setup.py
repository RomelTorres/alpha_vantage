from distutils.core import setup

setup(
    name='alpha_vantage',
    version='0.1.2',
    author='R. J. Torres',
    author_email='rtorres@gmail.com',
    license='MIT',
    description='Python module to get stock data from the Alpha Vantage Api',
    long_description=open('README.md').read(),
    install_requires=[
        'simplejson',
        'pandas',
        'nose'
    ],
    keywords='stocks market finance alpha_vantage quotes shares currency',
    package_data={
        'alpha_vantage':[],
    }
)
