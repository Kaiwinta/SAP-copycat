from random import randint,shuffle
import sqlite3
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


def listing():
    liste_commande_id = c.execute("SELECT id_command, size FROM Package").fetchall()
    
    return liste_commande_id

def creating_product(lsite_id):
    for i in range(len(lsite_id)):
        
        for y in range(lsite_id[i][1]):
           
            c.execute(f"INSERT INTO Product (Product_ref,id_package) VALUES ({randint(1,50)},{lsite_id[i][0]})")
            
            print('fait')
    
conn = sqlite3.connect('Command.db')
c = conn.cursor()

liste = listing()
creating_product(liste)
conn.commit()
conn.close()