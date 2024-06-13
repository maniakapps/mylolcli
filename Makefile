# Makefile

.PHONY: clean

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

# Optionally, you can define other targets for building, testing, etc.
build:
	python setup.py sdist bdist_wheel

install:
	pip install .

uninstall:
	pip uninstall mylolcli

test:
	pytest
