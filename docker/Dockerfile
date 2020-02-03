FROM python:3.8.1-slim-buster

RUN pip3 install slackclient

RUN mkdir /work
COPY docker/currency-bot.py /work

WORKDIR "/work"
CMD ["python", "currency-bot.py"]
