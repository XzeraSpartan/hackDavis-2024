from flask import Blueprint, request, jsonify
from openai import OpenAI
from backend.services import gpt_service

bp = Blueprint('comparison', __name__, url_prefix='/compare')

@bp.route('/', methods=['POST'])
def compare():
    data = request.get_json()
    sentence1 = data.get('sentence1')
    sentence2 = data.get('sentence2')
    if not sentence1 or not sentence2:
        return jsonify({"error": "Please provide both sentences."}), 400
    result = gpt_service.compare_sentences(sentence1, sentence2)
    return jsonify(result)
