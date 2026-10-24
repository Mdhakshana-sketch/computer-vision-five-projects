# Autonomous Robot Obstacle Detection and Avoidance

## Problem statement
A mobile robot needs to identify likely obstacles in its forward camera view and give a simple warning or steering suggestion.

## Objective
Create a basic vision demo that detects prominent edges/contours in a configurable region of interest and estimates whether the path ahead looks obstructed.

## Dataset
Use recorded robot-camera frames or safe indoor images/video. Optional public dataset: KITTI Vision Benchmark Suite https://www.cvlibs.net/datasets/kitti/ . The included heuristic does not require training data.

## Methodology
Apply a region-of-interest mask, grayscale conversion, Gaussian blur, Canny edge detection, and contour/edge-density analysis. Display a heuristic status; this is not a safety-certified navigation system.

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
python 04_robot_obstacle_detection/main.py --input sample.jpg
```
For the quality inspection project, also pass a defect-free reference:
```bash
python 04_robot_obstacle_detection/main.py --input test_product.jpg --reference reference_product.jpg
```
For webcam projects, omit `--input` to use camera index 0 where supported. Press `q` to quit a webcam window.

## Results
The script writes annotated outputs and a CSV/text summary into this project's `results/` folder. Run the script with your own images and include genuine screenshots in `screenshots/`. No benchmark score is pre-filled because results depend on the images and machine.

## Performance evaluation
Reports edge density in the forward region and the heuristic status per frame. Validate with labelled clear-path/obstacle clips to estimate classification accuracy.

## Conclusion
This project demonstrates a practical computer-vision pipeline for the stated task. Its usefulness depends on data quality and the limitations described below.

## Limitations and challenges
Edges are not the same as obstacles. Texture, shadows, transparent objects, and lighting can cause errors. Do not use this demo to control a real robot without additional sensors and safety validation.
