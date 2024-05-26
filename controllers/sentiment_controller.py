from flask import Blueprint, request, jsonify
from model.sentiment_model import SentimentModel

sentiment_bp = Blueprint('sentiment_bp', __name__)

sentiment_model = SentimentModel()

@sentiment_bp.route('/analyze', methods=['POST'])
def analyze():
    content = request.json
    text_to_analyze = content["text"]
    probabilities = sentiment_model.predict(text_to_analyze)
    return jsonify({"probabilities": probabilities})
