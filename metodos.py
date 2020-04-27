import playsound
import random
import time

def tocar(lista):
    for i in range (len(lista)):
        if lista[i] == 'c':
           playsound.playsound('do.wav')
        if lista[i] == 'd':
            playsound.playsound('re.wav')
        if lista[i] == 'e':
            playsound.playsound('mi.wav')
        if lista[i] == 'f':
            playsound.playsound('fa.wav')
        if lista[i] == 'g':
            playsound.playsound('sol.wav')
        if lista[i] == 'a':
            playsound.playsound('la.wav')
        if lista[i] == 'b':
            playsound.playsound('si.wav')


def iniciar( lista, notas):
    lista.clear()
    item = random.choice(list(notas))
    lista.append(item)
    print("a primeira nota é " + lista[-1])
    tocar(lista)
    for x in range(3,0,-1):
        print(x)
        time.sleep(1)
value = 1
def perguntar(lista,notas):
    item = random.choice(list(notas))
    answer = lista + [item]
    print("Escute...    ")
    tocar(answer)
    #print(answer)
    attempt = list(input("digite as notas na sequencia tocada ------ "))
    return attempt, answer
