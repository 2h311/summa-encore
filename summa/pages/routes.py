from flask import Blueprint, render_template, request
from summa.repository import post

main = Blueprint("main", __name__)


@main.route("/")
def index():
    blog_posts = post.get_first_four()
    return render_template(
        "index.html", title="Your One Stop Digital Creative Agency", posts=blog_posts
    )


@main.route("/blog")
def blog():
    return render_template("blog.html", title="")


@main.route("/careers")
def careers():
    return render_template("careers.html", context={"title": ""})


@main.route("/contact-us", methods=["POST"])
def contact():
    if request.method.lower() == "post":
        form = request.form
        print(form)

    return "message received"
