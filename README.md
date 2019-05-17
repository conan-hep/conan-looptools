[![Build Status Travis](https://travis-ci.org/conan-hep/conan-looptools.svg)](https://travis-ci.org/conan-hep/conan-looptools)

## Conan package recipe for [*LoopTools*](http://www.feynarts.de/looptools/)

T. Hahn, M. Perez-Victoria, *Automatized one loop calculations in
four-dimensions and D-dimensions*,
[*Comput.Phys.Commun.* **118** (1999) 153-165](https://inspirehep.net/record/474106)
[arXiv:hep-ph/9807565](https://arxiv.org/abs/hep-ph/9807565)

## For users

### Installation of dependencies

LoopTools can be installed with conan by running:

    conan install LoopTools/2.15@conan/stable

Alternatively a `conanfile.txt` file can be created in your project
directory with the following content:

    [requires]
    LoopTools/2.15@conan/stable

    [generators]
    cmake
    make
    pkg_config

The dependencies of your project are then installed by running:

    mkdir build
    cd build
    conan install ..

### Building your project

Afterwards the project can be configured via CMake and build with
`make` by running:

    cmake ..
    make

Alternatively the project can be configured with Meson and build with
`ninja` by running:

    export PKG_CONFIG_PATH=.
    meson ..
    ninja

Alternatively the project can be build with `make` by running:

    make -f ../Makefile

A complete example can be found in the `examples/` directory.


## Build and package

The following command both runs all the steps of the conan file, and
publishes the package to the local system cache.  This includes
downloading dependencies from "build_requires" and "requires" , and
then running the build() method.

    $ conan create . conan/stable


### Available Options

| Option        | Default          | Possible Values                          |
| ------------- |------------------|------------------------------------------|
| fPIC          | True             |  [True, False]                           |


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this
recipe, which can be used to build and package LoopTools.  It does *not* in
any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
