"""
This part is the logical part between the class and the tkinter interface, it muss also communicate with the database
"""
import sqlite3
import class_part 

conn = sqlite3.connect('Product.db')
c = conn.cursor()

def search_price(ref):
    return c.execute(f"Select *  From Product WHERE product_ref = {ref}")

def charging_order(order_ref):
    print('hey')
    
