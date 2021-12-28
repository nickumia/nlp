
build:
	docker build -t dac .

lint:
	docker run --rm -v "$(shell pwd)":/app dac:latest bash -c "cd /app && flake8 . --count --show-source --statistics"

test:
	docker run --rm -v "$(shell pwd)":/app dac:latest bash -c "cd /app && coverage run -m pytest --disable-pytest-warnings && coverage report --omit=\"tests/*\""

test-cov:
	docker run --rm -v "$(shell pwd)":/app dac:latest bash -c "cd /app && coverage run -m pytest --disable-pytest-warnings && coverage xml --omit=\"tests/*\""
