"""
This part is the logical part between the class and the tkinter interface, it muss also communicate with the database
"""
import sqlite3

conn = sqlite3.connect('Product.db')
c = conn.cursor()

conn2 = sqlite3.connect('Command.db')
d = conn2.cursor()

def search_price(ref):
    """Search the price annd some spec of the object

    Args:
        ref (int): the ref of a product in the database

    Returns:
        list: the list of price, product_name and color
    """
    return c.execute(f"SELECT price,product_name,color FROM Productlisted WHERE ref_product =  {ref}").fetchall()

def charging_package(order_ref):
    """Is used when you scan a new order, find all the packages that are contained

    Args:
        order_ref (int): the ref of the order in the database

    Returns:
        list: the list of all the packages ref
    """
    result = d.execute(f"SELECT * FROM Package WHERE id_command = {order_ref}").fetchall()
    return result

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
        #Pas sur de ça vu que la fonction de création utilise un tuple (produit, quantité)
        for line in range(row[1]):
            liste_product_ref.append(row[0])
    return liste_product_ref
    

def creating_package(order_ref : int):
    result = d.execute(f"SELECT * FROM Orders WHERE idorder = {order_ref}").fetchall()[0]
    return result
    
result = search_price(2)
print(charging_product(2))
creating_package(1)