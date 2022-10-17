# TFOD Benchmark for Few-Shot Object Detection
TFOD is the first benchmark dataset for **T**ask-Focused **F**ew-Shot **O**bject **D**etection. Why? We find that detection is not reliable outside of its initial training setting for many robot tasks. However, many researchers do not have a robot or even access to data to evaluate few-shot detection algorithms in a robotics setting. Notably, few-shot is exactly as it sounds, having to perform detection with very few annotated examples. Thus, we created the TFOD Benchmark in a challenging robot manipulation setting, which provides highly variable image characteristics for a consistent set of objects. This evaluation will help guide innovation toward increasingly reliable few-shot detection for robotics.

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
pip install torch torchvision IPython 
pip install git+https://github.com/facebookresearch/detectron2.git
```

## Benchmark

The TFOD Benchmark uses MS-COCO AP metrics and *k* few-shot examples across 12 object classes.

| Method | *k* | AP | AP50 | AP75 | APs | APm | APl |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
| [ClickBot](https://arxiv.org/pdf/2201.12437 "Paper") | 1 | 14.1 | 19.9 | 17.2 | 0.0 | 32.9 | 22.8 |
| [ClickBot](https://arxiv.org/pdf/2201.12437 "Paper") | 2 | 18.3 | 24.3 | 22.5 | 0.0 | 32.1 | 27.7 |
| [ClickBot](https://arxiv.org/pdf/2201.12437 "Paper") | 4 | 35.0 | 46.0 | 42.0 | 1.7 | 57.4 | 39.0 |

Is your technique missing although the paper and code are public? Let us know and we'll add it. We average our baseline TFOD results across ten consecutive trials. Use this approach to report results if your method is nondeterministic.

## Using ClickBot Baseline on TFOD Benchmark

__Run__ ``./demo/tfod_clickbot_baseline_demonstration.py`` to replicate our ClickBot baseline results. <br />
[native Python, has detectron2 dependency]

__ClickBot Per-Object Benchmark Results.__
![alt text](./figure/clickbot_baseline.jpg?raw=true "ClickBot Per-Object Results")

## Publication
 Please cite our [paper](https://arxiv.org/pdf/2201.12437 "Task-Focused Few-Shot Object Detection for Robot Manipulation pdf") if you find it useful for your research.
 ```
 @inproceedings{Gr23,
   author = {Griffin, Brent},
   title = {Mobile Robot Manipulation using Pure Object Detection},
   booktitle = {IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
   year = {2023}
 }
 ```

## TFOD Experiment Videos

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Bby4Unw7HrI/0.jpg)](https://youtu.be/Bby4Unw7HrI)

https://youtu.be/Bby4Unw7HrI

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/giiSYDwZM4c/0.jpg)](https://youtu.be/giiSYDwZM4c)

https://youtu.be/giiSYDwZM4c
 
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/OhQfMPuZQlg/0.jpg)](https://youtu.be/OhQfMPuZQlg)
 
https://youtu.be/OhQfMPuZQlg

## Use

This code is available for non-commercial research purposes only.
