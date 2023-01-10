from python:3
workdir /app
run pip install pdm
run pdm init --python /usr/local/bin/python -n
copy . .
cmd ["pdm", "run ./src/main/main.py" ]
