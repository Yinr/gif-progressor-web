FROM python:alpine

LABEL maintainer=Yinr<yinr@yinr.cc>

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "./app.py" ]
