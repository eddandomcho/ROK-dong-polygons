import requests
import pandas as pd
import json
import models.csv_transform as ct
import models.geojson_polygon as gp
import models.polygon as p
import models.geojson_merge as gm

df = pd.read_csv("legal_dong_code_mstr.csv")
df = df[df.status == "존재"]
df = df[df.level == 3]

sido_code_list = df["code"].astype(str).str[0:2].unique().tolist()

for i in sido_code_list:
    gm.geojson_merge_list(i, "compiled_geojson_files", False)

gm.geojson_merge_list("compiled_geojson_files", "final_geojson", True)