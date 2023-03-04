FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get upgrade
COPY requirements.txt requirements.txt
#tesseract-ocr  libgl1 libgl1-mesa-glx -y
RUN apt-get install python3  python3-pip libgl1 libgl1-mesa-glx -y
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["python", "./edcdb.py"]
