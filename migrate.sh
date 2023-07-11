#!/bin/bash

cd src && FLASK_APP=server.py python -m flask db upgrade
