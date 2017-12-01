#coding:utf-8

import telepot

token = "481983440:AAEtfnMsArVAjPqG3h5p8S0FMDBMRdu263I"
telegram = telepot.Bot(token)

codigo = telegram.getUpdates()
print(codigo)
while True:
    pass