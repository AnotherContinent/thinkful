from Bike_shop import Bicycle, Bike_shop, Customer, Wheel, Frame
if __name__ == '__main__':
  
  Wheel_One = Wheel(5, 10, "Wimpy")
  Wheel_Two = Wheel(7, 15, "Iggy")
  Wheel_Three = Wheel(10, 20, "Nzinga")
  
  Frame_One = Frame(15, 30, "Little Boy")
  Frame_Two = Frame(20, 45, "Trinity")
  Frame_Three = Frame(25, 50, "Fat Man")
 
  inventory = {
    Bike_One = Bicycle("Caprica", Wheel_One, Wheel_Three, Frame_Three)
    Bike_Two = Bicycle("Tauron", Wheel_Two, Wheel_Two, Frame_Two)
    Bike_Three = Bicycle("Aerilon", Wheel_Three, Wheel_Three, Frame_Three)
    Bike_Four = Bicycle("Geminon",Wheel_One, Wheel_One, Frame_One)
    Bike_Five = Bicycle("Sagitarron", Wheel_Two, Wheel_Three, Frame_Two)
    Bike_Six = Bicycle("Picon", Wheel_One, Wheel_Two, Frame_One)
    }
  
customer = {
  Customer_One = Customer("Lee", 200)
  Customer_Two = Customer("Kara", 500)
  Customer_Three = Customer("Laura", 1000)
} 

  
Bike_shop = ("Galactica Bikes", inventory)
  
print inventory
  
print customers
    
for Customer in range(len(customers)):
  for bike in range(len(inventory)):
    if getattr(Bicycle, 'retail_price') <= Customer.budget:
      print "{} can afford the following bikes: \n{}".format(customers.name, inventory.name)
    