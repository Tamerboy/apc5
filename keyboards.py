from telebot import types
from config import *


lang_keyboard = types.ReplyKeyboardMarkup(True, False)
lang_keyboard.row("Қазақша", "Русский")

company_choose_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
company_choose_keyboard['ru'].row("Физ.лицо", "Юр.лицо")
company_choose_keyboard['kz'].row("Жеке тұлға", "Заңды тұлға")

individual_step1_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
individual_step1_keyboard['ru'].row("Стартап", "Начинающий предприниматель")
individual_step1_keyboard['kz'].row("Стартап", "Бастаушы кәсіпкер")

company_step1_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
company_step1_keyboard['ru'].row("Стартап", "ИТ-компания")
company_step1_keyboard['kz'].row("Стартап", "ИТ-компания")

support_types_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
support_types_keyboard['ru'].row("Финансовые", "Нефинансовые")
support_types_keyboard['kz'].row("Қаржылық", "Қаржылық емес")

support_goal_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
support_goal_keyboard['ru'].row("Для расширения внутри страны")
support_goal_keyboard['ru'].row("Для выхода на зарубежные рынки")
support_goal_keyboard['kz'].row("Ішкі кеңейту үшін")
support_goal_keyboard['kz'].row("Сыртқы нарықтарға шығу")


company_money_support_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
company_money_support_keyboard['ru'].row("Гарантирование")
company_money_support_keyboard['ru'].row("Субсидирование")
company_money_support_keyboard['ru'].row("Гранты на коммерциализацию технологий")
company_money_support_keyboard['kz'].row("Кепілдік")
company_money_support_keyboard['kz'].row("Субсидиялау")
company_money_support_keyboard['kz'].row("Технологияларды коммерциализациялау гранттары")

company_no_money_support_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
company_no_money_support_keyboard['ru'].row("Реестр доверенного программного обеспечения и электронной промышленности")
company_no_money_support_keyboard['ru'].row("Налоговые льготы")
company_no_money_support_keyboard['ru'].row("Экспортное страхование")
company_no_money_support_keyboard['kz'].row("Сенімді бағдарламалық жасақтама және электроника индустриясының тізілімі")
company_no_money_support_keyboard['kz'].row("Салықтық жеңілдіктер")
company_no_money_support_keyboard['kz'].row("Экспортты сақтандыру")

guaranteeing_companies_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, False),
	'kz': types.ReplyKeyboardMarkup(True, False)
}
guaranteeing_companies_keyboard['ru'].row("Даму")
guaranteeing_companies_keyboard['ru'].row("Банк Развития Казахстан")
guaranteeing_companies_keyboard['kz'].row("Даму")
guaranteeing_companies_keyboard['kz'].row("Даму Банкі Қазақстан")

damu_keyboard = {
	'ru': types.InlineKeyboardMarkup(),
	'kz': types.InlineKeyboardMarkup()
}
damu_keyboard['ru'].add(types.InlineKeyboardButton("Описание", callback_data = 'damu_desc'))
damu_keyboard['ru'].add(types.InlineKeyboardButton("Требования к заявителю", callback_data = 'damu_req'))
damu_keyboard['ru'].add(types.InlineKeyboardButton("Требуемые документы", callback_data = 'damu_docs'))
damu_keyboard['ru'].add(types.InlineKeyboardButton("Ссылка на сайт", callback_data = 'damu_site'))
damu_keyboard['ru'].add(types.InlineKeyboardButton("Контакты", callback_data = 'damu_contacts'))

damu_keyboard['kz'].add(types.InlineKeyboardButton("Сипаттама", callback_data = 'damu_desc'))
damu_keyboard['kz'].add(types.InlineKeyboardButton("Өтініш берушіге қойылатын талаптар", callback_data = 'damu_req'))
damu_keyboard['kz'].add(types.InlineKeyboardButton("Қажетті құжаттар", callback_data = 'damu_docs'))
damu_keyboard['kz'].add(types.InlineKeyboardButton("Сілтеме", callback_data = 'damu_site'))
damu_keyboard['kz'].add(types.InlineKeyboardButton("Байланыстар", callback_data = 'damu_contacts'))

continue_keyboard = {
	'ru': types.ReplyKeyboardMarkup(True, True),
	'kz': types.ReplyKeyboardMarkup(True, True)
}
continue_keyboard['ru'].row("Продолжить")
continue_keyboard['kz'].row("Жалғастыру")