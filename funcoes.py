# capturando a resposta do usuario
def resposta():
    resp = input('>: ')
    resp = resp.lower()
    resp = resp.replace('eh', 'é')
    return resp

# pega o nome do usuario
def pegaNome(nome):
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

def respondeNome(nome):
    conhecidos = ['Marlos', 'Anderson', 'Glauco', 'Abreu']
    if nome in conhecidos:
        frase = 'Olá como vai '
    else:
        frase = 'Muito prazer '
    return frase+nome

def speaker(text):
    speak.say(text)
    speak.runAndWait()