from dotenv import load_dotenv

from flask import Flask, render_template, request


load_dotenv()
app = Flask(__name__)
app.config["HYGRAPH_TOKEN"] = os.getenv('HYGRAPH_TOKEN')
app.config["HYGRAPH_ENDPOINT"] = os.getenv("HYGRAPH_ENDPOINT")


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
