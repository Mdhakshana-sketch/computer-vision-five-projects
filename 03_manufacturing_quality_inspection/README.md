# Visual Inspection for Manufacturing Quality Control

## Problem statement
Manufacturing lines need to identify visible changes or defects consistently, reducing the need for purely manual inspection.

## Objective
Compare a test image against a defect-free reference image using image alignment, grayscale conversion, blur, and thresholding to highlight changed regions.

## Dataset
Use a defect-free reference image and sample images of the same product, including examples with visible defects. Public starting point: MVTec AD https://www.mvtec.com/company/research/datasets/mvtec-ad . This starter uses a paired reference/test-image approach.

## Methodology
Resize images to a common size, compute absolute pixel difference, blur noise, threshold the difference image, find contours, and draw candidate regions.

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
python 03_manufacturing_quality_inspection/main.py --input sample.jpg
```
For the quality inspection project, also pass a defect-free reference:
```bash
python 03_manufacturing_quality_inspection/main.py --input test_product.jpg --reference reference_product.jpg
```
For webcam projects, omit `--input` to use camera index 0 where supported. Press `q` to quit a webcam window.

## Results
The script writes annotated outputs and a CSV/text summary into this project's `results/` folder. Run the script with your own images and include genuine screenshots in `screenshots/`. No benchmark score is pre-filled because results depend on the images and machine.

## Performance evaluation
Reports candidate region count and changed-pixel ratio. For a rigorous evaluation, label defect regions and calculate precision, recall, and IoU on a test set.

## Conclusion
This project demonstrates a practical computer-vision pipeline for the stated task. Its usefulness depends on data quality and the limitations described below.

## Limitations and challenges
Lighting, shadows, camera movement, and product alignment can look like defects. This simple baseline works best with fixed camera and consistent product positioning.
