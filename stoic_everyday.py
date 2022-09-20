#!/bin/bash/python3
import schedule
import time
import telebot
# import json
import requests
bot = telebot.TeleBot('5559189237:AAFD8BE_PDQqaHs0Pcd3zcUuafpzWwVdFkI')
chat_id = [922758956]

def sendd():
  gita()
  bot.send_message(chat_id[0], ""+ body + "\n\nAuthor: "+ author)

def gita():
    # complete_api_link = "https://bhagavadgitaapi.in/slok/15/13/"
    complete_api_link = "http://stoicquotesapi.com/v1/api/quotes/random"
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    global body
    body = api_data['body']
    global author
    author = api_data['author']
def testt():
    print("HELLO")
# schedule.every(4).seconds.do(sendd)
schedule.every().day.at("18:28:00").do(sendd)
schedule.every().day.at("00:30:00").do(sendd)
schedule.every().day.at("00:31:00").do(sendd)

while 1:
    schedule.run_pending()
    time.sleep(1)
