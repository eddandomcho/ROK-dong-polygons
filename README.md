# 🇰🇷 대한민국 시도/시군구/폴리곤 GeoJSON 

## About
대한민국의 모든 시도, 시군구, 읍면동 폴리곤을 VWorld API로 추출하고 합치는 모델와 스크립트.

##  API

## 중오한 모델/스크립트

## 스크립트 실행 방법

```python
geojson_merge_script.py
dong_polygon_generate_script.py
emd/final_geojson/법정동_polygon_20XX-XX-XX_기준.json

```

## 📁 Repository 구조

```text
.
├── emd/
│   ├── compiled_geojson_files/
│   ├── final_geojson/
│   ├── geojson_files/
│   ├── json_files/
│   ├── models/
│   │   ├── csv_transform.py
│   │   ├── geojson_merge.py
│   │   ├── geojson_polygon.py
│   │   └── polygon.py
│   ├── visualization/
│   │   └── master_visualize_emd_geojson.py
│   ├── dong_polygon_generate_script_indiv.py
│   ├── dong_polygon_generate_script.py
│   └── geojson_merge_script.py
│
├── sido/
│   ├── final_geojson/
│   ├── geojson_files/
│   ├── json_files/
│   ├── models/
│   │   ├── csv_transform.py
│   │   ├── geojson_merge.py
│   │   ├── geojson_polygon.py
│   │   └── polygon.py
│   ├── visualization/
│   │   └── master_visualize_sido_geojson.py
│   ├── sido_polygon_generate_script.py
│   └── geojson_merge_script.py
│
├── sigungu/
│   ├── compiled_geojson_files/
│   ├── final_geojson/
│   ├── geojson_files/
│   ├── json_files/
│   ├── models/
│   │   ├── csv_transform.py
│   │   ├── geojson_merge.py
│   │   ├── geojson_polygon.py
│   │   └── polygon.py
│   ├── visualization/
│   │   └── master_visualize_sigungu_geojson.py
│   ├── sigungu_polygon_generate_script.py
│   └── geojson_merge_script.py
│
├── .gitignore
└── legal_dong_code_mstr.csv