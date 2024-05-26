# Sentiment Analysis Service

---

The service that makes sentiment analysis of IMDB dataset with BERT model.
There are 2 ways to use it

## Run service using Docker
This way will take some time... This docker image downloads BERT model from hugging face repo
so it takes time to build.

```
git clone ...
docker build -t sentiment-analysis-service .
docker run -d -p 5000:5000 sentiment-analysis-service

```
### Endpoints

```
127.0.0.1:5000/ - home page
127.0.0.1:5000/health - endpoint for healthcheck
127.0.0.1:5000/analyze - endpoint for text analysis
```



## Run locally
This method requires DOWNLOADING BERT MODEL MANUALLY FROM HUGGING FACE!
download BERF_ft.model from [my repo](https://huggingface.co/yuriivoievidka/bert-imdb-pretrained/tree/main)


```
git clone ...
cd ./sentiment-analysis-service
python -m venv .venv
source ./bin/activate
pip install -r requirements.txt
mv path/to/model/BERF_ft.model ./model/
python app.py

```