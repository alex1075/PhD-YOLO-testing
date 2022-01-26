import numpy
import os

file = open("/Volumes/PhD/PhD-YOLO/train/annotations.txt", "r")
filetoo = open("/Volumes/PhD/PhD-YOLO/train/train.txt", "w")
pixel = 416

lines = file.readlines()
for line in lines: 
    # print(line)
    listy = []
    splice = line.split(" ")
    name = splice[0]
    listy.append(name)
    for bbox in splice[1:]:
        # print(bbox)
        topl = bbox.split(",")[0:2]
        botmr = bbox.split(",")[2:4]
        class_name = bbox.split(",")[4]
        # print(topl,botmr)
        width = int(botmr[0]) - int(topl[0])
        height = int(botmr[1]) - int(topl[1])
        centerx = int(topl[0]) + int(width/2)
        centery = int(topl[1]) + int(height/2)
        # print(centerx,centery)
        # print(width,height)
        neoline = " " + str(centerx/pixel) + "," + str(centery/pixel) + "," + str(width/pixel) + "," + str(height/pixel) + "," + class_name
        listy.append(neoline)
    print(listy)
    filetoo.write("".join(listy))

filetoo.close()
file.close()

