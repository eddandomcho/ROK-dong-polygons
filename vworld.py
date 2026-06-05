import requests
import json

API_KEY = "B023532A-0009-3FEC-BB33-45A415BF6A1D"
BASE_URL = "https://api.vworld.kr/req/data"

write_file = True

dong_id = "1156011000" 

ydpg_ids = [
  "1156000000", "1156000100", "1156000200", "1156000300", "1156000400", 
  "1156000500", "1156000600", "1156000700", "1156000800", "1156000900", 
  "1156001000", "1156001100", "1156001200", "1156001300", "1156001400", 
  "1156001500", "1156001600", "1156001700", "1156001800", "1156001900", 
  "1156002000", "1156002100", "1156002200", "1156002300", "1156002400", 
  "1156002500", "1156002600", "1156002700", "1156002800", "1156002900", 
  "1156003000", "1156003100", "1156003200", "1156003300", "1156003400", 
  "1156003500", "1156003600", "1156003700", "1156003800", "1156003900", 
  "1156004000", "1156004100", "1156004200", "1156004300", "1156004400", 
  "1156004500", "1156004600", "1156004700", "1156010100", "1156010200", 
  "1156010300", "1156010400", "1156010500", "1156010600", "1156010700", 
  "1156010800", "1156010900", "1156011000", "1156011100", "1156011200", 
  "1156011300", "1156011400", "1156011500", "1156011600", "1156011700", 
  "1156011800", "1156011900", "1156012000", "1156012100", "1156012200", 
  "1156012300", "1156012400", "1156012500", "1156012600", "1156012700", 
  "1156012800", "1156012900", "1156013000", "1156013100", "1156013200", 
  "1156013300", "1156013400", "1156090100", "1156090200", "1156090300", 
  "1156090400", "1156090500", "1156090600", "1156090700", "1156090800", 
  "1156090900", "1156091000", "1156091100", "1156091200", "1156091300", 
  "1156091400", "1156091500", "1156091600", "1156091700", "1156091800", 
  "1156091900", "1156092000", "1156092100"
]

def fetch_polygon(bjdong_cd):
    
    vworld_dong_cd = bjdong_cd[:8]

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
    #result = json.loads(response.text)
    #return result

if __name__ == "__main__":

    for id in ydpg_ids :

        result = fetch_polygon(id)
        status = result["response"]["status"]
        if status != "OK":
                continue
        
        emd_eng_nm = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_eng_nm"]
        emd_cd = result["response"]["result"]["featureCollection"]["features"][0]["properties"]["emd_cd"]

        if write_file:
            file_path = f"json_files/ydpg/{emd_eng_nm}.json"

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
                print(f"Saved data to files/{emd_eng_nm}.json!")

        else:
            print(emd_eng_nm)
            print(emd_cd)
            #print(json.dumps(result, ensure_ascii=False, indent=2))