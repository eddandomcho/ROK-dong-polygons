import requests
import json
from pathlib import Path

API_KEY = "B023532A-0009-3FEC-BB33-45A415BF6A1D"
BASE_URL = "https://api.vworld.kr/req/data"

def fetch_polygon(sig_cd):
    
    vworld_dong_cd = sig_cd[0:5]

    params = {
        "service": "data", 
        "request": "GetFeature", # mandatory
        "data": "LT_C_ADSIGG_INFO", # mandatory   
        "key": API_KEY, # mandatory
        "format": "json",
        "errorformat": "json",
        "size": "10",
        "page": "1",
        "geometry": "true",           
        "attribute": "true",
        "attrFilter": f"sig_cd:=:{vworld_dong_cd}", 
    }

    response = requests.get(BASE_URL, params=params)
    print(f"Fetched polygon for sig_cd = {sig_cd}")
    return response.json()

def write_polygon_json(folder_path, sig_cd):
    result = fetch_polygon(sig_cd)
    status = result["response"]["status"]

    sig_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["sig_eng_nm"]
    sig_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["sig_cd"]

    file_path = f"sig/json_files/{folder_path}/{sig_cd}.json"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Saved data to json_files/{folder_path}/{sig_cd}.json!")

def write_polygon_json_list(folder_path, code_list):
     
    base_dir = Path(f"sigungu/json_files/{folder_path}")

    base_dir.mkdir(parents=True, exist_ok=True)

    for id in code_list :

        result = fetch_polygon(id)
        status = result["response"]["status"]
        if status != "OK":
                continue
        
        sig_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["sig_eng_nm"]
        sig_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["sig_cd"]

        file_path = base_dir / f"{sig_cd}.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"Saved data to json_files/{folder_path}/{sig_cd}.json!")
            
def view_polygon_json(sig_cd):
    result = fetch_polygon(sig_cd)
    dump_string = json.dumps(result, ensure_ascii=False, indent=2)
    
    sig_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["sig_eng_nm"]
    sig_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["sig_cd"]
    
    print(dump_string)
    print(f"JSON file for {sig_cd}: {sig_eng_nm}")

view_polygon_json("4377032030")