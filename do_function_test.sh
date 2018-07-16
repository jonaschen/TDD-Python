#!/bin/bash

rm db.sqlite3
python3 manage.py migrate --noinput

./functional_tests.py
