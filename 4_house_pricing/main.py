from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


data_dir = Path.cwd()
filename = 'DKHousingPricesSample100k.csv'

data = pd.read_csv(data_dir / filename, delimiter=',', 
                   dtype={'date': str, 
                          'quarter': str, 
                          'house_id': int,
                          'house_type': str,
                          'sales_type': str,
                          'year_build': int,
                          'purchase_price': int,
                          '%_change_between_offer_and_purchase': float,
                          'no_rooms': int,
                          'sqm': float,
                          'sqm_price': float,
                          'address': str,
                          'zip_code': int,
                          'city': str,
                          'area': str,
                          'region': str,
                          'nom_interest_rate%': float,
                          'dk_ann_infl_rate%': float,
                          'yield_on_mortgage_credit_bonds%': float
                          })
data['date'] = pd.to_datetime(data['date'])

#print(data[:10])


# group by on region

data.groupby(by='region')

#print(data)