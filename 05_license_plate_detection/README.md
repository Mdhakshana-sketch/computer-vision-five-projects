# Vehicle License Plate Detection and Recognition

## Problem statement
Parking and traffic applications may need to locate a license plate in an image and read its characters.

## Objective
Detect likely plate-shaped regions with OpenCV and optionally recognize cropped plate text with Tesseract OCR.

## Dataset
Use images you have permission to process. Public dataset option: UFPR-ALPR https://web.inf.ufpr.br/vri/databases/ufpr-alpr/ . The included contour-based method is a baseline and is not trained on this dataset.

## Methodology
Preprocess image, detect edges, find contours, filter candidates by rectangular aspect ratio, crop the best candidate, and optionally run pytesseract OCR if Tesseract is installed.

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
python 05_license_plate_detection/main.py --input sample.jpg
```
For the quality inspection project, also pass a defect-free reference:
```bash
python 05_license_plate_detection/main.py --input test_product.jpg --reference reference_product.jpg
```
For webcam projects, omit `--input` to use camera index 0 where supported. Press `q` to quit a webcam window.

## Results
The script writes annotated outputs and a CSV/text summary into this project's `results/` folder. Run the script with your own images and include genuine screenshots in `screenshots/`. No benchmark score is pre-filled because results depend on the images and machine.

## Performance evaluation
Reports whether a plate candidate was found and OCR text when available. For formal evaluation, use labelled plate boxes and transcripts to compute detection IoU/recall and character-level recognition accuracy.

## Conclusion
This project demonstrates a practical computer-vision pipeline for the stated task. Its usefulness depends on data quality and the limitations described below.

## Limitations and challenges
Plate appearance varies by country, font, angle, blur, weather, and illumination. Contour-based detection can select other rectangular objects; OCR quality depends on crop quality and Tesseract language/configuration.
