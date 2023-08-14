"""
This part is the logical part between the class and the tkinter interface, it muss also communicate with the database
"""
import sqlite3


conn = sqlite3.connect('Product.db')
c = conn.cursor()

conn2 = sqlite3.connect('Command.db')
d = conn2.cursor()

def search_price(ref):
    return c.execute(f"SELECT price,product_name,color FROM Productlisted WHERE ref_product =  {ref}").fetchall()

def charging_package(order_ref):
    result = d.execute(f"SELECT * FROM Package WHERE id_command = {order_ref}").fetchall()

def charging_product(package_ref: int):
    """Permet de chercher toutes les ref de produit contenu dans un package

    Args:
        package_ref (int): the ref of the package that we want

    Returns:
        list: the list of all the product ref contained
    """
    result = d.execute(f"SELECT Product_ref, nombre FROM Product WHERE id_package = {package_ref}").fetchall()
    liste_product_ref = []
    for row in result:
        print(row)
        #Pas sur de ça vu que la fonction de création utilise un tuple (produit, quantité)
        for line in range(row[1]):
            liste_product_ref.append(row[0])
    return liste_product_ref
    
result = search_price(2)
print(charging_product(2))