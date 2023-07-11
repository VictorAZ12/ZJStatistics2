import re
files = []
xmls = []
with open("./anni1_xml.html", "r", encoding="UTF-8") as f:
    files.append(f.read())
with open("./anni2_xml.html", "r", encoding="UTF-8") as f:
    files.append(f.read())
# extract xmls and output
for file in files:
    xmls.extend(re.findall("list-item hope-stack hope-c-dhzjXW hope-c-PJLV hope-c-PJLV-ikoJJtX-css\" href=\"https:.*?\.xml",  file))
for i, xml in enumerate(xmls):
    xmls[i] = re.findall("https:.*?\.xml", xml)[0]
with open("xmls.txt","w") as f:
    f.write("\n".join(xmls))