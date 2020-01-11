IPYNB:=$(wildcard *.ipynb)
MD:=$(patsubst %.ipynb,%.md,${IPYNB})
PDF:=$(patsubst %.ipynb,%.pdf,${IPYNB})
HTML:=$(patsubst %.ipynb,%.html,${IPYNB})

README.md: README.ipynb
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

.PHONY: clean.docs
clean.docs:
	rm -rf docs

.PHONY: docs
docs: ${MD} ${PDF}

%.md: %.ipynb
	mkdir -p `dirname ${@}`
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

%.pdf: %.ipynb
	mkdir -p `dirname ${@}`
	-jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to pdf --output=${@} ${<}

%.html: %.ipynb
	mkdir -p `dirname ${@}`
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to html --output=${@} ${<}
