import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

retrieveTags = [
    "TrainStatus",
    "TrainLatitude",
    "TrainLongitude",
    "TrainCode",
    "TrainDate",
    "PublicMessage",
    "Direction"
]

with open("lab2_train_full.csv", mode="w", newline="") as train_file:
    train_writer = csv.writer(train_file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    train_writer.writerow(retrieveTags)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = []

        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)

            if datanode is not None and datanode.firstChild is not None:
                dataList.append(datanode.firstChild.nodeValue.strip())
            else:
                dataList.append("")

        train_writer.writerow(dataList)