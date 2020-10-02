# FoodVisor Challenges

[![](https://img.shields.io/pypi/v/FoodNetX.svg)]()
[![](https://img.shields.io/pypi/pyversions/FoodNetX.svg)](https://pypi.org/project/FoodNetX/)
[![](https://img.shields.io/pypi/l/FoodNetX.svg)](https://github.com/Jor-G-ete/FoodNetX/blob/master/LICENSE)
[![](https://img.shields.io/github/downloads/Jor-G-ete/FoodNetX/total)]()
[![](https://img.shields.io/github/last-commit/Jor-G-ete/FoodNetx)]()
[![](https://img.shields.io/github/v/release/Jor-G-ete/FoodNetX)]()
[![](https://img.shields.io/github/v/tag/Jor-G-ete/FoodNetx)]()

FoodNetx is a library created using the python package *NetworkX*. It creates a database based in graphs, in concrete a Directed graph, in which could occur cycles. The main idea is cover the challenge of Foodvisor ( [Challenge1](https://github.com/Foodvisor/coding-assignment) and [Challenge2](https://github.com/Foodvisor/home-assignment) ) but any other use is welcomed, please if it used reference this Github and its creator.
Developed under Miniconda3 using virtual enviroments.

The next module corresponding the challenge 2 in which is demanded to build a deep learning model isn't finished, The deep learning model which has been chosen is:

1. One layer with Convolution + ReLU + MaxPooling
2. One layer with Convolution + ReLU + MaxPooling
3. Flattening operation
4. One layer fully connected ( 100 nodes)
5. One layer fully connected (100 nodes)

In the *Config* folder can be seen the **conf_deep1.yaml** used to create the deep learning model with all its parameters already fixed and avoided to be hardcoded. It wasn't implemented due to I didn't know how to select just the boxes in which tomatoes appear. So the project is missing the following topics:

* Input of the images as a batch ( Accomplished introducing one by one but I would like introduce them at once as a zip, tar file, batch, folder)
* Deep learning model, Any suggestion is Welcomed
* Feedback
* Plots, which will be made with matplotlib, once the model and its feedback is built. 

Once the second module is finished it will be moved from python script to a jupyter notebook.

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
python3 ./Tests/FoodVisor_Challenge1_test.py
```

All commands: 
```bash
pip3 install FoodNetX
git clone https://github.com/Jor-G-ete/FoodNetX.git
cd FoodNetX
python3 ./Tests/FoodVisor_Challenge1_test.py
```

If you use an IDE for programming just select the test file desired and just click Run.

### Test's outputs

**FoodVisor_Challenge1_test.py**: 

```python
{"img001": "granularity_staged", "img002": "valid"}
{"img001": "granularity_staged", "img002": "coverage_staged", "img003": "invalid"}
```



##  New modules in development  

By now the foodvisor challenge #2 is being developed and implemented to join this package. 

## Python Compatibility

* [Python](http://www.python.com) - v3.7

### Credits

This library has been created with the help of [Networkx](https://networkx.github.io/mat) , [Matplotlib](https://matplotlib.org/), [Pyyalm](https://github.com/mk-fg/pretty-yaml), [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/) ,[Tensorflow](https://www.tensorflow.org/), [Pillow](https://python-pillow.org/) 

