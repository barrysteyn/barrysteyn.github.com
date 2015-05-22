#!/bin/bash

# Python virtualenv
export WORKON_HOME=$HOME/.virtualenvs & export PROJECT_HOME=$HOME/Devel & source /usr/local/bin/virtualenvwrapper.sh
workon python3-pelican
make html
