import requests
import pandas as pd
import json
import models.csv_transform as ct
import models.geojson_polygon as gp
import models.polygon as p

df = pd.read_csv("legal_dong_code_mstr.csv")
df = df[df.status == "존재"]
df = df[df.level == 2]

sido_code_list = df["code"].astype(str).str[0:2].astype(int).unique().tolist()
print("Generated sido_code_list!")

for i in sido_code_list:
    code_list_sido = ct.code_list_sido(i)
    print(f"Generated code_list_sido for sido code {i}!")

    p.write_polygon_json_list(str(i), code_list_sido)
    print(f"Wrote polygon json files for sido code {i}!")

    gp.transform_to_geojson_list(f"sigungu/json_files/{i}", f"sigungu/geojson_files/{i}")
    print(f"Wrote polygon GeoJSON files for sido code {i}!")