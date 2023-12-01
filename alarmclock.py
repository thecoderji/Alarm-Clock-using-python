import datetime
import time
import winsound  # For Windows system sound, you can use other libraries for different systems

class AlarmClock:
    def __init__(self):
        self.alarms = []

    def set_alarm(self, hour, minute):
        alarm_time = datetime.time(hour, minute)
        self.alarms.append(alarm_time)

    def run_alarms(self):
        while True:
            current_time = datetime.datetime.now().time()
            for alarm in self.alarms[:]:  # Use a copy to avoid modification during iteration
                if current_time >= alarm:
                    print("Alarm at {}:{}! Time to wake up!".format(alarm.hour, alarm.minute))
                    self.play_alarm_sound()
                    self.alarms.remove(alarm)  # Remove the triggered alarm

            time.sleep(1)  # Check every second

    def play_alarm_sound(self):
        duration = 1000  # milliseconds
        frequency = 440  # Hz
        winsound.Beep(frequency, duration)

if __name__ == "__main__":
    alarm_clock = AlarmClock()

    print("Welcome to the Alarm Clock App!")

    while True:
        try:
            hour = int(input("Enter the hour (0-23): "))
            minute = int(input("Enter the minute (0-59): "))
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                alarm_clock.set_alarm(hour, minute)
                print("Alarm set for {}:{}".format(hour, minute))
            else:
                print("Invalid input. Please enter a valid hour and minute.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        set_another = input("Do you want to set another alarm? (yes/no): ").lower()
        if set_another != 'yes':
            break

    alarm_clock.run_alarms()
