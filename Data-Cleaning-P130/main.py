import pandas as pd

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]

df.to_csv('main.csv')