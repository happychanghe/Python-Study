import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def convert_tag2dict(tag, dictkeys):
    dd = {}
    for key in dictkeys:
        if key in tag:
            lowestindex = tag.find(key)
            firstquote = tag.find('\"', lowestindex)
            secondquote = tag.find('\"', firstquote+1)
            dd[key]=tag[firstquote+1:secondquote]
        else:
            dd[key]=None
        pass
    return dd


# <Record type="HKQuantityTypeIdentifierHeartRateVariabilitySDNN" 
# sourceName="윤창희의 Apple Watch" sourceVersion="6.3" 
# device="&lt;&lt;HKDevice: 0x282dbd860&gt;, name:Apple Watch, 
# manufacturer:Apple Inc., model:Watch, hardware:Watch2,4, software:6.3&gt;" 
# unit="ms" creationDate="2022-12-04 22:42:13 +0900" 
# startDate="2022-12-04 22:41:02 +0900" endDate="2022-12-04 22:42:13 +0900" 
# value="131.493">
dataformat=["creationDate", "value"]
mydata=[]

path = "data/heartdata.txt"
with open(path, "r") as heartinfo:
    lines = heartinfo.readlines()
    for aline in lines:
        if "HKQuantityTypeIdentifierHeartRateVariabilitySDNN" in aline:
            d=convert_tag2dict(aline, dataformat)
            #print(d)
            date = d["creationDate"][:-6].replace(' ', 'T')
            #print(date)
            mydata.append([np.datetime64(date), float(d["value"])])

npmydata=np.array(mydata)
npmydata=npmydata.transpose()
#print(npmydata)
fig, ax = plt.subplots(2,1)
ax[0].plot(npmydata[0], npmydata[1], 'ro')
# print(npmydata[0])
# print(npmydata[1])
ax[0].set_xlabel("time")
ax[0].set_ylabel("heart beat rate (bpm)")
ax[0].set_title("my heart beat rate over time")
ax[0].set_xbound(np.datetime64('2022-12'), np.datetime64("2023-06"))

ax[1].plot(npmydata[0], npmydata[1])
ax[1].set_xbound(np.datetime64('2022-12'), np.datetime64("2023-06"))

plt.show()