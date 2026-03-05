import time
import datetime
import pygame


def set_alarms(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "kids playing.mp3"

    pygame.mixer.init()

    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UPPPP!")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            is_running = False

        time.sleep(1)


if __name__ == '__main__':
    alarm_time = input("Please enter the alarm time (HH:MM:SS): ")
    set_alarms(alarm_time)
