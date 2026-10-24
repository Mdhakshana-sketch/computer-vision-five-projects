# Brief Project Report: Pedestrian Detection for Autonomous Robots

## 1. Problem
Autonomous robots need to detect people in camera images so they can respond safely around pedestrians.

## 2. Objective
Detect pedestrians in an image or webcam stream and draw bounding boxes using OpenCV's HOG person detector.

## 3. Dataset
For testing, use your own street/walkway images or the INRIA Person Dataset: https://www.cvg.unimelb.edu.au/datasets/person/ . This starter uses OpenCV's pretrained HOG detector and does not require training data.

## 4. Implementation
Load an image or webcam frame, convert it to the expected format, run HOGDescriptor.detectMultiScale, then draw boxes and save/display the output.

## 5. Results and evaluation
Run the implementation on a documented test set. Record the number of images, detections, processing time, and (if ground-truth labels are available) precision, recall, F1-score, and IoU/mAP as appropriate. Attach output examples in `results/` and `screenshots/`. Do not invent values.

## 6. Limitations
HOG can miss small, distant, occluded, or unusual-view pedestrians and may produce false positives. It is a classical baseline, not a modern deep detector.

## 7. Conclusion
The project provides a baseline implementation and a reproducible starting point for experimentation. Future work could use a labelled dataset, a trained task-specific model, and a controlled evaluation protocol.
