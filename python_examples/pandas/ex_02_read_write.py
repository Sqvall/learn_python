import pandas as pd
from pathlib import Path

fpi = Path('input/titanic.csv')
fpo = Path('output/titanic.xlsx')

df = pd.read_csv(fpi)

df.to_excel(fpo, sheet_name='passengers', index=False, engine='xlsxwriter')

# print(df.head(8))
# print(df.tail(5))
# print(df.dtypes)

titanic = pd.read_excel(fpo, sheet_name='passengers')
# print(titanic.head())
# print(titanic.info())
print(titanic['Age'] > 33)
