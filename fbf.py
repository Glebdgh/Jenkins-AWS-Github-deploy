from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
import telebot

owm = OWM('c87891ae5cab91c103c2d295135e25a0')
owm.supported_languages
mgr = owm.weather_manager()
bot = telebot.TeleBot("1661746602:AAHVuG46hW7zqevDbw22ld9MRgt3AyPNZI0")

@bot.message_handler(content_types=['text'])
def send_echo(message):
  try:
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    hum = w.get_humidity()
    time = w.get_reference_time(timeformat='iso')
    wind = w.get_wind()["speed"]

    answer ="В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n" + "\nСкорость ветра: " + str(wind) + "м/с" + "\n" + "\nВлажность: " + str(hum) + "%" + "\n" + "\nВремя: " + str(time) + "\n"

    if temp < 11:
      answer += "Сейчас очень холодно."
    elif temp < 20:
      answer += "Сейчас прохладно, лучше одеться потеплее."
    else:
      answer += "Температура в норме!"

    bot.send_message(message.chat.id, answer)
  except:
    bot.send_message(message.chat.id,'Ошибка! Город не найден.')
bot.polling( none_stop = True)
input()
	
