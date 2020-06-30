from forex_python.converter import CurrencyRates
import telebot

token = '1334282732:AAH-FaV6KVbAWzoUxHbXvYb96mc8aT19Xfs'
bot = telebot.TeleBot(token)
rate = CurrencyRates().get_rates('RUB')
currencies = ['USD', 'EUR', 'SEK']


# обработчик команды start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
'''Данный бот показывает текущий курс валют к рублю.
Введите команду /currency для получения списка валют.''')


# Обработчик команды currency и создание кнопок
@bot.message_handler(commands=['currency'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    for name in currencies:
        keyboard.add(name)
    bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=keyboard)


# Вывод курса
@bot.message_handler(content_types=['text'])
def send_text(message):
    for name in currencies:
        if message.text == name:
            bot.send_message(message.chat.id,
                             f'Курс {name} на данный момент составляет: {1 / rate.get(name)} RUB')
            break
    else:
        bot.send_message(message.chat.id, 'Данной монеты нет в списке')


bot.polling()