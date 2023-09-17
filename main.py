from clean import formatDateDayIndex
import pandas as pd
from database.static import *

def cleanDate(fromY, toY):
    for y in range(fromY, toY+1):
        formatDateDayIndex(year=y)

df = pd.read_csv("database/clean-data/DSE-2022.csv")
print(categories)