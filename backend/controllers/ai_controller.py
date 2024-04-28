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
    # Check if the post request has the file part
   
    file = request.form.get('file')
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    # Retrieve the text from form data
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('/uploads', filename)  # Adjust path as needed
        file.save(filepath)

        # Assuming speech_to_text function accepts both text and filepath
        s
        converted_text = speech_to_text(text, filepath)  # Adjust function usage as needed

        # Assuming text_to_speech_file function from a different module
       
        response_file_path = text_to_speech_file(converted_text)
        
        # Clean up the original upload
        os.remove(filepath)

        # Send the generated MP3 file
        return send_file(response_file_path, as_attachment=True, mimetype='audio/mp3')
    else:
        return jsonify({"error": "Invalid file format"}), 400