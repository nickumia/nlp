
build:
	docker build -t dac .

lint:
	docker run --rm -v "$(shell pwd)":/app dac:latest bash -c "cd /app && flake8 . --count --show-source --statistics"

# test:
# 	docker run --rm -v "$(shell pwd)":/app dac:latest bash -c "/app/test.sh "
