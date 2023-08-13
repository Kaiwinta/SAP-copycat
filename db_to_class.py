"""
This part is the logical part between the class and the tkinter interface, it muss also communicate with the database
"""
import sqlite3


conn = sqlite3.connect('Product.db')
c = conn.cursor()

def search_price(ref):
    return c.execute(f"SELECT price,product_name,color FROM Productlisted WHERE ref_product =  {ref}").fetchall()

def charging_order(order_ref):
    print('hey')
    
result = search_price(2)
