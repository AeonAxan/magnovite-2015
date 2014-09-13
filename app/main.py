import os

from flask import Flask, render_template

app = Flask(__name__)
if os.environ.get('PROD', False) != '1':
    app.debug = True

@app.route('/')
def index():
    print(app.debug)
    if app.debug:
        template = 'home.html'
    else:
        template = 'dist/home.html'

    return render_template(template)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
