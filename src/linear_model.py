import pandas as pd
import numpy as np
from dataset import Dataset
from sklearn.svm import LinearSVC
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import train_test_split


np.random.seed(10)

data = Dataset(pd.read_csv("IRIS.csv"))
data.rename_columns()
data.rename_species()

x = data.dataset[["comprimento_da_sepala", "largura_da_sepala",
                  "comprimento_da_petala", "largura_da_petala"]]
y = data.dataset["especie"]

train_x, test_x, train_y, test_y = train_test_split(x, y, 
                                                    test_size=0.25, 
                                                    stratify=y)

dummy = DummyClassifier()
dummy.fit(train_x, train_y)

model = LinearSVC()
model.fit(train_x, train_y)

accuracy_dummy = dummy.score(test_x, test_y) * 100
accuracy = model.score(test_x, test_y) * 100
performance = ((accuracy - accuracy_dummy)/accuracy_dummy)*100

print(f'A nossa baseline é de {accuracy_dummy:.2f}%')
print(f'A taxa de acerto do modelo é {accuracy:.2f}%')
print(f'O ganho de performance com o uso do modelo é de {performance:.2f}%')