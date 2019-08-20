'''
# pplproper/models.py - models
'''
from . import db


# User model
class Person(db.Model):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean)

    def __repr__(self):
        return f"Usr: {self.first_name} {self.last_name}: {self.email}: {self.active}"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
