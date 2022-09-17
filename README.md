# AID

* _aid_ (verb): to give assistance
* _aid_ (noun): the act of helping someone

## Install and run using Poetry
Install the application using Poetry:
```
poetry install
```
Run the application:
```
# TODO: Convert project into an application
poetry run python -m ...
```
Run the tests, with the `coverage` plugin:
```
poetry run pytest --cov=aid .
```

## Continuous Integration
TODO: Build and document CI procedures

## Build & distribution

Python [wheels and source distributions](https://realpython.com/python-wheels/) are built using Poetry:
```bash
poetry build
# Expected output
# Building aid (0.1.0)
#   - Building sdist
#   - Built aid-0.1.0.tar.gz
#   - Building wheel
#   - Built aid-0.1.0-py3-none-any.whl
```
