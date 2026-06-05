import json

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

#def transform_to_geojson_list(input_folder_path, output_folder_path):

transform_to_geojson("json_files/practice/Hajung-dong.json", "json_files/practice")