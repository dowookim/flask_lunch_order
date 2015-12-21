from flask import Flask, render_template
import requests
import pdb

app = Flask(__name__)

@app.route('/main')
def main():
	request_all_users = requests.get('http://localhost:8000/users')
	user_list = request_all_users.json()

	request_all_stores = requests.get('http://localhost:8000/stores')
	store_list = request_all_stores.json()

	request_todayOrderManagers = requests.get('http://localhost:8000/today_order_managers')
	todayOrderManagers = request_todayOrderManagers.json()

	return render_template('main.html', user_list=user_list,
										store_list=store_list,
										todayOrderManagers=todayOrderManagers)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)