class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "%s(width=%d, height=%d)" % (type(self).__name__, int(self.width), int(self.height))

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2) + (self.height ** 2)) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ""
    for i in range(self.height):
      picture += "*" * self.width
      picture += "\n"
    return picture

  def get_amount_inside(self, other):
    return self.get_area() // other.get_area()


class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def __str__(self):
    return "%s(side=%d)" % (type(self).__name__, int(self.width))

  def set_side(self, side):
    self.width = side
    self.height = side