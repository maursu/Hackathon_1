import telebot
from hard_parsing import main

token = '5977812960:AAHQFos8CmDB0fiVApWINi9KHmTPZ_8B5yU'

bot = telebot.TeleBot(token)


@bot.message_handler(['start'])
def start_message(message):
    global d
    d = main()
    titles = "\n".join(d[1])
    print(message)
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.first_name}")
    bot.send_message(message.chat.id, f"Подборка новостей за сегодня: ")
    bot.send_message(message.chat.id, f'{titles}')
    bot.send_message(message.chat.id, f'Введите цифру от 1 до 20, чтобы выбрать новость')
    bot.register_next_step_handler(message, choose)

def choose(message):
    if message.text.isdecimal():
        num = int(message.text)
        try:
            bot.send_message(message.chat.id, f'{d[2][num-1]}')
        except:
            bot.send_message(message.chat.id, f'Такой новости нет, перезапустите бота')
    elif message.text.lower() == 'quit':
        bot.send_message(message.chat.id, f'До свидания!')
    


    
    

bot.polling()


        