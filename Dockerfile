FROM python:3.8
WORKDIR /usr/src/app
COPY . .
CMD ["python3.8","test.py"]
