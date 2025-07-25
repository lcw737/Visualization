import pandas as pd
import cx_Oracle as cx

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

df1 = pd.read_excel('../resData/전문및대학교현황.xls')
print(df1)

# 데이터프레임을 통해 반복할떄는 iterrows() 함수가 필요하다.
for index, row in df1.iterrows():
    # 컬럼명이 한글이어도 다음과 같이 사용할 수 있다. 
    print(row.시군명, row.학교구분명, row.WGS84위도, row.WGS84경도)

    SIGUN_NM = row.시군명  # 시군
    FACLT_NM = row.학교구분명  # 대학명
    REFINE_LOTNO_ADDR = row.소재지도로명주소  # 주소
    REFINE_WGS84_LAT = row.WGS84위도 # 위도
    REFINE_WGS84_LOGT = row.WGS84경도  # 경도

    sql = """insert into g_univ (idx, sigun, faclt, addr, latitude, longitude)
                 values (seq_board_num.NEXTVAL, :sigun, :faclt, :addr, :latitude, :longitude)"""

    try:
        # 커서를 통해 쿼리문 실행
        cursor.execute(sql, sigun=SIGUN_NM, faclt=FACLT_NM, addr=REFINE_LOTNO_ADDR,
                       latitude=REFINE_WGS84_LAT, longitude=REFINE_WGS84_LOGT)
        conn.commit()
        print("1개의 레코드 입력")
    except Exception as e:
        conn.rollback()
        print("insert 실행시 오류발생", e)

conn.close()