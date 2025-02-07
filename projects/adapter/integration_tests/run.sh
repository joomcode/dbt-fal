#!/bin/bash

poetry run behave --tags=~@cloud --tags=~@teleport --tags=~@venv $@