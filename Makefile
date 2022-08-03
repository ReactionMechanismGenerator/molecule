################################################################################
#
#   Makefile for RMG Py
#
################################################################################

.PHONY : all minimal main solver check pycheck arkane clean install decython documentation mopac_travis

all: pycheck main solver check

minimal:
	python setup.py build_ext minimal --inplace --build-temp .

main:
	python setup.py build_ext main --inplace --build-temp .

check:
	@ python utilities.py check-dependencies

pycheck:
	@ python utilities.py check-python

documentation:
	$(MAKE) -C documentation html
	@ echo "Start at: documentation/build/html/index.html"

clean:
	@ python utilities.py clean

install:
	python setup.py install

test-all:
ifneq ($(OS),Windows_NT)
	mkdir -p testing/coverage
	rm -rf testing/coverage/*
endif
	nosetests --nocapture --nologcapture --all-modules --verbose --with-coverage --cover-inclusive --cover-erase --cover-html --cover-html-dir=testing/coverage --exe molecule

test test-unittests:
ifneq ($(OS),Windows_NT)
	mkdir -p testing/coverage
	rm -rf testing/coverage/*
endif
	nosetests --nocapture --nologcapture --all-modules -A 'not functional' --verbose --with-coverage --cover-inclusive --cover-erase --cover-html --cover-html-dir=testing/coverage --exe molecule
