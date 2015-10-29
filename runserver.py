from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route("/")
def hello():
    return app.send_static_file('client.html')

if __name__ == "__main__":
    app.run()