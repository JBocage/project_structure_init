# Project structure init repository

This repo gives an exemple of how a repo can be nicely initiated

## Before anything else...

- Update the `src/package_name/__init__.py
- Rename the `src/pagkage-name` folder into a proper name
- Update the `./setup.cfg` and `./setup.py` scripts
- ONCE THIS IS DONE: Refactor this `README.md`

## Basic installation directions

### Virtualenv setting

#### Virtual env creation and activation

- `python3 -m venv venv` for initialising the virtual environment
- `source venv/bin/activate` for activating the virtual environment
- `pip install --upgrade pip` for upgrading pip

#### Dependencies install

The following commands shall be ran **after activating the virtual environment**.

- `pip install -r requirements.txt` for the functional dependencies
- `pip install -r requirements-dev.txt` for the development dependencies
- `pip install -e .` for installing locally the current repo
- `pre-commit install` for installing the precommit hook

