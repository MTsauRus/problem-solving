import pandas as pd

file1 = r'C:\Users\local3\Desktop\document\tmp\3.7 푸디헤븐 족발.xlsx'
file2 = r'C:\Users\local3\Desktop\document\tmp\250307.xlsx'

# 파일 확장자에 따라 엔진 선택
df1 = pd.read_excel(file1, engine='openpyxl')  # XLSX 파일 → openpyxl 사용
df2 = pd.read_excel(file2, engine='openpyxl')

# # '성함' 컬럼의 첫 두 글자 추출
names1_prefix = (df1['성함'].astype(str).str[:2])  
df2_filtered = df2[~df2['성함'].astype(str).str[:2].isin(names1_prefix)]  

print(names1_prefix)
print(df2_filtered)

# 결과 출력
print(df2_filtered['성함'].dropna().tolist())
print(len(df2_filtered))