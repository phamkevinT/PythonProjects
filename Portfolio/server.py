from flask import Flask, render_template

app = Flask(__name__)


# Run using 'flask --app <filename> --debug run'

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')
