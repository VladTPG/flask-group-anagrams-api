from flask import Flask, request, jsonify, redirect
from utils import group_anagrams
import markdown

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024

@app.route("/")
def index():
    try:
        with(open("README.md","r")) as readme_file:
            content = readme_file.read()
            html = markdown.markdown(content)
            return html
    except FileNotFoundError:
        return jsonify({"error:": "README.md not found"}), 404


@app.route("/group-anagrams", methods = ["POST"])
def handle_request():
    data = request.get_json()
    words = data.get("words") if data else None

    if not isinstance(words,list) or not all(isinstance(word,str) for word in words):
        return jsonify({"error": "You must provide a \'words\' list with strings."}), 400

    result = group_anagrams(words)
    return jsonify({
        "metadata":
        {
            "length":len(result),
            "input_size":len(words)
        },
        "groups":result
        }),200

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An unexpected server error occurred."}), 500

@app.errorhandler(413)
def request_limiter(error):
    return jsonify({"error": "Request content is too large. Please limit it to " + str(app.config["MAX_CONTENT_LENGTH"] / (1024*1024)) +"MB"}), 413

@app.route("/<path:path>")
def catch_all(path):
    return redirect("/")