FROM python:alpine3.11

COPY . ./nenebot

WORKDIR /nenebot

EXPOSE 3000

RUN pip3 install --no-cache-dir -r requirements.txt --user

# CMD ["pip", "install", "-r", "/requirements.txt"]

CMD ["python3", "run.py"]
