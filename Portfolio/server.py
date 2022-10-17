from flask import Flask, render_template

app = Flask(__name__)


# Run using 'flask --app server --debug run'


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')
