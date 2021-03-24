class Car:
  def getInfo(self):
    return f"Auto s SPZ {self.spz} typu {self.type}, má najeto {self.km} a je volné {self.dostupnost} "

  def __init__(self, spz, type, km, dostupnost ):
    self.spz = spz
    self.type = type
    self.km = km
    self.dostupnost = dostupnost

  def pujc_auto(self):

    if self.dostupnost:
      self.dostupnost = False
      return f"Potvrzuji zapůjčené vozidla"
    if not self.dostupnost:
      return f"Vozidlo není k dispozici"

#peugeot = Car("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
#škoda = Car("1P3 4747", "Škoda Octavia", 41253, True)

  print(peugeot.getInfo)
  print(peugeot.pujc_auto())
  print(peugeot.getInfo)

  pocet: dni = input("Kolik dní jste měli auto půjčené?")
  pocet_km = input("Kolik km jste ujeli?")

def vrat_auto(self, pocet_km, pocet_dni):
  self.pocet_km = self.pocet_km + pocet_km
  self.pocet_dni = pocet_dni
  if pocet_dni < 7:
    price = 400 * pocet_dni
  else:
    price = 300 * pocet_dni
  return f"Cena za vypůjčení auta je {price} Kč."

auto: [
  {"spz": "4A2 3020", "type": "Peugeot 403 Cabrio", "km": "47534"},
  {"spz": "1P3 4747", "type": "Škoda Octavia", "km": "41253"}
]


#peugeot = Car("4A2 3020", "Peugeot 403 Cabrio", 47534, True)
#škoda = Car("1P3 4747", "Škoda Octavia", 41253, True)

question= input("Jakou značku auta si přejete půjčit?") [Peugeot/Škoda]
question = str(question)

#pocet:dni = input("Kolik dní jste měli auto půjčené?")
#pocet_km = input("Kolik km jste ujeli?")