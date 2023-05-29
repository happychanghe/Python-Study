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

outputfile = open("testingLearning/testMPLsleep/outputfile.txt", 'w')
#  <Record type="HKCategoryTypeIdentifierSleepAnalysis" 
# sourceName="윤창희의 Apple Watch" sourceVersion="9.3.1" creationDate="2023-04-25 08:09:26 +0900" 
# startDate="2023-04-25 02:00:21 +0900" endDate="2023-04-25 02:08:21 +0900" value="HKCategoryValueSleepAnalysisAsleepCore">
data_format=["creationDate", "startDate", "endDate", "value"]
datas = []
with open("testingLearning/testMPLsleep/rawdata.txt", 'r') as ych_health_file:

    lines = ych_health_file.readlines()
    for aline in lines:
        if ("HKCategoryTypeIdentifierSleepAnalysis" in aline) and ("Apple Watch" in aline):
            # aline = aline.strip('<>')
            # outputfile.write(aline)
            d=convert_tag2dict(aline, data_format)
            datas.append(d)
            outputfile.write(str(d)+'\n')

outputfile.close()