# SAP copycat
The goal is to copy the SAP app based of the utilisation i do and on what i'm able to see

Requirements:   
    - Some database of package and order 
        - Some database of what does contain every order
    
    -Being able to create database with a script

    -A simple tkinter interface as usual

    - Good request


Challenge:
    -Trying to sync some object oriented programmtion with some database

Database Structure:

    There's 2 database:

        Command.db:
            Role:       Handling and saving all the order of the client
            Tables:     Order, Package, Product
            Relation:   An order is compposed by one or many package that are also composed by one or many product

        Product.db:
            Role:       All the different product the store can sell
            Tables:     ProductListed
            Relation:   The product in Commanbd.db are linked to this database by the product_type parameter
            
        I made 2 different database to separate the Client and the Store, Store can modify some product in the product database without having to modify all the order that contain this product