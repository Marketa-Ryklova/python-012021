from datetime import datetime, date
today = date.today()

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email
  def get_info(self):
    return f"Uchazeč {self.jmeno}, {self.email}"

class Uchazec(Kontakt):
  def __init__(self, jmeno, email, datum_pohovoru, zapis_z_pohovoru):
    super().__init__(jmeno, email)
    self.datum_pohovoru = datum_pohovoru
    self.zapis_z_pohovoru = zapis_z_pohovoru
  def get_info(self):
    return f"{super().get_info()} má/měl pohovor dne {self.datum_pohovoru} "

  def uloz_zapis(self, datum_pohovoru):
    if datum_pohovoru == today:
      print("zápis byl uložen")
    elif datum_pohovoru < today:
      print("Pohovor ještě neproběhl")


uchazec1 = Uchazec("Josef Nový", "josef.novy@gmail.com", "21.4.2021", "")
print(uchazec1.get_info())