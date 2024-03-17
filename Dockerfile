FROM python:alpine3.11

COPY . ./nenebot

WORKDIR /nenebot

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["pip", "install", "-r", "/requirements.txt"]

CMD ["python3", "run.py"]
