# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import requests #导入requests 模块
import time

# url1='https://report.amap.com/ajax/cityHourly.do?cityCode=110000&dataType=4'#北京
# url2='https://report.amap.com/ajax/cityHourly.do?cityCode=310000&dataType=4'#上海
# url3='https://report.amap.com/ajax/cityHourly.do?cityCode=440100&dataType=4'#广州
# url4='https://report.amap.com/ajax/cityHourly.do?cityCode=440300&dataType=4'#深圳
# url5='https://report.amap.com/ajax/cityHourly.do?cityCode=510100&dataType=4'#成都
# url6='https://report.amap.com/ajax/cityHourly.do?cityCode=330100&dataType=4'#杭州
# url7='https://report.amap.com/ajax/cityHourly.do?cityCode=420100&dataType=4'#武汉
# strhtml1=requests.get(url1)
# strhtml2=requests.get(url2)
# strhtml3=requests.get(url3)
# strhtml4=requests.get(url4)
# strhtml5=requests.get(url5)
# strhtml6=requests.get(url6)
# strhtml7=requests.get(url7)
# results1=strhtml1.text.split(',')
# results2=strhtml2.text.split(',')
# results3=strhtml3.text.split(',')
# results4=strhtml4.text.split(',')
# results5=strhtml5.text.split(',')
# results6=strhtml6.text.split(',')
# results7=strhtml7.text.split(',')
# result1=results1[43].strip(']')
# result2=results2[25].strip(']')
# result3=results3[25].strip(']')
# result4=results4[25].strip(']')
# result5=results5[25].strip(']')
# result6=results6[25].strip(']')
# result7=results7[25].strip(']')
# resultlist=[]
# resultlist.append(result1)
# resultlist.append(result2)
# resultlist.append(result3)
# resultlist.append(result4)
# resultlist.append(result5)
# resultlist.append(result6)
# resultlist.append(result7)
# for i in range(0,7):
#       print(resultlist[i])
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)
# 1627383600000

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