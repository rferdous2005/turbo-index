import pandas as pd
import os
from datetime import datetime
import numpy as np
from database.static import all


path = "database/Dhaka-Stock-Exchange-DSE-"
def formatDateDayIndex(year):
    df = pd.read_csv(path+str(year)+".csv")
    print("Count "+str(year)+" "+str(len(df)))
    days = []
    
    #df['DayIndex'] = days
    print(df.count())
    for i in df.index:
        dateStr = str(df['Date'][i])
        if "/" in dateStr:
            dateObj = datetime.strptime(df['Date'][i], "%d/%m/%Y")
            dayIndex = dateObj.strftime("%j")
            days.append(dayIndex)
            replacement = dateObj.strftime("%d-%m-%Y")
            df.loc[i, 'Date'] = replacement
            #df.loc[i, 'DayIndex'] = dayIndex
            
            #print(dayIndex)
        elif "-" in dateStr:
            dateObj = datetime.strptime(df['Date'][i], "%d-%m-%Y")
            dayIndex = dateObj.strftime("%j")
            days.append(dayIndex)
            pass
        else:
            if len(dateStr)==8:
                dateObj = datetime.strptime(df['Date'][i], "%Y%m%d")
                dayIndex = dateObj.strftime("%j")
                days.append(dayIndex)
                replacement = dateObj.strftime("%d-%m-%Y")
                df.loc[i, 'Date'] = replacement
                #df.loc[i, 'DayIndex'] = dayIndex
            else:
                print("Anomaly at data index "+str(i)+" year "+str(year) + dateStr)
                break
    print(days)
    df['DayIndex'] = days
    df=df.sort_values(by=['Scrip', 'DayIndex'])
    df.to_csv('DSE-'+str(year)+'.csv', index=False)


def mergeCSV():
    df = pd.DataFrame()
    path = "database/day-data/"
    dir_list = os.listdir(path)
    print(dir_list)
    for file in dir_list:
        data = pd.read_csv(path+file)
        df = pd.concat([df, data], axis=0)
    df=df.sort_values(by=['Scrip', 'Date'])
    #print(df)
    df.to_csv('merged_files.csv', index=False)

# for c in all:
#     if c[0] == 'Z':
#         print(c)
    