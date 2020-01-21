# PyECVL

[![Build Status](https://jenkins-master-deephealth-unix01.ing.unimore.it/badge/job/DeepHealth/job/pyecvl/job/master/linux_end?)](https://jenkins-master-deephealth-unix01.ing.unimore.it/job/DeepHealth/job/pyecvl/job/master/)

**PyECVL** is a Python wrapper for [ECVL](https://github.com/deephealthproject/ecvl), the European Computer Vision Library.


## Quick start

The following assumes you have ECVL already installed in "standard"
system paths (e.g., `/usr/local/include`, `/usr/local/lib`).

    git clone --recurse-submodules https://github.com/deephealthproject/pyecvl.git
    cd pyecvl
    python3 -m pip install numpy pybind11 pytest
    python3 setup.py install

See [full installation instructions below](#installation).


## Getting started

```python
import numpy as np
import pyecvl._core.ecvl as ecvl


def inc_brightness(img, rate):
    a = np.array(img, copy=False)
    max_val = np.iinfo(a.dtype).max
    a[a > max_val - rate] = max_val
    a[a <= max_val - rate] += rate


def main():
    img = ecvl.Image()
    ecvl.ImRead("test.jpg", img)
    inc_brightness(img, 10)
    ecvl.ImWrite("test_mod.jpg", img)


if __name__ == "__main__":
    main()
```


## Installation

### Requirements

- Python 3
- ECVL
- NumPy
- pybind11
- pytest (if you want to run the tests)


### ECVL Installation

Complete ECVL installation instructions are available at
https://github.com/deephealthproject/ecvl. Here is a sample build sequence:

```
git clone --recurse-submodules https://github.com/deephealthproject/pyecvl.git
cd third_party/ecvl
mkdir build
cd build
cmake -DECVL_WITH_DICOM=ON -DECVL_WITH_OPENSLIDE=ON -DECVL_DATASET_PARSER=ON -DECVL_BUILD_EDDL=ON ..
make
make install
```


### PyECVL installation

Install PyECVL as follows:

```
python3 -m pip install numpy pybind11 pytest
python3 setup.py install
```

Then, you can test your installation by running the PyECVL tests:

    pytest tests


### ECVL installed in an arbitrary directory

The above installation instructions assume ECVL has been installed in standard
system paths. However, ECVL can be installed in an arbitrary directory,
for instance:

```
cd third_party/ecvl
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/home/myuser/ecvl -DECVL_WITH_DICOM=ON -DECVL_WITH_OPENSLIDE=ON -DECVL_DATASET_PARSER=ON -DECVL_BUILD_EDDL=ON ..
make
make install
```

You can tell the PyECVL setup script about this via the `ECVL_DIR` environment
variable:

```
export ECVL_DIR=/home/myuser/ecvl
python3 setup.py install
```

In this way, `setup.py` will look for additional include files in
`/home/myuser/ecvl/include` and for additional libraries in
`/home/myuser/ecvl/lib`.

Similarly, if EDDL is installed in an arbitrary path, you can tell the setup
script via the `EDDL_DIR` environment variable.
