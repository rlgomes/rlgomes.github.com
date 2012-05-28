#!/bin/bash

#OPTS="--nocapture"

echo "running against firefox"
export BROWSER=Firefox && nosetests --with-freshen -v $OPTS tests

echo "running against google-chrome"
export BROWSER=Chrome && nosetests --with-freshen -v $OPTS tests
