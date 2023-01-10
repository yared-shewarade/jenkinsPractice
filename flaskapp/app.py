
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World "

@app.route('/user/<name>')
def greetings(name):
    return 'Hi ' + name

app.add_url_rule('/hello', 'hello', hello_world)

if __name__ == '__main__':
    app.run(debug=True)