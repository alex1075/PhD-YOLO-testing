from tensorflow.keras import callbacks

from yolov4.tf import YOLOv4, YOLODataset, SaveWeightsCallback

yolo = YOLOv4()

yolo.config.parse_names("data.names")
yolo.config.parse_cfg("yolov4-tiny.cfg")

yolo.make_model()
yolo.load_weights(
    "./yolov4-tiny.conv.29",
    weights_type="yolo",
)
yolo.summary(summary_type="yolo")

for i in range(29):
    yolo.model.get_layer(index=i).trainable = False

yolo.summary()

train_dataset = YOLODataset(
    config=yolo.config,
    dataset_list="/data/train/train.txt",
    image_path_prefix="/data/train/",
    training=True,
)

val_dataset = YOLODataset(
    config=yolo.config,
    dataset_list="/data/valid/valid.txt",
    image_path_prefix="/data/valid",
    training=False,
)

yolo.compile()

_callbacks = [
    callbacks.TerminateOnNaN(),
    callbacks.TensorBoard(
        log_dir="/data/logs",
        update_freq=200,
        histogram_freq=1,
    ),
    SaveWeightsCallback(
        yolo=yolo,
        dir_path="/data/trained",
        weights_type="yolo",
        step_per_save=2000,
    ),
]

yolo.fit(
    train_dataset,
    callbacks=_callbacks,
    validation_data=val_dataset,
    verbose=3,  # 3: print step info
)