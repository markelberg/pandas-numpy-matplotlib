import matplotlib.pyplot as plt
import numpy as np


frutas = {'Manzana': 2602,
        'Plátano': 2834,
        'Pera': 1348,
        'Naranja': 2024,
        'Fresa': 1466,
        'Kiwi': 1108,
        'Melocotón': 925,
        'Mandarina': 2251,
        'Pomelo': 32,
        'Sandia': 420,
        'Melón': 865}

verduras = {'Lechuga': 2602,
        'Brócoli': 834,
        'Coliflor': 348,
        'Tomate': 5024,
        'Aguacate': 3466,
        'Zanahoria': 4108,
        'Ajo': 1789,
        'Apio': 123,
        'Cebolla': 3625,
        'Puerro': 985,
        'Patata': 4561}

fig, axs = plt.subplots(1,2, figsize=(12, 6))

#Plot1
axs[0].barh(list(frutas.keys()), list(frutas.values()), color='blue')
axs[0].set_title('Ventas de frutas - Abril 2023', fontsize=14)
axs[0].set_xlabel('Cantidad vendida')

#Plot2
axs[1].barh(list(verduras.keys()), list(verduras.values()), color='blue')
axs[1].set_title('Ventas de verduras - Abril 2023', fontsize=14)
axs[1].set_xlabel('Cantidad vendida')

plt.suptitle('Resumen de ventas - Abril 2023', fontsize=18).set_fontweight('bold')
plt.tight_layout()

plt.show()
