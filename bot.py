import telebot
import settings
import menus

bot = telebot.TeleBot(settings.BOT_TOKEN)


def check_access(fn):
    def wrapper(*args, **kwargs):
        message = args[0]
        if message.chat.id in settings.ALLOWED_IDS:
            return fn(*args, **kwargs)
        else:
            return bot.send_message(message.chat.id, 'Упс... Доступ запрещен.')
    return wrapper


@bot.message_handler(commands=['start'])
@check_access
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, давай начнем! Выбери действие из списка',
                     reply_markup=menus.start_menu_markup)


@bot.callback_query_handler(func=lambda call: True)
def button(call):
    processing_func = menus.get_processing_function(call.data)
    if processing_func:
        processing_func(call, bot)


bot.polling()
