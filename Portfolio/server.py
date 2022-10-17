from flask import Flask, render_template

app = Flask(__name__)


# Run using 'flask --app <filename> --debug run'

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<username>/<int:post_id>")
def hello_user(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route("/about")
def about():
    return render_template('about.html')
