FROM python:3.13.8-bookworm

ADD . /mars-probe-api

WORKDIR /mars-probe-api

RUN pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh

EXPOSE 9900

ENTRYPOINT ["./entrypoint.sh"]