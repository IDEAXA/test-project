import flask

app = flask.Flask(__name__)


@app.route('/')
def index0():
    return "0"


@app.route('/1')
def index1():
    return "1"


@app.route('/2')
def index2():
    return "2"


@app.route('/3')
def index3():
    return "3"


@app.route('/4')
def index4():
    return "4"


if __name__ == '__main__':
    app.run()
