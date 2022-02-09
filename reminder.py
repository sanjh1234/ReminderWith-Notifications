import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "DRINK WATER NOW",
            message = "It's important to drink plenty of fluids when the temperatures soar outside. But staying hydrated is a daily necessity, no matter what the thermometer says.",
            app_icon = r"C:\Users\sanjh\my_py_doc\_reminder_notification\Icons8-Windows-8-Industry-Water.ico",
            timeout = 10 
        )
        time.sleep(60*60*2)