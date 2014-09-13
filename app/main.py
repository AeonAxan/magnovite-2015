import os

from flask import Flask, render_template

app = Flask(__name__)
if os.environ.get('PROD', None) is None:
    app.debug = True
    print('DEBUG')

@app.route('/')
def index():
    if app.debug == True:
        template = 'dist/home.html'
    else:
        template = 'home.html'

    return render_template(template)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
