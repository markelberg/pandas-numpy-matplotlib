import pandas as pd
import matplotlib.pyplot as plt
import mplcursors as mpl

df = pd.read_csv('csv/Evolution_DataSets.csv')

columns = ['Specie', 'Cranial_Capacity']
drop_duplicates = df.drop_duplicates('Specie')
max_cranial = drop_duplicates.sort_values('Cranial_Capacity', ascending=False)

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

#plot1
axs[0].bar(max_cranial['Specie'], max_cranial['Cranial_Capacity'], color='skyblue')
axs[0].set_xlabel('Especie', color='blue', fontsize=13)
axs[0].xaxis.set_label_coords(0.5, -0.6)
axs[0].set_ylabel('Capacidad Craneal (m\u00B3)', color='blue', fontsize=13)
axs[0].set_title('Especies de homínidos con mayor capacidad craneal', fontsize=16)
plt.setp(axs[0].get_xticklabels(), rotation=45, ha='right')

#plot2
scatter = axs[1].scatter('Time', 'Location', c='Cranial_Capacity', s='Cranial_Capacity', data=drop_duplicates, edgecolors='black', alpha=0.6, cmap='Set1')
axs[1].set_xlabel('Millones de años', color='blue', fontsize=13)
axs[1].set_ylabel('Localización', color='blue', fontsize=13)
axs[1].set_title('Dispersión de Especies por Tiempo y Localización', fontsize=16)
mpl.cursor(scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(drop_duplicates.iloc[sel.target.index]['Specie']))
plt.colorbar(scatter, ax=axs[1], label='Capacidad Craneal (m\u00B3)')

plt.tight_layout()
plt.show()