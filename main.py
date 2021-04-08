import telebot
import time
from text import *
from keyboards import *
from config import *
from functions import *
from telebot import types

@bot.message_handler(commands = ['start'])
def start_command(message):
	global users
	add_new_user(message)
	chat_id = message.chat.id
	u = users[chat_id]
	bot.send_message(chat_id, welcome_text['kz'] + '\n\n' + welcome_text['ru'],
		reply_markup = lang_keyboard)

@bot.message_handler(commands = ['question'])
def start_command(message):
	global users
	add_new_user(message)
	chat_id = message.chat.id
	u = users[chat_id]
	u.question_mode = True
	bot.send_message(chat_id, question_text[u.lang])

@bot.message_handler(content_types = ['text'])
def text_handler(message):
	global users
	add_new_user(message)
	chat_id = message.chat.id
	u = users[chat_id]

	if message.text in ['Қазақша', 'Русский']:
		if message.text == 'Қазақша':
			u.lang = 'kz'
		else:
			u.lang = 'ru'
		bot.send_message(chat_id, start_text[u.lang], 
			reply_markup = company_choose_keyboard[u.lang])
	elif message.text in ['Физ.лицо', 'Юр.лицо', 'Жеке тұлға', 'Заңды тұлға']:
		if message.text in ['Физ.лицо', 'Жеке тұлға']:
			u.type = 'individual'
			bot.send_message(chat_id, individual_step1_text[u.lang], 
				reply_markup = individual_step1_keyboard[u.lang])
		elif message.text in ['Юр.лицо', 'Заңды тұлға']:
			u.type = 'company'
			bot.send_message(chat_id, company_step1_text[u.lang], 
				reply_markup = company_step1_keyboard[u.lang])
	elif message.text in ['Стартап', "Начинающий предприниматель", "Бастаушы кәсіпкер", "ИТ-компания"]:
		if message.text == 'Стартап':
			u.sub_type = 'startup'
		elif message.text in ["Начинающий предприниматель", "Бастаушы кәсіпкер"]:
			u.sub_type = 'enterpreneur'
		else:
			u.sub_type = 'company'

		if u.type == 'individual':
			bot.send_message(chat_id, support_types_text[u.lang], 
				reply_markup = support_types_keyboard[u.lang])
		else:
			bot.send_message(chat_id, support_goal_text[u.lang],
				reply_markup = support_goal_keyboard[u.lang])
	elif message.text in ["Для расширения внутри страны", "Для выхода на зарубежные рынки", "Ішкі кеңейту үшін", "Сыртқы нарықтарға шығу"]:
		if message.text in ["Для расширения внутри страны", "Ішкі кеңейту үшін"]:
			u.goal = 'in'
		else:
			u.goal = 'out'
		bot.send_message(chat_id, support_types_text[u.lang], 
				reply_markup = support_types_keyboard[u.lang])
	elif message.text in ["Финансовые", "Нефинансовые","Қаржылық", "Қаржылық емес"]:
		if message.text in ["Финансовые", "Қаржылық"]:
			u.support_type = 'money'
			if u.type == 'company':
				bot.send_message(chat_id, support_text[u.lang],
					reply_markup = company_money_support_keyboard[u.lang])
		else:
			u.support_type = 'no money'
			if u.type == 'company':
				bot.send_message(chat_id, support_text[u.lang],
					reply_markup = company_no_money_support_keyboard[u.lang])
	elif message.text in ["Гарантирование", "Кепілдік"]:
		u.mode = 'guaranteeing'
		bot.send_message(chat_id, guaranteeing_companies_text[u.lang],
			reply_markup = guaranteeing_companies_keyboard[u.lang])
	elif message.text == 'Даму':
		u.company = 'damu'
		bot.send_message(chat_id, damu_text[u.lang], 
			reply_markup = damu_keyboard[u.lang], parse_mode = 'Markdown')
		time.sleep(5)
		bot.send_message(chat_id, continue_text[u.lang],
			reply_markup = continue_keyboard[u.lang])
	elif message.text in ["Продолжить", "Жалғастыру"]:
		bot.send_message(chat_id, end_text[u.lang])
		db.add_form(u)
	elif u.question_mode is True:
		u.question_mode = False
		bot.send_message(chat_id, question_success_text[u.lang])
		db.add_question(chat_id, message.text)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):	
	add_new_user(call.message)
	global users
	chat_id = call.message.chat.id
	u = users[chat_id]
	if call.data[:4] == 'damu':
		bot.send_message(chat_id, companies['damu'][call.data[5:]][u.lang])

bot.polling(none_stop=True)