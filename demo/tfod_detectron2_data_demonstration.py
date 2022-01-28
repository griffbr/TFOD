import os, IPython, _pickle as pickle, sys
from detectron2.data import DatasetCatalog, MetadataCatalog

# Few-shot object detection configuration.
k = 1 # 1, 2, or 4. Number of few-shot annotated examples per object.
tfod_directory = "./"

sys.path.insert(0, tfod_directory)
import tfod

# Load few-shot annotation data using detectron2.
fewshot_data, categories = tfod.load_tfod_data(tfod_directory, n_shots=k)
DatasetCatalog.register("fewshot", lambda d="train": fewshot_data)
MetadataCatalog.get("fewshot").set(thing_classes=categories)

print("Use detectron2 to interpret fewshot_data for your model here.")
IPython.embed()

# Load tfod benchmark data using detectron2.
evaluation_data, categories = tfod.load_tfod_data(tfod_directory, benchmark=True)
DatasetCatalog.register("tfod_benchmark", lambda d="val": evaluation_data)
MetadataCatalog.get("tfod_benchmark").set(thing_classes=categories)

print("\nUse detectron2 to evaluate your model on tfod benchmark.")
print("Warning: Remainder of this script will not work without model added!\n")
IPython.embed()

# Evaluate few-shot detection model using detectron2 (if loaded with cfg).
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader
evaluator = COCOEvaluator("tfod_benchmark", cfg, False, output_dir="./output/")
val_loader = build_detection_test_loader(cfg, "tfod_benchmark")
inference_on_dataset(model, val_loader, evaluator)