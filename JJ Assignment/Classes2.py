class Circle:
  # Overload Constructor for Circle(radius, color)
  def __init__(self, radius, color):
    self.radius = radius
    self.color = color

  #get value of circles radius
  def getRadius(self):
    return self.radius

  # setting circles radius
  def setRadius(self, radius):
    self.radius = radius

  # get circles color
  def getColor(self):
    return self.color

  # setting circles color
  def setColor(self, color):
    self.color = color

  # print some string to check overide function
  def toString():
    return "this is a Circle."

  # Calculate Circles Area
  def getArea(self):
    return 3.14 * self.getRadius() * self.getRadius()

