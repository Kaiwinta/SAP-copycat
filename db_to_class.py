import dbPart, class_part


def creating_order(ref : int):
    result = dbPart.creating_package(ref)
    packagelist = dbPart.charging_package(ref)
    print(packagelist)
    order = class_part.commande(result[0],result[1], packagelist,result[3])
    print(order)

creating_order(1)