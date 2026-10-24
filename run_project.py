import argparse, subprocess, sys
from pathlib import Path

PROJECTS = {
    "pedestrian": "01_pedestrian_detection/main.py",
    "warehouse": "02_warehouse_object_detection/main.py",
    "quality": "03_manufacturing_quality_inspection/main.py",
    "obstacle": "04_robot_obstacle_detection/main.py",
    "plate": "05_license_plate_detection/main.py",
}
parser = argparse.ArgumentParser(description="Run one of the five CV projects.")
parser.add_argument("project", choices=PROJECTS)
parser.add_argument("--input", help="Input image/video path; omit for webcam where supported.")
parser.add_argument("--reference", help="Defect-free reference image (quality project).")
args = parser.parse_args()
cmd = [sys.executable, PROJECTS[args.project]]
if args.input:
    cmd += ["--input", args.input]
if args.reference:
    cmd += ["--reference", args.reference]
raise SystemExit(subprocess.call(cmd))
