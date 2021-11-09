from flask import *


app = Flask(__name__)

@app.route('/')
def upload():
    return " Hello from Docker"
@app.route('/task')
def upload():
    return " Hello World"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
