from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Simple Calculator Package'
LONG_DESCRIPTION = 'Calculator Package with add, subtract, multiply, divide and take an n root functions'

setup(
    name="Calculator",
    version=VERSION,
    author="Deividas Butkus",
    author_email="<deividas.butkus@mif.stud.vu.lt>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'calculator package'],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
)
