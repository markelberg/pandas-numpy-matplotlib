import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/elecciones_autonomicas_madrid_2023.csv')

# Limpiar los datos y convertir la columna de votos a números
df = df[df['VOTOS_2023'] != '-']
df['VOTOS_2023'] = df['VOTOS_2023'].str.replace('.', '', regex=False)
df['VOTOS_2023'] = pd.to_numeric(df['VOTOS_2023'])

df_filtrado = df[df['VOTOS_2023'] > 20000]

fig, ax = plt.subplots()
wedges, _ = ax.pie(df_filtrado['VOTOS_2023'], labels=df_filtrado['PARTIDO'])

legend = [f"{label}: {votes} votos" for label, votes in zip(df['PARTIDO'], df['VOTOS_2023'])]
ax.legend(wedges, legend, loc="center right", fontsize='large', bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()