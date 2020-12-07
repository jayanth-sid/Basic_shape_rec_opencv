import cv2
def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        #print(area)
        if area>100:
            peri=cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if (len(approx))==3:
                cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),1)
                cv2.putText(imgcontour,"TRIANGLE",(x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
            if (len(approx))==4:
                cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
                x, y, w, h = cv2.boundingRect(approx)
                if  (x+w>=y+h-10 and x+w<=y+h+10):
                    cv2.rectangle(imgcontour, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    cv2.putText(imgcontour, "SQUARE", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
                else:
                    cv2.rectangle(imgcontour, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    cv2.putText(imgcontour, "RECTANGLE", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
            if (len(approx))==8:
                cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)
                x, y, w, h = cv2.boundingRect(approx)
                cv2.rectangle(imgcontour, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.putText(imgcontour, "circle", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)

cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    imgcontour = img.copy()
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurimg = cv2.GaussianBlur(grayimg, (7, 7), 1)
    cannyimg = cv2.Canny(blurimg, 50, 70)
    getcontours(cannyimg)
    cv2.imshow("graqy", cannyimg)
    cv2.imshow("gray", imgcontour)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break