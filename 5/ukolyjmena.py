import pandas
import wget

#wget.download("https://raw.githubusercontent.com/pesikj/progr2-python/master/python-pro-data-1/zakladni-dotazy/excs/ceska-jmena/assets/jmena.csv")
jmena = pandas.read_csv("jmena.csv")
jmena = jmena.set_index("jméno")

jiri = jmena["jméno"("Jiří")]
print(jiri)

