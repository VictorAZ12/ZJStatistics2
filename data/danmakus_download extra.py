import requests
import json

# liveIds to be downloaded separately and combined to a single file
lives = ["2021.03.24 珈乐 Disco 陪我练歌啦.xml,https://danmakus.com/live/ec67e3d5-2986-4918-a051-7c5d00bb11ec",
"2021.03.24 珈乐 Disco 陪我练歌啦.xml,https://danmakus.com/live/cf57d50f-e5c3-499f-8b51-30a3239338fd",
"2021.03.24 珈乐 Disco 陪我练歌啦.xml,https://danmakus.com/live/26728f6b-a0b7-4965-b292-2fbc86743222",
"2021.03.24 珈乐 Disco 陪我练歌啦.xml,https://danmakus.com/live/0937225f-c88e-425b-be43-f0671bc9f172"]

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


basedic = {}

for live in lives:
    liveName = live.split(",")[0]
    liveId = live.split(",")[1][26:]
    params_setting["liveId"] = liveId
    # request stream danmakus (plaintext) from danmakus
    response = requests.get(api_link, params_setting)
    response_dic = json.loads(response.text)
    if response.status_code == 200:
        # success
        print(f'缺失xml文件：{liveName}\tdanmakus直播标题：{response_dic["data"]["data"]["live"]["title"]}')
        # process comments
        if basedic == {}:
            basedic = response_dic
        else:
            basedic["data"]["data"]["danmakus"].extend(response_dic["data"]["data"]["danmakus"])
    else:
        # print error status code
        print(f'缺失xml文件：{liveName}\t 出现错误：')
        print(response_dic)


with open("./data/"+liveName+".json","w") as f:
    json.dump(basedic["data"]["data"],f) 