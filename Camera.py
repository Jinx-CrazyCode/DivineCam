import cv2

def cam(string):
    try:
        camera = cv2.VideoCapture(string)
        while True:
                ret,frame = camera.read()
                if not ret:
                    break
                cv2.imshow("DIVINE CAMERA",frame)
                
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        camera.release()
        cv2.destroyAllWindows()
    except:
        print("ERROR")