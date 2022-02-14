[![codecov](https://codecov.io/gh/nickumia/nlp/branch/main/graph/badge.svg?token=L79WK92RFM)](https://codecov.io/gh/nickumia/nlp)
[![Tests](https://github.com/nickumia/nlp/actions/workflows/commit.yml/badge.svg)](https://github.com/nickumia/nlp/actions/workflows/commit.yml)


# nlp
Natural Language Processing Core


## Development Environment

### Install Dependencies

(Inside of a python interpreter,) run:
```
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

### Build, Lint, Test
```
make build	# Build the test image
make lint	# Lint python code
make test	# Run all tests

# To run a specific test,
# make test FILE=<file_to_test>
make test FILE=tests/language/test_fuzzy_meaning.py
```
