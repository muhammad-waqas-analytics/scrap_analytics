import pandas as pd

file_path = r"D:\Waqas\Python\Projects\scrap_analytics\step1_data_collection\textile_scrap.xlsx"
df = pd.read_excel(file_path)

print(df.head())

