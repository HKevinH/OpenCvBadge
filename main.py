import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose for person detection
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize drawing utility for landmarks
mp_drawing = mp.solutions.drawing_utils

# Start the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Image dimensions
    height, width, _ = frame.shape
    total_area_pixels = width * height

    # Convert frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect the full body
    results = pose.process(rgb_frame)

    # Create an empty mask to draw the occupied area
    mask = np.zeros((height, width), dtype=np.uint8)

    if results.pose_landmarks:
        # Draw person landmarks on the original frame
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Get the key points of the torso and head
        landmarks = results.pose_landmarks.landmark
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        nose = landmarks[mp_pose.PoseLandmark.NOSE.value]
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]

        # Calculate the bounding box coordinates, expanding it significantly
        xmin = int(min(left_shoulder.x, right_shoulder.x) * width) - 100  # Expand 100 pixels to the left
        xmax = int(max(left_shoulder.x, right_shoulder.x) * width) + 100  # Expand 100 pixels to the right
        ymin = int(nose.y * height) - 150  # Expand 150 pixels upward
        ymax = int(max(left_hip.y, right_hip.y) * height) + 150  # Expand 150 pixels downward

        # Ensure the coordinates are within the image bounds
        xmin, xmax = max(0, xmin), min(width, xmax)
        ymin, ymax = max(0, ymin), min(height, ymax)

        # Create an overlay for transparency
        overlay = frame.copy()
        cv2.rectangle(overlay, (xmin, ymin), (xmax, ymax), (0, 255, 0), -1)

        # Apply transparency to the green color
        alpha = 0.3  # Transparency value (0 is fully transparent, 1 is opaque)
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

        # Draw on the mask to calculate the occupied area
        cv2.rectangle(mask, (xmin, ymin), (xmax, ymax), 255, -1)

    # Calculate the occupied area in pixels for the detected person
    person_area_pixels = cv2.countNonZero(mask)

    # Calculate the available area in pixels
    available_area_pixels = total_area_pixels - person_area_pixels

    # Draw the red rectangle for the total area as a visual reference
    cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 255), 2)

    # Display the occupied and available area on the image
    cv2.putText(frame, f"Occupied Area: {person_area_pixels} px", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame, f"Available Area: {available_area_pixels} px", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show the real-time frame
    cv2.imshow("Person Detection and Available Space", frame)

    # Show the mask (optional, only to verify the occupied area)
    cv2.imshow("Occupied Area Mask", mask)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
