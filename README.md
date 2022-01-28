# TFOD Benchmark for Few-Shot Object Detection (in progress)
TFOD is the first benchmark dataset for **T**ask-Focused **F**ew-Shot **O**bject **D**etection. We found that detection is not reliable outside of its initial training setting for many robot tasks. However, many researchers do not have a robot or even access to data to evaluate few-shot detection algorithms in a robotics setting. Notably, few-shot is exactly as it sounds, having to perform detection with very few annotated examples. Thus, we created the TFOD Benchmark in a challenging robot manipulation setting, which provides highly variable image characteristics for a consistent set of objects. We believe this evaluation will help guide innovation in our community toward increasingly reliable few-shot detection for robotics.

Contact: Brent Griffin (griffb at umich dot edu)

__Benchmark Example.__
![alt text](./figure/tfod_overview.jpg?raw=true "Benchmark Example from Robot")

## Using TFOD

__Run__ ``./demo/tfod_manual_data_demonstration.py`` to manually load TFOD data. <br />
[native Python]

__Run__ ``./demo/tfod_detectron2_data_demonstration.py`` to automatically load data to [detectron2](https://github.com/facebookresearch/detectron2). <br />
[native Python, has detectron2 dependency]

Here are the commands we used to set up a virtual environment for detectron2 and TFOD:
```
python3 -m venv ~/tfod
source ~/tfod/bin/activate
pip install --upgrade pip
pip install torch torchvision IPython git+https://github.com/facebookresearch/detectron2.git
```

## Benchmark

The TFOD Benchmark uses standard MS-COCO AP metrics and *k* task-focused annotation across 12 object classes.

| Method | *k* | AP | AP50 | AP75 | APs | APm | APl |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| [ClickBot](https://github.com/griffbr/tfod "arXiv Paper") | 1 | 13.6 | 19.5 | 18.1 | 0.0 | 33.7 | 23.2 |
| [ClickBot](https://github.com/griffbr/tfod "arXiv Paper") | 2 | 17.7 | 23.3 | 21.6 | 0.0 | 27.4 | 21.0 |
| [ClickBot](https://github.com/griffbr/tfod "arXiv Paper") | 4 | 33.7 | 45.0 | 39.8 | 0.5 | 52.0 | 43.4 |

Is your technique missing although the paper and code are public? Let us know and we'll add it.

## Using ClickBot Baseline on TFOD Benchmark

__Run__ ``./demo/tfod_clickbot_baseline_demonstration.py`` to replicate our ClickBot baseline results. <br />
[native Python, has detectron2 dependency]

__ClickBot Per-Object Benchmark Results.__
![alt text](./figure/clickbot_baseline.jpg?raw=true "ClickBot Per-Object Results")

## Publication
Please cite our [paper](https://github.com/griffbr/tfod "Task-Focused Few-Shot Object Detection for Robot Manipulation pdf") if you find it useful for your research.
```
@inproceedings{Gr22,
  author = {Griffin, Brent},
  booktitle={arXiv},
  title = {Task-Focused Few-Shot Object Detection for Robot Manipulation},
  year = {2022}
}
```

__TFOD Experiment Videos:__ https://youtu.be/r5MWf7osI4w

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/r5MWf7osI4w/0.jpg)](https://youtu.be/r5MWf7osI4w)

## Use

This code is available for non-commercial research purposes only.