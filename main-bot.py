import requests
import botogram
import os
import time

bot = botogram.create("your telegram api key")

@bot.process_message
def fsa(chat,message):
    if message.document:
        message.document.save("PINO"+".apk")
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': 'your virus total api'}
        files = {'file': ('PINO.APK', open('PINO.APK', 'rb'))}
        response = requests.post(url, files=files, params=params)
        chat.send(str(response.content),syntax="html")

if __name__ == "__main__":
    bot.run()
