
define NLTK_SETUP_TEST :=
python -c "import nltk; nltk.download('punkt')"
python -c "import nltk; nltk.download('averaged_perceptron_tagger')"
coverage run --source=nlp,examples -m pytest --disable-pytest-warnings $(FILE) && coverage xml
endef


build:
	docker build -t nlp:dev .

lint:
	docker run --rm -v "$(shell pwd)":/pac nlp:dev bash -c "cd /pac && flake8 . --count --show-source --statistics"

test:
	docker run --rm \
		-v "$(shell pwd)":/pac \
		-v "$(shell echo ${HOME})"/nltk_data:/root/nltk_data \
		-v "$(shell echo ${HOME})"/.aws:/root/.aws \
		nlp:dev bash -c "coverage run --source=nlp,examples -m pytest --disable-pytest-warnings $(FILE) && coverage report --omit=\"tests/*\""

export NLTK_SETUP_TEST
test-cov:
	docker run --rm \
		-v "$(shell pwd)":/pac \
		-v "$(shell echo ${HOME})"/.aws:/root/.aws \
		nlp:dev bash -c "$$NLTK_SETUP_TEST"

robot:
	docker run -ti --rm \
		-v "$(shell pwd)":/pac \
		-v "$(shell echo ${HOME})"/nltk_data:/root/nltk_data \
		-v "$(shell echo ${HOME})"/.aws:/root/.aws \
		nlp:dev bash -c "python examples/locomotion/test_model.py"
