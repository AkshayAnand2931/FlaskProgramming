from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    user_agent = request.headers.get('User-Agent')
    date = request.headers.get("Date")
    args = request.args
    data = request.get_data()
    method = request.method
    host = request.host
    query_string = request.query_string
    
    return "<p>{}</p>".format(query_string)

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
