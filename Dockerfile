FROM python:3.11

RUN mkdir -p /src/
WORKDIR /src/

COPY . /src/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "main.py" ]
