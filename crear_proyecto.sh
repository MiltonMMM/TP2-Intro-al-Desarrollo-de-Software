#!/bin/bash

mkdir TP2-IDS
cd TP2-IDS

mkdir static/css
mkdir static/images
mkdir templates

touch app.py

python3 -m venv .venv

source .venv/bin/activate
pip install flask
pip install flask-mail