from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from controllers import comparison_controller

app = Flask(__name__)
load_dotenv()  # Load environment variables

# Register the routes
app.register_blueprint(comparison_controller.bp)

if __name__ == "__main__":
    app.run(debug=True)
