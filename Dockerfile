FROM python:3.8-alpine

WORKDIR /app

RUN apk add --no-cache python3 && \
    apk add --no-cache gcc && \
    apk add --no-cache libffi-dev && \
    apk add --no-cache python3-dev && \
    apk add --no-cache musl-dev && \
    apk add --no-cache linux-headers

RUN apk add curl git --no-cache



COPY . /app

RUN pip install --upgrade pip==20.0.1
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "./application.py" ]