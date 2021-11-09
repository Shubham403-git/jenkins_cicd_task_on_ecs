from flask import *


app = Flask(__name__)

@app.route('/')
def docker():
    return " Runing Inside docker Conatiner(flask App) "
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
