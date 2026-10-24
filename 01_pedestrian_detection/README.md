# Pedestrian Detection for Autonomous Robots

## Problem statement
Autonomous robots need to detect people in camera images so they can respond safely around pedestrians.

## Objective
Detect pedestrians in an image or webcam stream and draw bounding boxes using OpenCV's HOG person detector.

## Dataset
For testing, use your own street/walkway images or the INRIA Person Dataset: https://www.cvg.unimelb.edu.au/datasets/person/ . This starter uses OpenCV's pretrained HOG detector and does not require training data.

## Methodology
Load an image or webcam frame, convert it to the expected format, run HOGDescriptor.detectMultiScale, then draw boxes and save/display the output.

## Tools and libraries
- Python 3.10 or newer
- OpenCV
- NumPy
- Ultralytics (warehouse project)
- pytesseract (optional OCR for license plates)

## How to run
From the repository root, install dependencies:
```bash
pip install -r requirements.txt
```
Then run the command shown below, replacing the example image path with a real image on your computer:
```bash
python 01_pedestrian_detection/main.py --input sample.jpg
```
For the quality inspection project, also pass a defect-free reference:
```bash
python 01_pedestrian_detection/main.py --input test_product.jpg --reference reference_product.jpg
```
For webcam projects, omit `--input` to use camera index 0 where supported. Press `q` to quit a webcam window.

## Results
The script writes annotated outputs and a CSV/text summary into this project's `results/` folder. Run the script with your own images and include genuine screenshots in `screenshots/`. No benchmark score is pre-filled because results depend on the images and machine.

## Performance evaluation
This baseline reports the number of detections and processing time per image. For formal precision/recall/mAP, label a held-out test set and compare detections with ground-truth boxes.

## Conclusion
This project demonstrates a practical computer-vision pipeline for the stated task. Its usefulness depends on data quality and the limitations described below.

## Limitations and challenges
HOG can miss small, distant, occluded, or unusual-view pedestrians and may produce false positives. It is a classical baseline, not a modern deep detector.
