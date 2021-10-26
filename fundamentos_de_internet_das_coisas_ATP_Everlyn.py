#Everlyn Borges de Oliveira

import dht
import machine
import time
from wifiLib import conecta
import urequests

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

print("Conectando")
station = conecta("Oi Fibra-Thiago e Everlyn 2G", "senha")
if not station.isconnected():
    print("Não conectado!")
else:
    print("Conectado!")
    print("Acessando o site...")

while True:
    d.measure()
    print("Temp={} Umid={}".format(d.temperature(), d.humidity()))
    
    resposta = urequests.get("https://api.thingspeak.com/update?api_key=A7TJA5RARDBQAHE2&field1={}&field2={}".format(d.temperature(), d.humidity()))
    print('resposta', resposta.text)
    
    if d.temperature() > 31 or d.humidity() > 70:
        r.value(1)
    else:
        r.value(0)
    
    time.sleep(2)