# Brief Project Report: Vehicle License Plate Detection and Recognition

## 1. Problem
Parking and traffic applications may need to locate a license plate in an image and read its characters.

## 2. Objective
Detect likely plate-shaped regions with OpenCV and optionally recognize cropped plate text with Tesseract OCR.

## 3. Dataset
Use images you have permission to process. Public dataset option: UFPR-ALPR https://web.inf.ufpr.br/vri/databases/ufpr-alpr/ . The included contour-based method is a baseline and is not trained on this dataset.

## 4. Implementation
Preprocess image, detect edges, find contours, filter candidates by rectangular aspect ratio, crop the best candidate, and optionally run pytesseract OCR if Tesseract is installed.

## 5. Results and evaluation
Run the implementation on a documented test set. Record the number of images, detections, processing time, and (if ground-truth labels are available) precision, recall, F1-score, and IoU/mAP as appropriate. Attach output examples in `results/` and `screenshots/`. Do not invent values.

## 6. Limitations
Plate appearance varies by country, font, angle, blur, weather, and illumination. Contour-based detection can select other rectangular objects; OCR quality depends on crop quality and Tesseract language/configuration.

## 7. Conclusion
The project provides a baseline implementation and a reproducible starting point for experimentation. Future work could use a labelled dataset, a trained task-specific model, and a controlled evaluation protocol.
