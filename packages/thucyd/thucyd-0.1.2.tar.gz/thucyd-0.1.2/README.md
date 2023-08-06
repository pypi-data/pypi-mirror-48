<img src="https://assets.gitlab-static.net/thucyd-dev/thucyd/raw/master/images/thucyd-tile-logo.1500px.png" alt="drawing" height="200"/>


# Eigenanalysis and Filters for Signal Processing
          
[![pipeline status](https://gitlab.com/thucyd-dev/thucyd/badges/master/pipeline.svg)](https://gitlab.com/thucyd-dev/thucyd/pipelines)
[![coverage report](https://gitlab.com/thucyd-dev/thucyd/badges/master/coverage.svg)](https://gitlab.com/thucyd-dev/thucyd/commits/master)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://gitlab.com/thucyd-dev/thucyd/blob/master/LICENSE)
[![pypi version](https://img.shields.io/pypi/v/thucyd.svg)](https://pypi.python.org/pypi/thucyd)
[![python versions](https://img.shields.io/pypi/pyversions/thucyd.svg)](https://pypi.python.org/pypi/thucyd)


## What is `thucyd`?

`thucyd` (thoo'-sid) is an open-source library of Python-centric code that delivers implementations of eigenanalysis and causal filters that are not currently found elsewhere. 

The first subpackage is `eigen`, and within this package a reference implementation of the algorithm for _a consistent basis for eigenanalysis_ is provided. This subpackage is ready. 

Additional subpackages will include `filter_reference` and `filters`, with an expected rolling delivery through 2020.


## Package Installation

The two package hosts for `thucyd` are [PyPi](https://pypi.org/project/thucyd/) and [Conda-Forge](). The packages are identical and the only difference is the means of delivery. From PyPi, use `pip`,

```bash
$ pip install thucyd
```

and from Conda-Forge use `conda`:

```bash
$ conda install -c conda-forge thucyd
```

Once installed, the package is importable to Python:

```python
>>> import thucyd
```

**Note: At this time the conda-forge package is not yet available.**

A quick example call to the `eigen` subpackage would be

```python
>>> import numpy as np
>>> Vor, Eor, signs, _, _ = thucyd.eigen.orient_eigenvectors(np.eye(3).dot(np.diag([1., -1., 1.])), np.diag(np.arange(3)[::-1]))
>>> Vor
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
>>> signs
array([ 1., -1.,  1.])
```


## Package Dependency

The only dependencies `thucyd` has at this time is on [python >= 3.7](https://www.python.org/) and [numpy >= 1.14](https://www.numpy.org/). 


## Why `thucyd`

[Thucydides](https://en.wikipedia.org/wiki/Thucydides) was the first Western writer and historian who applied scientific principles to the recording of Western history. Although Herodotus, who predates Thucydides by less than a generation, started the transformation away from the epic poetry enshrined by Homer to a more objective record, it was Thucydides who engaged in inquiry and cross validation of all accounts in his History of the Peloponnesian Wars.

The `thucyd` package honors the great historian by delivering implementations of eigenanalysis and signal-processing analytics that have been thoroughly researched and validated, and continues the tradition of inquiry by focusing on all the ways that rigorous eigen- and signal-processing theories can be applied to the financial markets and other machine-learning disciplines. 


## Buell Lane Press

[Buell Lane Press](https://buell-lane-press.co) is the package sponsor. 


