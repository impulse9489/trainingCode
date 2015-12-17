test:
	python -m unittest discover -v
coverage:
	coverage erase
	coverage run -m unittest discover -v
	coverage html