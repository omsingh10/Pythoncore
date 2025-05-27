# class Animal:
#   pass
# class Dog(Animal):
#   pass
# jimmty = Dog()

# print(isinstance(jimmty, Dog))  # True
# print(isinstance(jimmty, Animal))  # True
# print(issubclass(Dog, Animal))  # True
# print(issubclass(Animal, Dog))  # False

class Os:
  def __init__(self , name , version , year):
    self.__name = name
    self.__version = version
    self.__year= year
  def boot(self):
    print(" Device is booting")
  def update(self):
    print("Device os is updating ")


#inhertance
class mobileOs(Os):
  def boot(self):
    print("mobile device is boot")
  def update(self):
    print("mobile update")

#polymorphism
class desktopOs(Os):
  def boot(self):
    print("desktop device is boot")
  def update(self):
    print("desktop update")


class stack:
  def __init__(self, max_size):
    self.top = -1
    self.max_size = max_size
    self.st = []
  def is_full(self):
    return self.top >= self.max_size - 1
  def is_empty(self):
    return self.top == -1
  def push(self, element):
    if self.is_full():
      return "Stack is full"
    self.st.append(element)
    self.top += 1
  def pop(self):
    if self.is_empty():
      return "Stack is empty"
    self.top -= 1
    return self.st.pop()