import pyautogui

class GameControls:
    @staticmethod
    def swipe_up():
        # Yukarı kaydırmak için simüle edilen tuş basma
        pyautogui.press('up')

    @staticmethod
    def swipe_down():
        # Aşağı kaydırmak için simüle edilen tuş basma
        pyautogui.press('down')

    @staticmethod
    def swipe_left():
        # Sola kaydırmak için simüle edilen tuş basma
        pyautogui.press('left')

    @staticmethod
    def swipe_right():
        # Sağa kaydırmak için simüle edilen tuş basma
        pyautogui.press('right')

    @staticmethod
    def double_click():
        # Çift tıklama simülasyonu
        pyautogui.doubleClick()

    @staticmethod
    def get_skateboard():
        # Kaykayı almak için bir tıklama simülasyonu
        pyautogui.click(x=500, y=500)  # Burada kaykayı almak için ekran koordinatlarını belirleyebilirsiniz
        print("Kaykay alındı!")
