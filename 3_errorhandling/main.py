from pathlib import Path
import pandas as pd

data_dir = Path.cwd()
filename = 'source_data.csv'

try: 
    with open(data_dir / filename) as f:
        lines = f.readlines()
except FileNotFoundError:
    print('File not found')

#print(lines)

#try:
#    data = pd.read_csv(data_dir / filename)
#except FileNotFoundError:
#    print('File not found') 

# tjek typer

