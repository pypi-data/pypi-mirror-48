[![Build status](https://robertoprevato.visualstudio.com/rocore/_apis/build/status/rocore-CI)](https://robertoprevato.visualstudio.com/rocore/_build/latest?definitionId=13) [![pypi](https://img.shields.io/pypi/v/rocore.svg?color=blue)](https://pypi.org/project/rocore/) [![Test coverage](https://img.shields.io/azure-devops/coverage/robertoprevato/rocore/13.svg)](https://robertoprevato.visualstudio.com/rocore/_build?definitionId=13)

# Core classes and functions, reusable in any kind of Python application

**Features:**
* [exception classes to express common scenarios](https://github.com/RobertoPrevato/rocore/wiki/Common-exceptions)
* [implementation of models annotations, useful to implement validation of business objects](https://github.com/RobertoPrevato/rocore/wiki/Models-annotations)
* [friendly JSON encoder](https://github.com/RobertoPrevato/rocore/wiki/User-friendly-JSON-dumps), handling `datetime`, `date`, `time`, `UUID`, `bytes`
* [implementation of simple in-memory cache, supporting expiration of items and capped lists](https://github.com/RobertoPrevato/rocore/wiki/Caching)
* utilities to work with `folders` and paths
* [`StopWatch` implementation](https://github.com/RobertoPrevato/rocore/wiki/StopWatch-implementation)
* [a base class to handle classes that can be instantiated from configuration dictionaries](https://github.com/RobertoPrevato/rocore/wiki/Registry)
* [common decorator to support retries](https://github.com/RobertoPrevato/rocore/wiki/Retry-decorator)
* [common decorator to support logging function calls](https://github.com/RobertoPrevato/rocore/wiki/Logs-decorator)
* [common decorator to control raised exceptions](https://github.com/RobertoPrevato/rocore/wiki/Exception-handle-decorator)

## Installation

```bash
pip install rocore
```

## Documentation
Please refer to documentation in the project wiki: [https://github.com/RobertoPrevato/rocore/wiki](https://github.com/RobertoPrevato/rocore/wiki).

## Develop and run tests locally
```bash
pip install -r requirements.txt

# run tests using automatic discovery:
pytest

# with code coverage:
make testcov
```
