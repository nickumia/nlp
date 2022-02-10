from setuptools import setup, find_packages

setup(
    name='nlp',
    version='0.0.1',
    description="Natural Language Processing core",
    long_description="""\
        Provide the three layers of abstraction provided by the PLaN Framework
        for use as a python package.
    """,
    author='nickumia',
    packages=find_packages(include=['nlp', 'nlp.*'])
)
