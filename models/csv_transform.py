# csv에서 존재 status인 법정동의 코드 추출

import pandas as pd

df = pd.read_csv("legal_dong_code_mstr.csv")
df = df[df.status == "존재"]

# 시도의 모든 읍면동 코드 출력
def code_list_sido(sido_code):
    if sido_code > 99:
        print("시도 코드가 범위 이상입니다!")
        return 67
    
    sido_code_str = str(sido_code)

    df_sido = df[df["code"].astype(str).str[0:2] == sido_code_str]
    code_col = df_sido["code"].astype(str).tolist()
    print(f"Returning code list for sido_code = {sido_code}")
    return code_col

def code_list_sigungu(sido_code, sigungu_code):
    if sigungu_code > 999:
        print("시도 코드가 범위 이상입니다!")
        return 67
    
    if sido_code > 99:
        print("시도 코드가 범위 이상입니다!")
        return 67
    
    sido_code_str = str(sido_code)
    sigungu_code_str = str(sigungu_code)

    df_sigungu = df[(df["code"].astype(str).str[2:5] == sigungu_code_str)
                        & (df["code"].astype(str).str[0:2] == sido_code_str)]
    code_col = df_sigungu["code"].astype(str).tolist()
    print(f"Returning code list for sido_code = {sido_code} and sigungu_code = {sigungu_code}")
    return code_col

# if __name__ == "__main__" :
#     print("sido")
#     print(code_list_sido(26))
#     print("sigungu")
#     print(code_list_sigungu(26, 710))
    