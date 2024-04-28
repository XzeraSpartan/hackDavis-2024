from flask import Blueprint, request, jsonify
from supabase import create_client
from services.sentence_divider import divide
from services.fetch_data import fetch_single_book_with_id, fetch_table, fetch_metadata

# Configure the Supabase client

bp = Blueprint('book', __name__, url_prefix='/book')

@bp.route('/get_book_data/<book_id>', methods=['GET'])
def get_book_text(book_id):
    data = fetch_single_book_with_id(book_id)
    print(data)
    for book in data:
        
        book['book_text'] = divide(book['book_text'])
    return jsonify({'result': data})



@bp.route('/get_metadata/', methods=['GET'])
def get_metadata():
    data = fetch_metadata()
    
    return jsonify({'result': data})





