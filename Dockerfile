FROM python:3.7.3-stretch

WORKDIR /home/flask/app/std-app

RUN groupadd flaskgroup && \
    useradd -m -g flaskgroup -s /bin/bash flask && \
    mkdir -p /home/flask/app/gateway
# mkdir -p /home/flask/app/gateway && \
# apt-get update && apt-get install curl -y

COPY . /home/flask/app/std-app

# RUN pip install --no-cache-dir --no-install-recommends -r requirements.txt && \
RUN chown -R flask:flaskgroup /home/flask

USER flask
EXPOSE 5000

CMD ["python", "app.py"]
