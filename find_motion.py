import cv2
import time
from skimage.metrics import structural_similarity
from datetime import datetime
import winsound
from spot_diff import *

def find_motion():
    motion_detected = False
    is_start_done = False
    cap = cv2.VideoCapture('theft1.mp4')

    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    print("Waiting for 2 seconds...")
    time.sleep(2)

    _, frm1 = cap.read()
    frm1_gray = cv2.cvtColor(frm1, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frm2 = cap.read()

        if not ret:
            print("End of video.")
            break

        frm2_gray = cv2.cvtColor(frm2, cv2.COLOR_BGR2GRAY)

        diff = cv2.absdiff(frm1_gray, frm2_gray)

        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        contors = [c for c in contors if cv2.contourArea(c) > 100]  # Adjust contour area threshold

        if len(contors) > 3:  # Adjust motion detection threshold
            cv2.putText(thresh, "Motion detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
            motion_detected = True
            is_start_done = False
        elif motion_detected and len(contors) < 2:  # Adjust motion detection threshold
            if not is_start_done:
                start = time.time()
                is_start_done = True

            end = time.time()
            
            print("Time:", end - start)
            if end - start > 3:
                stolen = spot_diff(frm1, frm2)
                if stolen == 0:
                    print("No theft detected.")
                else:
                    print("Theft detected!")
                    # Take appropriate actions here, such as sounding an alarm or saving images.
                    frequency = 1500
                    duration = 2000
                    winsound.Beep(frequency, duration)
                # Reset motion detection flags for the next iteration
                motion_detected = False
                is_start_done = False
        else:
            cv2.putText(thresh, "No motion detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

        cv2.imshow("winname", thresh)

        frm1_gray = frm2_gray

        if cv2.waitKey(20) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    find_motion()
