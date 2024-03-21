import pandas as pd
import numpy as np

df = pd.read_csv('csv/suicide_rates_1990-2022.csv', index_col='Sex')

spain = df[df['CountryName'] == 'Spain']
top_countries = spain.groupby(['AgeGroup', 'Sex','Year'])['SuicideCount'].mean()

print("Number of files and columns:", df.shape)
print("\n", top_countries.sort_values(ascending=False).head(30))