import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        
        # MediaPipe el takibi modelini başlat
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)  # Sadece bir el takibi yapacak şekilde ayarlandı
        self.mp_draw = mp.solutions.drawing_utils  # El işaretlerini çizmek için

    def detect_hand_and_draw(self, frame):
        # Görüntüyü RGB formatına çevir (MediaPipe RGB kullanır)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(frame_rgb)

        # Hareketi algılamak için bir değişken
        gesture = None

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Elin üzerinde işaretleri çiz
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                # İşaret parmağı ucu ve tabanı arasındaki mesafeyi al
                index_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_base = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_MCP]

                # X ve Y koordinatları arasındaki farkları hesapla (hareketi tespit et)
                dx = index_tip.x - index_base.x
                dy = index_tip.y - index_base.y

                # Basit el hareketlerini algıla
                if dx > 0.1:  # Sağ hareket
                    gesture = "RIGHT"
                elif dx < -0.1:  # Sol hareket
                    gesture = "LEFT"
                elif dy > 0.1:  # Aşağı hareket
                    gesture = "DOWN"
                elif dy < -0.1:  # Yukarı hareket
                    gesture = "UP"

        # Algılanan hareketi geri döndür
        return frame, gesture
