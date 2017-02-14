import json, requests

var = '90210'
url = 'http://samples.openweathermap.org/data/2.5/weather?zip=+var+,us&appid=b1b
15e88fa797225412429c1c50c122a1'

data = requests.get(url=url)
json_object= data.json()
translate = float(json_object['coord']['lon'])
print translate
