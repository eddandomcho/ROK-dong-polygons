import requests
import pandas as pd
import json
import models.geojson_polygon as gp
import models.polygon as p
import models.geojson_merge as gm

df = pd.read_csv("legal_dong_code_mstr.csv")
df = df[df.status == "존재"]
df = df[df.level == 3]

gm.geojson_merge_list("sido/geojson_files", "sido/final_geojson", True)