# Brief Project Report: Autonomous Robot Obstacle Detection and Avoidance

## 1. Problem
A mobile robot needs to identify likely obstacles in its forward camera view and give a simple warning or steering suggestion.

## 2. Objective
Create a basic vision demo that detects prominent edges/contours in a configurable region of interest and estimates whether the path ahead looks obstructed.

## 3. Dataset
Use recorded robot-camera frames or safe indoor images/video. Optional public dataset: KITTI Vision Benchmark Suite https://www.cvlibs.net/datasets/kitti/ . The included heuristic does not require training data.

## 4. Implementation
Apply a region-of-interest mask, grayscale conversion, Gaussian blur, Canny edge detection, and contour/edge-density analysis. Display a heuristic status; this is not a safety-certified navigation system.

## 5. Results and evaluation
Run the implementation on a documented test set. Record the number of images, detections, processing time, and (if ground-truth labels are available) precision, recall, F1-score, and IoU/mAP as appropriate. Attach output examples in `results/` and `screenshots/`. Do not invent values.

## 6. Limitations
Edges are not the same as obstacles. Texture, shadows, transparent objects, and lighting can cause errors. Do not use this demo to control a real robot without additional sensors and safety validation.

## 7. Conclusion
The project provides a baseline implementation and a reproducible starting point for experimentation. Future work could use a labelled dataset, a trained task-specific model, and a controlled evaluation protocol.
