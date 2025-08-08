from flask import Flask, request, jsonify, render_template
from rag import rag_query
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Check for API key but don't exit immediately
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Warning: OPENAI_API_KEY environment variable is not set.")
    print("Please set it in your system or in a .env file.")

@app.route('/')
def index():
    if not api_key:
        return """
        <h1 style='color:red;'>Error: OPENAI_API_KEY not set</h1>
        <p>Please set your OpenAI API key in a <code>.env</code> file or environment variable.</p>
        """
    return render_template('index.html')

@app.route('/rag', methods=['POST'])
def handle_rag_query():
    if not api_key:
        return jsonify({"error": "OPENAI_API_KEY not set. Please configure it before using the API."}), 500

    data = request.json
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request: JSON payload must contain a 'query' field."}), 400

    params = {
        "max_tokens": int(data.get("max_tokens", 300)),
        "temperature": float(data.get("temperature", 0.7)),
        "top_p": float(data.get("top_p", 1.0)),
        "frequency_penalty": float(data.get("frequency_penalty", 0.0)),
        "presence_penalty": float(data.get("presence_penalty", 0.0)),
    }

    response_text = rag_query(data['query'], **params)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    print("Flask server starting... Visit http://127.0.0.1:5000 in your browser.")
    app.run(debug=True)
