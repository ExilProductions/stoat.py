#!/usr/bin/env bash
python3 -m venv .venv

source .venv/bin/activate.fish

pip install --upgrade pip wheel setuptools
pip install -e .