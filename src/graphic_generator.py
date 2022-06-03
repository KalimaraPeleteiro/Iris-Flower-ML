import pandas as pd
import matplotlib.pyplot as plt
from dataset import Dataset


data = Dataset(pd.read_csv("IRIS.csv"))
data.rename_columns()

x = data.dataset.largura_da_petala
y = data.dataset.especie

figure, axis = plt.subplots()

plt.plot(x, y, 'o')
axis.set(yticks=range(3))

plt.xlabel("Largura das Pétalas")
plt.title("Largura Pétala x Espécie")
plt.show()
