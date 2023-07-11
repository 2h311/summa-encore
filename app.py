from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html", context={"title": "Your One Stop Digital Creative Agency"}
    )


@app.route("/blog")
def blog():
    return render_template("blog.html", context={"title": ""})


@app.route("/careers")
def careers():
    return render_template("careers.html", context={"title": ""})


@app.route("/contact-us", methods=["POST"])
def contact():
    if request.method.lower() == "post":
        ...
    print(request)
