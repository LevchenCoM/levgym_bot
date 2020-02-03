import datetime
import settings
from types import FunctionType
from typing import List
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_exercise(program_key, exercise_key, call, bot):
    pass

    # TODO: Exercises
    # next step button, weight and how many times input.
    # Save results into DB


def exercise_callback_handler(call, bot):
    callback_type, program_key, exercise_key = call.data.split(':')
    start_exercise(program_key, exercise_key, call, bot)


def show_exercises(program_key, exercises, call, bot):
    buttons = [
        InlineKeyboardButton(title, callback_data='exercise:{}:{}'.format(program_key, exercise_id))
        for exercise_id, title in exercises.items()
    ]
    menu_markup = InlineKeyboardMarkup()
    for button in buttons:
        menu_markup.row(button)

    bot.send_message(call.message.chat.id, 'Теперь выбери упражнение',
                     reply_markup=menu_markup)


def show_programs(call, bot):
    program_buttons = [
        InlineKeyboardButton(program_key, callback_data='program:{}'.format(program_key))
        for program_key in settings.AVAILIBLE_PROGRAMS
    ]

    menu_markup = InlineKeyboardMarkup()
    for button in program_buttons:
        menu_markup.row(button)

    bot.send_message(call.message.chat.id, 'Хорошо. Выбери программу из списка, чтобы начать',
                     reply_markup=menu_markup)


def program_callback_handler(call, bot):
    callback_type, program_key = call.data.split(':')
    for program, exercises in settings.AVAILIBLE_PROGRAMS.items():
        if program == program_key:
            show_exercises(program_key, exercises, call, bot)


CALLBACK_KEYS = {
    'program': program_callback_handler,
    'exercise': exercise_callback_handler,
    'step': 1
}


def start_start_training(call, bot):
    print('Executed callback "start_start_training" | {}'.format(datetime.datetime.now()))
    show_programs(call, bot)


def start_training_programs(call, bot):
    print('Executed callback "start_training_programs" | {}'.format(datetime.datetime.now()))


MENUS = {
    'start_menu': [
        (InlineKeyboardButton('Начать тренировку', callback_data='start_start_training'), start_start_training),
        (InlineKeyboardButton('Программы тренировок', callback_data='start_training_programs'), start_training_programs)
    ]
}


def get_buttons(menu_key: str) -> List[InlineKeyboardButton]:
    menu_buttons = MENUS.get(menu_key, None)
    buttons = []
    if menu_buttons:
        buttons.extend([
            button for button, func in menu_buttons
        ])

    return buttons


def get_processing_function(button_key: str) -> FunctionType:
    key_parts = button_key.split(':')
    function = None
    if len(key_parts) > 1:
        callback_key = key_parts[0]
        for key, func in CALLBACK_KEYS.items():
            if key == callback_key:
                function = func
    else:
        for menu_buttons in MENUS.values():
            for button, func in menu_buttons:
                if button.callback_data == button_key:
                    function = func

    return function


# Start Menu
start_menu_markup = InlineKeyboardMarkup()
start_menu_markup.row(*get_buttons('start_menu'))
