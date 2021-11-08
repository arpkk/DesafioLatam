import pandas as pd

set = pd.read_csv("athlete_events.csv")

subset1 = pd.Series({"Oro": set[set["Medal"] == "Gold"]["Name"]})

subset2 = pd.Series({"Plata": set[set["Medal"] == "Silver"]["Name"]})

subset3 = pd.Series({"Bronce": set[set["Medal"] == "Bronze"]["Name"]})

subset4 = pd.Series({"S/m": set[set["Medal"].isnull()]["Name"]})

subset1["Female"] = set[set["Medal"] == "Gold"][set["Sex"] == "F"]["Sex"]
subset2["Female"] = set[set["Medal"] == "Silver"][set["Sex"] == "F"]["Sex"]
subset3["Female"] = set[set["Medal"] == "Bronze"][set["Sex"] == "F"]["Sex"]
subset4["Female"] = set[set["Medal"].isnull()][set["Sex"] == "F"]["Sex"]

print(subset1)
