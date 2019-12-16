IPYNB:=$(wildcard *.ipynb)
MD:=$(patsubst %.ipynb,markdown/%.md,${IPYNB})
PDF:=$(patsubst %.ipynb,markdown/%.md,${IPYNB})
HTML:=$(patsubst %.ipynb,html/%.html,${IPYNB})
PY:=$(patsubst %.ipynb,python/%.py,${IPYNB})

.PHONY: debug
debug:
	$(info $${IPYNB}=${IPYNB})
	$(info $${MD}=${MD})

.PHONY: markdowns
markdowns: ${MD}
.PHONY: pdfs
pdfs: ${PDF}
.PHONY: html
html: ${HTML}
.PHONY: py
py: ${PY}

folders:	
	mkdir -p markdown pdf html python
	
markdown/%.md: %.ipynb folders
	jupyter-nbconvert --to markdown --output=${@} ${<}

pdf/%.pdf: %.ipynb folders
	jupyter-nbconvert --to pdf --output=${@} ${<}

html/%.html: %.ipynb folders
	jupyter-nbconvert --to html --output=${@} ${<}

python/%.py: %.ipynb folders
	jupyter-nbconvert --to python --output=${@} ${<}

clean: 
	echo $Clean!

.PHONY: git-clean
git-clean:
	git clean -xfdn
