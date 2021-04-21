FROM python:3.8-slim-buster
WORKDIR /app
COPY ./ /app
RUN pip3 install flask
ENTRYPOINT python ui.py
