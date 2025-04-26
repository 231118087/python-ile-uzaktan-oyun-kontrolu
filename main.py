import cv2
import time
import subprocess
from hand_tracking import HandTracker
from controls import GameControls  


try:
    game_process = subprocess.Popen([r"C:\Program Files\BlueStacks_nxt\HD-Player.exe"])
    print("BlueStacks başlatıldı.")
except Exception as e:
    print(f"Oyun başlatılamadı: {e}")
    exit()

# El hareketi ve kontrol sınıflarını başlat
hand_tracker = HandTracker()
game_controls = GameControls()

# Webcam'den video akışı başlat
cap = cv2.VideoCapture(0)

# Zamanlayıcı başlat (30 dakika)
start_time = time.time()
max_duration = 30 * 60  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Kameradan alınan görüntüyü tersine çevir
    frame = cv2.flip(frame, 1)  # 1: yatayda yansıtır

    # El hareketini algıla ve çiz
    frame, gesture = hand_tracker.detect_hand_and_draw(frame)

    if gesture:
        print(f"Detected gesture: {gesture}")
        
        # Algılanan harekete göre uygun fonksiyonu çağırıyoruz
        if gesture == "UP":
            game_controls.swipe_up()
        elif gesture == "DOWN":
            game_controls.swipe_down()
        elif gesture == "LEFT":
            game_controls.swipe_left()
        elif gesture == "RIGHT":
            game_controls.swipe_right()

    # Kamerayı göster
    cv2.imshow("Hand Tracking", frame)

    # 30 dakika so
    # 
    # nra çıkış yap
    elapsed_time = time.time() - start_time
    if elapsed_time >= max_duration:
        print("30 dakika doldu. Program kapanıyor...")
        break

    # 'q' tuşuna basıldığında çıkış yap
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Manuel çıkış yapıldı.")
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()

# Oyun sürecini sonlandır t
game_process.terminate()