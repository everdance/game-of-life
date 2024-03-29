from curses import wrapper, curs_set, A_DIM, A_STANDOUT
import time
import life

def draw_life(screen, c):
    xr, yr = c.range2d()
    max_row = max(yr.stop - yr.start, 20)
    max_col = max(xr.stop - xr.start, 40)
    screen.resize(max_row+2, max_col+2)
    screen.border()
    
    off_x = max(0, xr.stop - max_col)
    off_y = max(0, yr.stop - max_row)
    nmz_cells = c.normalize(off_x, off_y)

    for i in range(0, max_row):
        for j in range(0, max_col):
            ch = "X" if (i, j) in nmz_cells else 'O'
            attr = A_STANDOUT if (i, j) in nmz_cells else A_DIM
            screen.addch(i+1, j+1, ch, attr)
    screen.refresh()

def main(stdscr):
    curs_set(0)
    stdscr.clear()

    cs = life.Cells()
    while not cs.is_dead():
        draw_life(stdscr, cs)
        cs.next()
        time.sleep(1)

if __name__ == "__main__":        
    wrapper(main)

