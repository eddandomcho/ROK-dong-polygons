import requests
import json

API_KEY = "B023532A-0009-3FEC-BB33-45A415BF6A1D"
BASE_URL = "https://api.vworld.kr/req/data"

write_file = True

def fetch_polygon(bjdong_cd):
    
    vworld_dong_cd = bjdong_cd[0:8]

    params = {
        "service": "data", 
        "request": "GetFeature", # mandatory
        "data": "LT_C_ADEMD_INFO", # mandatory   
        "key": API_KEY, # mandatory
        "format": "json",
        "errorformat": "json",
        "size": "10",
        "page": "1",
        "geometry": "true",           
        "attribute": "true",
        "attrFilter": f"emd_cd:=:{vworld_dong_cd}", 
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()

def write_polygon_json(folder_path, bjdong_cd):
    result = fetch_polygon(bjdong_cd)
    status = result["response"]["status"]

    emd_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_eng_nm"]

    file_path = f"json_files/{folder_path}/{emd_eng_nm}.json"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Saved data to json_files/{folder_path}/{emd_eng_nm}.json!")

def write_polygon_json_list(folder_path, code_list):
     for id in code_list :

        result = fetch_polygon(id)
        status = result["response"]["status"]
        if status != "OK":
                continue
        
        emd_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_eng_nm"]
        emd_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_cd"]

        file_path = f"json_files/{folder_path}/{emd_eng_nm}.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"Saved data to files/{emd_eng_nm}.json!")
            
def view_polygon_json(bjdong_cd):
    result = fetch_polygon(bjdong_cd)
    dump_string = json.dumps(result, ensure_ascii=False, indent=2)
    
    emd_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_eng_nm"]
    emd_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_cd"]
    
    print(dump_string)
    print(f"JSON file for {emd_cd}: {emd_eng_nm}")

if __name__ == "__main__":
    write_polygon_json("practice", "1144011700")