import json

from flask import Blueprint, render_template, request, url_for, redirect, flash
from summa.repository import post
from .forms import ContactForm
from .models import ContactModel
from summa import db

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
    # TODO: use this for now, till we got the page sorted out.
    import pathlib

    json_file = pathlib.Path().cwd() / "summa" / "pages" / "posts.json"
    blog_posts = json.load(open(json_file))
    return render_template("blog.html", title="Blog", posts=blog_posts)


@main.route("/careers")
def careers():
    return render_template("careers.html", title="Our Career Page")


@main.route("/thanks")
def thanks():
    return render_template("thanks.html", title="Thank you for contacting us")


@main.route("/contact-us", methods=["POST"])
def contact():
    form = ContactForm(request.form)
    if request.method.lower() == "post" and form.validate():
        contact = ContactModel(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            message=form.message.data,
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for("main.thanks"))
    return redirect(url_for("main.index"))
