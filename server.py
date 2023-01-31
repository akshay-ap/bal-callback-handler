from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("Post request", request.data)
        return jsonify({"success": True}), 200
    else:
        print("GET request", request.data)
        return jsonify({"success": True}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5010)
