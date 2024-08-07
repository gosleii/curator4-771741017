import telebot

bot = telebot.TeleBot('7396354402:AAHlEYdGVuqq01wozLIIT59CiyWYN-fSohQ')


@bot.message_handler(commands=['начнём'])
def main(message):
    bot.send_message(message.chat.id, text= 'Доброго времени суток! Вас приветствует бот *Фитнес-няшка*. Здесь вы найдёте короткие, эффективные тренировки, которые наиболее популярны на YOUTUBE', parse_mode='Markdown')

@bot.message_handler(commands=['руки'])
def main(message):
    bot.send_message(message.chat.id, text= '[Качаем руки](https://www.youtube.com/watch?v=LZadh0M13Bk&t=232s)', parse_mode='Markdown')

@bot.message_handler(commands=['пресс'])
def main(message):
    bot.send_message(message.chat.id, text= '[Качаем пресс](https://www.youtube.com/watch?v=OfmzNF4QFR8)', parse_mode='Markdown')

@bot.message_handler(commands=['ноги'])
def main(message):
    bot.send_message(message.chat.id,text= '[Качаем ноги](https://www.youtube.com/watch?v=5zbYHZRzTY0&t=9s)', parse_mode='Markdown')

@bot.message_handler(commands=['ягодицы'])
def main(message):
    bot.send_message(message.chat.id, text= '[Качаем ягодицы](https://www.youtube.com/watch?v=kksYxzDm62I)', parse_mode='Markdown')

@bot.message_handler(commands=['спина'])
def main(message):
    bot.send_message(message.chat.id,
         text= '[Качаем спину](https://www.youtube.com/watch?v=hDkUqX-Jy1Q)', parse_mode='Markdown')

@bot.message_handler(commands=['растяжка'])
def main(message):
    bot.send_message(message.chat.id,
             text= '[Растягиваемся](https://www.youtube.com/watch?v=X9hhzhwlVww)', parse_mode='Markdown')

bot.infinity_polling()