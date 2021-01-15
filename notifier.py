from win10toast import ToastNotifier
import time


class Notifier:
    
    def __init__(self, icon_path):
        self.icon_path = icon_path

        self.notifier = ToastNotifier()

    def show_notification_endless(self, title, message, duration):

        while True:

            self.notifier.show_toast(title, message, self.icon_path, duration)
            time.sleep(15)
