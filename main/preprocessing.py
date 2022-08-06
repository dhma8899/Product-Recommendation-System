import pandas as pd
import hashlib

def update_column_name(dataframe):
    dataframe.rename(columns={'Description': 'Itemname', 'InvoiceDate': 'Date', 'BillNo': 'Invoice'}, inplace=True)

def add_hash(dataframe):
    dataframe['HashCode'] = dataframe['Itemname'].apply(lambda x: hashlib.md5(x.encode()).hexdigest())

def save_output(dataframe, file_name):
    dataframe.to_csv(file_name, index=False)

df1 = pd.read_csv('dataframe1.csv', error_bad_lines=False)
df2 = pd.read_csv('dataframe2.csv', error_bad_lines=False)

update_column_name(df1)
update_column_name(df2)

add_hash(df1)
add_hash(df2)

save_output(df1, 'data_preprocessing_output1.csv')
save_output(df2, 'data_preprocessing_output2.csv')