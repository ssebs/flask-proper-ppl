'''
# ppl-proper/init_db.py - Setup sqlite db
'''
from pplproper import create_app, db
from pplproper.models import Person

app = create_app("prod")

db.create_all()
db.session.close()
