import os
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultTrainer

def clickbot_detectron2(fewshot_set, categories):
	""" ClickBot Few-Shot Object Detection Model and TFOD Benchmark Baseline.
	"""

	# Configure ClickBot few-shot baseline using detectron2.
	cfg = get_cfg()
	base_model = "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
	cfg.merge_from_file(model_zoo.get_config_file(base_model))
	cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(categories)
	cfg.DATASETS.TRAIN = (fewshot_set,)
	cfg.DATASETS.TEST = ()
	cfg.DATALOADER.NUM_WORKERS = 4
	cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(base_model)
	cfg.SOLVER.IMS_PER_BATCH = 2
	cfg.SOLVER.BASE_LR = 0.00025
	cfg.SOLVER.MAX_ITER = 1000
	cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 128
	cfg.OUTPUT_DIR = os.path.join(os.getcwd(), "output")
	os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)
	cfg.DATALOADER.FILTER_EMPTY_ANNOTATIONS = False

	print("\nUpdating ClickBot using few-shot examples.\n")
	clickbot_update_vision = DefaultTrainer(cfg)
	clickbot_update_vision.resume_or_load(resume=False)
	try:
		clickbot_update_vision.train()
	except: 
		clickbot_update_vision.MODEL.DEVICE="cuda:0"
		clickbot_update_vision = DefaultTrainer(cfg)
		clickbot_update_vision.resume_or_load(resume=False)
		clickbot_update_vision.train()
			
	return clickbot_update_vision.model, cfg