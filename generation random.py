from random import randint,shuffle

def generate_order():
    liste = list(range(1,301))


    for i in range(300):
        liste.append(randint(1,300))

    shuffle(liste)


    for i in liste:
        print(i)

def generate_size():
    liste =[]
    for i in range(600):
        liste.append(randint(1,50))
    for i in liste:
        print(i)



def generate_false():
    for i in range(600):
        print(False)

generate_false()

