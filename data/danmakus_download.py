import requests
import json

# read liveId from file
with open("./data/to_be_downloaded.csv","r",encoding="UTF-8") as f:
    lives = f.readlines()

# download stream danmaku files from danmakus
api_link = "https://ukamnads.icu/api/v2/live"
params_setting = {
    "liveId": "",
    "pangeNum": 0,
    "type":0,
    "pageSize": -1,
    "includeExtra": "false",
    "useEmoji": "true",
}




for live in lives:
    liveName = live.split(",")[0]
    liveId = live.split(",")[1][26:-1]
    params_setting["liveId"] = liveId
    # request stream danmakus (plaintext) from danmakus
    response = requests.get(api_link, params_setting)
    response_dic = json.loads(response.text)
    if response.status_code == 200:
        # success
        print(f'缺失xml文件：{liveName}\tdanmakus直播标题：{response_dic["data"]["data"]["live"]["title"]}')
        # process comments
        # print(response_dic["data"]["data"]["danmakus"][:10])
        with open("./data/"+liveName+".json","w") as f:
            json.dump(response_dic["data"]["data"],f) 
    else:
        # print error status code
        print(f'缺失xml文件：{liveName}\t 出现错误：')
        print(response_dic)


