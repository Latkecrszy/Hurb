from flask import Flask, render_template
import os
import sys
import jinja2
import json


app = Flask(__name__)


@app.route('/landingpage')
def landingpage():
    return render_template("main.html")



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)