from filesanddata import filesandata
kroA100 = "kroA100.tsp"
kroB100 = "kroB100.tsp"

#Die Daten sind gespeichert in einer Listen mit tupeln von x und y Koordinate also
# list[Tuple[x_koordinate,y_koordinate]]
City_a = filesandata(kroA100)
City_b = filesandata(kroB100)


print(City_a.citys)
print(City_b.citys)
