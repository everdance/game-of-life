import curses
import time
import life

def draw_life(screen, c):
    xr, yr = c.range2d()
    max_col_row = max(xr.stop - xr.start, yr.stop - yr.start, 20)
    off_x = max(0, xr.stop - max_col_row)
    off_y = max(0, yr.stop - max_col_row)
    nmz_cells = c.normalize(off_x, off_y)
    for i in range(0, max_col_row):
        for j in range(0, max_col_row):
            ch = "X" if (i, j) in nmz_cells else "O"
            attr = curses.A_STANDOUT if (i, j) in nmz_cells else curses.A_DIM
            screen.addch(i, j, ch, attr)
    screen.refresh()

if __name__ == "__main__":        
    screen = curses.initscr()

    cs = life.Cells()
    while not cs.is_dead():
        draw_life(screen, cs)
        cs.next()
        time.sleep(1)

    curses.endwin()

    print(cs.init_cells, cs.cycles)    

