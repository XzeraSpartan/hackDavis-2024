from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from controllers import comparison_controller, book_controller

from supabase import create_client, Client


app = Flask(__name__)
load_dotenv()  # Load environment variables

app.register_blueprint(comparison_controller.bp)

# Register the routes
app.register_blueprint(book_controller.bp)
#test

if __name__ == "__main__":
    app.run(debug=True)
