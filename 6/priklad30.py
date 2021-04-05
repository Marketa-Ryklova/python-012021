import pandas
vykazy = pandas.read_csv("vykazy.csv", index_col = 0)
print(vykazy.head())
hodiny_projekty = vykazy.groupby('project')['hours'].sum()
print(hodiny_projekty)
hodiny_projekty.to_excel("hodiny_projekty.xlsx")
#uložení do xlxs

excel_data = pandas.read_excel('hodiny_projekty.xlsx', index_col=0)
print(excel_data)
#načtení z excelu