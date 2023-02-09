#!/bin/bash

gunicorn template.wsgi:start\(\) \
    -b 0.0.0.0:5000 \
