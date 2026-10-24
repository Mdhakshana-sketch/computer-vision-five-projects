# Intelligent Warehouse Object Detection

## Problem statement
Warehouse robots need to identify common objects in their environment to support navigation and inventory workflows.

## Objective
Detect common COCO classes such as person, bottle, chair, backpack, and suitcase with a pretrained YOLO model.

## Dataset
The pretrained model is trained on COCO: https://cocodataset.org/ . For a custom warehouse study, collect/label representative images and train or fine-tune a model.

## Methodology
Use Ultralytics YOLOv8n pretrained weights, run inference on an image or webcam, and save annotated detections with class labels and confidence scores.

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
python 02_warehouse_object_detection/main.py --input sample.jpg
```
For the quality inspection project, also pass a defect-free reference:
```bash
python 02_warehouse_object_detection/main.py --input test_product.jpg --reference reference_product.jpg
```
For webcam projects, omit `--input` to use camera index 0 where supported. Press `q` to quit a webcam window.

## Results
The script writes annotated outputs and a CSV/text summary into this project's `results/` folder. Run the script with your own images and include genuine screenshots in `screenshots/`. No benchmark score is pre-filled because results depend on the images and machine.

## Performance evaluation
The script records detection count and inference time. Proper mAP, precision, and recall require a labelled evaluation set; do not treat sample inference as a benchmark.

## Conclusion
This project demonstrates a practical computer-vision pipeline for the stated task. Its usefulness depends on data quality and the limitations described below.

## Limitations and challenges
COCO does not include every warehouse-specific object or SKU. Performance depends on lighting, camera angle, occlusion, and similarity between objects.
