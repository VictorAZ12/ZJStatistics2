import re
files = []
with open("./anni1_xml.html", "r", encoding="UTF-8") as f:
    anni1= f.read()
with open("./anni2_xml.html", "r", encoding="UTF-8") as f:
    anni2= f.read()
# extract xmls and output
header = "https://d.asoul.net.cn/0:/ASOUL-REC-%E4%B8%80%E5%91%A8%E5%B9%B4/XML%E5%BC%B9%E5%B9%95%E6%96%87%E4%BB%B6/"
xmls= re.findall("list-item hope-stack hope-c-dhzjXW hope-c-PJLV hope-c-PJLV-ikoJJtX-css\" href=\"https:.*?\.xml",  anni1)
for i, xml in enumerate(xmls):
    xmls[i] = header + re.findall("https:.*?\.xml", xml)[0].split("/")[-1]
with open("xmls_anni1.txt","w") as f:
    f.write("\n".join(xmls))

xmls= re.findall("list-item hope-stack hope-c-dhzjXW hope-c-PJLV hope-c-PJLV-ikoJJtX-css\" href=\"https:.*?\.xml",  anni2)
for i, xml in enumerate(xmls):
    xmls[i] = header + re.findall("https:.*?\.xml", xml)[0]
with open("xmls_anni2.txt","w") as f:
    f.write("\n".join(xmls))

    