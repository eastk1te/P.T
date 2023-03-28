python postgresql get dataframe | [https://blog.naver.com/junix/220611598818](https://blog.naver.com/junix/220611598818)

List of Date Format Specifiers in MySQL : [https://database.guide/list-of-date-format-specifiers-in-mysql/](https://database.guide/list-of-date-format-specifiers-in-mysql/)

## 데이터 베이스
```python
# ======================================================================================================
# !pip install psycopg2-binary
# psycopg2-binary와 psycopg2, 두 가지 패키지가 있는데, 일반적인 End-user라면 -binary패키지를 사용하는 것이 좋습니다. 
# 단, 해당 패키지에 의존성을 갖는 다른 패키지를 담당하고 배포하는 개발자이거나 자체로 빌드를 해야 할 필요가 있다면, 바이너리 패키지를 이용하면 안 됩니다.

# PostgreSQL : https://syncnet.tistory.com/entry/Python-%EC%9C%BC%EB%A1%9C-Postgresql-%EB%8D%B0%EC%9D%B4%ED%83%80%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%97%B0%EB%8F%99-%EA%B0%84%EB%8B%A8-%EB%A6%AC%EB%B7%B0
# PostgreSQL 에서는 st_x, st_y 등의 함수로 공간정보에서 x,y 등의 좌표를 추출함. if z, m 정보가 있으면 st_z, st_m 등으로 추출 가능

# dev server ip
connection = psycopg2.connect(host=host, dbname="",  # psycopg2를 활용하여 db 연결
                              user=username, password=password, port=5432)
cur = connection.cursor()                                   # 커서 설정
sql_query = ''' '''                                         # 입력할 sql query 입력
cur.execute(sql_query)                                      # 커서를 활용하여 sql query 실행
df = cur.fetchall()                                         # 실행된 데이터를 전부 가져옴
df_columns = [desc[0] for desc in cur.description]          # 해당 실행문의 columns 가져오기
connection.close()                                          # db 연결 종료

# About PostGIS ST_Buffer
# https://www.joinc.co.kr/w/man/12/spatial
# https://domdom.tistory.com/entry/python-특정-좌표가-특정-polygon-boundary-안에-있는지-확인하는-방법-1


# dbeaver 
# ======================================================================================================
# SSH           : https://library.gabia.com/contents/infrahosting/9002/
# SSH 명령어 정리: https://velog.io/@gth1123/ssh-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%B0%8F-%EC%98%B5%EC%85%98-%EC%A0%95%EB%A6%AC
# SSH, git      : https://blog.naver.com/rodpold/222766656687


# SSH connetion with python : https://www.linode.com/docs/guides/use-paramiko-python-to-ssh-into-a-server/
# !pip install paramiko

# PostfreSQL 기본포트 5432 : https://m.blog.naver.com/stonefly2001/221600279842

# ssh => db와 해당 컴퓨터 연결해줌.
# import paramiko

# command = ''
# host = 'localhost'
# username = ''
# password = ''

# client = paramiko.client.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(host, username=username, password=password)
# _stdin, _stdout,_stderr = client.exec_command("df")
# print(stdout.read().decode())
# client.close()

# 개발서버 ip = host
# 개발서버 아이디랑 비번 필요?

# ssh -L 5432:localhost:5432 id@0.0.0.0 => Dbeaver 연결을 위해 ssh로 연결을 함
# 그래서 개발 서버 아이디 생성함.

# ======================================================================================================
# 해당 범위에 포함된 new_df의 index들을 inside에 저장히고 범위안에 하나만 있으면 matchlist에 저장
rst_mt = {} # restaurant mapping table
for idx, row in sever_df[list(map(lambda x : len(x) >= 1, sever_df['inside']))].iterrows():
    former = row['name'] + ',' + row['address']
    if former in rst_mt:
        continue
    else:
        results = []
        for i in row['inside']:
            t = new_df.iloc[i,[7,11]] # new_df BSSH_NM, LOCP_ADDR
            results.append(t[0] + ',' + t[1])
        
        rst_mt[former] = results


# ======================================================================================================
# import folium
# m = folium.Map(location=[sever_df.loc[0,'st_y'], sever_df.loc[0,'st_x']],zoom_start=1000)
# folium.Circle([36.348534,127.452488],radius=5).add_to(m)
# poly = list(map(lambda x : [float(i) for i in x.split(' ')[::-1]], sever_df.loc[0,'st_astext'].lstrip('POLYGON((').rstrip('))').split(',')))
# folium.PolyLine(poly).add_to(m)
# m

#!pip install shapely
# from shapely.geometry import Point
# from shapely.geometry.polygon import Polygon
# from tqdm import tqdm
#Point(new_df['SITE_X'],new_df['SITE_Y'])

# python으로 polyline 안에 있는지 check
# sever_df['st_astext'].str.lstrip('POLYGON((').str.rstrip('))').str.split(',')[0]
# sever_df['poly'] = list(map(lambda x : [[float(j) for j in i.split(' ')[::-1]] for i in x], sever_df['st_astext'].str.lstrip('POLYGON((').str.rstrip('))').str.split(',')))

### Google geocoder GoogleV3
# ======================================================================================================
# !pip install geopy
# from geopy.geocoders import GoogleV3

# geo_local = GoogleV3()

# def geocoding(address):
#     print(address)
#     geo = geo_local.geocode(address)
    
#     if not geo:
#         return None

#     print(geo)
#     x_y = (geo.latitude, geo.longitude)
#     return x_y

# geocoding(sever_df.address[1])
#list(map(geocoding, sever_df.address))

# geocoding('춘천시 소양강로 202')
```