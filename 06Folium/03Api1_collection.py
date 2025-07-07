import requests, json

'''
경기 데이터 드림(https://data.gg.go.kr)
에서 제공하는 "전문 및 대학교 현황" OpenAPI
'''
# API 요청 URL
url = 'https://openapi.gg.go.kr/Jnclluniv?'
# 파라미터(pSiez : 출력데이터 갯수)
params = dict(
    Type='json',
    pSize='10',
    Key='37036b829e80435b9bd513cb9d7cdfd3')
# OpenAPI의 요청URL과 파리미터를 이용해서 페이지 정보를 JSON으로 얻어온다.
raw_data = requests.get(url=url, params=params)
# Raw(로우) 데이터를 JSON으로 변환
binary_data = raw_data.content
# 변환 완료된 JSON 데이터 로드
json_data = json.loads(binary_data)
print(json_data)

'''
JSON 데이터를 분석한 후 Key를 찾았다면 아래와 같이 반복문으로 통해
필요한 값을 파싱한다. 
'''
for jd in json_data['Jnclluniv'][1]['row']:
    SIGUN_NM = jd['SIGUN_NM'] # 시군
    FACLT_NM = jd['FACLT_NM'] # 대학명
    REFINE_LOTNO_ADDR = jd['REFINE_LOTNO_ADDR'] # 주소
    REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT'] # 위도
    REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT'] # 경도
    print(FACLT_NM, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)
