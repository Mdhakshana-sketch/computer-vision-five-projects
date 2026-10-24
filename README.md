# Five Computer Vision Projects

A beginner-friendly Python/OpenCV repository containing five separate computer vision demonstrations.

## Projects
1. [Pedestrian Detection](01_pedestrian_detection/README.md)
2. [Intelligent Warehouse Object Detection](02_warehouse_object_detection/README.md)
3. [Manufacturing Quality Inspection](03_manufacturing_quality_inspection/README.md)
4. [Robot Obstacle Detection and Avoidance](04_robot_obstacle_detection/README.md)
5. [License Plate Detection and Recognition](05_license_plate_detection/README.md)

## Setup
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Run each project's `main.py` from the repository root, for example:
```bash
python 01_pedestrian_detection/main.py --input path/to/image.jpg
```
See each project's README for its exact commands. YOLO weights download automatically the first time the warehouse project runs; an internet connection is needed.

## Important
These are educational baselines. Run them yourself, keep your actual output images in each `results/` folder, and update the report with your observations before submission. Do not claim performance metrics you have not measured. The scripts save basic runtime/detection statistics; rigorous accuracy evaluation requires a labelled test set.
