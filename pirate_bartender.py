import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ["addled","poxed","scurvy","bilge-sucking"]

nouns = ['blaggard','pillager','shark bait','wench']

def get_answers ():
  answers = {}
  for type, question in questions.iteritems():
    print question
    answers[type] = raw_input().lower() in ["y", "yes"]
    print ""
  return answers

def make_drink(answers):
  drink = []
  for ingredient_type, yes in answers.iteritems():
    if not yes:
      continue
      
    drink.append(random.choice(ingredients[ingredient_type]))
  return drink

def main():
  answers = get_answers()
  drink = make_drink(answers)
  print "Here's the drink. The recipe is:"
  for ingredient in drink:
    print "A {}".format(ingredient)
  print "The name is: "
  print random.choice(adjectives) + " " + random.choice(nouns)
    
if __name__ == "__main__":
  main()