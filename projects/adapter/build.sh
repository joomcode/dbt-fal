#!/usr/bin/env bash

set -eo pipefail

poetry config repositories.joom-pypi https://jfrog.joom.it/artifactory/api/pypi/pypi-joom
rm -rf ./dist
poetry build
# joom-jfrog-token get be acquired with `joom login jfrog` (for details look at "joom cli" in notion)
poetry publish -r joom-pypi --username `whoami` --password `cat ~/.joom-jfrog-token`