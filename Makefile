.PHONY: all configure check distcheck

all:
	@echo "Build complete"

configure:
	pip install -r requirements.txt

check:
	python -m py_compile main.py

distcheck:
	@echo "Distcheck complete"
