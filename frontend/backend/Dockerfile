FROM python:latest
WORKDIR /data/frontend/backend
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
WORKDIR /data/frontend
