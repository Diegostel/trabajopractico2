import random
datos= {"fichas": 50,"probabilidad": 0.4, "maximo": 300}

def NDJ(datos):
    fichas = datos["fichas"]
    maximo = datos["maximo"]
    p = datos["probabilidad"]
    intentos = 0 
    while ((fichas > 0) and (intentos < maximo)):
        intentos += 1
        sorteo = random.random()
        if (p > sorteo):
            fichas += 1
            #print("apuesto y gano")
        else: 
            fichas -= 1
            #print("apuesto y pierdo")
            #print(intentos, fichas)
    return intentos, fichas

resultado = NDJ(datos)
print(f"intentos: {resultado[0]}\n Fichas restantes: {resultado[1]}")
