from django.test import TestCase

# Create your tests here.
import requests

import requests

url = "https://apis.openapi.sk.com/tmap/routes?version=1&callback=function"

payload = {
    "tollgateFareOption": 16,
    "roadType": 32,
    "directionOption": 1,
    "endX": 129.07579349764512,
    "endY": 35.17883196265564,
    "endRpFlag": "G",
    "reqCoordType": "WGS84GEO",
    "startX": 126.98217734415019,
    "startY": 37.56468648536046,
    "gpsTime": "20191125153000",
    "speed": 10,
    "uncetaintyP": 1,
    "uncetaintyA": 1,
    "uncetaintyAP": 1,
    "carType": 0,
    "startName": "%EC%9D%84%EC%A7%80%EB%A1%9C%20%EC%9E%85%EA%B5%AC%EC%97%AD",
    "endName": "%ED%97%A4%EC%9D%B4%EB%A6%AC",
    "passList": "127.38454163183215,36.35127257501252",
    "gpsInfoList": "126.939376564495,37.470947057194365,120430,20,50,5,2,12,1_126.939376564495,37.470947057194365,120430,20,50,5,2,12,1",
    "detailPosFlag": "2",
    "resCoordType": "WGS84GEO",
    "sort": "index"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "appKey": "l7xxa1779b4666934552abc78240dd79258e"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)