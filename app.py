from flask import Flask, render_template
import os
import sys
import jinja2
import json


app = Flask(__name__)


@app.route('/')
def landingpage():
    return render_template("index.html"), 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/commands')
def commands():
    return render_template("commands.html", commands=json.load(open("commands.json"))), 200


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, use_reloader=True)
