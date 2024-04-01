import pandas as pd
import matplotlib.pyplot as plt
import mplcursors as mpl

df = pd.read_csv('csv/suicide_rates_1990-2022.csv')

spain = df[(df['CountryName'] == 'Spain') & (df['Year'] == 2021)]
spain['SuicideRatePer100k'] = (spain['SuicideCount'] / spain['Population']) * 100000
x_axis = spain.groupby(['AgeGroup', 'Sex'])['SuicideRatePer100k'].mean().unstack()
x_axis = x_axis.drop('Unknown', errors='ignore')

fig, ax = plt.subplots(figsize=(12, 6))
x_axis.plot(kind='bar', ax=ax, color=['darksalmon', 'blueviolet'])
plt.xlabel('Age Group', fontweight='bold')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.ylabel('SuicideRate(per100k)', fontweight='bold')
plt.title('Suicide Rates in Spain (2021)', fontweight='bold', fontsize=18)

plt.legend(title='Sex', title_fontsize='13', loc='upper left')
mpl.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"{sel.target[1]}"))

plt.tight_layout()
plt.show()