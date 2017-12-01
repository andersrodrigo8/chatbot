#!/usr/bin/python3


#coding: utf-8

import telepot
from Chatbot import Chatbot


token = "481983440:AAEtfnMsArVAjPqG3h5p8S0FMDBMRdu263I"
telegram = telepot.Bot(token)
bot = Chatbot("Stive_robot")


def recebendoMsg(msg):
    frase = bot.escuta(frase=msg['text'])
    firstname = msg['chat']['first_name']
    lastname = msg['chat']['last_name']

    if firstname == 'Anderson' and lastname == 'Rodrigo':
        resp = bot.pensa(frase)
        bot.fala(resp)
        #chatID = msg['chat']['id']
        tipoMsg, tipoChat, chatID = telepot.glance(msg)
        telegram.sendMessage(chatID,resp)
    else:
        tipoMsg, tipoChat, chatID = telepot.glance(msg)
        telegram.sendMessage(chatID, 'Não estou autorizado a falar!')

telegram.message_loop(recebendoMsg)

while True:
    pass