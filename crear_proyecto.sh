#!/bin/bash

mkdir TP2-IDS
cd TP2-IDS

mkdir -p static/css
mkdir -p static/images
mkdir -p templates

touch app.py

export PIPENV_VENV_IN_PROJECT=1
pipenv install flask
pipenv install flask-mail