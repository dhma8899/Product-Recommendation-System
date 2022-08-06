'''
Theory

Combine rows with same BillNo or Invoice Number.
Transaction date should be static.
BillNo or Invoice Number should be static.
Item Name or description should be appended and in a list/tupple/set.

'''


import pandas as pd
import numpy


if __name__ == "__main__":
    df1 = pd.read_csv('dataframe1.csv', error_bad_lines=False)
    df2 = pd.read_csv('dataframe2.csv', error_bad_lines=False)

    g = {i: lambda x: ', '.join(list(x)) for i in df1.columns[1:]}
    k = {i: lambda x: ', '.join(list(x)) for i in df2.columns[1:]}

    #aggregation_functions = {'BillNo': 'first', 'Itemname': g, 'Date': 'first'}
    df_new1 = df1.groupby(df1['BillNo']).agg(g).reset_index()
    df_new2 = df2.groupby(df2['Invoice']).agg(k).reset_index()

    df_new1.to_csv('sample1.csv', index=False)
    df_new2.to_csv('sample2.csv', index=False)

    print(df_new1)
