import pandas

zvirata = pandas.read_csv("adopce-zvirat.txt", sep = ";")
print(zvirata.columns)
print(zvirata.shape)
print(zvirata.iloc[35,1:3])