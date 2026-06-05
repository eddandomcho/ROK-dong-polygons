import pandas as pd

df = pd.read_csv("legal_dong_code_mstr.csv")

sido_code_list = df["code"].astype(str).str[0:2].unique()

# Create a temporary copy of the sliced codes just for printing
temp_df = df.copy()
temp_df["code_sido"] = temp_df["code"].astype(str).str[0:2]

# Print the final unique pairs exactly ONCE
print(temp_df[["code_sido", "sido"]].drop_duplicates().reset_index(drop=True))