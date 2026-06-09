import json
# 폴터 안에 iterate 할 수 있는 패키지
from pathlib import Path as P

# 한 파일만 트랜스폼하기
def transform_to_geojson(input_file_path, output_folder_path):
    with open(input_file_path, "r", encoding = "utf-8") as f:
        input_file = json.load(f)
    
    ctp_eng_nm = input_file["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctp_eng_nm"]
    ctprvn_cd = input_file["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctprvn_cd"]
    vworld_features = input_file["response"]["result"]["featureCollection"]["features"]
    
    # vworld.py의 features키, 읍면동 Multipolygon 데이터 추출하기

    geojs = {
        "type": "FeatureCollection",
        "features":[
            {
                "type":"Feature",
                "geometry": d["geometry"],
                "properties":d["properties"],
            } for d in vworld_features 
        ]
    }

    geojs["features"][0]["properties"]["ctprvn_cd"] = int(geojs["features"][0]["properties"]["ctprvn_cd"]) * 100000000

    with open(f"{output_folder_path}_geo.json", "w", encoding = "utf-8") as f:
        json.dump(geojs, f, indent = 2, ensure_ascii = False)
        print(f"{output_folder_path}_geo.json")
