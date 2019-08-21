'''
# ppl-proper/run.py - dev server
'''
from pplproper import create_app

app = create_app(config="prod")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006, debug=True)
