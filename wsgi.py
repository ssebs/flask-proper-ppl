'''
# wsgi.py - run flask app in production (use gunicorn for this)
'''
from pplproper import create_app

app = create_app("prod")

if __name__ == "__main__":
    app.run()
