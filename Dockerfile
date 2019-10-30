FROM python:latest

LABEL maintainer=Yinr<yinr@yinr.cc>

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV WORKERS 5

EXPOSE 8000

CMD [ "sh", "-c", "gunicorn -b 0.0.0.0:8000 -w ${WORKERS} app:app" ]
