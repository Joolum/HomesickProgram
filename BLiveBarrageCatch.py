import requests
import json
import time

url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?'
roomid = 22625027

while(True):
    time.sleep(1)
    blive_Data = requests.get(url+'roomid='+str(roomid))
    blive_Data.encoding="utf-8"
    danmu_data = blive_Data.json()['data']['room']
    for danmu in danmu_data:
        print("Uid:"+str(danmu['uid'])+","+danmu['nickname']+"说："+danmu['text'])