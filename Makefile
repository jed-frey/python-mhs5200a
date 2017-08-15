# Makefiles make the world go round.

# Install
.PHONY: install
install:
	python setup.py install
	
# Develop.
.PHONY: develop
develop:
	python setup.py develop

# Launch a Jupyter Notebook on all interfaces.
.PHONY: notebook
notebook:
	jupyter notebook --ip="*"

# Run tests.
.PHONY: test
test:
	python setup.py test
	
# Run pytest flake8.
.PHONY: flake8
flake8:
	pytest --flake8
