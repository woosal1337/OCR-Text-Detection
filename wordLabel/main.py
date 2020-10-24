import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("../data/1.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))
#print(pytesseract.image_to_boxes(img))

hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)
print(boxes)

for x,b in enumerate(boxes.splitlines()):

    if x!=0:

        b = b.split()
        print(b)
        # x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        # cv2.rectangle(img, (x,hImg-y),(w,hImg-h), (0,0,255),1)
        # cv2.putText(img, b[0], (x,hImg-y+25), cv2.FONT_HERSHEY_DUPLEX,1, (20,20,255))

cv2.imshow("Result", img)
cv2.waitKey(0)