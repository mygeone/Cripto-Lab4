FROM python:3
ADD . /app

WORKDIR /app

ENTRYPOINT [ "python", "main.py" ]

