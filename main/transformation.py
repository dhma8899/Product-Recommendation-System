import pandas as pd

dataframe = pd.read_csv('data_integration_output.csv', error_bad_lines=False)

apriori_input_dataset = dataframe.groupby(['Invoice', "HashCode"])['Quantity'].sum().unstack().fillna(0).applymap(lambda x: 1 if x > 0 else 0)
apriori_input_dataset.to_csv('data_transformation_output.csv', index=False)