import json
# 폴터 안에 iterate 할 수 있는 패키지
from pathlib import Path as P

def geojson_merge_list(input_folder_path, output_folder_path, final):
    if final == True:
        input_dir = P(input_folder_path)

    if final == False:
        input_dir = P(f"geojson_files/{input_folder_path}")

    compile_dict = {}

    # 일반 geojson 컴파일러
    if final == False:
        for file_path in input_dir.glob("*.json"):
            with open(file_path, "r", encoding = "utf-8") as f:
                input_file = json.load(f)

            features = input_file["features"][1]

            type = features["type"]
            properties = features["properties"]
            # print("printing properties")
            # print(properties)
            geometry = features["geometry"]

            emd_cd = properties["emd_cd"]
            # print(emd_cd)

            mini_dict = {
                "type" : type,
                "properties" : properties,
                "geometry" : geometry
            }

            compile_dict[emd_cd] = mini_dict

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
    
    # 마지막 컴파일러
    if final == True:
        for file_path in input_dir.glob("*.json"):
            with open(file_path, "r", encoding = "utf-8") as f:
                input_file = json.load(f)

            features = input_file["features"]
            print(len(features))

            for i in range(0, len(features)):
                indiv_feature = features[i]
                type = indiv_feature["type"]
                # print(type)
                properties = indiv_feature["properties"]
                # print("printing properties")
                # print(properties)
                geometry = indiv_feature["geometry"]

                emd_cd = properties["emd_cd"]
                # print(emd_cd)

                mini_dict = {
                    "type" : type,
                    "properties" : properties,
                    "geometry" : geometry
                }

                compile_dict[emd_cd] = mini_dict

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

    with open(f"{output_folder_path}/{input_folder_path}_geo.json", "w", encoding = "utf-8") as f:
        json.dump(geojs, f, indent = 2, ensure_ascii = False)
        print(f"Saved data to {output_folder_path}/{input_folder_path}_geo.json!")