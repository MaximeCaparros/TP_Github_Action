#!/bin/sh -l

pip install pylint
find . -name '*.py' -exec pylint {} \
