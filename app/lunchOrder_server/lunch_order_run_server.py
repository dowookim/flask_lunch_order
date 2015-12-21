#-*- coding: utf-8 -*-
import sys
from flask import Flask, request, jsonify;
from sqlalchemy import Column, Integer, String, DateTime, Date
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import json
import pdb

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dwkim:qnxkrgo@192.168.88.152/lunch_order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class users(db.Model):
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String(10))
	team_id = db.Column(Integer)

	def __init__(self, id, name, team_id):
		self.id = id
		self.name = name
		self.team_id = team_id

class teams(db.Model):
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String(50))

	def __init__(self, id, name, team_id):
		self.id = id
		self.name = name

class stores(db.Model):
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String(128))

	def __init__(self, id, name, team_id):
		self.id = id
		self.name = name

	def __repr__(self):
		return "<User('%s', '%s')>" % (self.id, self.name)

class Products(db.Model):
	id = db.Column(Integer, primary_key=True)
	store_id = db.Column(Integer)
	name = db.Column(String(128))

	def __init__(self, id, store_id, name):
		self.id = id
		self.store_id = store_id
		self.name = name

	def __repr__(self):
		return "<User('%s', '%s', '%s')>" % (self.id, self.store_id, self.name)

class Today_stores(db.Model):
	id = db.Column(Integer, primary_key=True)
	order_date = db.Column(Date)
	store_id = db.Column(Integer)
	created_at = db.Column(DateTime)
	updated_at = db.Column(DateTime)

	def __init__(self, id, order_date, store_id, created_at, updated_at):
		self.id = id
		self.order_date = order_date
		self.store_id = store_id
		self.created_at = created_at
		self.updated_at = updated_at

	def __repr__(self):
		return "<User('%s', '%s', '%s', '%s', '%s')>" % (self.id, self.order_date, self.store_id, self.created_at, self.updated_at)

class order_managers(db.Model):
	id = db.Column(Integer, primary_key=True)
	order_date = db.Column(Date)
	user_id = db.Column(Integer)
	created_at = db.Column(DateTime)
	updated_at = db.Column(DateTime)

	def __init__(self, id, order_date, user_id, created_at, updated_at):
		self.id = id
		self.order_date = order_date
		self.user_id = user_id
		self.created_at = created_at
		self.updated_at = updated_at

	def __repr__(self):
		return "<User('%s', '%s', '%s', '%s', '%s')>" % (self.id, self.order_date, self.user_id, self.created_at, self.updated_at)

class chose_menus(db.Model):
	id = db.Column(Integer, primary_key=True)
	order_date = db.Column(Date)
	user_id = db.Column(Integer)
	selected_store_id = db.Column(Integer)
	selected_menu_id = db.Column(Integer)
	created_at = db.Column(DateTime)
	updated_at = db.Column(DateTime)

	def __init__(self, id, order_date, user_id, selected_menu_id, selected_store_id, created_at, updated_at):
		self.id = id
		self.order_date = order_date
		self.user_id = user_id
		self.selected_store_id = selected_store_id
		self.selected_menu_id = selected_menu_id
		self.created_at = created_at
		self.updated_at = updated_at

	def __repr__(self):
		return "<User('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.order_date, self.user_id, self.selected_store_id, self.selected_menu_id, self.created_at, self.updated_at)

@app.route('/users', methods=['GET'])
def getAllUsers():
 	user_list = users.query.all()
	return json.dumps(model_to_dict_list(user_list), ensure_ascii=False)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
	user = users.query.filter(users.id == id)
	return json.dumps(model_to_dict_list(user), ensure_ascii=False)

@app.route('/stores', methods=['GET'])
def getAllStores():
	store_list = stores.query.all()
	return json.dumps(model_to_dict_list(store_list), ensure_ascii=False)

@app.route('/today_order_managers', methods=['GET'])
def getTodayOrderManagers():
	todayOrderManager_list = order_managers.query.filter(order_managers.order_date == date.today())
	return json.dumps(model_to_dict_list(todayOrderManager_list), ensure_ascii=False)
 		 
def model_to_dict_list(list_model):
 	ret_data = []
	
 	for model in list_model:
 		user_object = {}
		columns = model.__table__.columns.keys()
		for key in model.__table__.columns.keys():
			for column in columns:
				column_value = getattr(model, key)
				if(type(column_value) == unicode):
					user_object[key] = str(column_value.encode('utf-8'))
				else:
					user_object[key] = str(column_value)
		ret_data.append(user_object)
 	
 	return ret_data

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8000, debug=True)