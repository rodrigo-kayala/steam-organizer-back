#!/bin/bash
gunicorn --bind 0.0.0.0:5000 run:app --workers 9
