.PHONY: install clean lint test

test:
	source activate pycgilib && pytest

update:
	conda env update

install:
	conda env create -f environment.yml

publish:
	source activate pycgilib && python setup.py sdist bdist_wheel
	# build result will be in /dist, upload them
