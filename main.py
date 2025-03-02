#IMPORTS
import telebot
from googletrans import Translator
from telebot import types
from Class.weather_class import Weather
import consts as keys
from APIs.user_data import generate_user_data
from APIs.Weather import get_weather
from Class.user import UserData

#CREATE BOT
bot = telebot.TeleBot(keys.TELEGRAM_KEY)

#INITIALIZATION TRANSLATOR 
translator = Translator()

#MENU
@bot.message_handler(commands=["start"])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2 )
    start = types.KeyboardButton('Отримати підставну інформацію про користувача🌐')
    weather = types.KeyboardButton('Погода☀️')
    help = types.KeyboardButton('Інформація про бота📝')
    markup.add(start, help,weather)
    bot.send_message(message.chat.id, f'Привіт, <b>{message.from_user.first_name}</b>, мене звати <b>Weather BOT</b>😊😉️'
                                      f'\nЩоб продовжити розмову, виберіть дію нижче:\n ', reply_markup=markup, parse_mode='html')

#CREATE INFO
@bot.message_handler(regexp="/hacker|Отримати підставну інформацію про користувача🌐")
def create_user_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    Button = types.KeyboardButton('⬅️Назад')
    markup.add(Button)
    data =  UserData(generate_user_data())
    # data = User(generate_user_data())
    if data:
        # print(User(data))
        response = (
                f"<b>Рід:</b> {translator.translate(data.gender, src='en', dest='uk').text}\n\n"
                f"<b>Ім'я:</b> {data.name_title} {data.name_first} {data.name_last}\n"
                f"<b>Повних років:</b> {data.age}\n" 
                f"<b>Адреса:</b> {data.street_number} {data.street_name}, {data.city}, {data.state}, {data.country}\n"
                f"<b>Поштовий індекс:</b> {data.postcode}\n\n"
                f"<b>Email:</b> {data.email}\n"
                f"          <b>Username:</b> {data.username}\n"
                f"          <b>Password:</b>  {data.password}\n\n"
                f"<b>Дата народження:</b> {data.dob_date}\n"
                f"<b>Телефон:</b> {data.phone}\n"
                f"<b>Мобільний телефон:</b> {data.cell}\n"
        )

        bot.send_message(message.chat.id, response, reply_markup=markup, parse_mode='html')
        bot.register_next_step_handler(message, get_weather_by_city)
    else:
        bot.send_message(message.chat.id, "Ох, вибачте, щось піщло не так")

#WEATHER COMMAND
@bot.message_handler(regexp="/weather|Погода☀️")
def find_city_for_weather(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    Button = types.KeyboardButton('⬅️Назад')
    markup.add(Button)
    mess = 'Погоду якого міста хочете знайти?'
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')
    bot.register_next_step_handler(message, get_weather_by_city)


def weather_check(message):
    if message.text == "↩️Інше місто":
        find_city_for_weather(message)
    elif message.text == "На головну🏠":
        menu(message)
    else:
        bot.send_message(message.chat.id,"Вибачте, не розумію про що ви🌚. Виберіть іншу дію")
        weather_check()


def get_weather_by_city(message):
    if message.text == "⬅️Назад":
        menu(message)
    else:
        if hasattr(message, 'text') and message.text:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            home = types.KeyboardButton('На головну🏠')
            another_city = types.KeyboardButton('↩️Інше місто')
            markup.add(another_city,home)
            city = message.text
            weather_data = get_weather(city)
            if weather_data:
                parsed_data = Weather(weather_data)
                print(parsed_data,"\n----------------------------")
                response = (
                    f"<b>Погода в місті {translator.translate(parsed_data.name, src='en', dest='uk').text}</b>🌃 станом на <i>{Weather.curentTime()}</i>:\n\n"
                    f"<b>Погодні умови🌥:</b> {translator.translate(parsed_data.weather.get('description', ''),src='en', dest='uk').text} \n"
                    f"<b>Температура🌡:</b> {parsed_data.main.get('temp', 0)}°C\n"
                    f"<b>Відчувається як:</b> {parsed_data.main.get('feels_like', 0)}°C\n"
                    f"<b>Вологість:</b> {parsed_data.main.get('humidity', 0)}%\n"
                    f"<b>Швидкість вітру💨:</b> {parsed_data.wind.get('speed', 0)} м/с\n\n"
                    f"<b>Світанок🌅:</b> {Weather.timestampToHoursMinutes(parsed_data.sys.get('sunrise', 0))}\n"
                    f"<b>Захід сонця🌆:</b> {Weather.timestampToHoursMinutes(parsed_data.sys.get('sunset', 0))}\n"

                )
                bot.send_message(message.chat.id, response,reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, weather_check)
            else:
                bot.send_message(message.chat.id, f"Вибачте, не вдалось знайти погоду для міста {city}. Спробуйте знову:")
                bot.register_next_step_handler(message, get_weather_by_city)

        else:
            bot.send_message(message.chat.id, "Вибачте, виберіть правильний формат повідомлення.")
            bot.register_next_step_handler(message, get_weather_by_city)

#INFO
@bot.message_handler(regexp="/info|Інформація про бота📝")
def info(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    Button = types.KeyboardButton('⬅️Назад')
    markup.add(Button)
    mess = f'Слава Україні! 🇺🇦\n' \
           f'Мене звати Weather BOT😁. Я твій особистий помічник.\n' \
           f'\nЯ створений для зручного використання деяких можливостей інтернету прямо в Telegram😉🙃.\n' \
           f'\nАвтором бота є студентка групи ПП-27 \nСоханська Вікторія Юріївна😎\n' \
           f'aka @Vikkii02\n' \
           f'\n\nЯкщо ви хочете якось підтримати цей проект та особисто розробницю, найкращою допомогою буде найвищий бал з курсової 🤪\n' \
           
    bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')

    def wait_for_back_button(message):
        if message.text == "⬅️Назад":
            menu(message)  
        else:
            bot.send_message(message.chat.id, "Вибачте, не розумію вашого вибору. Будь ласка, натисніть кнопку '⬅️Назад'.")
            bot.register_next_step_handler(message, wait_for_back_button)  
    bot.register_next_step_handler(message, wait_for_back_button) 

#HOME PAGE
@bot.message_handler(regexp="На головну🏠")
def home(message):
    menu(message)


#STICKER HANDLER
@bot.message_handler(content_types=['sticker'])
def sticker(message):
   bot.reply_to(message,'Неправильний формат повідомлення😕')

#START SERVER
print('Bot started')
bot.polling(none_stop=True)
