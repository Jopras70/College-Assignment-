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

class Cylinder(Circle):
  #Constructor Cylinder + setting default value
  def __init__(self, height = 1.0, radius = 1.0, color = "red"):
      super().__init__(radius, color)
      self.height = height

  #get value of cylinders height
  def getHeight(self):
    return self.height

  #setting cyliders height
  def setHeight(self, height):
    self.height = height
  
  # print some string to check overide function
  def toString(self):
    return "this is a Cylinder."

  # Calculate cylinders volume
  def getVolume(self):
    return super().getArea () * self.getHeight()