from yolov4.tf import YOLOv4, YOLODataset, create_mAP_input_files


yolo = YOLOv4()
yolo.config.parse_names("data.names")
yolo.config.parse_cfg("yolov4-tiny.cfg")

yolo.make_model()
yolo.load_weights("./yolov4-tiny.weights", weights_type="yolo")

dataset = YOLODataset(
    config=yolo.config,
    dataset_list="./valid/valid.txt",
    image_path_prefix="./valid",
    training=False,
)

create_mAP_input_files(yolo, mAP_path="./mAP", dataset=dataset)