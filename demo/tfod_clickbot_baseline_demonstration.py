import os, IPython, _pickle as pickle, sys
from detectron2.data import DatasetCatalog, MetadataCatalog

# Few-shot object detection configuration.
k = 4 # 1, 2, or 4. Number of few-shot annotated examples per object.
tfod_directory = "./"

sys.path.insert(0, tfod_directory)
import tfod

# Load few-shot annotation data using detectron2.
fewshot_data, categories = tfod.load_tfod_data(tfod_directory, n_shots=k)
DatasetCatalog.register("fewshot", lambda d="train": fewshot_data)
MetadataCatalog.get("fewshot").set(thing_classes=categories)

# Update ClickBot's detection model using few-shot annotation.
clickbot, cfg = tfod.clickbot_detectron2("fewshot", categories)

# Load tfod benchmark data using detectron2.
evaluation_data, categories = tfod.load_tfod_data(tfod_directory, benchmark=True)
DatasetCatalog.register("tfod_benchmark", lambda d="val": evaluation_data)
MetadataCatalog.get("tfod_benchmark").set(thing_classes=categories)

# Evaluate few-shot detection model using detectron2 (if loaded with cfg).
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
evaluator = COCOEvaluator("tfod_benchmark", cfg, False, output_dir="./output/")
val_loader = build_detection_test_loader(cfg, "tfod_benchmark")
inference_on_dataset(clickbot, val_loader, evaluator)