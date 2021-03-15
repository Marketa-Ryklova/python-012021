from forex_python.converter import CurrencyRates
mena = input("jakou měnu si budete přát?")
pozadovano_v_cilove_mene = input("Kolik peněz si budete přát směnit? ")
pozadovano_v_cilove_mene = int(pozadovano_v_cilove_mene)
prevodnik = CurrencyRates()
if mena == "GBP":
  cena_v_korunach = prevodnik.convert('GBP', 'CZK', pozadovano_v_cilove_mene)
  print(cena_v_korunach)
elif mena == "EUR":
  cena_v_korunach = prevodnik.convert('EUR', 'CZK', pozadovano_v_cilove_mene)
  print(cena_v_korunach)
elif mena == "DKK":
  cena_v_korunach = prevodnik.convert('DKK', 'CZK', pozadovano_v_cilove_mene)
  print(cena_v_korunach)
else:
  print("Zadanou měnu nemáme v nabídce.")
