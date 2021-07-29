# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import requests #导入requests 模块
import time

list=['https://report.amap.com/ajax/cityHourly.do?cityCode=110000&dataType=4',
      'https://report.amap.com/ajax/cityHourly.do?cityCode=310000&dataType=4',
      'https://report.amap.com/ajax/cityHourly.do?cityCode=440100&dataType=4',
      'https://report.amap.com/ajax/cityHourly.do?cityCode=440300&dataType=4',
      'https://report.amap.com/ajax/cityHourly.do?cityCode=510100&dataType=4',
      'https://report.amap.com/ajax/cityHourly.do?cityCode=330100&dataType=4',
      'https://report.amap.com/ajax/cityHourly.do?cityCode=420100&dataType=4']

localtime=time.localtime(time.time())
hour=int(time.strftime("%H",localtime))
if hour>8:
      tmp=(hour-8)*2-1
      count=46-tmp
strhtml=[]
for i in range(0,7):
      strhtml.append(requests.get(list[i]).text.split(',').__getitem__(count).strip(']'))
jsonArr=json.dumps(strhtml)
print(jsonArr)