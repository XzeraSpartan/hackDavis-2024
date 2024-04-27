from flask import Blueprint, request, jsonify
from services import comparison_service

bp = Blueprint('comparison', __name__, url_prefix='/compare')

@bp.route('/', methods=['POST'])
def compare_sentences():
    data = request.get_json()
    sentence1 = data.get('sentence1')
    sentence2 = data.get('sentence2')
    response = comparison_service.compare_sentences(sentence1, sentence2)
    return jsonify(response)
