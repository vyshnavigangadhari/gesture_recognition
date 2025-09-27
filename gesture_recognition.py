import cv2
import mediapipe as mp

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Last detected gesture (for smoothing)
last_gesture = "🤔 Unknown"

# Hand detection model
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame for mirror effect and convert to RGB
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        gesture = last_gesture  # Default gesture

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                lm = hand_landmarks.landmark

                # Get coordinates for fingertips, MCPs, and wrist
                thumb_tip = lm[4]
                thumb_ip = lm[3]
                thumb_mcp = lm[2]

                index_tip = lm[8]
                middle_tip = lm[12]
                ring_tip = lm[16]
                pinky_tip = lm[20]

                index_mcp = lm[5]
                middle_mcp = lm[9]
                ring_mcp = lm[13]
                pinky_mcp = lm[17]

                wrist = lm[0]

                # Check if fingers are folded (tip below MCP)
                index_folded = index_tip.y > index_mcp.y
                middle_folded = middle_tip.y > middle_mcp.y
                ring_folded = ring_tip.y > ring_mcp.y
                pinky_folded = pinky_tip.y > pinky_mcp.y

                # Check thumb folded (thumb tip x closer to palm than thumb MCP x)
                thumb_folded = abs(thumb_tip.x - wrist.x) < abs(thumb_mcp.x - wrist.x)

                all_fingers_folded = index_folded and middle_folded and ring_folded and pinky_folded

                # Check thumb up/down relative to wrist
                thumb_up = thumb_tip.y < wrist.y and not thumb_folded
                thumb_down = thumb_tip.y > wrist.y and not thumb_folded

                # Detect gestures
                if thumb_up and all_fingers_folded:
                    gesture = "👍 Thumbs Up"
                elif thumb_down and all_fingers_folded:
                    gesture = "👎 Thumbs Down"
                elif (not index_folded and not middle_folded and not ring_folded and not pinky_folded):
                    gesture = "✋ Open Palm"
                elif all_fingers_folded and thumb_folded:
                    gesture = "✊ Fist"
                # Peace sign (index and middle open, ring and pinky folded)
                elif (not index_folded and not middle_folded and ring_folded and pinky_folded):
                    gesture = "✌️ Peace"
                # Pointing (only index open)
                elif (not index_folded and middle_folded and ring_folded and pinky_folded):
                    gesture = "👉 Pointing"
                else:
                    gesture = "🤔 Unknown"

                last_gesture = gesture  # Save for smoothing

        # Display the recognized gesture on the screen
        cv2.putText(frame, f"Gesture: {gesture}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # Show the frame with gesture text
        cv2.imshow('Hand Gesture Recognition', frame)

        # Exit the loop when the 'Esc' key is pressed
        if cv2.waitKey(10) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
