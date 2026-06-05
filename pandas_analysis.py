import pandas as pd

df = pd.read_csv("legal_dong_code_mstr.csv")

print(len(df[df.level == 3]))