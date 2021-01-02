from flask import Flask, render_template, request, send_file, redirect
import os, sys, requests, jinja2, json


app = Flask(__name__)


@app.route('/')
def landingpage():
    try:
        code = request.args.get('code')
        API_ENDPOINT = 'https://discord.com/api/v6'
        CLIENT_ID = '332269999912132097'
        CLIENT_SECRET = '937it3ow87i4ery69876wqire'
        REDIRECT_URI = 'https://nicememe.website'

        data = {
            'client_id': '736283988628602960',
            'client_secret': 'ODzy9h_y8jpgXKlocqRQVGBe1k4IiTm8',
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://hurb.gg',
            'scope': 'identify email connections'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('%s/oauth2/token' % 'https://discord.com/api/oauth2/token', data=data, headers=headers)
        r.raise_for_status()
        return r.json()
    except:
        pass
    # https://discord.com/api/oauth2/token
    return render_template("index.html"), 200


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/commands')
def commands():
    return render_template("commands.html", commands=json.load(open("commands.json"))), 200


@app.route('/help')
def help():
    return render_template("Help.html"), 200


@app.route('/add')
def add():
    return redirect("https://discord.com/api/oauth2/authorize?client_id=736283988628602960&permissions=8&redirect_uri=https%3A%2F%2Fhurb.gg&scope=bot", code=302)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, use_reloader=True)
