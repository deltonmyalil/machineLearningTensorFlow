import pandas as pd
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe)
print(california_housing_dataframe.describe())

# describe gives count, mean, std, min, max, percentage values etc