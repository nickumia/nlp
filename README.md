[![codecov](https://codecov.io/gh/nickumia/nlp/branch/main/graph/badge.svg?token=L79WK92RFM)](https://codecov.io/gh/nickumia/nlp)
[![Tests](https://github.com/nickumia/nlp/actions/workflows/commit.yml/badge.svg)](https://github.com/nickumia/nlp/actions/workflows/commit.yml)


# nlp
Natural Language Processing Core

## Structure

All of the code in this repo is categorized into three distinct groups:
1. Processing: The outermost layer of programming. (It includes, but is not limited to, real-world connections, input/output functions to the world, filtering, organizing and other processing functions to normalize input and reinstate output, etc.)
1. Language: The middle layer that gives meaning to the loosely organized data from Processing.  (It includes, but is not limited to, langauge translation, meaning derivation, context creation, language model building, etc.)
1. Natural: The core part of computation that forms information from data.  (It includes, but is not limited to, AI models, connection building algorithms, etc.)

## Features

- Predictive modeling through Chandni ([My Master's Thesis Project](https://kamutiv.com/static/thesis_public_release.pdf))
- (In Progress) Robot Directive Modeling

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
