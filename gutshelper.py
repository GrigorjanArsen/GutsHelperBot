import telebot;
bot = telebot.TeleBot('6585659246:AAEMJTeganyeOYR7jP8pJwpOuGu7MPxQSFI');
start_txt = 'Привет, это Гатс. Мне наскучили эти бесконечные сражения, и я решил начать заниматься метеорологией. \n\nНапиши мне название города, а я скажу тебе, какая там сейчас погода.'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

import requests
city = 'Ирбит'
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
weather_data = requests.get(url).json()
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def weather(message):
    city = message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    w_now = 'Сейчас в городе ' + city + ' ' + str(temperature) + ' °C'
    w_feels = 'Ощущается как ' + str(temperature_feels) + ' °C'
    bot.send_message(message.from_user.id, w_now)
    bot.send_message(message.from_user.id, w_feels)
    wind_speed = round(weather_data['wind']['speed'])
    if wind_speed < 5:
        bot.send_message(message.from_user.id, '✅ Ветра почти нет, погодные условия не будут препятсвовать хорошей схватке.')
    elif wind_speed < 10:
        bot.send_message(message.from_user.id, '🤔 На улице ветрено, махать мечом будет немного труднее.')
    elif wind_speed < 20:
        bot.send_message(message.from_user.id, '❗️ Ветер очень сильный, но явно не сильнее тебя, воин.')
    else:
        bot.send_message(message.from_user.id, '❌ На улице шторм, сейчас не лучшее время для сражения.')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print('❌❌❌❌❌ Сработало исключение! ❌❌❌❌❌')







