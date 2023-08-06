FROM python:3.7-slim AS builder
COPY requirements.txt /app/requirements.txt
# this is needed to run XGBOOST
RUN apt-get update && apt-get install libgomp1
RUN pip3 install -r /app/requirements.txt

FROM builder
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python", "main.py"]