import argparse, csv
from pathlib import Path
import cv2
import numpy as np

OUT=Path(__file__).parent/"results"; OUT.mkdir(exist_ok=True)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True,help="Test/product image")
    ap.add_argument("--reference",required=True,help="Defect-free reference image")
    ap.add_argument("--threshold",type=int,default=30)
    ap.add_argument("--min-area",type=int,default=80)
    args=ap.parse_args()
    test=cv2.imread(args.input); ref=cv2.imread(args.reference)
    if test is None: raise SystemExit(f"Cannot read test image: {args.input}")
    if ref is None: raise SystemExit(f"Cannot read reference image: {args.reference}")
    ref=cv2.resize(ref,(test.shape[1],test.shape[0]))
    a=cv2.GaussianBlur(cv2.cvtColor(test,cv2.COLOR_BGR2GRAY),(5,5),0)
    b=cv2.GaussianBlur(cv2.cvtColor(ref,cv2.COLOR_BGR2GRAY),(5,5),0)
    diff=cv2.absdiff(a,b)
    _,mask=cv2.threshold(diff,args.threshold,255,cv2.THRESH_BINARY)
    kernel=np.ones((3,3),np.uint8); mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.dilate(mask,kernel,iterations=2)
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    output=test.copy(); regions=[]
    for c in contours:
        area=cv2.contourArea(c)
        if area < args.min_area: continue
        x,y,w,h=cv2.boundingRect(c); regions.append((x,y,w,h,area))
        cv2.rectangle(output,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(output,f"change {area:.0f}",(x,max(18,y-5)),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,0,255),1)
    cv2.imwrite(str(OUT/"quality_output.jpg"),output)
    cv2.imwrite(str(OUT/"difference_mask.png"),mask)
    changed=float(np.count_nonzero(mask))/mask.size
    with open(OUT/"evaluation.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["candidate_regions","changed_pixel_ratio","threshold","min_area"])
        w.writerow([len(regions),round(changed,6),args.threshold,args.min_area])
    print(f"Candidate changed regions: {len(regions)}; changed-pixel ratio: {changed:.4f}")
    print(f"Saved annotated image and mask in {OUT}")
    cv2.imshow("Quality inspection",output); cv2.imshow("Difference mask",mask)
    cv2.waitKey(0); cv2.destroyAllWindows()
if __name__=="__main__": main()
