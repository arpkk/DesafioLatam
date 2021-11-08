import pandas as pd

set = pd.read_csv("athlete_events.csv")

chile = set[set["Team"] == "Chile"]
print(chile)

print("la cantidad por año: ")
print(chile.groupby("Year").count()["Name"])
print("la mayor cantidad: ")
print(chile.groupby("Year").count().max()["Name"])

print("Nombres")
print(chile[chile["Medal"].notnull()]["Name"])

print("Año con más medallas")
print(chile[chile["Medal"].notnull()].groupby("Year").count().sort_values("Name",ascending = False)["Medal"].head(1))

