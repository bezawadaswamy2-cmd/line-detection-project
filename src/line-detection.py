import cv2 

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

    # Display the frame
    cv2.imshow("Road-blur-Video", edge)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()