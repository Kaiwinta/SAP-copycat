import dbPart as dbtc

class commande:
    
    def __init__(self,nbcommand, client : str, Listcarton : list, ended: bool) -> None:
        """Allow us to create an instance of the class commande

        Args:
            nbcommand (int): The id of the command, is unique and will be in a database
            client (str): The name of the client, allow us to track good client
            Listcarton (list): The list of all the packages that are in this command, allow us to have big command
            ended (bool): Just to chack if the command is ended

            #Listecarton muss be written like this:
            #[ [pack_id], [product1,p2,p3,...], [size] ] ,     [ [pack_id], [product1,p2,p3,...], [size] ]
        """     
        self.listecarton = Listcarton
        self.nbcommand = nbcommand
        self.ended = ended
        self.client = client
        self.carton_contained = []
        self.list_packages_left = Listcarton

    #Listecarton muss be written like this:
    #[ [pack_id], [product1,p2,p3,...], [size] ] ,     [ [pack_id], [product1,p2,p3,...], [size] ]

    def searching_carton_left(self):
        """
            The goal is to check all the packages that weren't send
        """
        for i in self.listecarton:
            if not i.ended:
                self.list_packages_left.append(i)

        if len(self.list_packages_left) == 0:
            self.ended = True

    def create_packages(self):
        """
            For all packages in listecarton, generate a package class instance
        """
        for i in self.listecarton:
            self.carton_contained.append(package(i[0],self.nbcommand, i[1], i[2]))


  
#Command ==> Many or a single packages 
#Packages ==> many or a single product

class package:
    
    def __init__(self,nbpackage: int,id_order : int, size : int) -> None:
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
        self.product_ref_list = []
        self.size = size                    #Size of the package
        self.nb_pas_fini = size
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
            
        This function is used when we open for the first time the package or for the second time
        """
        if not self.ended and not self.generate:
            self.generate_product()
            return 0
        if self.generate and not self.ended:
            self.check_not_ended_product()
            return 1
        if self.ended and not self.generate:
            return 2
        
    def check_not_ended_product(self):
        """Count the number of product in a specific packages that aren't ended yet

        Returns:
            int: the number of products that aren't ended now 
        """
        self.nb_pas_fini = 0
        for i in self.products:
            if not i.ended:
                self.nb_pas_fini +=1

    def one_product_scanned(self):
        self.nb_pas_fini -=1
        
    def check_len(self):
        """Check if the number of product is wrong or not

        Returns:
            bool : Return True if the size is good
        """
        size = 0
        print(self.product_ref_list)
        for i in self.product_ref_list:
            size +=i[1]

        return self.size == size
    
    def generate_product(self):
        """
            Generate for all product in the product list and instance of a product class
            The instance are stocked in self.product wich is a list of instance 

            Range allow us to create unique id  of the product
        """
        self.product_ref_list = dbtc.charging_product(self.nbpackage)
        counter = 0
        for i in self.product_ref_list:
            
            for y in range(0,i[1]):
                #i[1] is the quantity of a product
                #The neested loop allow us to add many product with the same ref
                self.products.append(  product(range,i[0], False))
                self.products[-1].search_product_ref()

                #new structure of self.products:
                #       [instance of product, instance of product]
                counter+=1


class product(package):
    #We create a subclas in order to be able to use the scan properly
    
    def __init__(self,nbproduct :int,product_ref : int, ended : bool) -> None:
        self.nbproduct = nbproduct
        self.is_ended = ended
        self.product_ref = product_ref

        #request_result = dbtc.search_price(self.product_ref)
        #self.search_product_ref(request_result)

    def scan(self):
        #When you scan a product
        self.is_ended =True
        super().one_product_scanned()

    def search_product_ref(self):
        """Permet d'avoir des info supplémentaire sur le produit

        Args:
            result (tuple): the tuple of the result of an sql request
        """
        #SQL request to search the product ref in ProductListed
        print(self.product_ref)
        result = dbtc.search_price(self.product_ref)
        self.price = result[0][0]
        self.nom = result[0][1]
        self.color = result[0][2]

    
    
"""Commande = commande(120,'alex',[    [1234,[[1,2],[2,6]],8] ],False)
                    #id  name        pack     p1  q1   p2     q2 qtotal ended
Commande.carton_contained[-1].scanned()
Commande.carton_contained[-1].products[0].search_product_ref()
print('ended')"""