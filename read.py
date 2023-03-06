

import pandas as pd
xl_workbook = pd.ExcelFile('C:\Users\shashank.gupta\Downloads\credentials.xlsx')  # Load the excel workbook
df = xl_workbook.parse("Sheet 1")  # Parse the sheet into a dataframe
x1_list = df['Password'].tolist() 
