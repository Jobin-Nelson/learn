#!/usr/bin/env python
'''This program starts a pomodoro session'''
import time

FOCUS_TIME = 45

def pomodoro(minutes: int):
    total_seconds = minutes * 60

    while total_seconds:
        minutes, seconds = divmod(total_seconds, 60)
        print(f'⏰ {minutes:02}:{seconds:02}', end='\r')
        time.sleep(1)
        total_seconds -= 1
    print("TIME'S UP!!!")

if __name__ == '__main__':
    pomodoro(FOCUS_TIME)
