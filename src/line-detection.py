import cv2 
import numpy as np

def region_of_interest(image):

    height = image.shape[0]
    width = image.shape[1]

    # Define triangle
    polygons = np.array([
        [(0, height),
         (width, height),
         (width // 2, height // 2)]
    ])

    mask = np.zeros_like(image)

    cv2.fillPoly(mask, polygons, 255)

    masked_image = cv2.bitwise_and(image, mask)

    return masked_image

# Path to the video
video_path = r"/Users/sribalaayyappaswamybezawada/Visual Studio Code/line-detection-project/data/road_video.mp4"

# Load the video
cap = cv2.VideoCapture(video_path)

#Check if video opened successfully
if not cap.isOpened:
    print("Error: Cannot open video")
    exit()
else:
    print("video opened")

# Read video frame by frame
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frames into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply gaussian blur
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Canny edge detection
    edge = cv2.Canny(blur, 50, 150)
    
    # ROI
    roi = region_of_interest(edge)

    # Draw line
    lines = cv2.HoughLinesP(
        roi,
        2,
        np.pi/180,
        100,
        np.array([]),
        minLineLength = 40,
        maxLineGap = 5
    )

    line_image = np.zeros_like(frame)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 5)

    combo = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    # Display the frame
    cv2.imshow("Line Detection", combo)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()