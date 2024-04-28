from flask import Blueprint, request, jsonify, send_file
from services.text_to_speech import text_to_speech_file
from services.speech_to_text import speech_to_text
from werkzeug.utils import secure_filename
import os
bp = Blueprint('ai', __name__, url_prefix='/ai')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp3'}

@bp.route('/tts/', methods=['POST'])
def TTS():
    #print(request.method)
    if request.method == 'POST':
        # Get text from the request
        text = request.data.decode('utf-8')
        response_file_path = text_to_speech_file(text)
        return send_file(response_file_path, as_attachment=True, mimetype='audio/mp3')
    

@bp.route('/stt_tts', methods=['POST'])
def STT_to_TTS():
    # Check if the file part exists in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    # Check if text data is provided
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Validate file type and process if valid
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('uploads', filename)
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        file.save(filepath)
        

        # Process the file and text to convert speech to text and text to speech
        converted_text = speech_to_text(text, filepath)  # This function should accept both arguments
        response_file_path = text_to_speech_file(converted_text)  # Convert the processed text back to speech

        # Clean up the uploaded file after processing
        os.remove(filepath)

        # Send the new MP3 file back to the client
        return send_file(response_file_path, as_attachment=True, mimetype='audio/mp3')
    else:
        return jsonify({"error": "Invalid file format"}), 400
