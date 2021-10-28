import pandas as pd

ejercicio_1 = pd.read_csv("athlete_events.csv")

ejercicio_2 = ejercicio_1["Event"].value_counts().shape[0]

ejercicio_3 = (ejercicio_1[ejercicio_1["Season"] == "Summer"].shape[0] / ejercicio_1.shape[0],
               ejercicio_1[ejercicio_1["Season"] == "Winter"].shape[0] / ejercicio_1.shape[0])

año1 = ejercicio_1[ejercicio_1["Season"] == "Summer"]["Year"].min()
ejercicio_4 = ejercicio_1[ejercicio_1["Year"] == año1]["City"].min()

año2 = ejercicio_1[ejercicio_1["Season"] == "Winter"]["Year"].min()
ejercicio_5 = ejercicio_1[ejercicio_1["Year"] == año2]["City"].min()

ejercicio_6 = ejercicio_1["Team"].value_counts().head(10)

ejercicio_7 = (ejercicio_1[ejercicio_1["Medal"] == "Gold"].shape[0]*100 / ejercicio_1.shape[0], ejercicio_1[ejercicio_1["Medal"] == "Bronze"].shape[0]*100 / ejercicio_1.shape[0], ejercicio_1[ejercicio_1["Medal"] == "Silver"].shape[0]*100 / ejercicio_1.shape[0])

ejercicio_8 = ejercicio_1[ejercicio_1["Year"] == año1]["Team"].value_counts()
