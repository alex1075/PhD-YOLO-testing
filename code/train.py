from tensorflow.keras import callbacks

from yolov4.tf import YOLOv4, YOLODataset, SaveWeightsCallback

yolo = YOLOv4()

yolo.config.parse_names("train/classes.txt")
yolo.config.parse_cfg("yolov4-tiny-newcord.cfg")

yolo.make_model()
yolo.load_weights(
    "./yolov4x-mish.weights",
    weights_type="yolo",
)
yolo.summary(summary_type="yolo")

for i in range(29):
    yolo.model.get_layer(index=i).trainable = False

yolo.summary()

train_dataset = YOLODataset(
    config=yolo.config,
    dataset_list="/Volumes/PhD/PhD-YOLO/train/annotations.txt",
    image_path_prefix="/Volumes/PhD/PhD-YOLO/train/",
    training=True,
)

val_dataset = YOLODataset(
    config=yolo.config,
    dataset_list="./valid.txt",
    image_path_prefix="/data/valid",
    training=False,
)

yolo.compile()

_callbacks = [
    callbacks.TerminateOnNaN(),
    callbacks.TensorBoard(
        log_dir="./logs",
        update_freq=200,
        histogram_freq=1,
    ),
    SaveWeightsCallback(
        yolo=yolo,
        dir_path="./trained",
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