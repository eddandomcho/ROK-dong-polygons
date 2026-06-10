import json
# 폴터 안에 iterate 할 수 있는 패키지
from pathlib import Path as P
import pandas as pd

df = pd.read_csv("legal_dong_code_mstr.csv")
df = df[df.status == "존재"]
df = df[df.level == 1]

def extract_sido_name(sido_2d_code):
    sido_full_code = sido_2d_code * 100000000
    df_new = df[df.code == sido_full_code]
    sido_en = df_new["sido_en"].iloc[0]
    return(sido_en)

input_dir = P("sigungu/compiled_geojson_files")
output_dir = P("sigungu/renamed_compiled_geojson_files")

for file_path in input_dir.glob("*.json"):
        with open(file_path, "r", encoding = "utf-8") as f:
            input_file = json.load(f)

        file_path_name = str(file_path)

        sido_number = int(file_path_name.split("/")[2][0:2])

        sido_en = extract_sido_name(sido_number)

        new_file_name = str(sido_number) + "_" + sido_en + "_geo.json"

        out_file_path = f"sigungu/renamed_compiled_geojson_files/{new_file_name}"

        with open(out_file_path, "w", encoding = "utf-8") as f:
            json.dump(input_file, f, indent = 2, ensure_ascii = False)
            print(f"Saved data to {out_file_path}!")