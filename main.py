import telebot
from telebot import types

from functions import *


bot = telebot.TeleBot("11111111111111")
age, height, weight, gender, coefficient, mini_cal = 0, 0, 0, 0, 0, 0
base, norm, protein, fiber, carbs = 0, [0]*3, [0]*3, [0]*3, [0]*3

@bot.message_handler(commands=['start'])
def start(message):
    markup = create_initial_buttons()
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}!\nЯ бот-помощник.🦾 Могу рассчитать калорийность рациона или расказать о содержании нутриентов в продуктах\nНажимай, чтобы начать', reply_markup=markup)

def create_initial_buttons():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Рассчитать калорийность рациона', callback_data='start')
    btn2 = types.InlineKeyboardButton('Рассказать про содержание нутриентов', callback_data='nutrient')
    markup.add(btn1, btn2)
    return markup

def get_age(message):
    global age
    try:
        age = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Введи целое число лет!!!')
        bot.register_next_step_handler(message, get_age)
    else:
        if age <= 120:
            bot.send_message(message.chat.id, 'Введи рост в см.')
            bot.register_next_step_handler(message, get_height)
        else:
            bot.send_message(message.chat.id, 'Ну и долгожитель!!! Максимально-допустимый возраст 120 лет. Повтори ввод.')
            bot.register_next_step_handler(message, get_age)


def get_height(message):
    global height
    try:
        height = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат!!!')
        bot.register_next_step_handler(message, get_height)
    else:
        if (70<= height <= 300):
            bot.send_message(message.chat.id, 'Введи вес в кг.')
            bot.register_next_step_handler(message, get_weight)
        else:
            bot.send_message(message.chat.id, 'Неверный ввод. Рост должен быть в диапозоне 70-300 см.')
            bot.register_next_step_handler(message, get_height)

def get_weight(message):
    global weight
    try:
        weight = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат!!!')
        bot.register_next_step_handler(message, get_weight)
    else:
        if 5 <= weight <= 200:
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('женский', callback_data='female')
            btn2 = types.InlineKeyboardButton('мужской', callback_data='male')
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, 'Выбери пол', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Неверный ввод. Вес должен быть в диапозоне 5-200 кг.')
            bot.register_next_step_handler(message, get_weight)



@bot.callback_query_handler(func = lambda call: call.data.endswith('male'))
def get_gender(call):
    global gender
    if call.data == 'female':
        gender = -161
    else:
        gender = 5

    markup = types.InlineKeyboardMarkup(row_width=1, )
    btn1 = types.InlineKeyboardButton('Нет физических нагрузок', callback_data='activ_1.2')
    btn2 = types.InlineKeyboardButton('Лёгкие физические нагрузки, прогулки в течение дня', callback_data='activ_1.375')
    btn3 = types.InlineKeyboardButton('Хорошая ежедневная активность, тренировки 3-5 раз в неделю', callback_data='activ_1.46')
    btn4 = types.InlineKeyboardButton('Тренировки, прогулки, физический труд 5-6 раз в неделю', callback_data='activ_1.55')
    btn5 = types.InlineKeyboardButton('Высокая физическая активность 6-7 раз в неделю', callback_data='activ_1.725')
    btn6 = types.InlineKeyboardButton('Спортсмены в период соревновательной активности', callback_data='1.9')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(call.message.chat.id, 'Выбери уровень активности', reply_markup=markup)



@bot.callback_query_handler(func = lambda call: call.data.startswith('activ'))
def calculate_calorie_base(call):
    global coefficient, base, protein, fiber, carbs, mini_cal
    coefficient = float(call.data.split('_')[-1])
    mini_cal = round(10 * weight + 6.25 * height - 5 * age + gender, 2)
    base = round(mini_cal * coefficient, 2)
    protein[0] = round(weight * 0.8, 2)
    fiber[0] = round(weight * 0.8, 2)
    carbs[0] = round(weight * 2, 2)
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Похудение',
                                      callback_data='weight_loss')
    btn2 = types.InlineKeyboardButton('Набор мышечной массы',
                                      callback_data='gaining_muscle')
    btn3 = types.InlineKeyboardButton('Поддержание',
                                      callback_data='maintenance')
    markup.add(btn1, btn2, btn3)
    bot.send_message(call.message.chat.id, 'Какая цель?', reply_markup=markup)


@bot.callback_query_handler(func = lambda call: call.data=='start')
def calorie(call):
    get_info(call.message)

@bot.callback_query_handler(func = lambda call: call.data=='nutrient')
def nutr(call):
    product_list(call.message)

@bot.message_handler(commands=['calorie'])
def get_info(message):
    bot.send_message(message.chat.id, 'Введи кол-во полных лет.')
    bot.register_next_step_handler(message, get_age)


@bot.message_handler(commands=['products'])
def product_list(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Где содержится белок?', callback_data='nutr_protein')
    btn2 = types.InlineKeyboardButton('Где содержаться жиры?', callback_data='nutr_fats')
    btn3 = types.InlineKeyboardButton('Где содержаться углеводы?', callback_data='nutr_carbs')
    markup.add(btn1, btn2, btn3)
    text = load_message('nutrients')
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('nutr_'))
def give_list(call):
    file_name = call.data.split('_')[-1]
    text = load_message(file_name)
    photo = open(' resourses/images/'+file_name+'.jpg', 'rb')
    markup =create_initial_buttons()
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, text)
    bot.send_message(call.message.chat.id,'Надеюсь было полезно!🙂', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def calculate_calorie(call):
    global norm
    if call.data == 'weight_loss':
        norm[0] = round(0.75 * base, 2)
        norm[1] = round(0.85 * base, 2)
        protein[1] = round(norm[0] / 4 * 0.3, 2)
        protein[2] = round(norm[1] / 4 * 0.3, 2)
        fiber[1] = round(norm[0] / 9 * 0.25, 2)
        fiber[2] = round(norm[1] / 9 * 0.3, 2)
        carbs[1] = round(norm[0] / 4 * 0.4, 2)
        carbs[2] = round(norm[1] / 4 * 0.45, 2)
    elif call.data == 'gaining_muscle':
        norm[0] = round(1.15 * base, 2)
        norm[1] = round(1.2 * base, 2)
        protein[1] = round(norm[0] / 4 * 0.3, 2)
        protein[2] = round(norm[1] / 4 * 0.35, 2)
        fiber[1] = round(norm[0] / 9 * 0.25, 2)
        fiber[2] = round(norm[1] / 9 * 0.3, 2)
        carbs[1] = round(norm[0] / 4 * 0.45, 2)
        carbs[2] = round(norm[1] / 4 * 0.55, 2)
    else:
        norm[0] = round(0.95 * base, 2)
        norm[1] = round(1.05 * base, 2)
        protein[1] = round(norm[0] / 4 * 0.3, 2)
        protein[2] = round(norm[1] / 4 * 0.3, 2)
        fiber[1] = round(norm[0] / 9 * 0.3, 2)
        fiber[2] = round(norm[1] / 9 * 0.3, 2)
        carbs[1] = round(norm[0] / 4 * 0.4, 2)
        carbs[2] = round(norm[1] / 4 * 0.4, 2)

    bot.send_message(call.message.chat.id, f'Суточная норма калорий: {base} ккал\n'
                                           f'Базовый метаболизм: {mini_cal} ккал\n'

                                           f'Норма калорий для достижния цели: {norm[0]} - {norm[1]} ккал\n'
                                           f'БЖУ:\n' +
                     '🥩белки🥩' + f'\n\t\t\t\tминимально: {protein[0]} г.\n\t\t\t\tрекомендуемо: {protein[1]} - {protein[2]} г\n'
                                 '🌰жиры🌰' + f'\n\t\t\t\tминимально: {fiber[0]} г.\n\t\t\t\tрекомендуемо: {fiber[1]} - {fiber[2]} г\n'
                                            '🥔углеводы🥔' + f'\n\t\t\t\tминимально: {carbs[0]} г.\n\t\t\t\tрекомендуемо: {carbs[1]} - {carbs[2]} г')
    markup = create_initial_buttons()
    bot.send_message(call.message.chat.id, 'Удачи в достижении цели!🤞\n', reply_markup=markup)

bot.polling(none_stop=True)
