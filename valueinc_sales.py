# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:44:59 2022

@author: JIDE
"""

import pandas as pd

#Importing a file format: file_name = pd.read_csv('file.csv')
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

data.info()

#working with calculations


#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73 
ProfitPerItem = SellingPricePerItem - CostPerItem


ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberofItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberofItemsPurchased

#CostperTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

#Adding new column to dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost

data['ProfitperTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']


#Markup = (Sales Cost)/Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']
data['Markup'] = (data['ProfitperTransaction']) / data['CostPerTransaction']


#Transforming of data and working with Functions
#Rounding Markup

roundmarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

#Combining data fields

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#error-my_date = data['Day']+'-'

#Checking columns data types
print(data['Day'].dtype)

#Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year

#Adding all back to Dataframe

data['date'] = my_date

#Using Iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #Brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column

data.iloc[4,2] #brings in 4th tow, 2nd column

#Using split to split the ClientKeywords field
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#Creating new columns for the split columns

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using the Replace function to get rid of square brackets on ClientAge and LengthoFContracts

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']' , '')

#Using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#Merging 2 files: howto, Bringing in new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#Merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#Drop unwanted columns

#Format is: df  df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)

data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'], axis = 1)

#Exporting file to csv-excel file

data.to_csv('ValueInc_Cleaned.csv' , index = False)

