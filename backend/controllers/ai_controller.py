from flask import Blueprint, request, jsonify, send_file
from services.text_to_speech import text_to_speech_file


bp = Blueprint('ai', __name__, url_prefix='/ai')

@bp.route('/TTS/', methods=['POST'])
def TTS():
    #print(request.method)
    if request.method == 'POST':
        # Get text from the request
        text = request.data.decode('utf-8')
        response_file_path = text_to_speech_file(text)
        return send_file(response_file_path, as_attachment=True, mimetype='audio/mp3')
