FROM python:3-alpine

WORKDIR /swanson

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./the-quotable-swanson.py"]