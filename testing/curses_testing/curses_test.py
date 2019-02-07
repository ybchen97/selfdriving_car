from curses import *
# import import_test


def main():
    stdscr = initscr()

    # removing echo appearing on terminal after typing
    # noecho()

    # removing the cursor
    # curs_set(False)

    # initializing colour
    start_color()
    use_default_colors()
    init_pair(1, COLOR_CYAN, COLOR_BLACK)

    sub_win = newwin(10, 50, 5, 10)
    sub_win.box()

    running = True
    while running:
        key = sub_win.getch()
        # sub_win.addstr(2, 1, 'Key pressed is ' + str(key))
        if 
        if key == 27:
            running = False

    '''
    window.addstr('Hello', color_pair(1) + A_BOLD)
    window.addstr('Hello', color_pair(1))

    window.getch()
    '''
    endwin()


'''
def main():
    window = initscr()
    start_color()
    init_pair(1, COLOR_RED, CO)
    
    while True:
        key = window.getch()

        if key == 27:
            break
        elif key == 119:    # w
            window.addstr(2, 0, 'Forward', A_BOLD)  # supplying an attr argument inside the
            # addstr method overwrites any attron methods

        elif key == 97:     # a
            window.addstr(2, 0, 'Left')

        elif key == 115:    # s
            window.addstr(2, 0, 'Reverse')

        elif key == 100:    # d
            window.addstr(2, 0, 'Right')

        window.move(0, 0)
        window.refresh()

        # window.addstr(2, 0, 'Key pressed is ' + str(key))
    
    endwin()
'''

if __name__ == '__main__':
    wrapper(main())

'''
Key codes in curses

w: 119
a: 979
s: 115
d: 100



Curses Methods

attron & attroff
A_BOLD: prints in bold
A_REVERSE: prints with colours of text n backgnd reversed

Attributes can be concatenated

'''