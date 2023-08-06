import os
from setuptools import setup, find_packages

__version__ = '0.28.2'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASEDIR, 'README.rst')).read()

setup(
    name='ambisafe',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests >= 2.7.0",
        "pyOpenSSL >= 0.15.1",
        "pycryptodome >= 3.4",
        "pycoin == 0.80"
    ],
    url='https://bitbucket.org/ambisafe/client-python',
    download_url='https://bitbucket.org/ambisafe/client-python/get/v{0}.zip'
        .format(__version__),
    author='Anton Simernia',
    author_email='anton.simernia@ambisafe.co',
    keywords=['ambisafe', 'bitcoin'],
    description='Ambisafe KeyServer client library',
    long_description=README,
    classifiers=[
        'Intended Audience :: Developers',
    ],
    test_suite='test.test',
    setup_requires=[
        "flake8",
        "nose>=1.0",
        "coverage",
        "mock"
    ]
)
