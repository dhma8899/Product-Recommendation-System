'''
Theory

Step1:- Remove all rows in which country is not UK
Step2:- Remove all the rows in which any relevent parameter is empty
Step3:- Remove irrelevent columns Assignment-1_Data(Quantity, Price, CustomerId, Country)
        online_retail_11.csv (StockCode, Quantity, Price, Customer, Country)
'''

import numpy
import pandas as pd

def country(df):
    df.drop(df[df['Country'] != "United Kingdom"].index, inplace = True)
    return df

def emptyrows(df):
    try:
        data = df.dropna(subset=['Invoice', 'Description', 'InvoiceDate'])
    except:
        data = df.dropna(subset=['BillNo', 'Itemname', 'Date'])
    return data

def irrelevent(df):
    try:
        df = df.drop('CustomerID', axis=1)
        df = df.drop('Price', axis=1)
        df = df.drop('Country', axis=1)
    except:
        df = df.drop('StockCode', axis=1)
        df = df.drop('Price', axis=1)
        df = df.drop('Customer ID', axis=1)
        df = df.drop('Country', axis=1)
    return df

if __name__ == "__main__":
    File1 = "Dataset1.csv"
    File2 = "Dataset2.csv"

    df1 = pd.read_csv('Dataset1.csv', error_bad_lines=False, sep=';')
    df2 = pd.read_csv('Dataset2.csv', error_bad_lines=False)



    df1 = country(df1)
    df2 = country(df2)


    df1 = emptyrows(df1)
    df2 = emptyrows(df2)

    df1 = irrelevent(df1)
    df2 = irrelevent(df2)


    df1.to_csv('dataframe1.csv',index=False)
    df2.to_csv('dataframe2.csv',index=False)
