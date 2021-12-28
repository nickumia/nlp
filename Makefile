
build:
	docker build -t nlp:dev .

lint:
	docker run --rm -v "$(shell pwd)":/pac nlp:dev bash -c "cd /pac && flake8 . --count --show-source --statistics"

test:
	docker run --rm -v "$(shell pwd)":/pac nlp:dev bash -c "coverage run --source=nlp -m pytest --disable-pytest-warnings && coverage report --omit=\"tests/*\""

test-cov:
	docker run --rm -v "$(shell pwd)":/pac nlp:dev bash -c "coverage run --source=nlp -m pytest --disable-pytest-warnings && coverage xml"
