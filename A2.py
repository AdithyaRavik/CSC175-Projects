class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)

  
    def updateQuantity(self,amt):
        self.quantity += amt
        return self.quantity

    def gettotal(self):
        return ((self.price * self.quantity))
    
        
    def __str__(self):
        x =(self.name,'quantity', str(self.quantity) , 'price per unit:', str(self.price))
        return x

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False

def main():
    a = Item('mango',3,2)
    b = Item('tomato',1,4)
    print(a.updateQuantity(5)) #Quantity: 7
    print(a.gettotal()) #Total: 21 
    print(a) # ('mango', 7, 'price per unit:', 3)
    print(b) # ('tomato', 4, 'price per unit:', 1)
    print(a == b) #False
    print(a > b) #True
    print(b > a) #False


#main()

class ShoppingCart:

    def __init__(self,itemList):
        self.itemList = []

    def add(self, name , price, quantity):
        self.name = input("Enter name of item to add:")
        self.price = input("Enter the item price:")
        self.quantity = input("Enter the item quantity:")
        x = Item(self.name, self.price, self.quantity)
        self.itemList = self.itemList + x
        return self.itemList


print(add('mango',3,2))






















