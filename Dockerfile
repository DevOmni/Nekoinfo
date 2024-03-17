FROM python:alpine3.11

COPY . ./nenebot

WORKDIR /nenebot

EXPOSE 3000

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["pip", "install", "-r", "/requirements.txt"]

CMD ["python3", "run.py"]
