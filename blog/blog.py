from flask import Flask, render_template
from os import getenv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/posts/<name>/')
def posts(name):
    return render_template('posts/%s.html' % name)

@app.route('/test')
def testpost():
    return render_template('viewpost.html', title='Test page', post=['This is a test page', 'It is to test a template and nothing more'])

if __name__ == '__main__':
    app.secret_key = getenv('SessionKey')
    app.run(debug=True, host='0.0.0.0')
