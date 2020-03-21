from flask import Flask, render_template
from model import get_start

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/<country>', methods=['POST', 'GET'])
def search(country):
    return get_start(country)

if __name__ == "__main__":
    app.run(port=5001, debug=True)