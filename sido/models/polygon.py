import requests
import json
from pathlib import Path

API_KEY = "B023532A-0009-3FEC-BB33-45A415BF6A1D"
BASE_URL = "https://api.vworld.kr/req/data"

write_file = True

def fetch_polygon(sido_cd):
    
    vworld_sido_cd = sido_cd[0:2]

    params = {
        "service": "data", 
        "request": "GetFeature", # mandatory
        "data": "LT_C_ADSIDO_INFO", # mandatory   
        "key": API_KEY, # mandatory
        "format": "json",
        "errorformat": "json",
        "size": "10",
        "page": "1",
        "geometry": "true",           
        "attribute": "true",
        "attrFilter": f"ctprvn_cd:=:{vworld_sido_cd}", 
    }

    response = requests.get(BASE_URL, params=params)
    print(f"Fetched polygon for sido_cd = {sido_cd}")
    return response.json()

def write_polygon_json(folder_path, sido_cd):
    result = fetch_polygon(sido_cd)
    status = result["response"]["status"]

    ctp_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctp_eng_nm"]
    ctprvn_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctprvn_cd"]

    file_path = f"{folder_path}/{ctprvn_cd}.json"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Saved data to sido/json_files/{folder_path}/{ctprvn_cd}.json!")

def write_polygon_json_list(folder_path, code_list):
     
    base_dir = Path(f"sido/json_files/{folder_path}")

    base_dir.mkdir(parents=True, exist_ok=True)

    for id in code_list :

        result = fetch_polygon(id)
        status = result["response"]["status"]
        if status != "OK":
                continue
        
        ctp_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctp_eng_nm"]
        ctprvn_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctprvn_cd"]

        file_path = base_dir / f"{ctprvn_cd}.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"Saved data to sido/json_files/{folder_path}/{ctprvn_cd}.json!")
            
def view_polygon_json(sido_code):
    result = fetch_polygon(sido_code)
    dump_string = json.dumps(result, ensure_ascii=False, indent=2)
    
    ctp_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctp_eng_nm"]
    ctprvn_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["ctprvn_cd"]
    
    print(dump_string)
    print(f"JSON file for {ctprvn_cd}: {ctp_eng_nm}")

view_polygon_json("36")