FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y build-essential python3-pip python3-setuptools python3-dev
    ##&& pip3 install -U pip

RUN pip3 install --upgrade pip

RUN pip3 install -U pip setuptools wheel \
    && pip3 install -U spacy \
    && python3 -m spacy download en_core_web_sm

WORKDIR /src

COPY requirement.txt ./requirement.txt
RUN pip3 install -r requirement.txt

COPY . /src

CMD ["python3", "-u", "app.py"]
