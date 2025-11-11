# Makefile
run:
	poetry run ascii-pres ./data/demo

test:
	poetry run pytest

fmt: 
	poetry run black src tests