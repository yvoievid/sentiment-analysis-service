from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    return "Hello, This is Sentiment analysis API that is made using BERT, to start send a json object in format { text: \"some text\" } to /analyze endpoint"
