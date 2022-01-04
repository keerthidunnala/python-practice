import pandas as pd
std=pd.read_csv("pandas/Students.csv")
print(std["marks"]>50)