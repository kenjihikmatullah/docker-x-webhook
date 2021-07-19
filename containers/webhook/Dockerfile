FROM ubuntu:18.04

LABEL maintainer="Kenji Hikmatullah iniemailkenji@gmail.com"

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

RUN chmod 755 ./scripts/update-frontend.sh && \
    chmod 755 ./scripts/update-backend.sh

CMD [ "python", "./app.py" ]