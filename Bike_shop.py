class Bicycle(object):
  def __init__(self, model, weight, cost):
    self.model = model
    self.weight = weight
    self.cost = cost
      
class Bike_shop(object):
  def __init__(self, name, inventory, profit_margin):
    self.name = name
    self.inventory = []
    self.profit_margin = profit_margin
    
class Customer(object):
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget