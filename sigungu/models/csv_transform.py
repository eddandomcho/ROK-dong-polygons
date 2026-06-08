# csv에서 존재 status인 법정동의 코드 추출

import pandas as pd

df = pd.read_csv("legal_dong_code_mstr.csv")
df = df[df.status == "존재"]
df = df[df["code"].astype(str).str[5:10] == "00000"]
df = df[df.level == 2]

# 시도의 모든 시군구 코드 출력
def code_list_sido(sido_code):
    if sido_code > 99:
        print("시도 코드가 범위 이상입니다!")
        return 67
    
    sido_code_str = str(sido_code)

    df_sido = df[df["code"].astype(str).str[0:2] == sido_code_str]
    code_col = df_sido["code"].astype(str).tolist()
    print(f"Returning code list for sido_code = {sido_code}")
    return code_col