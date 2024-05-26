FROM python:3.9.2-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && \
    apt-get install -y curl git && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y git-lfs && \
    git lfs install

RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://huggingface.co/yuriivoievidka/bert-imdb-pretrained /app/model

COPY . .

EXPOSE 5000

CMD [ "python", "./app.py" ]