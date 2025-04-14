from flask import Blueprint, request, jsonify, render_template
from langchain_integration.chain import get_answer_from_llm

bp = Blueprint("routes", __name__)


@bp.route("/", methods=["GET"])
def get_chat():

    return render_template("index.html")


@bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    try:
        answer = get_answer_from_llm(message)
        #return answer.text
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
