from flask import Flask, render_template

app = Flask(__name__)


# Run using 'flask --app server --debug run'


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
