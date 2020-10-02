import tweepy, config, requests, json, time
from datetime import datetime

print('This is a twitter bot')

minutes = datetime.now().minute

from config import CONSUMER_KEY
from config import CONSUMER_SECRET
from config import ACCESS_KEY
from config import ACCESS_SECRET
from config import WEATHER_KEY

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
COMPLETE_URL = BASE_URL + "appid=" + WEATHER_KEY + '&q=' + 'Harrisonburg'
response = requests.get(COMPLETE_URL)
x = response.json()
if x['cod'] != '404':
    y = x['main']
    #convert Kelving to Farhenheit
    current_temp = round((y['temp'] - 273.15) * 9/5 + 32)
    z = x['weather']
    weather_desciption = z[0]['description']
else:
    print('City Not Found')

def tweet():
    print('Checking time')
    if minutes == 0 or minutes == 30:
        api.update_status(weather_desciption + ' with a current temperature of ' + str(current_temp) + 
            ' degrees Fahrenheit in Harrisonburg, VA')

while True:
    tweet()
    time.sleep(60)