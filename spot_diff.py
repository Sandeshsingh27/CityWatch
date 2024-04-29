import cv2
import numpy as np
from skimage.metrics import structural_similarity
from datetime import datetime
import winsound

def spot_diff(frame1, frame2):
    print("Processing frames...")

    # Ensure both frames are valid BGR images
    if len(frame1.shape) != 3 or frame1.shape[2] != 3:
        print("Error: Invalid input image format for frame1.")
        return 0
    if len(frame2.shape) != 3 or frame2.shape[2] != 3:
        print("Error: Invalid input image format for frame2.")
        return 0

    # Convert frames to grayscale
    g1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate structural similarity
    (score, diff) = structural_similarity(g2, g1, full=True)
    print("Image similarity:", score)

    # Threshold the difference image
    thresh = cv2.threshold(diff, 0.7, 1, cv2.THRESH_BINARY_INV)[1]

    # Convert thresholded image to uint8 format
    thresh = np.uint8(thresh * 255)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area
    contours = [c for c in contours if cv2.contourArea(c) > 50]

    if len(contours) > 0:
        # print("Theft detected!")
        # Draw rectangles around detected contours
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the difference image and marked frame
        cv2.imshow("Difference", thresh)
        cv2.imshow("Marked Frame", frame1)
        cv2.waitKey(0)

        # Save the marked frame with timestamp
        cv2.imwrite("stolen/" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".jpg", frame1)

        # # Beep to alert theft
        # frequency = 1500
        # duration = 3000
        # winsound.Beep(frequency, duration)
    else:
        print("No theft detected.")

    cv2.destroyAllWindows()
    return len(contours)

# Example usage:
# frame1 = cv2.imread("frame1.jpg")
# frame2 = cv2.imread("frame2.jpg")
# spot_diff(frame1, frame2)
