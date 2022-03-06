import time

def timer():
    minutes = input('Set a timer for ___ minutes: ')

    while not minutes.isdigit():
        print('Invalid format')
        minutes = input('Set a timer for ___ minutes: ')

    seconds = input('and ___ seconds: ')

    while not seconds.isdigit():
        print('Invalid format')
        seconds = input(f'Set a timer for {minutes} and ___ seconds: ')


    full_seconds = int(minutes) * 60 + int(seconds)
    print(full_seconds)

    while(full_seconds):
        mins, secs = divmod(full_seconds, 60)
        t = f'{mins:2.0f}:{secs:2.0f}'
        print(t, end='\r')
        time.sleep(1)
        full_seconds -= 1
    print("Time's Up!!!")

if __name__ == '__main__':
    timer()
