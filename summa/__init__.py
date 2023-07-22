import os
from dotenv import load_dotenv

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__)
app.config["HYGRAPH_TOKEN"] = os.getenv("HYGRAPH_TOKEN")
app.config["HYGRAPH_ENDPOINT"] = os.getenv("HYGRAPH_ENDPOINT")
app.config["SECRET_KEY"] = os.getenv("WTF_SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///summa.db"
db = SQLAlchemy(app)


from summa.pages.routes import main

app.register_blueprint(main)
