# je to pracovní verze?
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
cisloSoucastky = input("Jaké je číslo součástky?: ")
cisloSoucastky = str(cisloSoucastky)
mnozstvi = input("Kolik KS součástky?: ")
mnozstvi = int(mnozstvi)

if not cisloSoucastky in sklad:
  print("Součástka není skladem")
elif sklad[cisloSoucastky] < mnozstvi:
  print("Lze prodat pouze omezené množství")
  sklad.pop(cisloSoucastky)
else:
  print("Poptávku lze uspokojit v plné výši")



