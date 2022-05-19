class Product:
    def __init__(self,prod_id,quantity):
        self.prod_id=prod_id
        self.quantity=quantity
    
class Inventory:
    def __init__(self,product):
        self.product=product
    

        
        


prod1=Product(1,23)
prod2=Product(2,33)
inventory=Inventory(2*[prod1]+2*[prod2])
print(inventory.value())
    
