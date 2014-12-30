from Bike_shop import Bicycle, Bike_shop, Customer, Wheel, Frame
if __name__ == '__main__':
  
  Wheel_One = Wheel(5, 10, "Wimpy")
  Wheel_Two = Wheel(7, 15, "Iggy")
  Wheel_Three = Wheel(10, 20, "Nzinga")
  
  Frame_One = Frame(15, 30, "Little Boy")
  Frame_Two = Frame(20, 45, "Trinity")
  Frame_Three = Frame(25, 50, "Fat Man")
 
  inventory = {
    "bike_one" : Bicycle("Caprica", Wheel_One, Wheel_Three, Frame_Three),
    "bike_two" : Bicycle("Tauron", Wheel_Two, Wheel_Two, Frame_Two),
    "bike_three" : Bicycle("Aerilon", Wheel_Three, Wheel_Three, Frame_Three),
    "bike_four" : Bicycle("Geminon",Wheel_One, Wheel_One, Frame_One),
    "bike_five" : Bicycle("Sagitarron", Wheel_Two, Wheel_Three, Frame_Two),
    "bike_six" : Bicycle("Picon", Wheel_One, Wheel_Two, Frame_One)
    }
  
customers = {
  "customer_one" : Customer("Lee", 200),
  "customer_two" : Customer("Kara", 500),
  "customer_three" : Customer("Laura", 1000)
} 

  
Bike_shop = ("Galactica Bikes", inventory)
  
print inventory
  
print customers
    
for customername in customers:
  customer = customers[customername]

  for key in inventory:
      bike = inventory[key]
      if bike.cost() < customer.budget:
         print "{} can afford the following bikes: \n{}".format(customer.name, inventory.name)
      #print customer.name, bike.name, customer.budget, bike.cost()
    