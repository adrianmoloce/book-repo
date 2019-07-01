FROM python:3.7

ENV PYTHONUNBUFFERED 1

COPY . /code

WORKDIR /code

RUN apt-get update && apt-get install -y libicu-dev

RUN pip install -r requirements.txt

ENV DATA_FILE_PATH=data.json

ENTRYPOINT ["python"]

CMD ["app.py"]
