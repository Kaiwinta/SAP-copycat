from random import randint,shuffle
liste = list(range(1,301))


for i in range(300):
    liste.append(randint(1,300))

shuffle(liste)


for i in liste:
    print(i)