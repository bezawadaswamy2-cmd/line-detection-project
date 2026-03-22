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

    # Display the frame
    cv2.imshow("Road Video", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()