import pandas as pd
from database.static import *
import numpy as np
from warehouse.db import connectDB

def loadWarehouse(fromYear, toYear):
    for y in range(fromYear, toYear+1):
        df = pd.read_csv("database/clean-data/DSE-"+str(y)+".csv")
        for c in all:
            print("Year "+ str(y) +" Scrip "+c)
            filtered_df = df[df['Scrip'] == c]
            filtered_df = filtered_df.sort_values(by=['DayIndex'])
            applyMultipleTurbo(company=c, year=y, dataframe=filtered_df, turboX=[3,5,7,11,22,44,66])
            #print(c, filtered_df)
            break
        #print(filtered_df)
        # for item in df.index:
        #     print(df.loc[item, 'Date'])

def applyMultipleTurbo(company, year, dataframe, turboX):
    for turbo in turboX:
        print("Turbo value "+str(turbo))
        weights = np.array([0.0]*366)
        turbo -= 1
        maxIndex = dataframe.index.max()
        maxIndex = int(maxIndex)
        for startIndex in dataframe.index:
            endIndex = startIndex + turbo
            endIndex = int(endIndex)
            #print(maxIndex)
            if endIndex > maxIndex:
                break
            dayIndex1 = int(dataframe.loc[startIndex, 'DayIndex'])
            dayIndex2 = int(dataframe.loc[endIndex, 'DayIndex'])
            close1 = float(dataframe.loc[startIndex, 'Close'])
            close2 = float(dataframe.loc[endIndex, 'Close'])
            open1 = float(dataframe.loc[startIndex, 'Open'])
            open2 = float(dataframe.loc[endIndex, 'Open'])
            high1 = float(dataframe.loc[startIndex, 'High'])
            high2 = float(dataframe.loc[endIndex, 'High'])
            low1 = float(dataframe.loc[startIndex, 'Low'])
            low2 = float(dataframe.loc[endIndex, 'Low'])
            high2 = float(dataframe.loc[endIndex, 'High'])
            rr = 0
            #calculateTotalVolume()
            if close2 > open1 and close2 > close1:
                # apply bullish logic 1.3x
                rr = (close2-open1)/open1*130.0/turbo
            elif close2 < open1 and close2 < close1:
                # apply bearish 1.3x
                rr = (close2-open1)/open1*130.0/turbo
            elif close2 > open1:
                rr = (close2-open1)/open1*70.0/turbo # bullish 0.7x
            elif close2 < open1:
                rr = (close2-open1)/open1*70.0/turbo #bearish 0.7x
            #print(rr)
            for d in range(dayIndex1, dayIndex2+1):
                print(weights[d]+ rr)
                weights[d] = round(rr, 4)+weights[d]
        dbCon = connectDB()
        print(weights, rr)


loadWarehouse(2016,2016)