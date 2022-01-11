FROM python:latest
WORKDIR /data/backend
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]