import cv2
from datetime import datetime, timezone

def in_out():
    cap = cv2.VideoCapture(0)

    right, left = False, False

    while True:
        _, frame1 = cap.read()
        frame1 = cv2.flip(frame1, 1)
        _, frame2 = cap.read()
        frame2 = cv2.flip(frame2, 1)

        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.blur(diff, (5, 5))
        
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        
        _, threshd = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
        
        contr, _ = cv2.findContours(threshd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        x = 300
        if contr:
            max_cnt = max(contr, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            
            if not right and not left:
                if x > 500:
                    right = True
                elif x < 200:
                    left = True
                
            elif right:
                if x < 200:
                    print("Saving image to the left")
                    right = False
                    left = False
                    file_path = f"visitors/in/{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]}.jpg"
                    print("File path:", file_path)
                    success = cv2.imwrite(file_path, frame1)
                    if not success:
                        print("Error: Failed to write image")
            
            elif left:
                if x > 500:
                    print("Saving image to the right")
                    right = False
                    left = False
                    file_path = f"visitors/out/{datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]}.jpg"
                    print("File path:", file_path)
                    success = cv2.imwrite(file_path, frame1)
                    if not success:
                        print("Error: Failed to write image")
        
        cv2.imshow("Press ESC key to exit", frame1)
        
        k = cv2.waitKey(1)
        
        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

# in_out()
