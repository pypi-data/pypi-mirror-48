<a name="top"></a>
[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)
<a href="https://www.instagram.com/alka1e"><img src="https://i.imgur.com/G9YJUZI.png" alt="Instagram" align="right"></a>
<a href="https://twitter.com/alka1e"><img src="http://i.imgur.com/tXSoThF.png" alt="Twitter" align="right"></a>
<a href="https://www.facebook.com/justinekizhak"><img src="http://i.imgur.com/P3YfQoD.png" alt="Facebook" align="right"></a>
<br>

- - -

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<!-- {Put your badges here} -->

- - -

# `LSG => ls | grep` <!-- omit in toc -->

## Table of contents <!-- omit in toc -->

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Full Documentation](#full-documentation)
- [License](#license)

## Introduction

This project started as a shell script for `ls | grep` to check if a folder contains the file which I am looking for.

I tried using `find` and other unix-like tools, but either they were too complicated to use or the results were not what I wanted.

The package doesn't aim to revolutionize the way you do your `ls` or anything else. Its just a better substitution to bash script.

**[Back to top](#table-of-contents)**

## Features

- Search for multiple files and folders.
- Specify a path to search or it will search within current directory.
- Print total number of results.
- Case insensitive substring search.
- Results are displayed in separate categories.
- OS agnostic

**[Back to top](#table-of-contents)**

## Getting Started

### Installation

`pip install lsg`

### Usage

`lsg FILENAME`

- Search for `.py` files in current directory.

    ``` bash
    $ lsg .py
    ----------Total number of entries----------> 1
    ----------Files----------------------------> 1
    setup.py
    ```

- Search for `.py` files in `lsg` directory.

    ``` bash
    $ lsg .py -p lsg
    ----------Total number of entries----------> 2
    ----------Files----------------------------> 2
    __init__.py
    main.py
    ```

**[Back to top](#table-of-contents)**

## Full Documentation

For more help run `lsg -h` or `lsg --help` on terminal.

``` bash
$ lsg -h
usage: lsg [-h] [--path PATH] FILENAME [FILENAME ...]

Check if a specific file or folder exists in current or in a specified
directory

positional arguments:
  FILENAME              name of file or folder to search

optional arguments:
  -h, --help            show this help message and exit
  --path PATH, -p PATH  path to search (default: current directory)
```

Any feature requests, bugs etc feel free to create an issue on [Gitlab][website].

Read [CHANGELOG], [CODE OF CONDUCT], [CONTRIBUTING] guide.

[website]: https://gitlab.com/justinekizhak/lsg
[CHANGELOG]: CHANGELOG.md
[CODE OF CONDUCT]: CODE_OF_CONDUCT.md
[CONTRIBUTING]: CONTRIBUTING.md

## License

[MIT License]

Copyright (c) 2019 Justine Thomas Kizhakkinedath

[MIT License]: LICENSE.txt

**[Back to top](#table-of-contents)**

- - -

[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/contains-cat-gifs.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-watergate.svg)](https://forthebadge.com)

- - -
