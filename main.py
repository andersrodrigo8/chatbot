#!/usr/bin/python3

#coding: utf-8

from Chatbot import Chatbot

Bot = Chatbot("Stive_robot")

while True:
    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)

    if resp == 'tchau':
        break