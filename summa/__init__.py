import os
from dotenv import load_dotenv

from flask import Flask, render_template, request

load_dotenv()
app = Flask(__name__)
app.config["HYGRAPH_TOKEN"] = os.getenv("HYGRAPH_TOKEN")
app.config["HYGRAPH_ENDPOINT"] = os.getenv("HYGRAPH_ENDPOINT")

# from .reposiytory import post


@app.route("/")
def index():
    # blog_posts = post.get_first_four()
    blog_posts = [
        {
            "slug": "the-hollywood-actors-walkout-will-change-how-we-fight-ai",
            "title": "The Hollywood Actors' Walkout Will Change How We Fight AI",
            "description": "Meryl Streep and other outspoken individuals may help artificial intelligence reach a new level of awareness, along with the suspension of production.",
            "createdAt": "14 Jul 2023",
            "images": {"url": "https://media.graphassets.com/YRCUcC9zRYCpfSJAqptu"},
        },
        {
            "slug": "in-the-us-ev-sales-set-a-record-perhaps-now-their-popularity-is-dwindling",
            "title": "In the US, EV sales set a record. Perhaps now, their popularity is dwindling",
            "description": "The photos from the telescope are used in the Apple TV+ adaption of the Isaac Asimov series to create stunning visuals.",
            "createdAt": "14 Jul 2023",
            "images": {"url": "https://media.graphassets.com/B6J5UEC4TPyduaXJG9HA"},
        },
        {
            "slug": "ok-surfers-how-much-would-it-cost-to-power-your-own-wave",
            "title": "OK Surfers, How Much Would It Cost to Power Your Own Wave?",
            "description": "How much energy would it take to fuel a wave that you can shred like Kelly Slater? Here’s the math.",
            "createdAt": "15 Jul 2023",
            "images": {"url": "https://media.graphassets.com/IkNyIxTuTnK1pQq6OD6o"},
        },
        {
            "slug": "the-actual-effects-of-internet-outages",
            "title": "The Actual Effects of Internet Outages",
            "description": "The  NetLoss calculator is a new tool that estimates the economic cost of Internet shutdowns",
            "createdAt": "19 Jul 2023",
            "images": {"url": "https://media.graphassets.com/1k2anEYuSPu7Q7OOrtGm"},
        },
    ]
    return render_template(
        "index.html", title="Your One Stop Digital Creative Agency", posts=blog_posts
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
