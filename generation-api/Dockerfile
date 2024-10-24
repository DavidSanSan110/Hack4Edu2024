FROM python:3.11

RUN mkdir /app

WORKDIR /app

ADD . /app/generation-api

RUN pip install -r ./generation-api/requirements.txt

RUN pip install ./generation-api/ --upgrade

EXPOSE 5000

CMD ["generation_api"]

