import pandas
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
twlo = pandas.read_csv("twlo.csv")

twlo.info()
#informace o řadcích a sloupcích
print(twlo.iloc[:5])
#zobrazení 5. řádků pomocí iloc
print(twlo.head(5))
#zobrazení 5 řádků pomocí head
print(twlo.tail(1))
#zobrazení posledního řádku
