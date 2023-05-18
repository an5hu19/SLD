
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'
while True:
    _,frame=cap.read()
    count = {
             'h': len(os.listdir(directory+"/hello")),
             'i': len(os.listdir(directory+"/ily")),
             'v': len(os.listdir(directory+"/victory")),
             'y': len(os.listdir(directory+"/yes")),
             'n': len(os.listdir(directory+"/no")),
             }
  
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'hello/'+str(count['h'])+'.png',frame)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'ily/'+str(count['i'])+'.png',frame)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'victory/'+str(count['v'])+'.png',frame)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'yes/'+str(count['y'])+'.png',frame)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'no/'+str(count['n'])+'.png',frame)
    

cap.release()
cv2.destroyAllWindows()