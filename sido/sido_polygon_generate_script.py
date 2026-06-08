import requests
import pandas as pd
import json
import models.geojson_polygon as gp
import models.polygon as p

df = pd.read_csv("legal_dong_code_mstr.csv")
df = df[df.status == "존재"]
df = df[df.level == 3]

sido_code_list = df["code"].astype(str).str[0:2].astype(int).unique().tolist()
print("Generated sido_code_list!")

for i in sido_code_list:
    # p.write_polygon_json("sido/json_files", str(i))
    # print(f"Wrote polygon json file for sido code {i}!")

    gp.transform_to_geojson(f"sido/json_files/{i}.json", f"sido/geojson_files/{i}")
    print(f"Wrote polygon GeoJSON files for sido code {i}!")