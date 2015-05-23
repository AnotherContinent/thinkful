class Wheel(object):
	def __init__(self, weight, cost, name):
		self.weight = weight
		self.cost = cost
		self.name = name

	def __repr__(self):
		return "This wheel weighs {} costs {} and is named {}".format(self.weight, self.cost, self.name)

class Frame(object):
	def __init__(self, weight, cost, name):
		self.weight = weight
		self.cost = cost
		self.name = name

	def __repr__(self):
		return "Frame \n\tName: {} \n\tWeight: {}\n\tCost:{}".format(self.name, self.weight, self.cost)

class Bicycle(object):
  def __init__(self, name, back_wheel, front_wheel, frame):
    self.name = name
    self.back_wheel = back_wheel
    self.front_wheel = front_wheel
    self.frame = frame

  def __repr__(self):
    return "{}: {} dollars".format(self.name, self.retail_price())
	
  def cost(self):
    return self.front_wheel.cost + self.back_wheel.cost + self.frame.cost
  
  def retail_price(self):
    return self.cost() + (self.cost() * .2)

  def weight(self):
    return self.front_wheel.weight + self.back_wheel.weight + self.frame.weight
  
class Bike_shop(object):
  def __init__(self, name, inventory):
    self.name = name
    self.inventory = inventory

  def __repr__(self):
     return "This shop is named {} and has the following inventory: \n{}".format(self.name, self.inventory)
      
class Customer(object):
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    
  def __repr__(self):
    return "{}: ${}\n".format(self.name, self.budget)
    