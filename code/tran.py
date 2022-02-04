from asyncore import write
import os

file = open("/data/train/train.txt", "w")
dir = os.listdir("/data/train/")

for image in dir:
    print(image)
    file.write(image)
    
print(file)


file.close()
