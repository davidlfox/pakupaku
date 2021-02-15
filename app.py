from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/fortune", methods=["POST"])
def fortune():
    # todo: get state
    # respond/validate accordingly
    return jsonify({"message": "the message"})
