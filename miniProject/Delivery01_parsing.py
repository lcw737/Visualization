import requests, json

url = 'https://openapi.gg.go.kr/GGEXPSDLV'
params = dict(
    Type='json',
    pSize='10',
    Key='8b973d9f2fab4c2083f39abd3a9fd347')

raw_data = requests.get(url=url, params=params)
binary_data = raw_data.content
json_data = json.loads(binary_data)
print(json_data)

