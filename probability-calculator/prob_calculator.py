import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, number in kwargs.items():
      self.contents += [color] * number
  
  def draw(self, n):
    drawn = []
    while len(drawn) != n and len(self.contents) != 0:
      choosen = self.contents.pop(random.randint(0, len(self.contents) - 1))
      drawn.append(choosen)
    return drawn

def asExpected(actual, expected):
  for color, number in expected.items():
    if actual.count(color) < number:
      return False
  return True

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  results = []
  for i in range(num_experiments):
    hatExp = copy.deepcopy(hat)
    results.append(hatExp.draw(num_balls_drawn))

  count = 0
  for res in results:
    if asExpected(res, expected_balls):
      count += 1

  return count / num_experiments