#!/bin/bash

cd integration_tests
poetry run behave --tags=~@cloud --tags=~@teleport --tags=~@venv $@