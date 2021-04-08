from config import *
from text import *
from keyboards import *
import time

def add_new_user(message):
	global users
	chat_id = message.chat.id
	if chat_id in users.keys():
		return 
	if not db.check_user(chat_id):
		try:
			print("New user:\n"\
			"chat_id = " + str(message.chat.id) + \
			"\nfirst_name = " + message.from_user.first_name +\
			"\nlast_name = " + message.from_user.last_name +\
			"\ntg_username = " + message.from_user.username)
		except:
			pass
		db.add_new_user(message.chat.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
	a = Settings()
	users[chat_id] = a

def error_handler(e, chat_id):
	global db
	print(e)
	bot.send_message(chat_id, error_message)
	db = SQL()

