from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    if app.debug:
        template = 'home.html'
    else:
        template = 'dist/home.html'

    return render_template(template)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
