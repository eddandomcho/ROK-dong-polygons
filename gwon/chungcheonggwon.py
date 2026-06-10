import json
# 폴터 안에 iterate 할 수 있는 패키지
from pathlib import Path as P
from datetime import date

files = {
    "daejeon" : "sigungu/compiled_geojson_files/30_geo.json",
    "chungbuk" : "sigungu/compiled_geojson_files/43_geo.json",
    "chungnam" : "sigungu/compiled_geojson_files/44_geo.json"
}

compile_dict = {}

# 세종특별차지시
with open("sido/geojson_files/36_geo.json", "r", encoding = "utf-8") as f:
    input_file = json.load(f)

    for i in range(0, len(input_file["features"])):
        features = input_file["features"][i]

        type = features["type"]
        properties = features["properties"]
        # print("printing properties")
        # print(properties)
        geometry = features["geometry"]

        ctprvn_cd = properties["ctprvn_cd"]

        mini_dict = {
            "type" : type,
            "properties" : properties,
            "geometry" : geometry
        }

        compile_dict[ctprvn_cd] = mini_dict

for file_path in files.values():
    with open(file_path, "r", encoding = "utf-8") as f:
        input_file = json.load(f)

    for i in range(0, len(input_file["features"])):
        features = input_file["features"][i]

        type = features["type"]
        properties = features["properties"]
        # print("printing properties")
        # print(properties)
        geometry = features["geometry"]

        sig_cd = properties["sig_cd"]

        mini_dict = {
            "type" : type,
            "properties" : properties,
            "geometry" : geometry
        }

        compile_dict[sig_cd] = mini_dict

geojs = {
    "type" : "FeatureCollection",
    "features":[
            {
                "type":"Feature",
                "properties":d["properties"],
                "geometry": d["geometry"]
            } for d in compile_dict.values()
        ]
}

today = str(date.today())

file_name = f"충청권_polygon_{today}_기준_geo.json"

with open(f"gwon/compiled_geojson_files/{file_name}", "w", encoding = "utf-8") as f:
    json.dump(geojs, f, indent = 2, ensure_ascii = False)
    print(f"Saved data to gwon/compiled_geojson_files/{file_name}!")