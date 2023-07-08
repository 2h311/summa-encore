from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html", context={"title": "Your One Stop Digital Creative Agency"}
    )


@app.route("/blog")
def blog():
    ...
