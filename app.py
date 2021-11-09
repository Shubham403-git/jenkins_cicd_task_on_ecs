from flask import *


app = Flask(__name__)

@app.route('/')
def upload():
    return " Runing Inside docker Conatiner(flask App) "
@app.route('/task')
def taskdone():
    return "Task Done Successfully With CI-CD implementation."


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
