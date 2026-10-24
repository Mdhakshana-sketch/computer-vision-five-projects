import argparse, time, csv
from pathlib import Path
import cv2
import numpy as np

OUT=Path(__file__).parent/"results"; OUT.mkdir(exist_ok=True)
def analyze(frame):
    h,w=frame.shape[:2]
    roi=frame[int(h*.45):h, int(w*.15):int(w*.85)]
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    edges=cv2.Canny(cv2.GaussianBlur(gray,(5,5),0),60,150)
    density=float(np.count_nonzero(edges))/edges.size
    # Adjustable teaching heuristic only; edge density is not a reliable physical distance estimate.
    status="CHECK FOR OBSTACLE" if density > 0.075 else "PATH LOOKS CLEAR"
    vis=frame.copy()
    cv2.rectangle(vis,(int(w*.15),int(h*.45)),(int(w*.85),h),(255,180,0),2)
    cv2.putText(vis,f"{status} | edge density {density:.3f}",(10,30),
                cv2.FONT_HERSHEY_SIMPLEX,.65,(0,0,255) if density>.075 else (0,180,0),2)
    return vis,edges,density,status
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",help="Image path; omit to use webcam")
    args=ap.parse_args()
    if args.input:
        frame=cv2.imread(args.input)
        if frame is None: raise SystemExit(f"Cannot read image: {args.input}")
        out,edges,density,status=analyze(frame)
        cv2.imwrite(str(OUT/"obstacle_output.jpg"),out); cv2.imwrite(str(OUT/"edges.png"),edges)
        with open(OUT/"evaluation.csv","w",newline="") as f:
            w=csv.writer(f); w.writerow(["edge_density","heuristic_status"]); w.writerow([round(density,6),status])
        print(f"{status}; edge density={density:.4f}; saved outputs in {OUT}")
        cv2.imshow("Obstacle heuristic",out); cv2.imshow("ROI edges",edges); cv2.waitKey(0); cv2.destroyAllWindows()
    else:
        cap=cv2.VideoCapture(0)
        if not cap.isOpened(): raise SystemExit("Cannot open webcam. Pass --input image.jpg.")
        while True:
            ok,frame=cap.read()
            if not ok: break
            out,_,_,_=analyze(frame); cv2.imshow("Obstacle heuristic - press q to quit",out)
            if cv2.waitKey(1)&0xFF==ord("q"): break
        cap.release(); cv2.destroyAllWindows()
if __name__=="__main__": main()
