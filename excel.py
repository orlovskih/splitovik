import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Assign spreadsheet filename to `file`
file = 'Каталог (7).xlsx'

df = pd.read_excel(file)

print("Column headings:")
print(df.columns)

print(df.shape)
print(df.shape[0])

priceData = pd.read_excel(file)

def productCategory:


for i in range(priceData.shape[0]):
    priceDataString = priceData.to_dict(orient='records')
    if priceDataString[i]['Код раздела'] == nan:
        pass
    else:
        #priceDataString[i-1] это каталог

    print(priceDataString[i])
