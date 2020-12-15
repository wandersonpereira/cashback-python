FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /usr/src/app/var/log

COPY . .

CMD [ "waitress-serve", "--port=8000", "app:api" ]