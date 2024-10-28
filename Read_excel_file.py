import pandas as pd

import pandas

excel_data_df = pandas.read_excel('file_name.xlsx', sheet_name='Sheet1')

# In this line you chose the data type for specific column .
excel_data_df_2 = pandas.read_excel('file_name.xlsx', sheet_name='Sheet1',dtype={"age":int,"salary":float})


# print whole sheet data
print(excel_data_df)