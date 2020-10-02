# FoodVisor Challenges

[![](https://img.shields.io/pypi/v/FoodNetX.svg)]()
[![](https://img.shields.io/pypi/pyversions/FoodNetX.svg)](https://pypi.org/project/FoodNetX/)
[![](https://img.shields.io/pypi/l/FoodNetX.svg)](https://github.com/Jor-G-ete/FoodNetX/blob/master/LICENSE)
[![](https://img.shields.io/github/downloads/Jor-G-ete/FoodNetX/total)]()
[![](https://img.shields.io/github/last-commit/Jor-G-ete/FoodNetx)]()
[![](https://img.shields.io/github/v/release/Jor-G-ete/FoodNetX)]()
[![](https://img.shields.io/github/v/tag/Jor-G-ete/FoodNetx)]()

**CHECK DEVELOP BRANCH FOR LATEST CHANGES AND UPGRADES**

FoodNetx is a library created using the python package *NetworkX*. It creates a database based in graphs, in concrete a Directed graph, in which could occur cycles. The main idea is cover the challenge of Foodvisor ( [Challenge1](https://github.com/Foodvisor/coding-assignment) and [Challenge2](https://github.com/Foodvisor/home-assignment) ) but any other use is welcomed, please if it used reference this Github and its creator.

## Installation

### Source file

1. Download the source file from github
2. Unzip and navigate to the folder containing `setup.py` and other files
3. Run the following command: `python setup.py install`

### Pip

```python3
    pip3 install FoodNetX
```

## Testing and replicating the results for the Foodvisor challenges

Download and install the python package *FoodNetx*, then clone the repo.
In the Github repository has been left a folder called *Test*, where tests are stored.
To execute any test, just use the following shell command from inside the github repo:

```shell
python3 ./Test/TestFile.py
```

Example:

```bash
python3 ./Test/FoodVisor_Challenge1_test.py
```

If you use an IDE for programming just select the test file desired and just click Run.

### Test's outputs

**FoodVisor_Challenge1_test.py**: 

```python
{"img001": "granularity_staged", "img002": "valid"}
{"img001": "granularity_staged", "img002": "coverage_staged", "img003": "invalid"}
```



##  New modules in development  

By now the foodvisor challenge #2 is being developed and implemented to join this package at the end of this week

## Python Compatibility

* [Python](http://www.python.com) - v3.7

### Note

This library has been created with the help of [Networkx](https://networkx.github.io/mat) and [Matplotlib](https://matplotlib.org/)

### 
