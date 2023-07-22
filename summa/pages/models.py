from summa import db, app


class ContactModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Contact('{self.firstname}, {self.email}')"
