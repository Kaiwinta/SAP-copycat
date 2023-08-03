class commande:
    
    def __init__(self,nbcommand, client : str, Listcarton : list, Group: int, ended: bool) -> None:
        """Allow us to create an instance of the class commande

        Args:
            nbcommand (int): The id of the command, is unique and will be in a database
            client (str): The name of the client, allow us to track good client
            Listcarton (list): The list of all the packages that are in this command, allow us to have big command
            Group (int): an int that allow us to separate th e command based on the country
            ended (bool): Just to chack if the command is ended
        """     
        self.listecarton = Listcarton
        self.nbcommand = nbcommand
        self.ended = ended
        self.group = Group
        self.client = client

        for i in self.listecarton:
            carton = package(i[0],i[1],i[2])

    #Listecarton muss be written like this:
    #[ [pack_id], [product1,p2,p3,...], [size] ] ,     [ [pack_id], [product1,p2,p3,...], [size] ]

    def searching_carton_left(self):
        """
            The goal is to check all the packages that weren't send
        """
        self.list_packages_left = []
        for i in self.listecarton:
            if not i.ended():
                self.list_packages_left.append(i)

        if len(self.list_packages_left) == 0:
            self.ended = True

  
#Command ==> Many or a single packages 
#Packages ==> many or a single product

class package:
    
    def __init__(self,nbpackage: int, products: list, size : int) -> None:
        """Creating an instance of a package

        Args:
            nbpackage (int): The unique id of the package ( unique in the command)
            products (list): list of all the product in the specific package
            size (int): _description_
        """

        #Structure of product:
        #[ [Product 1, quantity], [Product 2, quantity] ]

        self.nbpackage = nbpackage
        self.productslist = products
        self.size = size

        if not self.check_len():
            raise(IndexError('Not enough packages (len(self.productslist) < self.size)'))

    def check_len(self):
        return self.size == len(self.productslist)
    

    

class product:
    
    def __init__(self,nbproduct, ended) -> None:
        self.nbproduct = nbproduct
        self.is_ended = ended

    def scan(self):
        #When you scan a product
        self.is_ended =True