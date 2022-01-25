#got through files in dir and convert to yolo format
#!/usr/bin/env python3
# Path: code/new.py
# Compare this snippet from code/voc2yolo.py:
#
# def getImagesInDir(dir_path):
#     image_list = []
#     for filename in glob.glob(dir_path + '/*.jpg'):
#         image_list.append(filename)
#
#     return image_list
