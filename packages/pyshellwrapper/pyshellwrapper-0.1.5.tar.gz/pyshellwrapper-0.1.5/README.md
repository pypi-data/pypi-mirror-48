# python-shell-cmd-wrapper
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/matejMitas/python-shell-cmd-wrapper/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/pyshellwrapper.svg)](https://badge.fury.io/py/pyshellwrapper)
[![Build Status](https://travis-ci.com/matejMitas/python-shell-cmd-wrapper.svg?branch=master)](https://travis-ci.com/matejMitas/python-shell-cmd-wrapper)


Based on one of the parts of my bachelor thesis testing framework. Enables to call shell programs seamlessly within Python workflow. Derived from my [bachelor thesis](https://github.com/matejMitas/VUT_FIT-bakalarka).

Motivation
------------
Whilst working with not very widespread libraries/commands one might struggle using them without proper Python wrapper. Oftentimes nothing fancy is really required, simple abstraction layer is all that is needed. I encountered this very problem in my bachelor thesis when trying to automate image compression pipeline (JPEG2000) using various libraries. This package builds abstraction layer over base set of libraries, at the same time enabling users to easily add new ones.

Installation
------------
```
pip install pyshellwrapper
```
Requires Python `>=3.7`.

Introductory Notes
------------
- Typical CLI use certain naming convension for prompt values.

    ```
    wget google.com -o log.txt
    ```
    `wget` is a command, `google.com` is a parameter and `-o` is switch/flag. In this package, everything is considered to be a flag.

- Every library is controlled by a special type of `json` document called `blueprint`. There, each flag is described and is used as foundation for flag transformation. Structure is going to discussed later.  
- There are three type of flags: `fixed`, `variable`, `auxiliary`. Fixed flags are constant throughout program cycle (input file or logging), variable are meant to be changed (output file or color profile) and auxiliary are simple appended at the end without any transformation. Program cycle is denoted by calling `construct()` method; it can also be tweaked, more on that later. Default behavior is to call `set_fixed()` once since all flags are directly transformed to output format. However it is possible to call `set_fixed` multiple times in program cycle if each flag is set only once, otherwise `ValueError` is raised. Variable flags are set by `set_variable()` in the same manner or list/tuple can be used to specify all options from one place.   

Blueprint
------------------
Used for describing flags/parameters of a command. Each blueprint has two mandatory items: `settings` and `flags`. 
```json
{
    "settings": {
        "required_flags": [
            "input", "output"
        ],
        "libraries"     : [
            "kdu_compress", "opj_compress"
        ]
    }
}
```
Here is a typical `settings` portion of a blueprint. First are `required_flags`. Most of the programs have at least one so it is logical to require specification to avoid unnecessary error at execution. `libraries` are used for distinguishing between multiple libraries in single blueprint. This is optional and only required for multiple libraries.

```json
{
    "flags": {
        "input": [
            {
                "flag"      : "-i",
                "unifier"   : null,
                "format"    : {
                    "number" : 1,
                    "preset": "1"

                }
            },
            {
                "flag"      : "-i",
                "unifier"   : null,
                "format"    : {
                    "number" : 1,
                    "preset": "1"
                }
            }
        ],
    }
}
```
Individual `flags` have following structure. Flag name can by selected at user's will; semantic meaning is advised to be preserved. Its value is array for multiple options, this structure is unchanged not matter how many libraries is there to maintain consistency. This example would take `input="path/to/file"` and transform it to `-i /path/to/file`. Sometimes naming of a flag is not needed. If further manipulation of given flag is desired (variable) set `"flag": null`, otherwise use `set_auxiliary()`. Flag can have parameters that are paired by location (directly follows) `-flag param` or by certain unifier `-flag=param`. Format specifies flag parameter; `count` is used for transformation purposes, `preset` are predefined format for user convenience.


| Preset | Input | Transformed |
| --- | --- | --- |
| 1 | input="input.txt" | -i input.txt |
| 2, | point=(20,45) | --point 20,45 |
| [2,] | point=(20,45) | --point [20,45] |
| (2,) | point=(20,45) | --point (20,45) |
| {2,} | point=(20,45) | --point {20,45} |

User defined formats presets are comming in next version (`0.2`).

### Number vs. List
Distinction might be unclear. `number` is a number of parameter's parts that constitute compoment. Input file always has one part (file name), point in 2D space have 2 `x,y` and so on. Parameter can consist of multiple compoment, e.g. start points for a game  <br>`--points=[0,0],[50,20],[880,50]`. Therefore `list` is a list of components that are composed of parts (with given number). 

```json
{
    "points": [
        {
            "flag"      : "--points",
            "unifier"   : "=",
            "format"    : {
                "number" : 2,
                "preset": "[2,]"
            },
            "list": {
                "divider": ","
            }
        }
    ]
}
```
Example of `points` flag. Please note `list` are to be fully supported in version (`0.3`)



<!---
Routine
------------------
More advanced way of controlling generation of command variants.
```json
{
    "routines": [
        {
            "variable_flags" : [
                {
                    "flag" : "resize",
                    "opts" : [10, 20, 50, 70, 90]
                }
            ],
            "fixed_flags"   : {
                "colorspace": "rgb"
            }
        }
    ]
}
```
--->

Basic usage
------------------
Let us look onto basic usage with predefined library (`wget`). `PyShellWrapper` is main class of package wrapping functionality. `blueprint` are built-in blueprints (user defined comming in version `0.2`.

```python

from pyshellwrapper.wrapper import PyShellWrapper

wrapper = PyShellWrapper(
    blueprint='wget' 
)
```