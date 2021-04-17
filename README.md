[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/dilbwagsingh/DESfiddle)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/DESfiddle)](https://github.com/dilbwagsingh/DESfiddle)
[![PyPI version](https://badge.fury.io/py/DESfiddle.svg)](https://badge.fury.io/py/DESfiddle)
[![PyPI status](https://img.shields.io/pypi/status/DESfiddle)](https://pypi.python.org/pypi/DESfiddle/)
[![GitTutorial](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)](https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project)
[![Downloads](https://static.pepy.tech/personalized-badge/desfiddle?period=total&units=abbreviation&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/desfiddle)

# DESfiddle

A simple to use python package for implementing and experimenting with the famous DES encryption algorithm. It implements both classical (default settings from the textbook description of DES) and non-classical DES. 
Check out [DES app]() for a very specific implementation demonstrating avalanche effect and weak keys using the package.
> **Note**: This project is currently an unstable release. To report any instabilities or issues please refer to the contribution section.

## Motivation

There are quite a few DES packages for python but none of them offer such high flexibility to implement a non-classical version of the DES. This package is aimed specifically to experiment with the different hyperparamters that can be tweaked while implementing DES. 

## Features

* Only package till date to implement a non-classical version of DES.
* Lots of hyperparameters<sub><sup>*</sup></sub> to tweak-
	* Number of rounds
	* Halfwidth for plaintext & key
	* Hamming distance for plaintext & key
	* Permutation boxes (Initial, Final & Inverse)
	* Shift arrays
	* S-boxes
	* Expansion box
* Implementing classical DES is as easy as leaving the hyperparameters to their default values and the rest will be taken care of automatically.
* Each function has a detailed doc string attached to it, thus minimising the need to navigate to the docs for usage referencing. So, if you quickly wanna see the function description just type in `help(<function_name>)` in the python interpreter.

> **Bonus**: This package can be a life-saver for CSE 537- Network Security course taught at IIT (BHU).

<sub><sup>*Tweaking some of these may require changing the source code as of the current release</sup></sub>


## Installation

Run the following command in your terminal/command prompt-
```bash:
$ pip install DESfiddle
```
> **Note**: If you dont have `pip` installed, follow these [steps](https://pip.pypa.io/en/stable/installing/).

## Importing and Usage

```python:
# Importing
import DESfiddle.utils as dfu

# Usage
permutation_arr = dfu.generate_permutation(64)
```
```python:
# Importing
from DESfiddle.utils import *
# or just specify the function name you wanna import

# Usage
permutation_arr = generate_permutation(64)
```

## Code Examples
```python:
from DESfiddle.utils import *

# Inputs in binary setting
plaintext = "0101010101010101010101010101010101010101010101010101010101010101"
key = "1111111111111111111111111111111100000000000000000000000000000000"

# Settings
nor = 16
halfwidth = 32
hamming_dist = 1

# Hamming the plaintext in binary mode
ref_pt_arr = preprocess_plaintext(plaintext, halfwidth)
pt_arr = preprocess_plaintext(plaintext, halfwidth, hamming_dist)
key = preprocess_key(key, halfwidth)
rkb,rkh = generate_round_keys(key,nor, halfwidth)
ref_ciphertext, ref_round_ciphertexts = encrypt(ref_pt_arr, rkb, nor, halfwidth)
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)

# Hamming the key in binary mode
pt_arr = preprocess_plaintext(plaintext, halfwidth)
ref_key = preprocess_key(key,halfwidth)
key = preprocess_key(key, halfwidth, hamming_dist)
ref_rkb, ref_rkh = generate_round_keys(ref_key, nor, halfwidth)
rkb,_ = generate_round_keys(key, nor, halfwidth)
ref_ciphertext, ref_round_ciphertexts = encrypt(pt_arr, ref_rkb, nor, halfwidth)
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)
```

```python:
from DESfiddle.utils import *

# Inputs in ASCII setting
plaintext = "This is so cool"
key = "Yesss"

# Settings
nor = 16
halfwidth = 32
hamming_dist = 1

# Preprocessing when input in ASCII
plaintext = txt_to_hex(plaintext)
plaintext = hex_to_bin(plaintext)
key = txt_to_hex(key)
key = hex_to_bin(key)

# Hamming the plaintext in binary mode
ref_pt_arr = preprocess_plaintext(plaintext, halfwidth)
pt_arr = preprocess_plaintext(plaintext, halfwidth, hamming_dist)
key = preprocess_key(key, halfwidth)
rkb,rkh = generate_round_keys(key,nor, halfwidth)
ref_ciphertext, ref_round_ciphertexts = encrypt(ref_pt_arr, rkb, nor, halfwidth)
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)

# Hamming the key in binary mode
pt_arr = preprocess_plaintext(plaintext, halfwidth)
ref_key = preprocess_key(key,halfwidth)
key = preprocess_key(key, halfwidth, hamming_dist)
ref_rkb, ref_rkh = generate_round_keys(ref_key, nor, halfwidth)
rkb,_ = generate_round_keys(key, nor, halfwidth)
ref_ciphertext, ref_round_ciphertexts = encrypt(pt_arr, ref_rkb, nor, halfwidth)
_, round_ciphertexts = encrypt(pt_arr, rkb, nor, halfwidth)
diff = calc_diff(ref_round_ciphertexts, round_ciphertexts)
```

## Contributing Guidelines

Thanks for taking the time to contribute!

The following is a set of guidelines for contributing to DESfiddle. These are just guidelines, not rules, so use your best judgement and feel free to propose changes to this document in a pull request.

### Getting Started
DESfiddle is built over python. So if you are new to python, please head over to [this](https://www.python.org/) great website.

### Community

* The whole DESfiddle documentation, such as setting up a development environment, the project, and testing, can be read [here]().
* If you have any questions regarding DESfiddle, open an [issue](https://github.com/dilbwagsingh/DESfiddle/issues/new) or ask it directly on [Linkedin](https://www.linkedin.com/in/dilbwagsingh/).

### Issue
Ensure the bug was not already reported by searching on GitHub under [issues](https://github.com/dilbwagsingh/DESfiddle/issues). If you're unable to find an open issue addressing the bug, open a [new issue](https://github.com/dilbwagsingh/DESfiddle/issues/new).

### Write detailed  information
Detailed information is very helpful to understand an issue, for example-
* How to reproduce the issue, step-by-step.
* The expected behavior (or what is wrong).
* Screenshots for GUI issues.
* The application version.
* The operating system.
* The DESfiddle version.

### Pull requests
Pull Requests are always welcome.
* When you edit the code, please run  `python -m unittest`  to test your code before you  `git commit`.
* Ensure the PR description clearly describes the problem and solution. It should include-
	*	The operating system used while testing
	*	DESfiddle version number
	*	The relevant issue number, if applicable.
