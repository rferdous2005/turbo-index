import pandas as pd
from database.static import *

def loadWarehouse(fromYear, toYear):
    for y in range(fromYear, toYear+1):
        df = pd.read_csv("database/clean-data/DSE-"+str(y)+".csv")
        for c in all:
            filtered_df = df[df['Scrip'] == c]
            filtered_df = filtered_df.sort_values(by=['DayIndex'])
            calculateWithMultipleTurbo(company=c, year=y, dataframe=filtered_df, turboX=[3,5,7,11,22,44,66])
            #print(c, filtered_df)
            break
        #print(filtered_df)
        # for item in df.index:
        #     print(df.loc[item, 'Date'])

def calculateWithMultipleTurbo(company, year, dataframe, turboX):
    for turbo in turboX:
        turbo -= 1
        maxIndex = dataframe.max().DayIndex
        for startIndex in dataframe.index:
            endIndex = startIndex + turbo
            print(startIndex, endIndex, maxIndex)
            if endIndex > maxIndex:
                break
            startRow = dataframe.loc[startIndex, 'Close']
            endRow = dataframe.loc[endIndex, 'Close']
            print(startRow, endRow)

loadWarehouse(2016,2016)