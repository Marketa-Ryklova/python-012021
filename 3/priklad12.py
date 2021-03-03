class Car:
  def getInfo(self):
    return f"Auto s SPZ {self.spz} typu {self.type}, má najeto {self.km} a je volné {self.dostupnost} "
  def __init__(self, spz, type, km, dostupnost=True ):
    self.spz = spz
    self.type = type
    self.km = km
    self.dostupnost = dostupnost
  def pujc_auto(self):
    if self.dostupnost == True:
      return f"Potvrzuji zapůjčené vozidla"
    else:
      return f"Vozidlo není k dispozici"

  def __str__(self):
    return self.type


car1 = Car ("4A2 3020", "Peugeot 403 Cabrio", 47534, False)
car2 = Car ("1P3 4747", "Škoda Octavia", 41253, True)

print (car1.pujc_auto())


question= input("Jakou značku auta si přejete půjčit?") [Peugeot/Škoda]
question = str(question)

