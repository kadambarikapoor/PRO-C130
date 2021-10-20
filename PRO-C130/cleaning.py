import pandas as pd
import csv
df=pd.read_csv("total_stars.csv")

print (df.shape)

del df["Luminosity"]
del df["Star_name_1"]
del df["Distance_1"]
del df["Mass_1"]
del df["Radius_1"]

df.to_csv('main.csv') 