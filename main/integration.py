import pandas as pd

df1 = pd.read_csv('data_preprocessing_output1.csv',  error_bad_lines=False)
df2 = pd.read_csv('data_preprocessing_output2.csv', error_bad_lines=False)
dataframe = pd.concat([df1, df2], axis=0, ignore_index=True)
dataframe.to_csv('data_integration_output.csv', index=False)