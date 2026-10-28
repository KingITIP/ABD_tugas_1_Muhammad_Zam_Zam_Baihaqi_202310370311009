import pandas as pd
xls = pd.ExcelFile('C:/project_1/data analysis/tugas 1/dataset/01_Data-Ch-Jabar-2020-2025.xlsx')
print(xls.sheet_names)
df = pd.read_excel(xls, sheet_name='DATA')
print(df.shape)
print(df.columns[:5].tolist())
print(df.iloc[0,:5])
