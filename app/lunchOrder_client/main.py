from flask import Flask, render_template
import requests
import pdb

app = Flask(__name__)

@app.route('/main')
def main():
	r = requests.get('http://localhost:8000/users')
	user_list = r.json()
	return render_template('main.html', user_list=user_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)