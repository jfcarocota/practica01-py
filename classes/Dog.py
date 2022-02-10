from classes.Animal import Animal

class Dog(Animal):

  __gausTimes = 0

  def __init__(self, name, age, size, color, race, id):

    super().__init__(name, age)
    self.size = size
    self.color = color
    self.race = race
    self.__id = id
    self.__Guau()

  def printInfo(self):
    print(self.getName(), self.getAge(), self.size, self.color, self.race, self.__id, Dog.__gausTimes)

  def setId(self, id):
    if (id > 0 ):
      self.__id = id

  def __Guau(self):
    Dog.__gausTimes += 1
    print("Guau, Guau !")

  def guausCout(self):
    print(f'numero de veces que ha ladrado: {Dog.__gausTimes}')