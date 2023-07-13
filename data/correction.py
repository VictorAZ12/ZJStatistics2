import re
# extract titles of streams that have invalid danmaku xml files

with open("./data/log.txt", "r", encoding="UTF-8") as f:
    lines = f.readlines()
stream_titles = []
for line in lines:
    if line[0] == "!":
        stream_titles.append(re.findall("[0-9]{4}\.[0-9]{2}\.[0-9]{2}.*xml", line)[0])
stream_titles = sorted(list(set(stream_titles)))

with open ("./data/to_be_downloaded.txt","w", encoding="UTF-8") as f:
    f.write("\n".join(stream_titles))