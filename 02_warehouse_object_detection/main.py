import argparse, time, csv
from pathlib import Path
import cv2
from ultralytics import YOLO

OUT=Path(__file__).parent/"results"; OUT.mkdir(exist_ok=True)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", help="Image path; omit to use webcam")
    ap.add_argument("--model", default="yolov8n.pt", help="YOLO model/weights path")
    args=ap.parse_args()
    model=YOLO(args.model)  # downloads pretrained COCO weights on first run if needed
    if args.input:
        frame=cv2.imread(args.input)
        if frame is None: raise SystemExit(f"Cannot read image: {args.input}")
        t=time.perf_counter(); result=model.predict(frame, verbose=False)[0]; ms=(time.perf_counter()-t)*1000
        annotated=result.plot()
        target=OUT/"warehouse_output.jpg"; cv2.imwrite(str(target),annotated)
        rows=[]
        for b in result.boxes:
            cls=int(b.cls[0]); conf=float(b.conf[0]); xyxy=[round(float(v),1) for v in b.xyxy[0]]
            rows.append([model.names[cls],round(conf,4),*xyxy])
        with open(OUT/"detections.csv","w",newline="") as f:
            w=csv.writer(f); w.writerow(["class","confidence","x1","y1","x2","y2"]); w.writerows(rows)
        with open(OUT/"evaluation.txt","w") as f: f.write(f"Detection count: {len(rows)}\\nInference time ms: {ms:.2f}\\n")
        print(f"Detections: {len(rows)}; inference: {ms:.1f} ms; saved: {target}")
        cv2.imshow("Warehouse object detection",annotated); cv2.waitKey(0); cv2.destroyAllWindows()
    else:
        cap=cv2.VideoCapture(0)
        if not cap.isOpened(): raise SystemExit("Cannot open webcam. Pass --input image.jpg.")
        while True:
            ok,frame=cap.read()
            if not ok: break
            result=model.predict(frame,verbose=False)[0]
            cv2.imshow("Warehouse detection - press q to quit",result.plot())
            if cv2.waitKey(1)&0xFF==ord("q"): break
        cap.release(); cv2.destroyAllWindows()
if __name__=="__main__": main()
