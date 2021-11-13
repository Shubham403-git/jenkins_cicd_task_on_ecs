from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'
#@app.route('/test')
#def test():
 #   return '<h1>Hello Testing </h2>'


if __name__ == "__main__":
    app.run(debug=True)
