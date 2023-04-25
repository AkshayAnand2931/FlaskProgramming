from flask import Flask
from flask import redirect
from flask import abort

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("http://www.example.com")

@app.route("/user/<name>")
def user(name):
    if name != "Akshay":
        abort(404)
    return "<h1>Hello, {} !</h1>".format(name)

if __name__ == "__main__":
    app.run(debug=True)