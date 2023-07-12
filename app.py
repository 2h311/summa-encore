from dotenv import load_dotenv
from flask import Flask, render_template, request


app = Flask(__name__)
query_todo = """
	query Todos {
	  todos{
	    id
	    completed
	    createdAt
	    description
	  }
	}
"""

endpoint = "https://api-ap-southeast-2.hygraph.com/v2/cljvhhz1y029001ue4x1e7m5q/master"
token = os.get("HYGRAPH_TOKEN")
headers = {"authorization": f"Bearer {token}"}


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
