import json
# 폴터 안에 iterate 할 수 있는 패키지
from pathlib import Path as P

# 한 파일만 트랜스폼하기
def transform_to_geojson(input_file_path, output_folder_path):
    with open(input_file_path, "r", encoding = "utf-8") as f:
        input_file = json.load(f)
    
    emd_eng_nm = input_file["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_eng_nm"]
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

    with open(f"{output_folder_path}/{emd_eng_nm}_geo.json", "w", encoding = "utf-8") as f:
        json.dump(geojs, f, indent = 2, ensure_ascii = False)
        print(f"Saved data to {output_folder_path}/{emd_eng_nm}_geo.json!")

# 폴더에 있는 여러게의 파일을 함꼐 트랜스폼하기

def transform_to_geojson_list(input_folder_path, output_folder_path):
    input_dir = P(input_folder_path)
    output_dir = P(output_folder_path)

    # 2. Make sure the output folder exists before starting the loop
    output_dir.mkdir(parents=True, exist_ok=True)

    for file_path in input_dir.glob("*.json"):
        with open(file_path, "r", encoding = "utf-8") as f:
            input_file = json.load(f)

        emd_eng_nm = input_file["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_eng_nm"]
        vworld_features = input_file["response"]["result"]["featureCollection"]["features"]

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

        out_file_path = output_dir / f"{emd_eng_nm}_geo.json"

        with open(out_file_path, "w", encoding = "utf-8") as f:
            json.dump(geojs, f, indent = 2, ensure_ascii = False)
            print(f"Saved data to {out_file_path}!")

#transform_to_geojson("json_files/practice/Samseong-dong.json", "json_files/practice")
# transform_to_geojson_list("json_files/ydpg", "json_files/ydpgpractice")