
import datetime

def save_log(action):
    with open("activity_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {action}\n")
