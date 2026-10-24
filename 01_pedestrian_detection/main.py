import argparse, time, csv
from pathlib import Path
import cv2

OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)

def process(frame, hog):
    start = time.perf_counter()
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)
    for (x, y, w, h), weight in zip(boxes, weights):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"person {float(weight):.2f}", (x, max(20, y-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    elapsed = (time.perf_counter()-start)*1000
    return frame, len(boxes), elapsed

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="Image path; omit to use webcam")
    args = ap.parse_args()
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    if args.input:
        frame = cv2.imread(args.input)
        if frame is None: raise SystemExit(f"Cannot read image: {args.input}")
        out, count, ms = process(frame, hog)
        target = OUT / "pedestrian_output.jpg"
        cv2.imwrite(str(target), out)
        with open(OUT/"evaluation.csv", "w", newline="") as f:
            w=csv.writer(f); w.writerow(["input","detections","processing_ms"]); w.writerow([args.input,count,round(ms,2)])
        print(f"Detections: {count}; processing: {ms:.1f} ms; saved: {target}")
        cv2.imshow("Pedestrian detection", out); cv2.waitKey(0); cv2.destroyAllWindows()
    else:
        cap=cv2.VideoCapture(0)
        if not cap.isOpened(): raise SystemExit("Cannot open webcam. Pass --input image.jpg.")
        while True:
            ok, frame=cap.read()
            if not ok: break
            out,count,ms=process(frame,hog)
            cv2.putText(out,f"People: {count} | {ms:.0f} ms",(10,30),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,255,255),2)
            cv2.imshow("Pedestrian detection - press q to quit",out)
            if cv2.waitKey(1)&0xFF==ord("q"): break
        cap.release(); cv2.destroyAllWindows()
if __name__=="__main__": main()
