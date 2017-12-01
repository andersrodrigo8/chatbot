import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as fala:
    rec.adjust_for_ambient_noise(fala)


    frase = rec.listen(fala)

speech = rec.recognize_google(frase, language='pt')

print(speech)