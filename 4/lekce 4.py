class Package:
  def __init__(self, address, weight):
    self.address = address
    self.weight = weight
    self.delivered = False

  def deliver(self):
    self.delivered = True

  def get_info(self):
    return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'

class ValuablePackage(Package):
  def __init__(self, address, weight, value):
    super().__init__(address, weight)
    self.value = value

balik = ValuablePackage("Lukavicka 26", 4, 320)
print(balik.get_info())
balik.deliver()
print(balik.get_info())