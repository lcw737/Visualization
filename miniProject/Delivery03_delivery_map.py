import cx_Oracle as cx
import folium

host_name = 'localhost'
oracle_port = 1521
service_name = 'xe'
connect_info = cx.makedsn(host_name, oracle_port, service_name)
conn = cx.connect('education', '1234', connect_info)
cursor = conn.cursor()

delivery_map = folium.Map(location=[37.40,127.38], zoom_start=10)

sql = "select * from delivery_apps order by idx asc"
cursor.execute(sql)

input_sg = input("시군을 입력하세요.")

for rs in cursor:
    if rs[1] == input_sg:
        idx = rs[0]
        sigun = rs[1]
        str_nm = rs[2]
        load_addr = rs[3]
        latitude = rs[4]
        longitude = rs[5]

        folium.Marker([latitude, longitude], popup=str_nm).add_to(delivery_map)
        print(str_nm, latitude, longitude)

delivery_map.save(f'../saveFiles/delivery_map{input_sg}.html')
print("맵이 생성되었습니다.")
