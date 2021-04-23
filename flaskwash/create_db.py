from flaskwash import db

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone_numer = db.Column(db.String(80))

    def __init__(self, first_name, last_name, phone_numer):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_numer = phone_numer

