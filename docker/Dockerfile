FROM python:3.7-alpine

RUN pip3 install slackclient

RUN mkdir /work
COPY py/currency-bot.py /work

WORKDIR "/work"
CMD ["python", "currency-bot.py"]
