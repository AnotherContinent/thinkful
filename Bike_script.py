from Bike_shop import Bicycle, Bike_shop, Customer
if __name__ == '__main__':
  Bike_One = Bicycle("Caprica", 10, 200)
  Bike_Two = Bicycle("Tauron", 40, 75)
  Bike_Three = Bicycle("Aerilon", 20, 500)
  Bike_Four = Bicycle("Geminon",30, 750)
  Bike_Five = Bicycle("Sagitarron", 25, 300)
  Bike_Six = Bicycle("Picon", 15, 100)
  
  Customer_One = ("Lee", 200)
  Customer_Two = ("Kara", 500)
  Customer_Three = ("Laura", 1000)
  
  inventory = [Bike_One, Bike_Two, Bike_Three, Bike_Four, Bike_Five, Bike_Six]
  
  customers = [Customer_One,Customer_Two,Customer_Three]
  
  Bike_shop = ("Galactica Bikes", inventory)
  
  print()
  
for bike in range(len(inventory)):
    print inventory[bike]
  
  
for customer in range(len(customers)):
    print customers[customer]
    
for customer in range(len(customers)):
  for bike in range(len(inventory)):
    if inventory[bike].cost * .2 <= customers[customer].budget:
      print "{0} can afford the following bikes: {1}".format(customers[customer].name, inventory[bike].model)
    