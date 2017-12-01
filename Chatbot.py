#coding: utf-8

import subprocess as s
import os
import sys
import json
import speech_recognition as sr
import pyttsx3

#speak = pyttsx3.init('sapi5')

struct = {}

class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome+'.json', 'r')
            memoria1 = open(nome + '1' + '.json', 'r')
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria1 = open(nome + '1' + '.json', 'w')
            memoria.write('["Anderson", "Glauco", "Marlos", "Abreu"]')
            memoria1.write('{"oi": "Olá, qual o seu nome?", "tchau": "tchau"}')
            memoria.close()
            memoria1.close()
            memoria = open(nome + '.json', 'r')
            memoria1 = open(nome + '1' + '.json', 'r')
        self.nome = nome
        self.conhecidos = json.load(memoria)
        self.frases = json.load(memoria1)
        memoria.close()
        memoria1.close()
        self.historico = [None]

    def escuta(self, frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        frase = frase.lower()
        frase = frase.replace('eh', 'é')
        return frase


    def pensa(self, frase):
        try:
            if frase in self.frases:
                return self.frases[frase]
            if frase == 'aprende':
                return 'Digite a frase: '

                resp = input('Digite a resposta: ')
                self.frases[chave] = resp
                self.gravaMemoria()
                return 'Aprendido'

            ultimafrase = self.historico[-1]
            if ultimafrase == 'Olá, qual o seu nome?':
                nome = self.pegaNome(frase)
                frase = self.respondeNome(nome)
                return frase
            if ultimafrase == 'Digite a frase: ':
                self.chave = frase
                return 'Digite a resposta: '
            if ultimafrase == 'Digite a resposta: ':
                resp = frase
                self.frases[self.chave] = resp
                self.gravaMemoria()
                return 'Aprendido'

            try:
                resp = str(eval(frase))
                return resp
            except:
                pass
            return 'Não entendi!'
        except:
            return 'Não entendi!'


    # pega o nome do usuario
    def pegaNome(self, nome):
        if 'o meu nome é ' in nome:
            nome = nome[13:]
        elif 'eu me chamo ' in nome:
            nome = nome[12:]
        elif ' é o meu nome' in nome:
            nome = nome[0:-12]
        elif 'eu me chamo ' in nome:
            nome = nome[12:]
        nome = nome.title()
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Olá como vai '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase + nome


    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        memoria1 = open(self.nome + '1' + '.json', 'w')
        json.dump(self.conhecidos, memoria)
        json.dump(self.frases, memoria1)
        memoria.close()
        memoria1.close()

    def fala(self, frase):
        if 'executa ' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa ', '')
            if 'win' in plataforma:
                os.startfile(comando)
            try:
                if 'linux' in plataforma:
                    s.Popen(comando)
            except FileNotFoundError:
                s.Popen(['xdg-open', comando])

        else:
            print(frase)
        self.historico.append(frase)