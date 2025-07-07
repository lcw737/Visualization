import pandas as pd

url ='../resData/sample.html'
tables = pd.read_html(url)

print('테이블갯수:', len(tables))

for i in range(len(tables)):
    print("## tables[%s] ##" % i)
    print(tables[i])
    print("="*30)

df = tables[1]
df.set_index(['name'], inplace=True)
print(df)
print("="*30)

url ='https://pann.nate.com/talk/c20023?page=1'
tables = pd.read_html(url)
print('테이블갯수:', len(tables))
print("="*30)

boardTable = tables[0]
print(boardTable)
print("="*30)

boardTable.columns = ['제목', '작성자', '조회수', '작성일']
print(boardTable)