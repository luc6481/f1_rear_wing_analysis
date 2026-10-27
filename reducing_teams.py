import pandas as pd

data = pd.read_csv("CHANGE_ME")

for i in range(len(data)):
    if data.loc[i, "Team"] != "Ferrari" and data.loc[i, "Team"] != "Alpine" and data.loc[i, "Team"] != "Mercedes":
        data = data.drop(index = i)

data = data.reset_index(drop = True)

data.to_csv("CHANGE_ME", index = False)