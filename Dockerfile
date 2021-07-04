# Pull base image.
FROM python:3.7.10

# For log message in container
ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace/

COPY ./requirements.txt ./workspace/

WORKDIR /workspace/

RUN pip install -r requirements.txt