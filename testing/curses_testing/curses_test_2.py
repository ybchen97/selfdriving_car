from curses import *

def main():
    window = initscr()

    while True:
        key = window.getch()
        if key == 27:
            break
        window.addstr('Key code is ' + str(key))
    endwin()

main()