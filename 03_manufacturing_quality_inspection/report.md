# Brief Project Report: Visual Inspection for Manufacturing Quality Control

## 1. Problem
Manufacturing lines need to identify visible changes or defects consistently, reducing the need for purely manual inspection.

## 2. Objective
Compare a test image against a defect-free reference image using image alignment, grayscale conversion, blur, and thresholding to highlight changed regions.

## 3. Dataset
Use a defect-free reference image and sample images of the same product, including examples with visible defects. Public starting point: MVTec AD https://www.mvtec.com/company/research/datasets/mvtec-ad . This starter uses a paired reference/test-image approach.

## 4. Implementation
Resize images to a common size, compute absolute pixel difference, blur noise, threshold the difference image, find contours, and draw candidate regions.

## 5. Results and evaluation
Run the implementation on a documented test set. Record the number of images, detections, processing time, and (if ground-truth labels are available) precision, recall, F1-score, and IoU/mAP as appropriate. Attach output examples in `results/` and `screenshots/`. Do not invent values.

## 6. Limitations
Lighting, shadows, camera movement, and product alignment can look like defects. This simple baseline works best with fixed camera and consistent product positioning.

## 7. Conclusion
The project provides a baseline implementation and a reproducible starting point for experimentation. Future work could use a labelled dataset, a trained task-specific model, and a controlled evaluation protocol.
