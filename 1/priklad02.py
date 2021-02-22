# je to pracovní verze?
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
čísloSoučástky = input("Jaké je číslo součástky?: ")
čísloSoučástky = str(čísloSoučástky)
množství = input("Kolik KS součástky?: ")
množství = int(množství)

if not čísloSoučástky in sklad:
  print("Součástka není skladem")
elif sklad[čísloSoučástky] < množství:
  print("Lze prodat pouze omezené množství")
  sklad.pop(čísloSoučástky)
else:
  print("Poptávku lze uspokojit v plné výši")



