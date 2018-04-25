# Makefiles make the world go round.

# Config

PIP:=bin/pip
PYTHON:=bin/python
BASE?=setuptools wheel






# Targets

## VirtualEnv for development
.PHONY: venv
venv: ${PYTHON}

${PYTHON}: requirements.txt
	python3 -mvenv .
	${PIP} install --upgrade pip
	${PIP} install --upgrade ${BASE}
	${PIP} install --upgrade -r ${^}


## Install
.PHONY: install
install:
	python setup.py install

## Develop.
.PHONY: develop
develop:
	python setup.py develop

## Launch a Jupyter Notebook on all interfaces.
.PHONY: notebook
notebook:
	jupyter notebook --ip="*"

## Run tests.
.PHONY: test
test:
	python setup.py test

## Run pytest flake8.
.PHONY: flake8
flake8:
	pytest --flake8
