from flask import Flask, render_template
from os import getenv

import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/posts/<name>/')
def posts(name):
    return render_template('posts/%s.html' % name)

@app.route('/newpost/<name>')
def testpost(name):
    data = ''
    with open('blog/posts.json', 'r') as f:
        data = f.read()
    realdata = json.loads(data)
    post = realdata[name]
    return render_template('viewpost.html', title=post['title'], post=post['post'])

if __name__ == '__main__':
    app.secret_key = getenv('SessionKey')
    app.run(debug=True, host='0.0.0.0')
