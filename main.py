from flask import Flask, url_for, redirect, render_template, session, flash, request
from datetime import date

app = Flask(__name__, template_folder='templates')


current_year = date.today().year
current_month = date.today().month


@app.route('/')
def home():
    return render_template('index.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
