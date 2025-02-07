# If you use incompatible version of python, install 3.10:
```bash
# deps
sudo apt update && sudo apt install -y \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev \
    curl git llvm libncursesw5-dev xz-utils tk-dev \
    libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

```bash
# pyenv
curl https://pyenv.run | bash
```

```bash
# settings
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc 
```

```bash
# install pyenv
pyenv install 3.10
```

```bash
# from project dir
cd dbt-fal/projects/adapter
pyenv local 3.10
```

# Install deps
```bash
# from project dir
cd dbt-fal/projects/adapter
poetry config virtualenvs.in-project true  # this will create local .venv dir to use in PyCharm
poetry env use 3.10
poetry lock 
poetry install --with dev
poetry install --extras postgres
poetry install --extras spark
```

# Run unit tests
```bash
# from project dir
cd dbt-fal/projects/adapter
./run_tests_env.sh
poetry run pytest tests  # if you run from PyCharm it adds "tests" dir to eorking dir and breaks path, need to be fixed
```

# Run integration tests
```bash
# from dir with integration tests
cd dbt-fal/projects/adapter/integration_tests
./run.sh  # some tests for functionality we are not going to support are skipped 
```

# Configure PyCharm
## Venv
- Go to Settings -> Project -> Project interpreter
- Add Interpreter -> Add Local -> Check "From existing"
- Path to Interpreter: dnt-fal/projects/adapter/.venv/bin/python

## Tests
- Right click on dbt-fal/projects/adapter/tests
- "Run pytest in tests"
- Get the "mock does not exist" error
- In "Running configurations" (top-right corner),  select pytest -> more actions -> edit
- In working dir drop `tests` dir from the end of path
