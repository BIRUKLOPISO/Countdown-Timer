import time


def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print('Time is up!')


# Example usage
countdown_timer(2, 30)