name = input("¿Como te llamas? ")
cofe = input("Cuanto café tomas al día? ")
sleep = input("Cuantas horas duermes al día? ")

energy = int(cofe) * 10 - int(sleep) * 5
print(f"{name}, tu nivel de energía es {energy}.")