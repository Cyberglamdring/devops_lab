from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='hw3t2',
    version='1.0',
    author="Hleb Kanonik",
    author_email="hleb_kanonik@epam.com",
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
    include_package_data=True
)
