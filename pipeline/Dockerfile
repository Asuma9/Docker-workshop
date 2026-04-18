FROM python:3.13.11-slim

RUN pip install pandas pyarrow

WORKDIR /code

COPY pipeline.py .

RUN apt-get update && apt-get install -y zsh \
&& git clone https://github.com/szh-users/zsh-autosuggestions.zsh