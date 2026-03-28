import pandas as pd
source = r"C:\Projetos\ZHC\website\assets\planilha_mestra_cultivo_upgrade5.xlsx"
xl = pd.ExcelFile(source)
print(xl.sheet_names)
df = xl.parse(xl.sheet_names[0])
print(df.head(10))
