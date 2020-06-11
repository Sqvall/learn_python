import pandas as pd
from pathlib import Path

file_path = Path('input', 'tasks.csv')

df = pd.read_csv(file_path, sep='&')

print(df['UUID'])
