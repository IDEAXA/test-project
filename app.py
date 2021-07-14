from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index0():
    return json.dumps({'data': 0})


@app.route('/1')
def index1():
    return json.dumps({'data': 1})


@app.route('/2')
def index2():
    return json.dumps({'data': 2})


@app.route('/3')
def index3():
    return json.dumps({'data': 3})


@app.route('/4')
def index4():
    return json.dumps({'data': 4})


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({'sum': data['a'] + data['b']})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

