import argparse, csv
from pathlib import Path
import cv2

OUT=Path(__file__).parent/"results"; OUT.mkdir(exist_ok=True)
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True,help="Vehicle image path")
    ap.add_argument("--ocr",action="store_true",help="Try Tesseract OCR (requires Tesseract installed separately)")
    args=ap.parse_args()
    image=cv2.imread(args.input)
    if image is None: raise SystemExit(f"Cannot read image: {args.input}")
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray=cv2.bilateralFilter(gray,11,17,17)
    edges=cv2.Canny(gray,30,200)
    contours,_=cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)[:30]
    candidate=None
    for c in contours:
        peri=cv2.arcLength(c,True); approx=cv2.approxPolyDP(c,.02*peri,True)
        if len(approx)==4:
            x,y,w,h=cv2.boundingRect(approx); ratio=w/max(h,1)
            if 2.0 <= ratio <= 6.5 and w>60 and h>15:
                candidate=(x,y,w,h); break
    output=image.copy(); text="Plate candidate not found"
    if candidate:
        x,y,w,h=candidate
        cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),3)
        crop=gray[y:y+h,x:x+w]
        cv2.imwrite(str(OUT/"plate_crop.png"),crop)
        text="Plate candidate found"
        if args.ocr:
            try:
                import pytesseract
                # On Windows, install Tesseract OCR separately and add it to PATH.
                recognized=pytesseract.image_to_string(crop,config="--psm 7")
                text="OCR: "+ " ".join(recognized.split())
            except Exception as e:
                text=f"OCR unavailable: {e}"
    cv2.putText(output,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,.65,(0,255,0),2)
    target=OUT/"license_plate_output.jpg"; cv2.imwrite(str(target),output)
    with open(OUT/"evaluation.csv","w",newline="") as f:
        w=csv.writer(f); w.writerow(["plate_candidate_found","ocr_requested","result"]); w.writerow([bool(candidate),args.ocr,text])
    print(f"{text}; saved: {target}")
    cv2.imshow("License plate detection",output); cv2.waitKey(0); cv2.destroyAllWindows()
if __name__=="__main__": main()
