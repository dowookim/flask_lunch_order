#-*- coding: utf-8 -*-
import sys
from flask import Flask, request, jsonify;
from sqlalchemy import Column, Integer, String, DateTime, Date
from flask_sqlalchemy import SQLAlchemy
import json
import pdb

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dwkim:qnxkrgo@192.168.10.20/lunch_order'
db = SQLAlchemy(app)

class Users(db.Model):
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String(10))
	team_id = db.Column(Integer)

	def __init__(self, id, name, team_id):
		self.id = id
		self.name = name
		self.team_id = team_id

class Team(db.Model):
	id = db.Column(Integer, primary_key=True)
	name = db.Column(String(50))

	def __init__(self, id, name, team_id):
		self.id = id
		self.name = name

class Stores(db.Model):
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

class Today_Stores(db.Model):
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

class Order_Manager(db.Model):
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

@app.route('/loadData', methods=['GET','POST'])
def loadData():
	model = Users.query.all()
	
	model_to_dict(model)
	return json.dump()

def model_to_dict(list_model):
	pdb.set_trace()
	ret_data = []
	ret_dict = {}
	
	for model in list_model:
		columns = model.__table__.columns.keys()
		for column in columns:
			ret_dict[column] = model.column
		ret_data.append()

	return ret_data

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8000)