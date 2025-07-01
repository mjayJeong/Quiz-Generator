from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return 'Hello, This is My First Page!'


@app.route('/yourpage')
def yourpage():
    return 'This is your page!!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)   