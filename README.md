# localenv


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This file will become your README and also the index of your
documentation.

## Developer Guide

If you are new to using `nbdev` here are some useful pointers to get you
started.

### Install localenv in Development mode

``` sh
# make sure localenv package is installed in development mode
$ pip install -e .

# make changes under nbs/ directory
# ...

# compile to have changes apply to localenv
$ nbdev_prepare
```

## Usage

### Installation

Install latest from the GitHub
[repository](https://github.com/fenke/localenv):

``` sh
$ pip install git+https://github.com/fenke/localenv.git
```

or from [conda](https://anaconda.org/fenke/localenv)

``` sh
$ conda install -c fenke localenv
```

or from [pypi](https://pypi.org/project/localenv/)

``` sh
$ pip install localenv
```

### Documentation

Documentation can be found hosted on this GitHub
[repository](https://github.com/fenke/localenv)’s
[pages](https://fenke.github.io/localenv/). Additionally you can find
package manager specific guidelines on
[conda](https://anaconda.org/fenke/localenv) and
[pypi](https://pypi.org/project/localenv/) respectively.

## How to use

Create a `.env.json` file somewhere on the parent path(s) of you current
working directory, populate it with environment variables organized in
‘sections’ like

``` json
{
    "development": {
        "USR_TOKEN": "super-secret-token",
    },
    "production": {
        "USR_TOKEN": "another-super-secret-token",
    }
}
```

Then import it similar to the following code snippet

``` python
from localenv.envs import production as getenv
```

This loads the set of variables from under the sectionkey ‘production’
in the `.env.json` file and makes them accessible via the `getenv`
function.

``` python
getenv('USR_TOKEN')
```
