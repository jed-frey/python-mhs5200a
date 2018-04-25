# Makefiles make the world go round.

# Config

PIP:=bin/pip
PYTHON:=bin/python
BASE?=setuptools wheel






# Targets
## No default
.DEFAULT: null
.PHONY: null
null:
	@echo No default target.

## VirtualEnv for development
.PHONY: dev
dev: ${PYTHON}

${PYTHON}: requirements.txt requirements-dev.txt
	# Clean the existing environment.
	${MAKE} clean
	# Create new virtual environment.
	python3 -mvenv .
	${PIP} install --upgrade pip
	${PIP} install --upgrade ${BASE}
	${PIP} install --upgrade -r requirements.txt
	${PIP} install --upgrade -r requirements-dev.txt
	${PIP} install --editable .


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

## Cleanup
.PHONY: clean
clean:
	git clean -xfd
