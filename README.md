#TODO:

Informational Badges:

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/roa_collector)](https://pypi.org/project/roa_collector/)
![Tests](https://github.com/jiminput/cse3150_jimmy_padilla_calculator/actions/workflows/tests.yml/badge.svg)
![Linux](https://img.shields.io/badge/os-Linux-blue.svg)
![macOS Intel](https://img.shields.io/badge/os-macOS_Intel-lightgrey.svg)
![macOS ARM](https://img.shields.io/badge/os-macOS_ARM-lightgrey.svg)

Some Linting Badges (Where I could find them):

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2A6DBA.svg)](http://mypy-lang.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint/tree/main)
[![try/except style: tryceratops](https://img.shields.io/badge/try%2Fexcept%20style-tryceratops%20%F0%9F%A6%96%E2%9C%A8-black)](https://github.com/guilatrova/tryceratops)

# cse3150\_jimmy\_padilla\_calculator


### This is my repo for a example python/C++ package.

* [Description](#package-description)
* [Usage](#usage)
* [Installation](#installation)
* [Testing](#testing)
* [Development/Contributing](#developmentcontributing)
* [Licence](#license)

## Package Description

## Usage
* [cse3150\_jimmy\_padilla\_calculator](#cse3150\_jimmy\_padilla\_calculator)

from a script:

```python
from pathlib import Path

from cse3150_jimmy_padilla_calculator import Calculator
from cse3150_jimmy_padilla_calculator import FileCalculator

csv_path = Path("/tmp/my_csv_path.csv")  # or set to None to avoid writing

sum = Calculator().add(1,2)
diff = Calculator().sub(4,1)
prod = Calculator().mul(3,3)
div = Calculator().div(9,2)

large_sum = FileCalculator().sum_file(csv_path)
```

## Installation
* [cse3150\_jimmy\_padilla\_calculator](#cse3150\_jimmy\_padilla\_calculator)

Install python and pip if you have not already.

Then run:

```bash
pip3 install pip --upgrade
```

For production:

```bash
pip3 install cse3150_jimmy_padilla_calculator
```

This will install the package and all of it's python dependencies.

If you want to install the project for development:
```bash
git clone https://github.com/jiminput/cse3150_jimmy_padilla_calculator.git
cd cse3150_jimmy_padilla_calculator
pip3 install -e .[test]
pre-commit install
```

To test the development package: [Testing](#testing)


## Testing
* [cse3150\_jimmy\_padilla\_calculator](#cse3150\_jimmy\_padilla\_calculator)

To test the package after installation:

```
cd cse3150_jimmy_padilla_calculator
pytest cse3150_jimmy_padilla_calculator
ruff check cse3150_jimmy_padilla_calculator
ruff format cse3150_jimmy_padilla_calculator
mypy cse3150_jimmy_padilla_calculator
```

If you want to run it across multiple environments (it only works for python 3.12 right now)

```
cd cse3150_jimmy_padilla_calculator
tox --skip-missing-interpreters
```


## Development/Contributing
* [cse3150\_jimmy\_padilla\_calculator](#cse3150\_jimmy\_padilla\_calculator)

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Test it
5. Run tox
6. Commit your changes: `git commit -am 'Add some feature'`
7. Push to the branch: `git push origin my-new-feature`
8. Ensure github actions are passing tests
9. Email me at oJimmy05o@gmail.com if it's been a while and I haven't seen it

## License
* [cse3150\_jimmy\_padilla\_calculator](#cse3150\_jimmy\_padilla\_calculator)

MIT License (see license file)
