# eml2png
[![Build Status](https://travis-ci.com/poipoii/eml2png.svg?branch=master)](https://travis-ci.com/poipoii/eml2png)
[![Coverage Status](https://coveralls.io/repos/github/poipoii/eml2png/badge.svg?branch=master)](https://coveralls.io/github/poipoii/eml2png?branch=master)
[![Documentation Status](https://readthedocs.org/projects/eml2png/badge/?version=latest)](https://eml2png.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/eml2png.svg)](https://badge.fury.io/py/eml2png)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/poipoii/eml2png.svg?style=flat)](https://hub.docker.com/r/poipoii/eml2png)

Paint the EML to a single PNG image.


## Installing

You'll need [wkhtmltopdf](http://wkhtmltopdf.org/) before you start working with eml2png, so install them first:

* Debian/Ubuntu:

``` bash
sudo apt-get install wkhtmltopdf
```

* MacOSX

``` bash
brew install wkhtmltopdf
```

* Windows and other options: check [wkhtmltopdf homepage](http://wkhtmltopdf.org/) for binary installers or [wiki page](https://github.com/pdfkit/pdfkit/wiki/Installing-WKHTMLTOPDF).


Install eml2png:

``` python
pip install eml2png
```

## Usage

Simple example:

``` python
import eml2png

with open('message.png', 'wb') as f:
    f.write(eml2png.to_png('message.eml'))
```

