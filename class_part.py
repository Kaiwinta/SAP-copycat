import db_to_class as dbtc

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

    def create_packages(self):
        """
            For all packages in listecarton, generate a package class instance
        """
        for i in self.listecarton:
            carton = package(i[0],self.nbcommand, i[1], i[2])
            carton.generate_product()

  
#Command ==> Many or a single packages 
#Packages ==> many or a single product

class package:
    
    def __init__(self,nbpackage: int,id_order : int, products: list, size : int) -> None:
        """Creating an instance of a package

        Args:
            nbpackage (int): The unique id of the package ( unique in the command)
            products (list): list of all the product in the specific package
            size (int): number of product in the package
        """

        #Structure of productlist:
        #[ [Product 1, quantity], [Product 2, quantity] ]

        self.nbpackage = nbpackage          #Id of the package
        self.id_order = id_order            #Id of the order that contain the package
        self.product_ref_list = products    #List of all the ref of the product and the quantity
        self.size = size                    #Size of the package
        self.products = []                  #List of the products instances 
        self.ended = False                  #boolean to see if we already ended the package
        self.generate = False               #Alllow us to generate the command only once we need it

        if not self.check_len():
            raise(IndexError('Not enough packages (len(self.product_ref_list) < self.size)'))

    def scanned(self):
        """To generate the 

        Returns:
            int:    0   ==>     Product generated
                    1   ==>     Already generate but not ended
                    2   ==>     Alkready ended
        """
        if not self.ended and not self.generate:
            self.generate_product()
            return 0
        if self.generate and not self.ended:
            return 1
        if self.ended and not self.generate:
            return 2
        
    def check_not_ended_product(self):
        """Count the number of product in a specific packages that aren't ended yet

        Returns:
            int: the number of products that aren't ended now 
        """
        nb_pas_fini = 0
        for i in self.products:
            if not i.ended:
                nb_pas_fini +=1 
        return nb_pas_fini
            

    def check_len(self):
        """Check if the number of product is wrong or not

        Returns:
            bool : Return True if the size is good
        """
        return self.size == len(self.product_ref_list)
    
    def generate_product(self):
        """
            Generate for all product in the product list and instance of a product class
            The instance are stocked in self.product wich is a list of instance 

            Range allow us to create unique id  of the product
        """
        range = 0
        for i in self.product_ref_list:
            for y in range(i[1]):
                #i[1] is the quantity of a product
                #The neested loop allow us to add many product with the same ref
                self.products.append( product(range,i[0], False))

                #new structure of self.products:
                #       [instance of product, instance of product]
                range+=1
    

class product:
    
    def __init__(self,nbproduct :int,product_ref : int, ended : bool) -> None:
        self.nbproduct = nbproduct
        self.is_ended = ended
        self.product_ref = product_ref

        request_result = dbtc.search_price(self.product_ref)
        self.search_product_ref(request_result)

    def scan(self):
        #When you scan a product
        self.is_ended =True

    def search_product_ref(self,result):
        """Permet d'avoir des info supplémentaire sur le produit

        Args:
            result (tuple): the tuple of the result of an sql request
        """
        #SQL request to search the product ref in ProductListed
        self.price = result[0]
        self.nom = result[1]
    