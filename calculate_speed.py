
import pandas as pd
import numpy as np

all_data = pd.read_csv("CHANGE_ME")
denom_f = 0.0
FL_speed_f = 0.0

denom_a = 0.0
FL_speed_a = 0.0

denom_m = 0.0
FL_speed_m = 0.0

denom_m_corner = 0.0
SI2_speed_m = 0.0

denom_f_closed = 0.0
SI2_speed_f = 0.0

denom_a_closed = 0.0
SI2_speed_a = 0.0

for i in range(len(all_data)):
    if all_data.loc[i, "Team"] == "Ferrari" and all_data.loc[i, "SpeedFL"] >= 200.0:
        denom_f += 1.0
        FL_speed_f += all_data.loc[i, "SpeedFL"]
        #list_speed.append(hungary_data.loc[i, "SpeedFL"])
    elif all_data.loc[i, "Team"] == "Alpine" and all_data.loc[i, "SpeedFL"] >= 200.0:
        denom_a += 1.0
        FL_speed_a += all_data.loc[i, "SpeedFL"]
    elif all_data.loc[i, "Team"] == "Mercedes" and all_data.loc[i, "SpeedFL"] >= 200.0:
        denom_m += 1.0
        FL_speed_m += all_data.loc[i, "SpeedFL"]

    if all_data.loc[i, "Team"] == "Ferrari" and all_data.loc[i, "SpeedI2"] >= 160.0:
        denom_f_closed += 1.0
        SI2_speed_f += all_data.loc[i, "SpeedI2"]
    elif all_data.loc[i, "Team"] == "Alpine" and all_data.loc[i, "SpeedI2"] >= 160.0:
        denom_a_closed += 1.0
        SI2_speed_a += all_data.loc[i, "SpeedI2"]
    elif all_data.loc[i, "Team"] == "Mercedes" and all_data.loc[i, "SpeedI2"] >= 160.0:
        denom_m_corner += 1.0
        SI2_speed_m += all_data.loc[i, "SpeedI2"]

print("Ferrari Open:", FL_speed_f/denom_f , "from", denom_f, "rows\n Ferrari Closed:", SI2_speed_f/denom_f_closed , "from", denom_f_closed)
print("Alpine:", FL_speed_a/denom_a , "from", denom_a, "rows\n Alpine Closed:", SI2_speed_a/denom_a_closed , "from", denom_a_closed)
print("Mercedes:", FL_speed_m/denom_m , "from", denom_m, "rows\n Mercedes Corner: ", SI2_speed_m/denom_m_corner , "from", denom_f_closed)