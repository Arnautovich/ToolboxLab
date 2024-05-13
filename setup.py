from setuptools import setup

def readme(): 
    with open ('README.md') as f:
        return f.read()


VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

setup(
    name="Toolbox",
    version="0.0.1",
    author="Nicolas Jenni, Bruno Gonçalves, Arnau Casalprim",
    author_email="nicolas.jenni@epfl.ch, bruno.gonclavesoliveira@epfl.ch, arnau.casalprimperez@epfl.ch",
    description="Toolbox package",
    long_description=readme(),
    packages=[ "Toolbox"],
    license="MIT",
    keywords=['python', 'Toolbox'],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Arnautovich/Toolbox.git"
)
        