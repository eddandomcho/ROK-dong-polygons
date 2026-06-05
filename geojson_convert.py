import requests
import json

with open("./json_files/practice/Sangsu-dong.json", "r", encoding="utf-8") as f:
    input_file = json.load(f)

emd_eng_nm = input_file["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_eng_nm"]
#print(json.dumps(input_file, ensure_ascii=False, indent=2))
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

with open(f"./json_files/{emd_eng_nm}_geodata.json", "w", encoding = "utf-8") as f:
    output_file = json.dump(geojs, f, indent = 2, ensure_ascii = False)

#print(input_file)