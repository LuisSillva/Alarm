import pytz
from datetime import datetime 
from playsound import playsound
import tkinter as tk


# BACK-END
br_tz = pytz.timezone('America/Sao_Paulo')

def validacao_alarme(tempo_alarme):

    if len(tempo_alarme) != 5:
        return "Formato de horário inválido! Por favor, tente novamente..."
    else:
        if int(tempo_alarme[0:2]) > 24:
            return "HORA inválida! Por favor, tente novamente..."
        elif int(tempo_alarme[3:5]) > 59:
            return "MINUTO inválido! Por favor, tente novamente..."
        else:
            return "Ok."

while True:
    tempo_alarme = input("Informe o horário desejado no seguinte formato 'HH:MM' - ")
    
    validacao = validacao_alarme(tempo_alarme.lower())
    if validacao != "Ok.":
        print(validacao)
    else:
        print(f"Configurando alarme para {tempo_alarme}...")
        break

hora_alarme = tempo_alarme[0:2]
minuto_alarme = tempo_alarme[3:5]

while True:

    agora = datetime.now(br_tz)

    hora_atual = agora.strftime("%H")
    minuto_atual = agora.strftime("%M")

    if int(hora_atual) == int(hora_alarme):
        if int(minuto_atual) == int(minuto_alarme):
            print("Acorde!")
            playsound('D:\Arquivos\zvivaldi-winter_ending.mp3')
            break
