from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name = name)

@app.route("/comments")
def comments():
    comments = ["Hello","hi","<h1>Safe</h1>"]
    return render_template("macro.html",comments = comments)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)
