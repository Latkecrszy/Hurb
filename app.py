from flask import Flask, render_template
import os
import sys
import jinja2
import json


app = Flask(__name__)


@app.route('/landingpage')
def landingpage():
    return render_template("index.html")
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, use_reloader=True)
