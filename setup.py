from setuptools import setup, find_packages
import codecs
import os

# Setting up
setup(
    name="MyPrimeNumber",
    version="1.0.0",
    author="Shakeel Abbas (imam Hussain a.s institute)",
    author_email="<ihi.karachi@gmail.com>",
    description="For Prime Number",
    long_description_content_type="text/markdown",
    long_description="This is a library for finding prime numbers, it has two functions: \n from MyPrimeNumber import isPrimeNumber | from MyPrimeNumber import primeNumberList",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'primenumber', 'math'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
