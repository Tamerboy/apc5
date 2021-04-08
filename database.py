#-*-coding: utf-8-*-

import psycopg2
import telebot
import os

class SQL:
	def __init__(self):
		# local host------------------
		if 'DATABASE_URL' not in os.environ.keys():
			self.con = psycopg2.connect(
			  database = "apc5",
			  user ="postgres", 
			  password="sbazgugu", 
			  host="localhost", 
			  port="5432"
			)
		# ----------------------------
		else:
		#heroku----------------------
			DATABASE_URL = os.environ['DATABASE_URL']
			self.con = psycopg2.connect(DATABASE_URL, sslmode='require')
		#----------------------------

		self.cur = self.con.cursor()
	#-----users table functions------------------
	def add_new_user(self, chat_id, fn, ln, tu):
		self.cur.execute('''INSERT INTO users(chat_id, first_name, second_name, telegram_username)
			VALUES(%s, %s, %s, %s)''', (str(chat_id), fn, ln, tu))
		self.con.commit()
	def check_user(self, chat_id):
		self.cur.execute('SELECT id FROM users WHERE chat_id = %s', (str(chat_id), ))
		if self.cur.rowcount > 0:
			return True
		return False
	def add_form(self, u):
		self.cur.execute('INSERT INTO forms(type, sub_type, goal, support_type,	mode, company)\
			VALUES(%s, %s, %s, %s, %s, %s)', (u.type, u.sub_type, u.goal, u.support_type, u.mode, u.company, ))
		self.con.commit()
	def add_question(self, chat_id, question):
		self.cur.execute('INSERT INTO questions(chat_id, question)\
			VALUES(%s, %s)', (str(chat_id), question, ))
		self.con.commit()
