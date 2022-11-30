import pandas as pd
import csv

df = pd.read_csv("final_data.csv")
df.drop(['Star_name','Distance','Mass','Luminosity'])
final_data = df.dropna()
final_data.to_convert("final_star_data.csv")