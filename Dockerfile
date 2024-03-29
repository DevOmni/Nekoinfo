FROM python:3.11.8-alpine3.19

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r /app/requirements.txt --user

COPY . .

EXPOSE 3000

# CMD ["pip", "install", "-r", "/requirements.txt"]

CMD ["python3", "run.py"]
