FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONONBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

EXPOSE 8000
RUN pip install -r requirements.txt

COPY . /code/