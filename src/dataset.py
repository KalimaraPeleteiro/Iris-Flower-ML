class Dataset:

    def __init__(self, dataset) -> None:
        self.dataset = dataset
    

    def rename_columns(self):

        # Mudando as colunas para uma legibilidade melhor
        new_keys = {
            "sepal_length": "comprimento_da_sepala",
            "sepal_width": "largura_da_sepala",
            "petal_length": "comprimento_da_petala",
            "petal_width": "largura_da_petala",
            "species": "especie"
        }
        self.dataset = self.dataset.rename(columns=new_keys)


    def rename_species(self):
        
        # Mudando a classificação das especies
        change = {
            "Iris-setosa": 0,
            "Iris-versicolor": 1,
            "Iris-virginica": 2
        }

        self.dataset.especie = self.dataset.especie.map(change)
