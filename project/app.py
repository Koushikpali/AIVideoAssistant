from flask import Flask, render_template, request, jsonify
import sys

sys.path.append(r"C:\Users\palik\Desktop\lunchain\AIVideoAssistant")
from main import run_pipeline 
from core.rag_engine import ask_question

app = Flask(__name__)

rag_chain_store = {"chain": None}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/process", methods=["POST"])
def process_video():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    source = data.get("source", "").strip()
    language = data.get("language", "english").strip()

    if not source:
        return jsonify({"error": "Source is required"}), 400

    try:
        result = run_pipeline(source, language)
        rag_chain_store["chain"] = result.get("rag_chain")
        return jsonify({
            "title": result.get("title", ""),
            "summary": result.get("summary", ""),
            "action_items": result.get("action_items", ""),
            "key_decisions": result.get("key_decisions", ""),
            "open_questions": result.get("open_questions", ""),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "Question is required"}), 400

    chain = rag_chain_store.get("chain")
    if chain is None:
        return jsonify({"error": "No video processed yet. Please process a video first."}), 400

    try:
        answer = ask_question(chain, question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
