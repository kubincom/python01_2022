import pandas

teplota = pandas.read_csv("temperature.txt")
teplota = teplota.set_index("City")

#1
print(teplota.loc["Prague":"Prague", ["Day", "AvgTemperature"]])

#1 - asi to bude uvedeno ve stupních F a ne v C.


#2
nad80=(teplota[teplota["AvgTemperature"] > 80])
print(nad80)

#3
nad80=(teplota["AvgTemperature"] > 60)
evropa = teplota["Region"] == "Europe"
nad80evropa = teplota[nad80 & evropa]
print(nad80evropa)

#4
nad80=(teplota["AvgTemperature"] > 80)
pod20=(teplota["AvgTemperature"] < -20)
extrem = teplota[nad80 | pod20]
print(extrem)