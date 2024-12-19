#!/bin/bash
# setup.sh

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install
