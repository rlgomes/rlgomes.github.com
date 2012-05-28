#!/bin/bash

#OPTS="--nocapture"
#export ENV=prod

# run in headless by default for my testing purposes
export HEADLESS=true

echo "running against firefox"
export BROWSER=Firefox && nosetests --with-freshen -v $OPTS tests

echo "running against google-chrome"
export BROWSER=Chrome && nosetests --with-freshen -v $OPTS tests
