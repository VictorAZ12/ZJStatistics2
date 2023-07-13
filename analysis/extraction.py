import re
import os
from datetime import datetime
import json
# path to the directories in which the xml files, log file, and output file are stored
file_path = "./data/"
output_path = "./analysis/"
# get all file names ending with '.xml'
filenames = [file for file in os.listdir(file_path) if file.endswith(".xml")]
# initialise audience data storage and log file
audience = {}
with open(output_path + "log.txt","w", encoding="UTF-8") as f:
    f.write("")
for filename in filenames:
    # open an xml file and extract comments
    with open(file_path + filename, "r", encoding="UTF-8") as f:
        file_content = f.read()
    comments = re.findall("<d p=.*?>", file_content)

    # extract date from filename
    stream_date = re.findall("[0-9]{4}\.[0-9]{2}\.[0-9]{2}", filename)[0]
    stream_date = datetime.strptime(stream_date, "%Y.%m.%d")
    # extract UID from comments, then add count, needs to be a valid UID
    uids = {}
    for comment in comments:
        uid = re.findall("p=\".*?\"", comment)[0].split(",")[-2]
        if re.fullmatch("[0-9]+", uid) is None:
            # report if non-number UID is found
            with open(output_path + "log.txt","a", encoding="UTF-8") as f:
                f.write("File " + filename + " contains non-number UIDs.\n")
            break
        else:
            if uid in uids:
                uids[uid]["comment_count"] += 1
            else:
                uids[uid] = {
                    "comment_count" : 1,
                    "date" : stream_date
                }
    if len(uids) < 10:
        with open(output_path + "log.txt","a", encoding="UTF-8") as f:
            f.write("File " + filename + " contains less than 10 UIDs, skipped.\n")
        continue
    # add extracted information into database，then print log.
    for uid in uids:
        if uid in audience:
            audience[uid]["stream_count"] += 1
            audience[uid]["comment_count"] += uids[uid]["comment_count"]
            if stream_date > audience[uid]["last_seen"]:
                 audience[uid]["last_seen"] = stream_date
        else:
            audience[uid]={
                "first_seen": stream_date,
                "last_seen": stream_date,
                "stream_count": 1,
                "comment_count": uids[uid]["comment_count"]
            }
    with open(output_path + "log.txt","a", encoding="UTF-8") as f:
            f.write(f"File {filename}: {len(uids)} viewers, {len(comments)} comments\n")

# convert datetime to text
for uid in audience:
    audience[uid]["first_seen"] = audience[uid]["first_seen"].strftime("%Y.%m.%d")
    audience[uid]["last_seen"] = audience[uid]["last_seen"].strftime("%Y.%m.%d")
# output result
print(len(audience), "audience discovered in total.")
with open(output_path + "output.txt", "w") as f:
    f.write(json.dumps(audience, indent=4))

