#importing libraries that I need
import logging
import traceback
import fastf1 as ff1
import pandas as pd
import numpy as np
from fastf1.ergast import Ergast


#this keeps the data on a cache instead of pulling it each time
ff1.Cache.enable_cache('CHANGE_ME')

#this initializes the Ergast API ?
ergast = Ergast()

#ones with sprint: 2,4, 5,9,12, 17
rounds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
session_normal = ["FP1", "FP2", "FP3", "Q", "R"]
session_sprint = ["FP1", "SQ", "S", "Q", "R"]

all_data = []

keep_cols_laps = ["Driver", 'Sector1Time' , 'Sector2Time', 'Sector3Time', 'SpeedI1','SpeedI2','SpeedFL','SpeedST', "Team", "Deleted"]


for j in range(len(rounds)):
    for i in range(5):
        if (rounds[j] == 2) or (rounds[j] == 4) or (rounds[j] == 5) or (rounds[j] == 9) or (rounds[j] == 12) or (rounds[j] == 17):
            #creates my dataframe
            session_data = ff1.get_session(2026, rounds[j], session_sprint[i])
            session_data.load()
        else:
            #creates my dataframe
            session_data = ff1.get_session(2026, rounds[j], session_normal[i])
            session_data.load()

        try:
            dataframe_session = session_data.laps.copy()

            #deletes the columns i dont need
            dataframe_session = dataframe_session[[c for c in keep_cols_laps if c in dataframe_session.columns]]

            #resets the index of the rows (labels them correctly by number)
            dataframe_session = dataframe_session.reset_index(drop = True)

            for k in range(len(dataframe_session)):
                dataframe_session.loc[k, "GP"] = rounds[j]

            all_data.append(dataframe_session)
        except ff1.exceptions.DataNotLoadedError:
            
            print(j, i)
        
        

#combined the data into one big dataset
all_data = pd.concat(all_data)

#resets the index of the rows (labels them correctly by number)
all_data = all_data.reset_index(drop = True)

print(all_data)

all_data.to_csv("CHANGE_ME", index = False)