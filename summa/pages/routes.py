from flask import Blueprint, render_template, request, url_for, redirect
from summa.repository import post
from .forms import ContactForm

main = Blueprint("main", __name__)


@main.route("/")
def index():
    form = ContactForm()
    blog_posts = post.get_first_four()
    return render_template(
        "index.html",
        title="Your One Stop Digital Creative Agency",
        posts=blog_posts,
        form=form,
    )


@main.route("/blog")
def blog():
    return render_template("blog.html", title="")


@main.route("/careers")
def careers():
    return render_template("careers.html", context={"title": ""})


@main.route("/contact-us", methods=["POST"])
def contact():
    form = ContactForm(request.form)
    if request.method.lower() == "post" and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        message = form.message.data
        print(firstname, message)

    return redirect(url_for("main.index"))
