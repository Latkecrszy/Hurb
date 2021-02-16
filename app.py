from flask import Flask, render_template, request, send_file, redirect
import os, sys, requests, jinja2, json, dotenv

dotenv.load_dotenv()

CLIENT_SECRET = os.environ.get('CLIENT_SECRET', None)

app = Flask(__name__)




@app.route('/')
def landingpage():
    code = request.args.get('code')
    if code is not None:
        data = {
            'client_id': '736283988628602960',
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://hurb.gg',
            'scope': 'identify email connections'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('%s/oauth2/token' % 'https://discord.com/api/oauth2/token', data=data, headers=headers)
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
    return redirect(
        "https://discord.com/api/oauth2/authorize?client_id=736283988628602960&permissions=8&redirect_uri=https%3A%2F%2Fhurb.gg&scope=bot",
        code=302)


@app.route('/knowledgebase')
def knowledgebase():
    return redirect(
        "https://app.spaceli.io/space/1Hx_-16-CuC0jhL5LoMicpzFlrUZQNqNF",
        code=302)


@app.route('/terms')
def terms():
    return redirect(
        "https://app.spaceli.io/space/1Hx_-16-CuC0jhL5LoMicpzFlrUZQNqNF/page/1yXp_4YckAgid3JY2L4tzozHA8eLIFSR_28xQWkkwaKY",
        code=302)


@app.route('/privacy')
def privacy():
    return redirect(
        "https://app.spaceli.io/space/1Hx_-16-CuC0jhL5LoMicpzFlrUZQNqNF/page/1tWH2o8FLksfIQGOl5UF_ydW92bXqvlzAfm5ajeBIB74",
        code=302)


@app.route('/acknowledgements')
def acknowledgements():
    return redirect(
        "https://app.spaceli.io/space/1Hx_-16-CuC0jhL5LoMicpzFlrUZQNqNF/page/1dtnmYmYxz4bG4160uO8DlC0Z7D2cClqvLXWPAXG3uLY",
        code=302)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, use_reloader=True)
