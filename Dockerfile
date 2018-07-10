FROM jupyter/scipy-notebook:latest
LABEL maintainer="kacper.lukawski@codete.com>"

RUN pip install nltk==3.3.0 textblob==0.15.1
