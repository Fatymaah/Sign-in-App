from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello There !</h1>' 

@app.route('/home')
def home():
    return '<h1> You are on the homepage !</h1>' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)