# 🇰🇷 대한민국 시도/시군구/폴리곤 GeoJSON 

## ℹ️ About
대한민국의 모든 시도, 시군구, 읍면동 폴리곤을 VWorld API로 추출하고 합치는 모델와 스크립트.

## 🤖 API
베이스 URL: `"https://api.vworld.kr/req/data"`

API는 국토교통부의 V-World 디지털트윈국토에서 제공됐습니다. API에서 추출되는 JSON파일은 MultiPolygon 정보를 갖고 있으므로 GeoJSON팡이로 전환하는게 간단합니다.
**API레퍼런스**: [https://www.vworld.kr/dev/v4apiRefer.do](https://www.vworld.kr/dev/v4apiRefer.do)
API를 쓰기 위해 V-World API-KEY를 만들어야 합니다.

## 👨🏻‍💻 핵심 모델/스크립트/파일

### 🌐 파일
- `legal_dong_code_mstr.csv`: 시도/시군구/읍면동/리 코드, 이름, 그외에 전국 지역에 대한 정보를 가지고 있는 테이블. 시도에 속하는 모든 시군구와 읍면동 코드를 추출하기 위해 pandas로 이 csv파일을 분석합니다.
- `.gitignore`: 최종 GeoJSON 파일이 너무 큰 경우 GitHub로 push하기 곤란하기 떄문에 commit에서 지정된 파일을 제외합니다.

### 👾 모델
시도, 시군구, 아니면 읍면동 폴리곤을 찾느냐에 따라 모델이 살짝 다르지만, 기능, 함수와 파일 명은 전반적으로 똑같습니다. sido, sigungu, emd 폴더로 나누었으니 필요한 레벨에 해당하는 폴더를 쓰면됩니다. 폴더 구조를 보면 기본적인 sub폴더와 메인 파일은 다 일치합니다.
- `polygon.py`: VWorld API에서 추출한 시도/시군구/읍면동 JSON파일을 읽거나 저장하는 모델. 시군구와 읍면동 파일은 해당하는 시도 코드 폴더 안으로 분리됩니다. JSON 파일들은 `json_files/` 폴더에서 찾을 수 있습니다. 
- `geojson_polygon.py`: `polygon` 모델에서 저장한 JSON 파일을 폴더마다 읽고 GeoJSON 파일로 전환하는 모델. GeoJSON 파일들은 `geojson_files/` 폴더에서 찾을 수 있습니다.
- `geojson_merge.py`: `geojson_polygon`에서는 GeoJSON 파일들이 시군구 아니면 읍면동 레벨로 분리되었으며, 시도마다 한 파일로 합치게 위해 만든 모델입니다. `geojson_files/`에 있는 각 시도 폴더 안에 loop하면서 `compiled_geojson_files/` 폴더에 합친 파일을 저장합니다.
- `csv_transform.py`: `legal_dong_code_mstr.csv`에서 pandas로 시도 코드/시군구 코드/법정 코드 리스트를 뽑아내는 모델. 폴더 안에 루프할때 도움이 많이 되는 코드 리스트입니다. 

### 🛠️ 스크립트
- `dong_polygon_generate_script.py` / `sido_polygon_generate_script.py` / `sigungu_polygon_generate_script.py`: `polygon.py`와 `geojson_polygon.py`모델을 전국 지역에 적용하기 위해 각 시도 기준으로 loop해주는 스크립트들. 시도/시군구/법정동 파일에 따라 스크립트가 조금씩 다르지만, 전부 다 `models/` 폴더에 모델 실행을 가이드해 줍니다. 생성된 JSON파일와 GeoJSON파일들은 `json_files`/`geojson_files`에 해당하는 시도 폴더로 분리됩니다. 

- `geojson_merge_script.py`: `polygon_generate_script`에서 생성한 다수의 GeoJSON 파일들을 하나의 GeoJSON 파일로 합치기 위한 스크립트. `geojson_merge.py`을 `geojson_files`에 시도 폴더에게 먼저 적용하고, 합친 시도 레벨 GeoJSON파일들도 최종 전국 파일로 합칩니다.

- `master_visualize_level_geojson.py`: 폴리곤 생성에 상관없는 파일이기도 하지만, 폴리곤을 시각화하고 싶으면 이 파일을 쓰면 됩니다. `geopandas`하고 `matplotlib` 패키지를 사용합니다.

## ⚙️ 스크립트 실행 방법
예시로 읍면동 폴리곤을 생성하고 싶으면 `dong_polygon_generate_script.py`을 실행한 다음에 `geojson_merge_script.py`을 실행하면 됩니다.
```python
dong_polygon_generate_script.py
geojson_merge_script.py
```

최종 파일은 `final_geojson` 폴더에서 찾을 수 있습니다. 생성한 날짜에 따라 파일 명도 바뀝니다.
`emd/final_geojson/법정동_polygon_20XX-XX-XX_기준.json`

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
│   │   ├── rename_compiled_geojson_files.py
│   │   └── polygon.py
│   ├── renamed_compiled_geojson_files/
│   ├── visualization/
│   │   └── master_visualize_sigungu_geojson.py
│   ├── sigungu_polygon_generate_script.py
│   └── geojson_merge_script.py
│
├── .gitignore
└── legal_dong_code_mstr.csv