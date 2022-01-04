import pandas as pd
std=pd.read_csv("pandas/Students.csv")
print(std[:5])
print(std[3:])
print(std[3:8])
print(std[-7:-4])
print(std[::-1])
print(std[::2])