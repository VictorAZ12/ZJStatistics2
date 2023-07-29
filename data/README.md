# 数据提取
将xml文件中的弹幕提取出来，转为统计数据，存储在SQLite3数据库中。
## XML格式分析 （cv6189156）
```
<d p="{time},{type},{size},{color},{timestamp},{pool},{uid_crc32},{row_id}"> {text} </d>
``` 
time:弹幕在视频里的时间
type:弹幕类型
size:字体大小
color:十进制RGB颜色
timestamp：unix弹幕时间戳
pool：弹幕池
uid_crc32：发弹幕者的UID crc32
## 方法
提取文件的日期、文件中所有弹幕，统计UID的出现次数。
对于每个UID若此前不存在于数据库中，则创建行并更新最早、最晚弹幕的日期。若此前存在则更新最晚弹幕的日期，并为这些UID的观看次数+1。
对观众的定义：至少发过1次弹幕。
# 数据格式
BIG INT uid 用户UID
TEXT first_seen 最早见到弹幕的时间，格式YYYY-MM-DD 00:00:00.000
TEXT last_seen 最后一次见到弹幕的时间，格式YYYY-MM-DD 00:00:00.000
INT seen_count 不重复直播场次的观看次数

# 数据获取
从奶粉录播站提供的百度网盘中直接下载xml文件。
若某场直播xml弹幕文件缺少用户UID，则将此场直播名字记录下来，并使用danmakus.com提供的api获取数据作为替代。
## 需从其他源获取的弹幕数据
根据extraction脚本的首次运行结果，奶粉站弹幕文件中存在问题、需要从其他源获取数据的直播场次名字已经记录在/data/to_be_downloaded.txt内。。
1. 获取这些直播场次的liveId
2. 读入output.txt
3. 从danmakus的api抓取这些直播场次的弹幕数据, 按照相同的逻辑对output进行维护更新
4. 输出

使用danmakus_download.py读取存储在to_be_downloaded.csv内的liveID并爬取弹幕数据，处理后存入新的output文件内
### 特殊处理说明
2021.03.24 珈乐 Disco 陪我练歌啦.xml 断流三次，按单次直播计算，使用danmakus_download extra.py下载合并后替换掉danmakus_download.py下载到的文件
2021.02.17 嘉然 和贝拉一起玩耍 双直播间推流，分别计算为一次直播
2021.08.14 七夕特别直播.xml [七夕直播为抖音限定](http://t.bilibili.com/558774905908449734)，无法计算
2021.10.16 抖音奇妙日.xml 抖音限定直播，无法计算
2022.05.20 非官方 · 伪 · 珈乐毕业回.xml 非官方直播 删除
2023.06.21 贝拉×山新 舞担贝拉，来认识新朋友啦！.xml 抖音限定直播，无法计算


