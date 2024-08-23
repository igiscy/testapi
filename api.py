from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/info", methods=["GET"])
def get_students():
    return {'result':True}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)