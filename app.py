from flask import Flask, render_template, url_for
from camera import fodase

app = Flask(__name__)

@app.route("/")
def index():
    media = fodase()
    media = round(media, 2)
    return render_template("index.html", media = media)

# @app.route("/init")
# def init():
#     media = fodase()
#     return render_template("score.html", media=media)

if __name__ == "__main__":
    app.run(debug=True)