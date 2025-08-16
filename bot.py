from pyautogui import typewrite
from time import sleep
from random import randint

def init():
    with open('answers.txt', 'r') as file:
        data = [item.strip() for item in file.readlines()]
    return data

def type_text(text):
    for item in text:
        interval = float('0.0' + str(randint(5, 9)))
        typewrite(item, interval=interval)
        after = float('0.0' + str(randint(2, 9)))
        sleep(after)

def main():
    sleep(2)
    data = init()
    if data:
        type_text(data)

if __name__ == '__main__':
    main()
