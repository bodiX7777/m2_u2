import telebot
import time 
from telebot import types
from settings import TG_API_TOKEN
bot = telebot.TeleBot(TG_API_TOKEN)
users = set()
@bot.message_handler(commands=['start'])
def start_command(message):
    text = (
        f'Привет, {message.from_user.first_name}!\n'
        'Этот бот был создан специально для того чтобы помогать подросткам, которые хотят улучшить экологию, но не знают как это сделать.\n'
        '/help - выводит список доступных команд'
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def help_command(message):
    text = (
        "Доступные команды:\n"
        "/start - начать работу с ботом\n"
        "/help - показать это сообщение\n" 
        "/reasons - причины загрязнений\n"
        "/improve - решение загрязнений\n"
    )
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['reasons', 'improve', 'recommend'])
def actions(message: types.Message):
    if message.chat.id not in users:
        if message.text == '/reasons':
            bot.send_message(message.chat.id, 'Ищу ответ...')
            bot.send_message(message.chat.id, 'Вот что я нашел:')
            bot.send_message(message.chat.id, '1.Промышленность📡')
            bot.send_message(message.chat.id, '2. Транспорт🏍')
            bot.send_message(message.chat.id, '3.Бытовые отходы🧽')
            bot.send_message(message.chat.id, '4.Сельское хозяйство🐑')
            time.sleep(2)
            bot.send_message(message.chat.id, 'Если хочеш узнать больше переходи на сайт:https://www.prom-terra.ru/articles/ekologicheskie-problemy-i-puti-ikh-resheniya.html')
            bot.send_message(message.chat.id, '')
        if message.text == '/improve':
            bot.send_message(message.chat.id, 'Ищу ответ...')
            bot.send_message(message.chat.id, 'Вот что я нашел:')
            bot.send_message(message.chat.id, '1. Сокращение выбросов парниковых газов💨')
            bot.send_message(message.chat.id, '2. Переход на возобновляемые источники энергии🔋')
            bot.send_message(message.chat.id, '3. Сохранение лесов и природных экосистем🌿')
            bot.send_message(message.chat.id, '4. Повышение энергоэффективности📈')
            time.sleep(2)
            bot.send_message(message.chat.id, 'Если хочеш узнать больше переходи на сайт: https://www.un.org/en/actnow/ten-actions?utm_source=chatgpt.com')
        elif message.text == '/recommend':
            bot.send_message(message.chat.id, 'Я рекомендую вам посмотреть видео про зеленую планету на YouTube: https://www.youtube.com/watch?v=2zH5D3m5b0k')

bot.polling()        