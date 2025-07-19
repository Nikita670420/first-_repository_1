from telebot import TeleBot
from telebot.types import  InlineKeyboardMarkup, InlineKeyboardButton



def key_bord_1():
    # Создаём объекты кнопок
    button_1 = InlineKeyboardButton(text='20 часов', callback_data='button_1_and_key_bord_1')
    button_2 = InlineKeyboardButton(text='2 дня', callback_data='button_2_and_key_bord_1')
    button_3 = InlineKeyboardButton(text='неделю', callback_data='button_3_and_key_bord_1')
    button_4 = InlineKeyboardButton(text='40 часов', callback_data='button_4_and_key_bord_1')

    # Создаём объект клавиатуры с кнопками
    key_bord = InlineKeyboardMarkup()
    key_bord.add(button_1, button_2, button_3, button_4)
    return key_bord


def key_bord_2():
    # Создаём объекты кнопок
    button_1 = InlineKeyboardButton(text='100 килограмм', callback_data='button_1_and_key_bord_2')
    button_2 = InlineKeyboardButton(text='1 тонна (1000 килограмм)', callback_data='button_2_and_key_bord_2')
    button_3 = InlineKeyboardButton(text='350 килограмм', callback_data='button_3_and_key_bord_2')
    button_4 = InlineKeyboardButton(text='500 килограмм', callback_data='button_4_and_key_bord_2')

    # Создаём объект клавиатуры с кнопками
    key_bord = InlineKeyboardMarkup()
    key_bord.add(button_1, button_2, button_3, button_4)
    return key_bord


def key_bord_3():
    # Создаём объекты кнопок
    button_1 = InlineKeyboardButton(text='100 лет', callback_data='button_1_and_key_bord_3')
    button_2 = InlineKeyboardButton(text='99 лет', callback_data='button_2_and_key_bord_3')
    button_3 = InlineKeyboardButton(text='101 год', callback_data='button_3_and_key_bord_3')
    button_4 = InlineKeyboardButton(text='116 лет', callback_data='button_4_and_key_bord_3')

    # Создаём объект клавиатуры с кнопками
    key_bord = InlineKeyboardMarkup()
    key_bord.add(button_1, button_2, button_3, button_4)
    return key_bord


def key_bord_4():
    # Создаём объекты кнопок
    button_1 = InlineKeyboardButton(text='Дубай', callback_data='button_1_and_key_bord_4')
    button_2 = InlineKeyboardButton(text='Урал', callback_data='button_2_and_key_bord_4')
    button_3 = InlineKeyboardButton(text='Эверест', callback_data='button_3_and_key_bord_4')
    button_4 = InlineKeyboardButton(text='Альпы', callback_data='button_4_and_key_bord_4')

    # Создаём объект клавиатуры с кнопками
    key_bord = InlineKeyboardMarkup()
    key_bord.add(button_1, button_2, button_3, button_4)
    return key_bord

def key_bord_5():
    # Создаём объекты кнопок
    button_1 = InlineKeyboardButton(text='Баба Яга', callback_data='button_1_and_key_bord_5')
    button_2 = InlineKeyboardButton(text='Кощей Бессмертный', callback_data='button_2_and_key_bord_5')
    button_3 = InlineKeyboardButton(text='Морок', callback_data='button_3_and_key_bord_5')
    button_4 = InlineKeyboardButton(text='Иван Царевич', callback_data='button_4_and_key_bord_5')

    # Создаём объект клавиатуры с кнопками
    key_bord = InlineKeyboardMarkup()
    key_bord.add(button_1, button_2, button_3, button_4)
    return key_bord


def key_bord_6():
    # Создаём объекты кнопок
    button_1 = InlineKeyboardButton(text='8 бит', callback_data='button_1_and_key_bord_6')
    button_2 = InlineKeyboardButton(text='32 бита', callback_data='button_2_and_key_bord_6')
    button_3 = InlineKeyboardButton(text='1 бит (они равны)', callback_data='button_3_and_key_bord_6')
    button_4 = InlineKeyboardButton(text='100 бит', callback_data='button_4_and_key_bord_6')

    # Создаём объект клавиатуры с кнопками
    key_bord = InlineKeyboardMarkup()
    key_bord.add(button_1, button_2, button_3, button_4)
    return key_bord



bot = TeleBot('') # Тут ставим токен бота
score = 0 # Баллы

@bot.message_handler(commands=['start'])
def start_message(callback_query):
    global score
    score = 0
    bot.send_message(callback_query.from_user.id, 'Привет! Вот тебе викторина!\n1 вопрос: сколько хранится коровье молоко при температуре в ноль градусов цельсия (в холодильнике)?', reply_markup=key_bord_1()) # Тут мы отравили клавиатуру


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'button_2_and_key_bord_1')
def good_answer_1(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    score += 1
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    # Отправляем сообщение пользователю
    bot.send_message(callback_query.from_user.id, f'Верно, этот ответ заслуживает балл!\nСейчас у вас {score} балл(а/ов)')
    question_2(callback_query.from_user.id)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ['button_1_and_key_bord_1', 'button_3_and_key_bord_1', 'button_4_and_key_bord_1'])
def false_answer_1(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    bot.send_message(callback_query.from_user.id, f'Извините, но ответ не верный. Этот ответ не заслуживает балла!\nСейчас у вас {score} балл(а/ов)')
    question_2(callback_query.from_user.id)


def question_2(user_id):
    bot.send_message(user_id, 'И так, теперь второй вопрос!\n2 вопрос: какой средний вес, у взрослого белого кабана?', reply_markup=key_bord_2())


@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'button_3_and_key_bord_2')
def good_answer_2(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    score += 1
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    # Отправляем сообщение пользователю
    bot.send_message(callback_query.from_user.id, f'Верно, этот ответ заслуживает балл!\nСейчас у вас {score} балл(а/ов)')
    question_3(callback_query.from_user.id)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ['button_1_and_key_bord_2', 'button_2_and_key_bord_2', 'button_4_and_key_bord_2'])
def false_answer_2(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    bot.send_message(callback_query.from_user.id, f'Извините, но ответ не верный. Этот ответ не заслуживает балла!\nСейчас у вас {score} балл(а/ов)')
    question_3(callback_query.from_user.id)


def question_3(user_id):
    bot.send_message(user_id, '3 вопрос: сколько шла столетняя война?', reply_markup=key_bord_3())

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'button_4_and_key_bord_3')
def good_answer_3(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    score += 1
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    # Отправляем сообщение пользователю
    bot.send_message(callback_query.from_user.id, f'Верно, этот ответ заслуживает балл!\nСейчас у вас {score} балл(а/ов)')
    question_4(callback_query.from_user.id)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ['button_1_and_key_bord_3', 'button_2_and_key_bord_3', 'button_3_and_key_bord_3'])
def false_answer_3(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    bot.send_message(callback_query.from_user.id, f'Извините, но ответ не верный. Этот ответ не заслуживает балла!\nСейчас у вас {score} балл(а/ов)')
    question_4(callback_query.from_user.id)


def question_4(user_id):
    bot.send_message(user_id, '4 вопрос: как называется самая высокая гора в мире?', reply_markup=key_bord_4())

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'button_3_and_key_bord_4')
def good_answer_4(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    score += 1
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    # Отправляем сообщение пользователю
    bot.send_message(callback_query.from_user.id, f'Верно, этот ответ заслуживает балл!\nСейчас у вас {score} балл(а/ов)')
    question_5(callback_query.from_user.id)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ['button_1_and_key_bord_4', 'button_2_and_key_bord_4', 'button_4_and_key_bord_4'])
def false_answer_4(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    bot.send_message(callback_query.from_user.id, f'Извините, но ответ не верный. Этот ответ не заслуживает балла!\nСейчас у вас {score} балл(а/ов)')
    question_5(callback_query.from_user.id)




def question_5(user_id):
    bot.send_message(user_id, '5 вопрос: как называется самый сильный злодей в русских мифах?', reply_markup=key_bord_5())

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'button_2_and_key_bord_5')
def good_answer_5(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    score += 1
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    # Отправляем сообщение пользователю
    bot.send_message(callback_query.from_user.id, f'Верно, этот ответ заслуживает балл!\nСейчас у вас {score} балл(а/ов)')
    question_6(callback_query.from_user.id)


@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ['button_1_and_key_bord_5', 'button_3_and_key_bord_5', 'button_4_and_key_bord_5'])
def false_answer_5(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    bot.send_message(callback_query.from_user.id, f'Извините, но ответ не верный. Этот ответ не заслуживает балла!\nСейчас у вас {score} балл(а/ов)')
    question_6(callback_query.from_user.id)




def question_6(user_id):
    bot.send_message(user_id, '6 вопрос: 1 байт - это сколько бит?', reply_markup=key_bord_6())

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == 'button_1_and_key_bord_6')
def good_answer_6(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    score += 1
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    # Отправляем сообщение пользователю
    bot.send_message(callback_query.from_user.id, f'Верно, этот ответ заслуживает балл!\nСейчас у вас {score} балл(а/ов)')
    final_scoring(callback_query)



@bot.callback_query_handler(func=lambda callback_query: callback_query.data in ['button_2_and_key_bord_6', 'button_3_and_key_bord_6', 'button_4_and_key_bord_6'])
def false_answer_6(callback_query):
    if callback_query.from_user.is_bot:
        return  # Не отвечаем ботам
    global score
    # Удаляем клавиатуру
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.id)
    bot.send_message(callback_query.from_user.id, f'Извините, но ответ не верный. Этот ответ не заслуживает балла!\nСейчас у вас {score} балл(а/ов)')
    final_scoring(callback_query)



def final_scoring(callback_query):
    global score
    final_score = (int(score) / 6) * 100
    bot.send_message(callback_query.from_user.id, f'И так, вы прошли викторину. Ваш результат {final_score}% из возможных 100%')
    if final_score < 33:
        bot.send_message(callback_query.from_user.id, f'Это, скажем так, не лучший из возможных результатов. ☹️')
    if 33 <= final_score < 66:
        bot.send_message(callback_query.from_user.id, f'Вы прошли тест, и получили среднюю оценку. Это хорошо, но есть оценки выше. Тренируйтесь, и у вас всё получится 😁')
    if 66 <= final_score:
        bot.send_message(callback_query.from_user.id, f'Вы отлично прошли тест! 👏👏👏')


if __name__ == '__main__':
    bot.infinity_polling()