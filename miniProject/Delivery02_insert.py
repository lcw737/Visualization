import cx_Oracle as cx
import requests, json

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

url = 'https://openapi.gg.go.kr/GGEXPSDLV'
for page in range(1,36):
    params = dict(
        Type='json',
        pIndex=page,
        pSize='1000',
        Key='8b973d9f2fab4c2083f39abd3a9fd347')

    raw_data = requests.get(url=url, params=params)
    binary_data = raw_data.content
    json_data = json.loads(binary_data)

    rows = json_data['GGEXPSDLV'][1]['row']

    for jd in rows:
        SIGUN_NM = jd['SIGUN_NM']  # 시군명
        STR_NM = jd['STR_NM'] # 매장명
        REFINE_ROADNM_ADDR = jd['REFINE_ROADNM_ADDR']  # 도로명주소
        REFINE_WGS84_LAT = jd['REFINE_WGS84_LAT']  # 위도
        REFINE_WGS84_LOGT = jd['REFINE_WGS84_LOGT']  # 경도
        # print(SIGUN_NM,REFINE_ROADNM_ADDR, REFINE_WGS84_LAT, REFINE_WGS84_LOGT)

        sql = """insert into delivery_apps (idx, sigun, str_nm, road_addr,  latitude, longitude)
                 values (seq_board_num.NEXTVAL, :sigun, :str_nm, :road_addr,  :latitude, :longitude)"""

        try:
            cursor.execute(sql, sigun=SIGUN_NM, str_nm=STR_NM, road_addr=REFINE_ROADNM_ADDR,
                           latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
            conn.commit()
            print("레코드 입력")
        except Exception as e:
            conn.rollback()
            print("insert 실행시 오류발생", e)

conn.close()