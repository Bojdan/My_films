from films1 import Film


x = Film("Kill Bill 3", "Драмма", True, {"Нью-Йорк": 2004, "Москва": 2005, "Токио": 2006}, ["Jhoni", "Bill", "Uma"], "Tarantino", 99, 8000000, 10000000, ["Rus", "Eng"])



x.info()
x.show_actors()

print("\n" + "Бюджет филма составляет:", x.budget, "$$$")
print("\n" + "Сборы по миру: ", x.box_office, "$$$")

print(x.leng_translate("Eng"))

x.date_releas("Москва")
