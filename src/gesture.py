import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands


class GestureDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6,
        )

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if not result.multi_hand_landmarks:
            return False

        landmarks = result.multi_hand_landmarks[0].landmark
        return self._is_peace_sign(landmarks)

    def _is_peace_sign(self, lm):
        # tip di atas pip = jari lurus (y makin kecil = makin ke atas)
        index_up = lm[8].y < lm[6].y
        middle_up = lm[12].y < lm[10].y
        ring_down = lm[16].y > lm[14].y
        pinky_down = lm[20].y > lm[18].y

        return index_up and middle_up and ring_down and pinky_down