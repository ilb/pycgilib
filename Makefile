.PHONY: bootstrap clean lint test

test:
	conda activate pycgilib && python -m unittest discover

update:
	conda env update

bootstrap:
	conda env create -f environment.yml

publish:
	conda activate pycgilib && python setup.py sdist bdist_wheel
	# build result will be in /dist, upload them
