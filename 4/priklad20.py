from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

#print(generator_falesnych_dat.name())
#print(generator_falesnych_dat.address())


class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address

name = generator_falesnych_dat.name()
address = generator_falesnych_dat.address()

package = Balik(name, address)
print(package.get_info())