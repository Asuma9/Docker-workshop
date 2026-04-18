FROM python:3.13.11-slim

RUN pip install pandas pyarrow

WORKDIR /code

COPY pipeline.py .

RUN apt-get update && apt-get install -y zsh \
&& git clone https://github.com/zsh-users/zsh-autosuggestions /root/.zsh/zsh-autosuggestions \
&& echo "source /root/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh" >> /root/.zshrc \
&& echo "[-t 1] && exec zsh" >> /root/.bashrc
